from fastmcp import FastMCP

mcp = FastMCP("Sum Server", auth_enabled=False)

@mcp.tool()
def sum(a: float, b: float) -> float:
    """Add two numbers together and return the result."""
    print(f"Sum called with a={a}, b={b}")
    result = a + b
    print(f"Returning result: {result}")
    return result

@mcp.tool()
def how_to_add_mcp_to_toqan() -> str:
    """Get simple step-by-step instructions on how to add an MCP server to Toqan."""
    return """
    How to Add an MCP Server to Toqan - Easy Guide
    
    Follow these simple steps:
    
    Step 1: Open Your Agent Settings
    - Go to your Toqan agent
    - Click on the "Tools" tab at the top
    - Look for the "MCP servers" section
    
    Step 2: Click "Add MCP Server"
    - You'll see a purple button that says "Add MCP Server"
    - Click it to open the setup form
    
    Step 3: Fill in the Details
    - Name: Give your server a friendly name (like "Sum Calculator")
    - URL: Enter the web address where your server is running
    - Protocol: Select "Streamable HTTP (Recommended)" from the dropdown
    - Authentication: Choose "None" if your server doesn't need a password
    
    Step 4: Confirm Safety
    - Check the two boxes at the bottom to confirm:
      ✓ This MCP is from a trusted source
      ✓ This MCP won't read sensitive information
    
    Step 5: Save
    - Click the purple "Save" button
    - Your MCP server is now connected!
    
    Step 6: Publish Your Changes
    - Click the "Publish" button at the bottom right
    - Your agent can now use the new tools!
    
    That's it! Your agent now has access to the tools from your MCP server.
    """

if __name__ == "__main__":
    mcp.run()
