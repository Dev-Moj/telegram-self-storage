import os
from datetime import datetime
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

# get https://my.telegram.org/auth > login > copy api_id and api_id > create and past to .env in root script dir
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
phone_number = os.getenv('phone_number')

proxy = {
    'proxy_type': 'HTTP',# HTTP and MTproto
    'addr': '127.0.0.1',
    'port': 8889,
    # secret:'***********',
}

client = TelegramClient('session_name', api_id, api_hash, proxy=proxy)


async def main():
    await client.start(phone=phone_number)
    print('started....')
    async for dialog in client.iter_dialogs(limit=100):
        if dialog.is_user:
            entity = dialog.entity
            async for message in client.iter_messages(entity, offset_date=datetime.now(), limit=20):
                if message.file and message.media.ttl_seconds:
                    fname = f'{message.id}.{message.file.mime_type.split("/")[1]}'
                    if not os.path.exists(fname):
                        print('Downloading...')
                        await client.download_media(message.media, fname)
                        await client.send_file('me', open(fname, 'rb'))
                        print('done...')


while True:
    try:
        client.loop.run_until_complete(main())
    except Exception as e:
        pass
