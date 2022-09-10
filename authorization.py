from config import PHONE, client
from telethon.errors.rpcerrorlist import SessionPasswordNeededError

# Client authorization - needed to work only for the first launch, if you had no session file (.session)
async def client_auth():
    if not await client.is_user_authorized():
        await client.send_code_request(PHONE)
        try:
            await client.sign_in(PHONE, input('Enter verification code: ')) # Code that you receive on Telegram account
                                                                            # from Telegram
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Enter your password: '))  # For the two-factor authentication