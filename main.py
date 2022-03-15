import random

from pyrogram import Client, filters
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import Photo
from data_config import API_ID, API_HASH, ID_ARCHIVE

api_id = API_ID
api_hash = API_HASH
id_archive = ID_ARCHIVE

app = Client("server_name", api_id, api_hash)


@app.on_message(filters.me & filters.command(["except_from"]))
def banned_handler(client, message):
    find_message = app.search_messages("VIckysW", query="#banned")
    try:
        banned_list = f"{message.command[1]}\n" + find_message[0].text
        message = app.send_message(id_archive, banned_list)
        client.pin_chat_message(id_archive, message.message_id)
    except:
        banned_list = f"{message.command[1]}\n" + "\n#banned \n **to ban somebody else write**: /except_from @somebody"
        message = app.send_message(id_archive, banned_list)
        client.pin_chat_message(id_archive, message.message_id)


    # check banned list
    try:
        find_message = app.search_messages("VIckysW", query="#banned")[0].text[:14].strip('@')
        if message.chat.username in find_message:
            return
    except IndexError:
        pass


    if message.from_user.username is not None:
        text = f"@{message.from_user.username}\n" \
               f"**ID**: #{message.chat.id}tag\n" \
               f"**__{message.text}__**"
        app.send_message(id_archive, text)
    else:
        text = f"#{message.from_user.first_name}\n" \
               f"**__{message.text}__**"
        app.send_message(id_archive, text)


@app.on_message(filters.private)
def media_handler(client, message):

    # check banned list
    try:
        find_message = app.search_messages("VIckysW", query="#banned")[0].text[:14].strip('@')
        if message.chat.username in find_message:
            return
    except IndexError:
        pass

    message.forward(id_archive)


app.run()
