import requests
import time
from config import BOT_TOKEN, CHAT_ID

KEYWORDS = [
    "hiring discord moderator",
    "discord mod hiring",
    "looking for discord mod",
    "discord moderator needed"
]

CONTEXT = ["nft", "crypto", "web3", "game", "gaming", "solana", "ethereum"]

seen = set()

def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check():
    url = "https://nitter.net/search?f=tweets&q=discord+mod+hiring"
    r = requests.get(url)

    text = r.text.lower()

    for k in KEYWORDS:
        for c in CONTEXT:
            if k in text and c in text:
                if text not in seen:
                    seen.add(text)
                    send(f"🚨 Hiring found for: {k} ({c})")
                    print("FOUND:", k, c)

while True:
    try:
        check()
        time.sleep(60)
    except Exception as e:
        print("Error:", e)
        time.sleep(60)
