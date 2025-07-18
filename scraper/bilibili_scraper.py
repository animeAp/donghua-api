import requests
from bs4 import BeautifulSoup

def get_latest_anime():
    url = "https://www.bilibili.tv/en"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Dummy response for now
    return [
        {"title": "Dragon Soul Rebirth", "link": "https://bilibili.tv/anime/12345"},
        {"title": "Martial God Ascension", "link": "https://bilibili.tv/anime/67890"}
    ]
