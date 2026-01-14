from fastapi import FastAPI, Query
import requests
from bs4 import BeautifulSoup
import re

app = FastAPI(title="Video URL Extractor API")

@app.get("/")
def home():
    return {"status": "video extractor running"}

@app.get("/extract")
def extract_video(url: str = Query(...)):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers, timeout=15)
    html = r.text

    video_urls = set()

    # mp4 / m3u8 direct
    video_urls.update(re.findall(r'https?://[^"\']+\.mp4', html))
    video_urls.update(re.findall(r'https?://[^"\']+\.m3u8', html))

    # iframe src
    soup = BeautifulSoup(html, "lxml")
    for iframe in soup.find_all("iframe"):
        src = iframe.get("src")
        if src:
            video_urls.add(src)

    return {
        "success": True,
        "found": len(video_urls),
        "videos": list(video_urls)
    }
