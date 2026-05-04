from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ safer init
api_key = os.getenv("TAVILY_API_KEY")
if not api_key:
    raise ValueError("TAVILY_API_KEY is missing in .env")

tavily = TavilyClient(api_key=api_key)


# 🔍 Web Search Tool
@tool
def websearch(query: str) -> str:
    """Search the web for recent and reliable information. Returns titles, URLs, and snippets."""
    try:
        results = tavily.search(query=query, max_results=5)

        out = []
        for r in results.get("results", []):
            out.append(
                f"Title: {r.get('title')}\n"
                f"URL: {r.get('url')}\n"
                f"Snippet: {r.get('content', '')[:300]}\n"
            )

        return "\n----\n".join(out) if out else "No results found."

    except Exception as e:
        return f"Search failed: {str(e)}"


# 🌐 Scrape Tool
@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL."""
    try:
        resp = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        soup = BeautifulSoup(resp.text, "html.parser")

        # remove unwanted elements
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        return text[:3000] if text else "No readable content found."

    except Exception as e:
        return f"Could not scrape URL: {str(e)}"