#!/usr/bin/env python3
"""
Helper script to save the MCP guide screenshots.

Since the images were uploaded in the chat, you'll need to manually save them:
1. Save Image 1 (agent interface) as: images/agent_interface.png
2. Save Image 2 (tools tab) as: images/tools_tab.png  
3. Save Image 3 (add MCP form) as: images/add_mcp_form.png

Or use this script if you have the image files:
    python setup_images.py <path_to_image1> <path_to_image2> <path_to_image3>
"""

import sys
import shutil
import os

def setup_images(img1_path, img2_path, img3_path):
    """Copy images to the correct locations."""
    os.makedirs('images', exist_ok=True)
    
    shutil.copy(img1_path, 'images/agent_interface.png')
    print(f"✓ Saved {img1_path} -> images/agent_interface.png")
    
    shutil.copy(img2_path, 'images/tools_tab.png')
    print(f"✓ Saved {img2_path} -> images/tools_tab.png")
    
    shutil.copy(img3_path, 'images/add_mcp_form.png')
    print(f"✓ Saved {img3_path} -> images/add_mcp_form.png")
    
    print("\n✓ All images saved successfully!")
    print("The how_to_add_mcp_to_toqan tool will now return these images as base64 data URLs.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    
    setup_images(sys.argv[1], sys.argv[2], sys.argv[3])
