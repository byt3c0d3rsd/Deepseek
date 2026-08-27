#!/usr/bin/env python3
"""
hyprid-vision.py — DeepSeek image vision via the Hyprid AI Gateway.

Downloads a quote image from azquotes.com, encodes it as a data URL, and sends
it along with a text prompt to the /v1/chat/completions endpoint. Uses the
DeepSeek model (deepseek-chat) only.
"""

import base64

import requests

BASE = "http://162.35.180.135:8484/api/v1"
KEY = "hk-XRNFr8oYJ48mp9uPEvrYGmAxOjH28MFkOdhl1azNbzI"
MODEL = "deepseek-chat"

IMG_URL = (
    "https://www.azquotes.com/vangogh-image-quotes/124/25/"
    "Quotation-Albert-Einstein-Weak-people-revenge-Strong-people-forgive-"
    "Intelligent-People-Ignore-124-25-28.jpg"
)

img_r = requests.get(IMG_URL, timeout=30)
img_r.raise_for_status()
b64 = base64.b64encode(img_r.content).decode()
mime = img_r.headers.get("Content-Type", "image/jpeg")

r = requests.post(
    f"{BASE}/chat/completions",
    headers={
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
    },
    json={
        "model": MODEL,
        "stream": False,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Read the image and tell me what it says."},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:{mime};base64,{b64}"},
                    },
                ],
            }
        ],
    },
    timeout=240,
)
r.raise_for_status()
d = r.json()

print(f"model   : {d.get('model')}")
print(f"reply   : {d['choices'][0]['message']['content']}")
