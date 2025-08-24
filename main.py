import asyncio
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest


api_id = 21215205
api_hash = '97bbb227522aa1983bf39eb8ae53809a'

client = TelegramClient('my_session', api_id, api_hash)

async def update_bio():
    while True:
        now = datetime.now().strftime("%H:%M")
        bio_text = f'{now}'
        await client(UpdateProfileRequest(about=bio_text))
        print(f'Updated bio to: {bio_text}')
        await asyncio.sleep(60)  
async def main():
    await update_bio()

with client:
    client.loop.run_until_complete(main())