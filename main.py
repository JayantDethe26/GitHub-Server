from mcp.server.fastmcp import FastMCP
import uvicorn
import requests
import os

# Create MCP server
mcp = FastMCP("GitHub")


# -------------------------
# Basic Math Tool
# -------------------------
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# -------------------------
# GitHub Repo Info Tool
# -------------------------
@mcp.tool()
def github_repo_info(owner: str, repo: str) -> str:
    """
    Get basic information about a GitHub repository
    """
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}"
        r = requests.get(url, timeout=10)

        if r.status_code != 200:
            return f"GitHub API returned {r.status_code}"

        data = r.json()

        return (
            f"Repository: {data.get('full_name')}\n"
            f"Description: {data.get('description')}\n"
            f"Stars: ⭐ {data.get('stargazers_count')}\n"
            f"Forks: {data.get('forks_count')}\n"
            f"Language: {data.get('language')}"
        )

    except Exception as e:
        return f"Error fetching repo info: {str(e)}"


# -------------------------
# GitHub File Fetch Tool
# -------------------------
@mcp.tool()
def github_get_file(owner: str, repo: str, path: str, branch: str = "main") -> str:
    """
    Fetch a file's content from a public GitHub repository.

    Example:
    owner = JayantDethe26
    repo = IntervueAI
    path = README.md
    branch = main
    """
    try:
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
        r = requests.get(raw_url, timeout=10)

        if r.status_code != 200:
            return f"File not found or error: {r.status_code}"

        content = r.text

        # Limit size to avoid huge responses
        if len(content) > 4000:
            content = content[:4000] + "\n\n... (truncated)"

        return content

    except Exception as e:
        return f"Error fetching file: {str(e)}"


# -------------------------
# Simple Prompt (for UI visibility)
# -------------------------
@mcp.prompt()
def test_prompt():
    """Test prompt to confirm MCP connection"""
    return "Hello from Demo MCP 🚀"


# -------------------------
# Run MCP Server (IMPORTANT)
# -------------------------
if __name__ == "__main__":
    mcp.run(transport="streamable-http")

