try:
    import requests
except Exception:
    class _MissingRequests:
        def get(self, *a, **k):
            raise ImportError('requests not installed')

    requests = _MissingRequests()


def fetch_json(url, timeout=5):
    """Fetch JSON from an API endpoint and return parsed object.

    Returns None on error.
    """
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return None
