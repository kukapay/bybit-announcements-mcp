# Bybit Announcements MCP

An MCP server that empowers AI agents to fetch, track, and act on Bybit announcements efficiently.

![GitHub License](https://img.shields.io/github/license/kukapay/bybit-announcements-mcp) 
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-active-brightgreen.svg)

## Features

- **Rich Querying**: Filter announcements by locale (e.g., `en-US`, `zh-TW`), type (e.g., `new_crypto`), tag (e.g., `Spot`), page, and limit (up to 50 results).
- **Formatted Output**: Returns clean, readable Markdown with titles, timestamps, event ranges, descriptions, and URLs—no raw JSON clutter.

## Installation

1. **Prerequisites**:
   - Python 3.10+
   - [uv](https://docs.astral.sh/uv/) (recommended for dependency management) or pip.

2. **Clone & Install**:
   ```bash
   git clone https://github.com/kukapay/bybit-announcements-mcp.git
   cd bybit-announcements-mcp
   uv sync 
   ```

3. Install to Claude Desktop:

   Install the server as a Claude Desktop application:
   ```bash
   uv run mcp install main.py --name "Bybit Announcements"
   ```

   Configuration file as a reference:

   ```json
   {
      "mcpServers": {
          "Bybit Announcements": {
              "command": "uv",
              "args": [ "--directory", "/path/to/bybit-announcements-mcp", "run", "main.py" ]
          }
      }
   }
   ```
   
   Replace /path/to/bybit-announcements-mcp with your actual installation path.
   
## Usage

The server exposes one core tool: `get_announcements`. Call it from your MCP client to fetch and format data.

### Tool: `get_announcements`
- **Description**: Retrieves Bybit announcements with customizable filters.
- **Arguments**:
  - `locale` (str, default: `"en-US"`): Language (e.g., `"en-US"`, `"zh-TW"`).
  - `type_` (str, optional): Announcement type (e.g., `"new_crypto"`, `"latest_activities"`).
  - `tag` (str, optional): Tag filter (e.g., `"Spot"`, `"Derivatives"`).
  - `page` (int, default: `1`): Pagination page.
  - `limit` (int, default: `20`, max: `50`): Results per page.
- **Returns**: A Markdown-formatted string like:
  ```
  Bybit Announcements (Page 1, Limit 20):

  ### New Listing: Arbitrum (ARB) — Deposit, Trade and Stake ARB to Share a 400,000 USDT Prize Pool! - 2023-03-17 10:00
  2023-03-17 10:00 ~ 2023-03-24 10:00

  Bybit is excited to announce the listing of ARB on our trading platform!

  https://announcements.bybit.com/en-US/article/new-listing-arbitrum-arb-deposit-trade-and-stake-arb-to-share-a-400-000-usdt-prize-pool--bltf662314c211a8616/

  ---

  ### 🔥 Listing of PIEVERSE on Convert & Bybit Savings - 2025-11-14 21:17

  2025-11-14 16:53 ~ 2025-11-14 16:53

  Bybit will be listing PIEVERSE on Convert on Nov 14, 2025, 1:30PM UTC and Bybit Savings at the respective dates and timings listed below.

  https://announcements.bybit.com/en-US/article/-listing-of-pieverse-on-convert-blt7a4a65a0b5cce7c2/

  ---
  ```

## License

MIT License. See [LICENSE](LICENSE) for details.

