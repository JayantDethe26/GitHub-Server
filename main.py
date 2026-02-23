from fastmcp import FastMCP
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
    """Get basic information about a GitHub repository"""
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
def github_get_file_by_name(owner: str, repo: str, filename: str, branch: str = "main") -> str:
    """
    Search the repository for a file by name and return its contents.
    User does NOT need to provide full path.
    """
    try:
        # Fetch repo tree
        tree_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
        tree_response = requests.get(tree_url, timeout=10)

        if tree_response.status_code != 200:
            return f"Could not fetch repo tree: {tree_response.status_code}"

        tree_data = tree_response.json()

        for item in tree_data.get("tree", []):
            if item["type"] == "blob" and item["path"].endswith(filename):
                file_path = item["path"]

                raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_path}"
                file_response = requests.get(raw_url, timeout=10)

                if file_response.status_code != 200:
                    return f"Found file but failed to fetch content: {file_response.status_code}"

                content = file_response.text

                if len(content) > 4000:
                    content = content[:4000] + "\n\n... (truncated)"

                return f"📂 Found at: {file_path}\n\n{content}"

        return f"File '{filename}' not found in repository."

    except Exception as e:
        return f"Error: {str(e)}"


# -------------------------
# Simple Prompt (for UI visibility)
# -------------------------
@mcp.prompt()
def test_prompt():
    """Test prompt to confirm MCP connection"""
    return "Hello from GitHub MCP 🚀"


# -------------------------
# Run MCP Server (Render Production Ready)
# -------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))

    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=port,
    )