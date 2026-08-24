import logging
import requests
from bs4 import BeautifulSoup
from typing import Dict, Any, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 LinkosterAEOBot/1.0"
}

def fetch_url(url: str, timeout: int = 10) -> Optional[requests.Response]:
    """Fetch HTTP response safely with exception handling."""
    try:
        response = requests.get(url, headers=DEFAULT_HEADERS, timeout=timeout)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch URL {url}: {e}")
        return None

def parse_html(html_content: str) -> BeautifulSoup:
    """Parse HTML content cleanly using lxml."""
    return BeautifulSoup(html_content, "lxml")
