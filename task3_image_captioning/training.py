import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import json
import os
from image_captioning_model import ImageCaptioningModel

class CaptionDataset(Dataset):
    def __init__(self, image_dir, annotations_file, transform=None):
        self.image_dir = image_dir
        self.transform = transform
        
        with open(annotations_file, 'r') as f:
            self.annotations = json.load(f)
        
    def __len__(self):
        return len(self.annotations)
    
    def __getitem__(self, idx):
        annotation = self.annotations[idx]
        image_path = os.path.join(self.image_dir, annotation['image'])
        image = Image.open(image_path).convert('RGB')
        
        if self.transform:
            image = self.transform(image)
        
        caption = annotation['caption']
        return image, caption

def train_model(data_dir, epochs=10, batch_size=16, learning_rate=1e-4):
    """
    Training function for custom dataset
    data_dir should contain:
    - images/ folder with images
    - annotations.json with format: [{"image": "img1.jpg", "caption": "description"}, ...]
    """
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # Data transforms
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                           std=[0.229, 0.224, 0.225])
    ])
    
    # Dataset and DataLoader
    dataset = CaptionDataset(
        image_dir=os.path.join(data_dir, 'images'),
        annotations_file=os.path.join(data_dir, 'annotations.json'),
        transform=transform
    )
    
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    
    # Model
    model = ImageCaptioningModel()
    model.to(device)
    
    # Optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    
    # Training loop
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for batch_idx, (images, captions) in enumerate(dataloader):
            images = images.to(device)
            
            # Extract image features
            image_features = model.extract_image_features(images)
            
            # Tokenize captions
            tokenized = model.tokenizer(
                captions, 
                padding=True, 
                truncation=True, 
                return_tensors='pt'
            ).to(device)
            
            # Forward pass
            optimizer.zero_grad()
            
            # Prepare inputs for GPT-2
            inputs_embeds = model.gpt2.transformer.wte(tokenized.input_ids)
            image_features_expanded = image_features.unsqueeze(1).expand(-1, inputs_embeds.size(1), -1)
            combined_embeds = inputs_embeds + image_features_expanded
            
            # Calculate loss
            outputs = model.gpt2(inputs_embeds=combined_embeds, labels=tokenized.input_ids)
            loss = outputs.loss
            
            # Backward pass
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
            
            if batch_idx % 10 == 0:
                print(f'Epoch {epoch+1}/{epochs}, Batch {batch_idx}, Loss: {loss.item():.4f}')
        
        avg_loss = total_loss / len(dataloader)
        print(f'Epoch {epoch+1}/{epochs} completed. Average Loss: {avg_loss:.4f}')
    
    # Save model
    torch.save(model.state_dict(), 'trained_caption_model.pth')
    print("Training completed. Model saved as 'trained_caption_model.pth'")
    
    return model

def evaluate_model(model, test_images):
    """Evaluate model on test images"""
    model.eval()
    results = []
    
    for image_path in test_images:
        try:
            # Load and preprocess image
            image = Image.open(image_path).convert('RGB')
            transform = transforms.Compose([
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                                   std=[0.229, 0.224, 0.225])
            ])
            
            processed_image = transform(image).unsqueeze(0).to(next(model.parameters()).device)
            
            # Generate caption
            image_features = model.extract_image_features(processed_image)
            caption = model.generate_caption(image_features)
            
            results.append({
                'image': image_path,
                'caption': caption
            })
            
        except Exception as e:
            print(f"Error processing {image_path}: {str(e)}")
    
    return results

if __name__ == "__main__":
    print("Training module for Image Captioning")
    print("To train on custom data:")
    print("1. Organize data as: data_dir/images/ and data_dir/annotations.json")
    print("2. Run: train_model('path/to/data_dir')")
    print("3. For evaluation: evaluate_model(model, ['test1.jpg', 'test2.jpg'])")
