#!/usr/bin/env python3
"""
Resize MCP guide screenshots to a smaller width for better display.
This reduces file size and makes them more suitable for inline display.
"""

from PIL import Image
import os

def resize_image(input_path, output_path, max_width=600):
    """
    Resize an image to a maximum width while maintaining aspect ratio.
    
    Args:
        input_path: Path to the input image
        output_path: Path to save the resized image
        max_width: Maximum width in pixels (default: 600)
    """
    with Image.open(input_path) as img:
        # Get original dimensions
        width, height = img.size
        
        # Calculate new dimensions if width exceeds max_width
        if width > max_width:
            ratio = max_width / width
            new_width = max_width
            new_height = int(height * ratio)
            
            # Resize with high-quality resampling
            resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Save with optimization
            resized.save(output_path, optimize=True, quality=85)
            print(f"✓ Resized {os.path.basename(input_path)}: {width}x{height} → {new_width}x{new_height}")
        else:
            # Image is already small enough, just optimize
            img.save(output_path, optimize=True, quality=85)
            print(f"✓ Optimized {os.path.basename(input_path)}: {width}x{height} (no resize needed)")

def main():
    """Resize all MCP guide images."""
    # Get the images directory (parent of helpers)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.dirname(script_dir)
    
    images = [
        'agent_interface.png',
        'tools_tab.png',
        'add_mcp_form.png'
    ]
    
    print("Resizing MCP guide images to max width 600px...\n")
    
    for image_name in images:
        input_path = os.path.join(images_dir, image_name)
        
        if not os.path.exists(input_path):
            print(f"✗ Skipping {image_name} - file not found")
            continue
        
        # Resize in place (overwrite original)
        resize_image(input_path, input_path, max_width=600)
    
    print("\n✓ All images processed!")
    print("\nFile sizes:")
    for image_name in images:
        path = os.path.join(images_dir, image_name)
        if os.path.exists(path):
            size_kb = os.path.getsize(path) / 1024
            print(f"  {image_name}: {size_kb:.1f} KB")

if __name__ == "__main__":
    main()
