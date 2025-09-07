# monitor.py
from telethon import TelegramClient

# Replace with your api_id and api_hash after approval
api_id = 123456
api_hash = 'your_api_hash'
client = TelegramClient('session', api_id, api_hash)

async def main():
    # Example: Fetch messages from a public channel
    async for message in client.iter_messages('channel_username'):
        print(f"Message: {message.text}, Emojis: {message.get_emojis()}")
        # Add logic to save links or notify for specific users

with client:
    client.loop.run_until_complete(main())
