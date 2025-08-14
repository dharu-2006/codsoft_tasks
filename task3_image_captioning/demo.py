from image_captioning_model import BLIPImageCaptioner
import matplotlib.pyplot as plt

def demo():
    print("Image Captioning AI Demo")
    print("=" * 40)
    
    # Initialize the captioner
    print("Initializing BLIP model...")
    captioner = BLIPImageCaptioner()
    print("Model loaded successfully!")
    
    # Test with a sample image URL
    test_image_url = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?w=500"
    
    print(f"\nTesting with sample image...")
    print(f"Image URL: {test_image_url}")
    
    try:
        # Generate caption
        caption, image = captioner.caption_image(test_image_url)
        
        print(f"\nGenerated Caption: {caption}")
        
        # Display the image with caption
        plt.figure(figsize=(8, 6))
        plt.imshow(image)
        plt.axis('off')
        plt.title(f"Caption: {caption}", fontsize=12, pad=20, wrap=True)
        plt.tight_layout()
        plt.show()
        
        print("\nDemo completed successfully!")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Make sure you have internet connection for the demo image.")

def caption_local_image(image_path):
    """Caption a local image file"""
    print(f"Captioning local image: {image_path}")
    
    try:
        captioner = BLIPImageCaptioner()
        caption = captioner.display_result(image_path)
        return caption
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

if __name__ == "__main__":
    demo()
    
    print("\n" + "=" * 40)
    print("To caption your own images:")
    print("1. Use: caption_local_image('path/to/your/image.jpg')")
    print("2. Or run: python gui.py for a graphical interface")
    print("3. Or run: python main.py for full testing")
