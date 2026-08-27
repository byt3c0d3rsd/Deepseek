#!/usr/bin/env python3
"""hyprid-chat.py — Interactive CLI chat with DeepSeek via Hyprid AI Gateway."""

import requests

BASE = "http://162.35.180.135:8484/api/v1"
KEY = "hk-XRNFr8oYJ48mp9uPEvrYGmAxOjH28MFkOdhl1azNbzI"
MODEL = "deepseek-chat"

print(f"DeepSeek interactive chat (Hyprid AI Gateway)")
print(f"Model: {MODEL}")
print(f"Server: {BASE}")
print("Type 'quit', 'exit', or Ctrl-C to stop.\n")

messages = []

while True:
    try:
        user = input("> ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        break

    if not user:
        continue
    if user.lower() in ("quit", "exit"):
        break

    messages.append({"role": "user", "content": user})

    r = requests.post(
        f"{BASE}/chat/completions",
        headers={
            "Authorization": f"Bearer {KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "stream": False,
            "messages": messages,
        },
        timeout=120,
    )
    r.raise_for_status()
    d = r.json()

    reply = d["choices"][0]["message"]["content"].strip()
    print(f"\n< {reply}\n")

    messages.append({"role": "assistant", "content": reply})
