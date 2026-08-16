"""
{{ plugin_name }} MCP Server
{{ description }}
"""
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

app = Server("{{ plugin_name }}")

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="example_tool",
            description="Example tool description",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Query parameter"
                    }
                },
                "required": ["query"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "example_tool":
        query = arguments.get("query", "")
        result = f"Processed: {query}"
        return [TextContent(type="text", text=result)]
    
    raise ValueError(f"Unknown tool: {name}")

if __name__ == "__main__":
    mcp.server.stdio.run(app)
