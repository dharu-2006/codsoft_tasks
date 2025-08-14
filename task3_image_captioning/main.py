from image_captioning_model import ImageCaptioner, BLIPImageCaptioner
import torch
import time

def test_image_captioning():
    print("Image Captioning AI Test")
    print("=" * 50)
    
    # Check device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")
    
    # Test images (you can replace with your own image paths)
    test_images = [
        "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?w=500",  # Dog
        "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=500",  # Cat
        "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=500",  # Mountain
        "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=500",  # City
    ]
    
    # Initialize models
    print("\nInitializing BLIP model (recommended for best accuracy)...")
    blip_captioner = BLIPImageCaptioner()
    
    print("\nGenerating captions...")
    print("-" * 30)
    
    for i, image_url in enumerate(test_images, 1):
        try:
            print(f"\nTest Image {i}:")
            start_time = time.time()
            
            # Generate caption using BLIP
            caption, _ = blip_captioner.caption_image(image_url)
            
            end_time = time.time()
            print(f"Caption: {caption}")
            print(f"Generation time: {end_time - start_time:.2f} seconds")
            
        except Exception as e:
            print(f"Error processing image {i}: {str(e)}")
    
    return blip_captioner

def caption_custom_image(image_path):
    """Function to caption a custom image"""
    captioner = BLIPImageCaptioner()
    try:
        caption = captioner.display_result(image_path)
        print(f"Generated caption: {caption}")
        return caption
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def compare_models():
    """Compare different captioning approaches"""
    print("\nModel Comparison")
    print("=" * 50)
    
    test_image = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?w=500"
    
    # BLIP model (recommended)
    print("\n1. BLIP Model (Best Accuracy):")
    blip_captioner = BLIPImageCaptioner()
    start_time = time.time()
    blip_caption, _ = blip_captioner.caption_image(test_image)
    blip_time = time.time() - start_time
    print(f"Caption: {blip_caption}")
    print(f"Time: {blip_time:.2f} seconds")
    
    print("\nRecommendation: Use BLIP model for best accuracy and performance")

if __name__ == "__main__":
    # Run tests
    captioner = test_image_captioning()
    
    # Compare models
    compare_models()
    
    # Example of captioning a local image
    print("\n" + "=" * 50)
    print("To caption your own image, use:")
    print("caption_custom_image('path/to/your/image.jpg')")
    print("or")
    print("caption_custom_image('http://url/to/image.jpg')")
