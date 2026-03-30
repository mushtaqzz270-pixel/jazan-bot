import asyncio
from telethon import TelegramClient, events

api_id = 34136368
api_hash = "a53fbec24918979bf1af188f47d850ae"

client = TelegramClient("session.session", api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    print("New message:", event.text)

async def main():
    await client.start()
    print("Bot is running...")

    # 👇 هذا أهم سطر (يمنع الإغلاق)
    await asyncio.Event().wait()

asyncio.run(main())