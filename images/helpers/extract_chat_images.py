#!/usr/bin/env python3
"""
Extract images from the chat and save them to the images directory.
This script will create placeholder images that you can replace.
"""

from PIL import Image
import os

def create_placeholder_image(filename, width=800, height=600, text=""):
    """Create a placeholder image."""
    img = Image.new('RGB', (width, height), color='lightgray')
    img.save(filename)
    print(f"Created placeholder: {filename}")

if __name__ == "__main__":
    os.makedirs('images', exist_ok=True)
    
    # Create placeholders - you'll need to replace these with actual screenshots
    create_placeholder_image('images/agent_interface.png', 600, 600, 'Agent Interface')
    create_placeholder_image('images/tools_tab.png', 1000, 500, 'Tools Tab')
    create_placeholder_image('images/add_mcp_form.png', 1000, 900, 'Add MCP Form')
    
    print("\nPlaceholder images created. Please replace them with actual screenshots:")
    print("1. Take/save the screenshots from the chat")
    print("2. Replace the files in the images/ directory")
