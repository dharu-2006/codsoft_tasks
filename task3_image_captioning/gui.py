from image_captioning_model import BLIPImageCaptioner
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageCaptioningGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Captioning AI")
        self.root.geometry("800x600")
        
        # Initialize the captioner
        self.captioner = BLIPImageCaptioner()
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Image Captioning AI", 
                              font=("Arial", 18, "bold"))
        title_label.pack(pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        # Load image button
        load_btn = tk.Button(button_frame, text="Load Image", 
                           command=self.load_image, font=("Arial", 12))
        load_btn.pack(side=tk.LEFT, padx=5)
        
        # Generate caption button
        caption_btn = tk.Button(button_frame, text="Generate Caption", 
                              command=self.generate_caption, font=("Arial", 12))
        caption_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        clear_btn = tk.Button(button_frame, text="Clear", 
                            command=self.clear_all, font=("Arial", 12))
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Image display
        self.image_label = tk.Label(self.root, text="No image loaded", 
                                   width=60, height=20, relief="sunken")
        self.image_label.pack(pady=10)
        
        # Caption display
        caption_frame = tk.Frame(self.root)
        caption_frame.pack(pady=10, fill=tk.X, padx=20)
        
        tk.Label(caption_frame, text="Generated Caption:", 
                font=("Arial", 12, "bold")).pack(anchor=tk.W)
        
        self.caption_text = tk.Text(caption_frame, height=4, width=80, 
                                   wrap=tk.WORD, font=("Arial", 11))
        self.caption_text.pack(fill=tk.X, pady=5)
        
        # Status
        self.status_label = tk.Label(self.root, text="Ready", 
                                   relief="sunken", anchor=tk.W)
        self.status_label.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Initialize variables
        self.current_image = None
        self.image_path = None
        
    def load_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")]
        )
        
        if file_path:
            try:
                self.image_path = file_path
                self.current_image = Image.open(file_path)
                self.display_image()
                self.status_label.config(text=f"Loaded: {file_path}")
                self.caption_text.delete(1.0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def display_image(self):
        if self.current_image:
            # Resize image for display
            display_size = (400, 300)
            image_copy = self.current_image.copy()
            image_copy.thumbnail(display_size, Image.Resampling.LANCZOS)
            
            # Convert to PhotoImage
            photo = ImageTk.PhotoImage(image_copy)
            
            # Update label
            self.image_label.config(image=photo, text="")
            self.image_label.image = photo  # Keep a reference
    
    def generate_caption(self):
        if not self.current_image or not self.image_path:
            messagebox.showwarning("Warning", "Please load an image first")
            return
        
        try:
            self.status_label.config(text="Generating caption...")
            self.root.update()
            
            # Generate caption
            caption, _ = self.captioner.caption_image(self.image_path)
            
            # Display caption
            self.caption_text.delete(1.0, tk.END)
            self.caption_text.insert(1.0, caption)
            
            self.status_label.config(text="Caption generated successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate caption: {str(e)}")
            self.status_label.config(text="Error generating caption")
    
    def clear_all(self):
        self.current_image = None
        self.image_path = None
        self.image_label.config(image="", text="No image loaded")
        self.image_label.image = None
        self.caption_text.delete(1.0, tk.END)
        self.status_label.config(text="Cleared")

def run_gui():
    root = tk.Tk()
    ImageCaptioningGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
