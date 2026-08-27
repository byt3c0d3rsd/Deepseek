# DeepSeek — Hyprid AI Gateway Example Scripts

Two Python examples that call a self-hosted Hyprid AI Gateway `/v1/chat/completions`
endpoint using the **DeepSeek** model (`deepseek-chat`).

## Files

| File | Description |
|------|-------------|
| `hyprid-chat.py` | Interactive CLI chat with DeepSeek — reads your input, keeps the message history alive with each turn, prints the model's reply. |
| `hyprid-vision.py` | Send a downloaded image + a text prompt to DeepSeek's multimodal endpoint and print the reply. |

## Quick start

```bash
python3 hyprid-chat.py
python3 hyprid-vision.py
```

## Model

These examples use **deepseek-chat** only.

## Credits

- **Hyprid AI Gateway** — self-hosted AI proxy for DeepSeek.
- **byt3c0d3rsd** — maintainer.
- **FlashBytes Team** — https://t.me/FlashBytesTeam

## License

[MIT License](LICENSE)
