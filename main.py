from fastmcp import FastMCP
import os

mcp = FastMCP("Test")

@mcp.tool()
def ping() -> str:
    return "pong"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=port,
        path="/mcp"   # 🔥 ADD THIS
    )