import base64
import json

IMAGES_DATA = {
    "agent_interface": "/9j/4AAQSkZJRgABAQAAAQABAAD/...",
    "tools_tab": "/9j/4AAQSkZJRgABAQAAAQABAAD/...",
    "add_mcp_form": "/9j/4AAQSkZJRgABAQAAAQABAAD/..."
}

def save_images_json():
    """Save placeholder for images - user needs to provide actual base64 data"""
    with open('mcp_guide_images.json', 'w') as f:
        json.dump(IMAGES_DATA, f, indent=2)
    print("Created mcp_guide_images.json - please update with actual base64 image data")

if __name__ == "__main__":
    save_images_json()
