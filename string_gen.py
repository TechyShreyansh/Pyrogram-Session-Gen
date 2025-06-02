from telethon.sessions import StringSession
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import PeerUser

micky_ = """
         _  ___    _   _  _     _ 
 / \_/ \(_)(  _ \ ( ) ( )( )   ( )
 |     || || ( (_)| |/ /  \ \_/ / 
 | (_) || || |  _ |   (     \ /   
 | | | || || (_( )| |\ \    | |   
 (_) (_)(_)(____/ ( ) (_)   (_)   
                  /(              
                 (__)             

Copyright (C) 2020-2023 by Tech-Shreyansh@Github, < https://github.com/TechyShreyansh >.
This file is part of < https://github.com/TechyShreyansh/MickyUB_Session-Gen > Project, and is released under the "GNU v3.0 License Agreement".
Please see < https://github.com/TechyShreyansh/STRING-SESSION/blob/main/LICENSE > All rights reserved.
"""

print(micky_)

api_id = int(input("Enter Your API ID: \n"))
api_hash = input("Enter Your API HASH : \n")

with TelegramClient(StringSession(), api_id, api_hash) as client:
                  me = client.get_me()
                  session_string = client.session.save()
                  formatted_msg = f"<b><u>String Session For {me.first_name}</u></b>\n\n<code>{session_string}</code>"

                  client.send_message("me", formatted_msg, parse_mode="html")
                  print(
                      f"String Has Been Sent To Your Saved Message : {me.first_name}"
                  )
