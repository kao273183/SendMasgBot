"""import telegram
import time
from pprint import pprint
bot_token = '5121800363:AAFW06cDWT4-Ae9U_L__geQ1wLEPESlILxo'
bot = telegram.Bot(token=bot_token)
chat_id = '-627525390'

def handle(msg):
    pprint(msg)

MessageLoop(bot, handle).run_as_thread()
print("I'm listening...")

while 1:
    time.sleep(5)

"""
from asyncio.windows_events import NULL
from urllib.parse import _NetlocResultMixinBase
import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
import os
import json
path_data = os.path.join(os.path.expanduser("~"), 'Desktop')
bot = telepot.Bot('5121800363:AAFW06cDWT4-Ae9U_L__geQ1wLEPESlILxo')
if os.path.isfile(path_data + "\chatid.json"):
        keyfile = open(path_data + '\chatid'+".json",encoding="UTF-8")
        data = json.load(keyfile)
        data['789'] = "titile"
        print(data)
        keyfile.close()
        keyfile = open(path_data + '\chatid'+".json","w",encoding="UTF-8")
        keyfile.write(json.dumps(data,sort_keys=True,indent=4,separators=(',', ': ')))
        keyfile.close()
"""def handle(msg):
    pprint(msg)
    #data = {'id':msg['chat']['id'],'title':msg['chat']['title']}
    
    if id != NULL:
        keyfile = open(path_data + '\chatid'+".json","a",encoding="UTF-8")
        keyfile.write(json.dumps(data))
        keyfile.close()
    #bot.sendMessage(msg['from']['id'],'test')"""

#MessageLoop(bot, handle).run_as_thread()
#print("I'm listening...")

#while 1:
#    time.sleep(1)