import os
import sys
from PIL import Image

def resize_image(image_path, max_size_kb=400):
    """Resize image to ensure it's under the specified size limit in KB."""
    with Image.open(image_path) as img:
        # Start with original dimensions
        width, height = img.size
        scale_factor = 1.0
        
        # Check file size and downscale as necessary
        while True:
            # Resize using the current scale factor
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            
            # Save to temporary file and check size
            temp_path = image_path + ".temp"
            resized_img.save(temp_path, format=img.format)
            
            # Check size of resized image
            if os.path.getsize(temp_path) <= max_size_kb * 1024:
                # If within size limit, replace original file and break
                resized_img.save(image_path, format=img.format)
                os.remove(temp_path)  # Clean up temporary file
                break
            else:
                # Adjust scale factor for further downscaling
                scale_factor *= 0.9

def resize_images_in_directory(root):
    """Find and resize images in the specified root's .vuepress/dist/assets directory."""
    # Construct the path to assets directory
    assets_dir = os.path.join(root, ".vuepress", "dist", "assets")
    
    # Supported image extensions
    image_extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp")

    # Traverse assets directory for image files
    for root_dir, _, files in os.walk(assets_dir):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_path = os.path.join(root_dir, file)
                print(f"Resizing: {image_path}")
                resize_image(image_path)

if __name__ == "__main__":
    # Ensure the script receives exactly one argument for the root directory
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)

    # Get root directory from command-line argument
    root = sys.argv[1]

    # Start resizing images in the specified directory
    resize_images_in_directory(root)
