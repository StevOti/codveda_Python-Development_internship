try:
    import requests
except Exception:
    # Provide a minimal stub so importing this module doesn't fail
    class _MissingRequests:
        def get(self, *a, **k):
            raise ImportError('requests not installed')

    requests = _MissingRequests()

import re


def fetch_title(url, timeout=5):
    """Fetch a page and return the <title> text (simple extraction).

    Uses a regex so BeautifulSoup is not required for tests.
    Returns None on error or if no title found.
    """
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        m = re.search(r"<title>(.*?)</title>", resp.text, re.IGNORECASE | re.DOTALL)
        if m:
            return m.group(1).strip()
        return None
    except Exception:
        return None


def fetch_text(url, timeout=5):
    """Return raw text content for a URL or None on error."""
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp.text
    except Exception:
        return None
