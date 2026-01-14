from fastapi import FastAPI, Query
import requests
from bs4 import BeautifulSoup

app = FastAPI(title="Text Extractor API")

@app.get("/")
def home():
    return {
        "status": "running",
        "usage": "/extract?url=https://example.com"
    }

@app.get("/extract")
def extract_text(url: str = Query(..., description="URL of webpage/app")):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "lxml")

        # remove scripts & styles
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        text = soup.get_text(separator=" ")

        clean_text = " ".join(text.split())

        return {
            "success": True,
            "url": url,
            "text": clean_text
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
