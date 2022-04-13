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
#from asyncio.windows_events import NULL
#from urllib.parse import _NetlocResultMixinBase
import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
import os
import json

path_data = os.path.join(os.path.expanduser("~"), 'Desktop')
bot = telepot.Bot('5121800363:AAFW06cDWT4-Ae9U_L__geQ1wLEPESlILxo')
dataPath = os.path.join(path_data, "chatid.json")

TesSend = "-627525390"
TestBotGroup = "-771771446"

def saveChatId(id=None,title=None):
    if os.path.isfile(dataPath):
        keyfile = open(dataPath,encoding="UTF-8")
        data = json.load(keyfile)
        keyfile.close()
    else:
        data = {}
    if id != None:
        data.update({id:title})
    keyfile = open(dataPath,"w+",encoding="UTF-8")
    keyfile.write(json.dumps(data))
    keyfile.close()
    return data

def handle(msg):
    global chatIds
    pprint(msg)
    id = msg['chat']['id']
    title = msg['chat']['title']
    message_id = msg['message_id']
    pprint(id)
    pprint(title)
    pprint(message_id)
    if id not in chatIds:
        chatIds = saveChatId(id,title)
    bot.forwardMessage(TestBotGroup, TesSend, message_id)
    bot.sendMediaGroup(chat_id, media)


# saveChatId("1qaz","2wsx")
# saveChatId("2wsx","2wsx")
chatIds = saveChatId()
# print(chatIds)
# print("2wsx" in chatIds)
# print("3edc" in chatIds)

"""if os.path.isfile(dataPath):
    keyfile = open(dataPath,encoding="UTF-8")
    data = json.load(keyfile)
    data['789'] = "titile"
    print(data)
    keyfile.close()
    keyfile = open(dataPath,"w",encoding="UTF-8")
    keyfile.write(json.dumps(data,sort_keys=True,indent=4,separators=(',', ': ')))
    keyfile.close()
else:
    keyfile = open(dataPath,"w",encoding="UTF-8")
    keyfile.write(json.dumps({}))
    keyfile.close()"""
"""def handle(msg):
    pprint(msg)
    #data = {'id':msg['chat']['id'],'title':msg['chat']['title']}
    
    if id != NULL:
        keyfile = open(path_data + '\chatid'+".json","a",encoding="UTF-8")
        keyfile.write(json.dumps(data))
        keyfile.close()
    #bot.sendMessage(msg['from']['id'],'test')"""

MessageLoop(bot, handle).run_as_thread()
print("I'm listening...")

while 1:
   time.sleep(1)