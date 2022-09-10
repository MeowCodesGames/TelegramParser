from telethon import TelegramClient

# Creating constants for authorization
PHONE = '' # Enter string of your phone number
API_ID = 0 # Enter int of your API_ID that you have to get from TelegramAPI
API_HASH = '' # Enter string of your API_HASH that you have to get from TelegramAPI as well


client = TelegramClient(PHONE, API_ID, API_HASH)