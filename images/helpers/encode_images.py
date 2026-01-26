import base64
import sys

def image_to_base64_data_url(image_path: str) -> str:
    """Convert an image file to a base64 data URL."""
    with open(image_path, 'rb') as image_file:
        encoded = base64.b64encode(image_file.read()).decode('utf-8')
    
    # Determine MIME type from extension
    ext = image_path.lower().split('.')[-1]
    mime_types = {
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'gif': 'image/gif',
        'webp': 'image/webp'
    }
    mime_type = mime_types.get(ext, 'image/png')
    
    return f"data:{mime_type};base64,{encoded}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python encode_images.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    print(image_to_base64_data_url(image_path))
