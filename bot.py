import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_TOKEN, API_ID, API_HASH

bot = Client("my_video_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

@bot.on_message(filters.private & filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("👋 कोई भी फाइल भेजिए, मैं उसे MP4 वीडियो में कन्वर्ट करूँगा (1 मिनट में)!")

@bot.on_message(filters.private & filters.document)
async def convert_file(client, message: Message):
    file = message.document
    if file.file_size > 2_000_000_000:
        return await message.reply_text("❌ फाइल 2GB से बड़ी है।")

    status = await message.reply_text("📥 डाउनलोड हो रहा है...")
    downloaded = await message.download()
    await status.edit_text("🎬 वीडियो में कन्वर्ज़न चल रही है...")

    output = f"{downloaded}_output.mp4"
    cmd = f"ffmpeg -i \"{downloaded}\" -c:v libx264 -preset ultrafast -crf 28 -c:a aac -b:a 128k \"{output}\" -y"

    process = await asyncio.create_subprocess_shell(cmd)
    await process.communicate()

    if os.path.exists(output):
        await status.edit_text("✅ कन्वर्ज़न पूरी हुई! भेजा जा रहा है...")
        await message.reply_video(video=output, caption="🎞️ Here's your converted video!")
        os.remove(output)
    else:
        await status.edit_text("❌ कन्वर्ज़न फेल हो गया।")

    os.remove(downloaded)

bot.run()
