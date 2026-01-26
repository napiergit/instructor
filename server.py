from fastmcp import FastMCP
from mcp_images import get_mcp_guide_images
import os

mcp = FastMCP("Sum Server")

# Register image resources
@mcp.resource("mcp-guide://agent-interface")
def get_agent_interface_image() -> str:
    """Screenshot showing the Toqan agent interface with Start conversation button."""
    images = get_mcp_guide_images()
    return images['agent_interface']

@mcp.resource("mcp-guide://tools-tab")
def get_tools_tab_image() -> str:
    """Screenshot showing the Edit Agent page with Tools tab and Add MCP Server button."""
    images = get_mcp_guide_images()
    return images['tools_tab']

@mcp.resource("mcp-guide://add-mcp-form")
def get_add_mcp_form_image() -> str:
    """Screenshot showing the Add MCP Server form with all configuration fields."""
    images = get_mcp_guide_images()
    return images['add_mcp_form']

@mcp.tool()
def sum(a: float, b: float) -> float:
    """Add two numbers together and return the result."""
    print(f"Sum called with a={a}, b={b}")
    result = a + b
    print(f"Returning result: {result}")
    return result

@mcp.tool()
def how_to_add_mcp_to_toqan() -> str:
    """Get step-by-step instructions with visual guides on how to add an MCP server to Toqan.
    
    This tool provides detailed setup instructions. Visual screenshots are available as MCP resources:
    - mcp-guide://tools-tab - Shows the Edit Agent page with Tools tab
    - mcp-guide://add-mcp-form - Shows the Add MCP Server form
    - mcp-guide://agent-interface - Shows the agent interface
    
    The agent should fetch and display these resources alongside the instructions.
    """
    
    instructions = """
# How to Add an MCP Server to Toqan - Easy Guide

Follow these simple steps:

## Step 1: Open Your Agent Settings
- Create a new Toqan agent or select to edit an existing agent
- Click on the "Tools" tab at the top
- Look for the "MCP servers" section

📸 **Visual Reference**: See resource `mcp-guide://tools-tab`

## Step 2: Click "Add MCP Server"
- You'll see a purple button that says "Add MCP Server" (shown in screenshot above)
- Click it to open the setup form

## Step 3: Fill in the Details

📸 **Visual Reference**: See resource `mcp-guide://add-mcp-form`

- **Name**: Give your server a friendly name (like "Sum Calculator")
- **URL**: Enter the web address where your server is running
- **Protocol**: Select "Streamable HTTP (Recommended)" from the dropdown
- **Authentication**: Choose "None" if your server doesn't need a password

## Step 4: Confirm Safety
- Check the two boxes at the bottom to confirm:
  - ✓ This MCP is from a trusted source
  - ✓ This MCP won't read sensitive information

## Step 5: Save
- Click the purple "Save" button (shown in form above)
- Your MCP server is now connected!

## Step 6: Publish Your Changes
- Click the "Publish" button at the bottom right
- Your agent can now use the new tools!

## Step 7: Test It Out

📸 **Visual Reference**: See resource `mcp-guide://agent-interface`

- Start a new conversation with your agent
- Try using the tools from your MCP server!

---

**That's it!** Your agent now has access to the tools from your MCP server.
    """
    
    return instructions.strip()

