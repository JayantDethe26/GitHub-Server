🤖 GitHub MCP Server

A lightweight Model Context Protocol (MCP) server built with FastMCP that exposes GitHub utilities for AI assistants like Claude.

This server can run:

🖥 Locally (STDIO or HTTP)

🌍 Remotely (deployed to Render / cloud)

🔌 Connected to any MCP-compatible client

✨ Features
Tool	Description
add	Add two integers (connectivity test tool)
github_repo_info	Fetch metadata (stars, forks, language, description) for any public GitHub repo
github_get_file	Read raw file contents from any public GitHub repository

Includes a test MCP Prompt (test_prompt) to verify connection status.

🚀 How To Use This Server
🖥 Option 1: Run Locally
1️⃣ Install Dependencies
pip install mcp requests

2️⃣ Start the Server
python server.py


If running in HTTP mode, it will start on:

http://localhost:8000


MCP endpoint:

http://localhost:8000/mcp

🔌 Connect to Claude (Local HTTP Mode)

Add this to your claude_desktop_config.json:

{
  "mcpServers": {
    "github-mcp": {
      "url": "http://localhost:8000/mcp"
    }
  }
}


Restart Claude.

🌍 Option 2: Use the Public Deployed Server

If deployed (for example on Render), the MCP endpoint will be:

https://your-app-name.onrender.com/mcp


To use it in Claude:

{
  "mcpServers": {
    "github-mcp": {
      "url": "https://your-app-name.onrender.com/mcp"
    }
  }
}


Now anyone can connect without installing Python.

🛠 Tool Usage Examples

Once connected in Claude, you can use:

🔹 Get Repo Info
Use github-mcp github_repo_info tool for owner=openai repo=openai-python

🔹 Fetch README
Use github-mcp github_get_file tool for owner=JayantDethe26 repo=IntervueAI path=README.md

🔹 Fetch File From Folder
Use github-mcp github_get_file tool for owner=JayantDethe26 repo=IntervueAI path=src/app.py


⚠ The path must match the full relative file path inside the repository.

🧠 How It Works
Claude (or MCP client)
        ↓
GitHub MCP Server
        ↓
GitHub REST API


The server acts as a bridge between AI assistants and GitHub.

🔐 Security Note

This server currently:

Accesses only public repositories

Has no authentication

Has no rate limiting

Before production use, consider adding:

API key protection

Request rate limiting

GitHub token support for private repos

📁 Project Structure
.
└── server.py

🧰 Built With

FastMCP

Requests

GitHub REST API

🚀 Roadmap

Private repo support (GitHub token)

Repo-wide search

Authentication layer

Rate limiting

Docker support

👨‍💻 Author

Jayant Dethe
GitHub: https://github.com/JayantDethe26