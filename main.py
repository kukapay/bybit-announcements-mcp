import httpx
from typing import Optional, List, Dict, Any
from datetime import datetime

from mcp.server.fastmcp import FastMCP
from mcp.types import CallToolResult, TextContent


mcp = FastMCP("Bybit Announcements MCP Server")


def _fetch_announcements(
    locale: str,
    type_: Optional[str] = None,
    tag: Optional[str] = None,
    page: int = 1,
    limit: int = 20,
) -> List[Dict[str, Any]]:
    """
    Internal helper to fetch raw announcements as list of dicts.
    """
    if limit > 50:
        raise ValueError("Limit must not exceed 50.")

    url = "https://api.bybit.com/v5/announcements/index"
    params = {
        "locale": locale,
        "page": page,
        "limit": limit,
    }
    if type_:
        params["type"] = type_
    if tag:
        params["tag"] = tag

    with httpx.Client() as client:
        response = client.get(url, params=params)
        data = response.json()

    if data.get("retCode") != 0:
        raise ValueError(f"API Error: {data.get('retMsg', 'Unknown error')}")

    result = data.get("result", {})
    announcements = result.get("list", [])
    return announcements


@mcp.tool()
def get_announcements(
    locale: str = "en-US",
    type_: Optional[str] = None,
    tag: Optional[str] = None,
    page: int = 1,
    limit: int = 20,
) -> str:
    """
    Fetch Bybit announcements and return them as a formatted list.

    Args:
        locale: Language for announcements (e.g., 'en-US', 'zh-TW').
        type_: Optional announcement type (e.g., 'new_crypto').
        tag: Optional announcement tag (e.g., 'Spot').
        page: Page number for pagination (default: 1).
        limit: Number of results per page (default: 20, max: 50).

    Returns:
        A formatted string of announcements.
    """
    anns = _fetch_announcements(locale, type_, tag, page, limit)
    if not anns:
        return "No announcements found."

    content = f"Bybit Announcements (Page {page}, Limit {limit}):\n\n"
    for ann in anns:
        title = ann.get("title", "N/A")
        desc = ann.get("description", "")
        url = ann.get("url", "")
        pub_ts = ann.get("publishTime") or ann.get("dateTimestamp")
        if pub_ts:
            time_str = datetime.fromtimestamp(pub_ts / 1000).strftime('%Y-%m-%d %H:%M')
        else:
            time_str = "N/A"

        start_ts = ann.get("startDateTimestamp")
        end_ts = ann.get("endDateTimestamp")
        if start_ts and end_ts:
            start_str = datetime.fromtimestamp(start_ts / 1000).strftime('%Y-%m-%d %H:%M')
            end_str = datetime.fromtimestamp(end_ts / 1000).strftime('%Y-%m-%d %H:%M')
            time_range = f"{start_str} ~ {end_str}"
        elif start_ts:
            start_str = datetime.fromtimestamp(start_ts / 1000).strftime('%Y-%m-%d %H:%M')
            time_range = start_str
        else:
            time_range = ""

        content += f"### {title} - {time_str}\n\n{time_range}\n\n{desc}\n\n{url}\n\n---\n\n"
    return content

if __name__ == "__main__":
    mcp.run()
