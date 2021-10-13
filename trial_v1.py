import asyncio
import sys
from telethon.sync import TelegramClient, events
import re
import webbrowser
import pyautogui as pg
import time
import os
import cv2
import urllib

api_id = 34534634646346
api_hash = '-----------------------------'
channelId = 'https://t.me/bottestmaker'

def findUrls(url):
    client.log_out()
    urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+', url)
    return urls
    

class CLITelegram(TelegramClient):
    def __init__(self, session_user_id, api_id, api_hash, on_message):
        super().__init__(session_user_id, api_id, api_hash)
        self.on_message = on_message
        self.start()

    async def message_handler(self, event):
        self.on_message(event.text)

    async def run(self):
        self.add_event_handler(self.message_handler, events.NewMessage)

        while True:
            # msg = await async_input('Enter a message: ')
            msg = (await loop.run_in_executor(None, sys.stdin.readline)).rstrip()
            if msg != "":
                #await self.send_message(channelId, msg)  
                 print('sym')

        self.run_until_disconnected()

def pyautobot():
    time.sleep(4.2)
    cords = pg.locateCenterOnScreen(r'C:\Users\Hamza\Desktop\boty\bnbnew.png', confidence=0.6)
    
    pg.move(cords)
    pg.doubleClick(cords)

    pg.typewrite("1")  # amount of bnb getting contributed
    sumbit = pg.moveRel(175, 100)

    pg.click(sumbit)


def on_message(message):
    print(message)

    urls = findUrls(message)
    for url in urls:
        webbrowser.open(url, new=2)
        pyautobot()


if __name__ == "__main__":

    client = CLITelegram('my_listener', api_id, api_hash, on_message)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.run())