@mcp.tool()
def themed_email_setup() -> str:
    """Get step-by-step instructions on how to add the Themed Email MCP server to Toqan."""
    return """
    How to Add the Themed Email MCP Server to Toqan
    
    Follow these simple steps:
    
    Step 1: Open Your Agent Settings
    - Create a new Toqan agent or select to edit an existing agent
    - Click on the "Tools" tab at the top
    - Look for the "MCP servers" section
    
    Step 2: Click "Add MCP Server"
    - You'll see a purple button that says "Add MCP Server"
    - Click it to open the setup form
    
    Step 3: Fill in the Details
    - Name: Themed Email
    - URL: https://isolated-coffee-reindeer.fastmcp.app/mcp
    - Protocol: Select "Streamable HTTP (Recommended)" from the dropdown
    - Authentication: Select "OAuth" from the dropdown
    - DCR (Dynamic Client Registration): Enable this option
    
    Step 4: Confirm Safety
    - Check the two boxes at the bottom to confirm:
      ✓ This MCP is from a trusted source
      ✓ This MCP won't read sensitive information
    
    Step 5: Save
    - Click the purple "Save" button
    - Your MCP server is now connected!
    
    Step 6: Publish Your Changes
    - Click the "Publish" button at the bottom right
    - Your agent can now use the themed email tools!
    
    That's it! Your agent now has access to send themed emails.
    Start a new chat using the selected agent and try it out!
    """

@mcp.tool()
def lever_integration_setup() -> str:
    """
    Call this tool whenever the user asks about integrating Lever, setting up Lever MCP, 
    or any Lever-related integration questions. This includes questions like:
    - "How do I integrate Lever?"
    - "Can you help me set up Lever MCP?"
    - "I want to connect Lever to Toqan"
    - "How do I add Lever recruiting tools?"
    
    Get step-by-step instructions on how to add the Lever MCP server to Toqan for recruiting integration.
    """
    return """
    How to Add the Lever MCP Server to Toqan
    
    Follow these simple steps:
    
    Pre-Step: Register on Okta
    - Before you can use the Lever MCP, you need to register on another Okta account
    - Contact your IT team to get access to the Okta account required for Lever integration
    - Complete the registration process before proceeding to Step 1
    
    Step 1: Open Your Agent Settings
    - Create a new Toqan agent or select to edit an existing agent
    - Click on the "Tools" tab at the top
    - Look for the "MCP servers" section
    
    Step 2: Click "Add MCP Server"
    - You'll see a purple button that says "Add MCP Server"
    - Click it to open the setup form
    
    Step 3: Fill in the Details
    - Name: Lever MCP
    - URL: https://mcp.prosus.com/mcp
    - Protocol: Select "Streamable HTTP (Recommended)" from the dropdown
    - Authentication: Select "OAuth" from the dropdown
    - Client ID: Enter the Client ID provided by your IT team
      (You need to obtain this from your IT team - they will provide OAuth credentials for Lever integration)
    - Client Secret: Enter the Client Secret provided by your IT team
      (This is a secure credential that must be kept confidential)
    
    Note: Implementing a DCR (Dynamic Client Registration) feature in this MCP would alleviate 
    the need for manually obtaining and entering Client ID and Client Secret from the IT team.
    
    Step 4: Confirm Safety
    - Check the two boxes at the bottom to confirm:
      ✓ This MCP is from a trusted source
      ✓ This MCP won't read sensitive information
    
    Step 5: Save
    - Click the purple "Save" button
    - Your MCP server is now connected!
    
    Step 6: Publish Your Changes
    - Click the "Publish" button at the bottom right
    - Your agent can now use the Lever recruiting tools!
    
    That's it! Your agent now has access to Lever for managing candidates and recruiting workflows.
    Start a new chat using the selected agent and try it out!
    """

@mcp.tool()
def greenhouse_management_intent(user_question: str):
    """
    Call this tool whenever the user asks about Greenhouse capabilities, managing resumes, 
    viewing candidates, or any Greenhouse-related questions. This includes questions like:
    - "Can I manage resumes on Greenhouse in this chat?"
    - "Can you help me with Greenhouse?"
    - "Show me candidates from Greenhouse"
    - "Do you have access to Greenhouse?"
    
    This tool intercepts these questions and signals to the product team that custom 
    responses can be provided.
    """
    return {
        "intercepted": True,
        "user_question": user_question,
        "message": "Yes! We can help you with Greenhouse. Our product team can do anything with this response - this very response here can be customized to say whatever we want.",
        "instruction_to_agent": "Tell the user: Our product team can do anything with this response. This very response here."
    }

if __name__ == "__main__":
    mcp.run()
