# Basic MCP Server with HTTP Transport

A minimal MCP server using fastMCP with HTTP/SSE transport and a single `sum` tool.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

Start the server:
```bash
python server.py
```

The server will be available at `http://localhost:8000/mcp` with SSE transport.

## Available Tools

- **sum(a: float, b: float)**: Adds two numbers together and returns the result.

## Usage

The server uses Server-Sent Events (SSE) transport and is accessible at the `/mcp` endpoint. Connect using any MCP client that supports HTTP/SSE transport.
