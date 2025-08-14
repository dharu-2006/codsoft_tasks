import torch
import torch.nn as nn
from torchvision import transforms, models
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import requests
from io import BytesIO

class ImageCaptioningModel(nn.Module):
    def __init__(self, embed_dim=512, vocab_size=50257):
        super(ImageCaptioningModel, self).__init__()
        
        # Pre-trained ResNet50 for feature extraction
        self.resnet = models.resnet50(pretrained=True)
        self.resnet.fc = nn.Linear(self.resnet.fc.in_features, embed_dim)
        
        # Pre-trained GPT-2 for text generation
        self.gpt2 = GPT2LMHeadModel.from_pretrained('gpt2')
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        
        # Add padding token
        self.tokenizer.pad_token = self.tokenizer.eos_token
        
        # Image feature projection
        self.image_projection = nn.Linear(embed_dim, self.gpt2.config.n_embd)
        
        # Freeze ResNet parameters for faster training
        for param in self.resnet.parameters():
            param.requires_grad = False
            
    def extract_image_features(self, images):
        with torch.no_grad():
            features = self.resnet(images)
        return self.image_projection(features)
    
    def generate_caption(self, image_features, max_length=50):
        # Create image token
        image_token = image_features.unsqueeze(1)
        
        # Start with beginning of sentence token
        input_ids = torch.tensor([[self.tokenizer.bos_token_id]], device=image_features.device)
        
        # Prepare inputs for GPT-2
        inputs_embeds = self.gpt2.transformer.wte(input_ids)
        inputs_embeds = torch.cat([image_token, inputs_embeds], dim=1)
        
        # Generate caption
        with torch.no_grad():
            outputs = self.gpt2.generate(
                inputs_embeds=inputs_embeds,
                max_length=max_length,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        # Decode and return caption
        caption = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return caption

class ImageCaptioner:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = ImageCaptioningModel()
        self.model.to(self.device)
        
        # Image preprocessing
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                               std=[0.229, 0.224, 0.225])
        ])
        
    def load_image(self, image_path):
        if image_path.startswith('http'):
            response = requests.get(image_path)
            image = Image.open(BytesIO(response.content)).convert('RGB')
        else:
            image = Image.open(image_path).convert('RGB')
        return image
    
    def preprocess_image(self, image):
        return self.transform(image).unsqueeze(0).to(self.device)
    
    def caption_image(self, image_path):
        # Load and preprocess image
        image = self.load_image(image_path)
        processed_image = self.preprocess_image(image)
        
        # Extract features and generate caption
        image_features = self.model.extract_image_features(processed_image)
        caption = self.model.generate_caption(image_features)
        
        return caption, image
    
    def display_result(self, image_path):
        caption, image = self.caption_image(image_path)
        
        # Display image and caption
        plt.figure(figsize=(10, 8))
        plt.imshow(image)
        plt.axis('off')
        plt.title(f"Generated Caption: {caption}", fontsize=14, pad=20)
        plt.tight_layout()
        plt.show()
        
        return caption

# Alternative implementation using BLIP model for better accuracy
class BLIPImageCaptioner:
    def __init__(self):
        from transformers import BlipProcessor, BlipForConditionalGeneration
        
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model.to(self.device)
    
    def load_image(self, image_path):
        if image_path.startswith('http'):
            response = requests.get(image_path)
            image = Image.open(BytesIO(response.content)).convert('RGB')
        else:
            image = Image.open(image_path).convert('RGB')
        return image
    
    def caption_image(self, image_path):
        image = self.load_image(image_path)
        
        # Process image and generate caption
        inputs = self.processor(image, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            out = self.model.generate(**inputs, max_length=50, num_beams=5)
        
        caption = self.processor.decode(out[0], skip_special_tokens=True)
        return caption, image
    
    def display_result(self, image_path):
        caption, image = self.caption_image(image_path)
        
        plt.figure(figsize=(10, 8))
        plt.imshow(image)
        plt.axis('off')
        plt.title(f"Generated Caption: {caption}", fontsize=14, pad=20)
        plt.tight_layout()
        plt.show()
        
        return caption
