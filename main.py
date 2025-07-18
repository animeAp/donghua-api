from fastapi import FastAPI
from scraper.bilibili_scraper import get_latest_anime

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Donghua API is running"}

@app.get("/anime")
def anime_list():
    return get_latest_anime()
