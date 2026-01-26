#!/usr/bin/env python3
"""
Save the screenshots from base64 data embedded in this script.
Run this to create the actual image files.
"""

import base64
import os

# These will be populated with actual base64 data
# For now, creating a script that you can populate with the image data

def save_image_from_base64(base64_data, filename):
    """Decode base64 and save as image file."""
    if not base64_data or base64_data == "PLACEHOLDER":
        print(f"Skipping {filename} - no data provided")
        return
    
    try:
        # Remove data URL prefix if present
        if base64_data.startswith('data:image'):
            base64_data = base64_data.split(',', 1)[1]
        
        image_data = base64.b64decode(base64_data)
        
        os.makedirs('images', exist_ok=True)
        with open(filename, 'wb') as f:
            f.write(image_data)
        print(f"✓ Saved {filename}")
    except Exception as e:
        print(f"✗ Error saving {filename}: {e}")

if __name__ == "__main__":
    # TODO: Populate these with actual base64 data from the screenshots
    images = {
        'images/agent_interface.png': 'PLACEHOLDER',
        'images/tools_tab.png': 'PLACEHOLDER',
        'images/add_mcp_form.png': 'PLACEHOLDER'
    }
    
    for filename, data in images.items():
        save_image_from_base64(data, filename)
    
    print("\nNote: This script has placeholder data.")
    print("The images from the chat need to be manually saved.")
    print("\nOptions:")
    print("1. Use screenshot tool to capture the images from chat")
    print("2. If on Mac, use Cmd+Shift+4 to capture each image")
    print("3. Save directly to the images/ folder with the correct names")
