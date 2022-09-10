from config import client
from connection import client_connect
from authorization import client_auth
from spammer import chats_parser, send_spam

async def start():
    await client_connect()
    await client_auth()
    users = await chats_parser()
    await send_spam(users)

client.loop.run_until_complete(start())