import base64
import os

def get_image_base64(image_path: str) -> str:
    """Convert an image file to base64 data URL."""
    if not os.path.exists(image_path):
        return ""
    
    with open(image_path, 'rb') as f:
        encoded = base64.b64encode(f.read()).decode('utf-8')
    
    ext = image_path.lower().split('.')[-1]
    mime_type = f'image/{ext}' if ext in ['png', 'jpg', 'jpeg', 'gif', 'webp'] else 'image/png'
    
    return f"data:{mime_type};base64,{encoded}"

def get_mcp_guide_images():
    """Get all MCP setup guide images as base64 data URLs."""
    base_dir = os.path.dirname(__file__)
    images_dir = os.path.join(base_dir, 'images')
    
    return {
        "agent_interface": get_image_base64(os.path.join(images_dir, 'agent_interface.png')),
        "tools_tab": get_image_base64(os.path.join(images_dir, 'tools_tab.png')),
        "add_mcp_form": get_image_base64(os.path.join(images_dir, 'add_mcp_form.png'))
    }
