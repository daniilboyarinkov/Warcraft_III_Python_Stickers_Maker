from pyrogram import Client
import os

# Don't forget about API ID and IP HASH of your user bot
client = Client("HERE SHOULD BE A CLIENT SESSION")

ne_folder = r"NE FOLDER"
orc_folder = r"ORC FOLDER"
ud_folder = r"UD FOLDER"
human_folder = r"HUMAN FOLDER"

folder = "" # One of the folders

ne_message = "🧝‍♂️🧝🧝‍♀️"
orc_message = "🧟‍♂️🧟🧟‍♀️"
ud_message = "🧛🧛‍♂️🧛‍♀️"
human_message = "👨‍🦳👨‍🦰🧔👨"

msg = "" # One of the messages

# All files in the folder
docs = os.listdir(folder)

index = 1

with client:
    client.send_document("@Stickers", fr"{folder}\{docs[0]}")
    print(fr"[LOG]: Отправляю: {folder}\{docs[0]}")

@client.on_message()
def automate(client, message):
    global index
    if "Стикер добавлен. Количество стикеров в наборе:" in message.text \
            or "Congratulations. Stickers in the set:" in message.text:
        client.send_document("@Stickers", fr"{folder}\{docs[index]}")
        print(fr"[LOG]: Отправляю: {folder}\{docs[index]}")
        index += 1
    elif "пришлите смайл" in message.text or "Now send me an emoji" in message.text:
        client.send_message("@Stickers", msg)
        print("[LOG]: Sticker was added!")


client.run()
