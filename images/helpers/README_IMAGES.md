# MCP Guide Images Setup

This MCP server now returns visual guides with the `how_to_add_mcp_to_toqan` tool.

## Required Images

Please save the following screenshots to the `images/` directory:

1. **agent_interface.png** - Screenshot showing the agent card with "Start conversation" button
2. **tools_tab.png** - Screenshot showing the Edit Agent page with Tools tab and "Add MCP Server" button  
3. **add_mcp_form.png** - Screenshot showing the Add MCP Server form with all fields

## How It Works

The tool now returns a structured dictionary with:
- `instructions`: Step-by-step text guide
- `images`: Dictionary of base64-encoded data URLs for each screenshot
- `display_hint`: Guidance for the consuming agent on how to display the images

The images are automatically loaded and base64-encoded when the tool is called, allowing them to be displayed inline with the instructions.

## Manual Image Setup

Save your three screenshots to the images directory with these names:
```bash
images/agent_interface.png
images/tools_tab.png
images/add_mcp_form.png
```

The images will be automatically loaded and returned as base64 data URLs when the tool is invoked.
