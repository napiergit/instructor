#!/bin/bash
# Resize MCP guide screenshots to a smaller width for better display
# Uses macOS built-in sips tool

IMAGES_DIR="$(cd "$(dirname "$0")/.." && pwd)"
MAX_WIDTH=300

echo "Resizing MCP guide images to max width ${MAX_WIDTH}px..."
echo ""

cd "$IMAGES_DIR"

for img in agent_interface.png tools_tab.png add_mcp_form.png; do
    if [ ! -f "$img" ]; then
        echo "✗ Skipping $img - file not found"
        continue
    fi
    
    # Get current dimensions
    width=$(sips -g pixelWidth "$img" | grep pixelWidth | awk '{print $2}')
    height=$(sips -g pixelHeight "$img" | grep pixelHeight | awk '{print $2}')
    
    if [ "$width" -gt "$MAX_WIDTH" ]; then
        # Calculate new height maintaining aspect ratio
        new_height=$((height * MAX_WIDTH / width))
        
        echo "✓ Resizing $img: ${width}x${height} → ${MAX_WIDTH}x${new_height}"
        sips -Z "$MAX_WIDTH" "$img" > /dev/null
    else
        echo "✓ $img: ${width}x${height} (no resize needed)"
    fi
done

echo ""
echo "✓ All images processed!"
echo ""
echo "File sizes:"
ls -lh agent_interface.png tools_tab.png add_mcp_form.png 2>/dev/null | awk '{print "  " $9 ": " $5}'
