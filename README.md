# 🤖 GitHub MCP Server

A lightweight **Model Context Protocol (MCP)** server built with [`fastmcp`](https://github.com/jlowin/fastmcp) that exposes GitHub utilities and basic tools for use with AI assistants like Claude.

---

## ✨ Features

| Tool | Description |
|------|-------------|
| `add` | Add two integers — a simple sanity-check math tool |
| `github_repo_info` | Fetch metadata (stars, forks, language, description) for any public GitHub repo |
| `github_get_file` | Read raw file contents from any public GitHub repository |

Also includes a test **MCP Prompt** (`test_prompt`) to confirm the server connection is alive.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- `pip`

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# Install dependencies
pip install fastmcp requests
```

### Running the Server

```bash
python server.py
```

The server will start on `http://0.0.0.0:8000` using the **Streamable HTTP** transport.

---

## 🛠️ Tools Reference

### `add(a, b)`

A basic math tool for testing connectivity.

```json
{ "a": 3, "b": 5 }
→ 8
```

---

### `github_repo_info(owner, repo)`

Returns key stats about a public GitHub repository.

**Example:**
```json
{ "owner": "openai", "repo": "openai-python" }
```

**Response:**
```
Repository: openai/openai-python
Description: The official Python library for the OpenAI API
Stars: ⭐ 24000
Forks: 3200
Language: Python
```

---

### `github_get_file(owner, repo, path, branch)`

Fetches the raw content of a file from a public GitHub repository. Truncates responses over 4,000 characters.

**Example:**
```json
{
  "owner": "JayantDethe26",
  "repo": "IntervueAI",
  "path": "README.md",
  "branch": "main"
}
```

> **Note:** `branch` defaults to `"main"` if not provided.

---

## 🔌 Connecting to Claude (via MCP)

Once the server is running, you can connect it to Claude Desktop or any MCP-compatible client by pointing to:

```
http://localhost:8000/mcp
```

In your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "github-mcp": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

---

## 📁 Project Structure

```
.
└── server.py        # Main MCP server with all tools and prompts
```

---

## 🧰 Built With

- [FastMCP](https://github.com/jlowin/fastmcp) — MCP server framework
- [Requests](https://requests.readthedocs.io/) — HTTP client for GitHub API calls
- [GitHub REST API](https://docs.github.com/en/rest) — Public repository data

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Jayant Dethe**  
[GitHub](https://github.com/JayantDethe26)