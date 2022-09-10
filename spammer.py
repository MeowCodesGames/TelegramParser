from config import client
import time
import random
import logging
from telethon.errors.rpcerrorlist import PeerFloodError

# Functionality for parsing and then spamming users
async def chats_parser():
    chats = [dialog for dialog in await client.get_dialogs() if dialog.is_group]
    print('Choose the chat you want to parse members from: ')
    # Console output of avaliable chats you want to parse members from
    [print(str(chats.index(i)) + ' - ' + i.title) for i in chats]

    your_choice = input('Input chats name: ')

    # Chat's members list iteration, then ID's members list creates
    users = [user.id for user in await client.get_participants(your_choice) if user.id]
    return users

async def send_spam(users):
    message = ['Hello!', 'Ola!', 'Ni Hao!']
    for user in users[:39]:

        # Creating delay to avoid Flood Exceptions
        delay = random.randint(15, 40)
        print("Sending message to: ", user)

        # Exceptions to protect your account from ban for flood and spam
        try:
            await client.send_message(user, random.choice(message))
        except PeerFloodError:
            logging.error('[!] Flood excepiton. Kill the programm. \n[!] Try later.')
            await client.disconnect()
            break

        # Other exceptions
        except Exception as e:
            logging.warning('[!] Excepiton:', e, '\n Trying complete to work...')
            continue
        else:
            if user != users[:39]:
                print(f"Waiting {delay} sec")
                time.sleep(delay)

    logging.INFO('\n End of the programm!')