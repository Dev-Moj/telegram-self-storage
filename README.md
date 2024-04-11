# Telegram Media Downloader(telegram-self-storage)

This Python script is designed to download media files from your Telegram account and send them to your own account. It utilizes the Telethon library, which provides easy-to-use methods for interacting with the Telegram API.

## Setup

Before running the script, you need to set up your Telegram API credentials and specify your phone number in a `.env` file in the root directory of the script. Follow these steps:

1. Go to [https://my.telegram.org/auth](https://my.telegram.org/auth) and log in with your Telegram account.
2. Copy the `api_id` and `api_hash` provided after logging in.
3. Create a `.env` file in the root directory of the script.
4. Paste the `api_id` and `api_hash` into the `.env` file.
5. Also, include your phone number in the `.env` file.

## Usage

1. Run the script using Python.
2. The script will prompt you to log in to your Telegram account. Follow the instructions.
3. Once logged in, the script will start downloading media files from your chats.
4. It will only download files that have a set TTL (Time To Live), ensuring you don't download files that are no longer available.
5. Downloaded files will be sent to your own account.
6. The script will continuously run, checking for new media files to download.

## Dependencies

You can install them using `pip`:

`pip install -r requirements.txt`


## Proxy

If you need to use a proxy to connect to Telegram, you can specify the proxy details in the `proxy` dictionary within the script. Modify the `proxy_type`, `addr`, and `port` fields according to your proxy settings.

## Error Handling

The script is designed to run continuously and handle exceptions gracefully. If any errors occur during execution, they will be caught and the script will continue running.

## Note

- This script is intended for educational purposes and personal use only. Respect the privacy and rights of others when using it.
- Be cautious while downloading media files, as they may contain sensitive or copyrighted content.

By using this script, you agree to abide by Telegram's terms of service and community guidelines.

Enjoy downloading your Telegram media effortlessly! 🚀