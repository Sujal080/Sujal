
# Telegram Video Converter Bot (Render-Ready)

✅ Converts any document file to MP4 video using FFmpeg (ultrafast — 1 minute conversion).

## Features

- Accepts large files up to 2GB
- Converts to MP4 with optimized FFmpeg settings
- Replies with the converted video
- Ready to deploy on **Render**

## How to Deploy on Render

1. Go to [https://render.com](https://render.com)
2. Create a **New Web Service**
3. Upload this ZIP as a GitHub repo or connect directly
4. Set the following Environment Variables:
    - `BOT_TOKEN`
    - `API_ID`
    - `API_HASH`
5. Set **Start Command** to:
```
python3 bot.py
```
6. Choose a plan (Starter or better recommended for speed)

## FFmpeg Optimization

- `-preset ultrafast` → max speed
- `-crf 28` → decent quality
- `-c:a aac -b:a 128k` → audio compatible with Telegram

---
