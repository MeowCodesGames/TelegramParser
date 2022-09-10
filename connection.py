from config import client

# Connecting to Telegramm API
async def client_connect():
    await client.connect()