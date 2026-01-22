from fastmcp import FastMCP

mcp = FastMCP("Sum Server")

@mcp.tool()
def sum(a: float, b: float) -> float:
    """Add two numbers together and return the result."""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="sse")
