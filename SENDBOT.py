import baseData as BD
import json
import os
from pprint import pprint
import time
from telepot.loop import MessageLoop
import telegram
 
mediaGroup = []

"""save Caht ID"""
def saveChatId(dataPath,chatId=None,chatTitle=None):
    if os.path.isfile(dataPath):
        keyfile = open(dataPath,encoding=BD.encoding)
        data = json.load(keyfile)
        keyfile.close()
    else:
        data = {}
    if chatId != None:
        data.update({chatId:chatTitle})
    keyfile = open(dataPath,"w+",encoding=BD.encoding)
    keyfile.write(json.dumps(data))
    keyfile.close()
    return data

"""組group暫存"""
def getGroup(mediaGroupId):
    for jsonObj in mediaGroup:
        if str(mediaGroupId) in jsonObj:
            return jsonObj
    mediaGroup.append({mediaGroupId:mediaGroupId,'media':[],'timestamp':time.mktime(time.localtime())})
    for jsonObj in mediaGroup:
        if str(mediaGroupId) in jsonObj:
            return jsonObj

"""組media"""
def genMedia(msg):
    data = {}
    if 'audio' in msg:
        data.update({'media':msg['audio']['file_id'],'type':'audio'})
    if 'document' in msg:
        data.update({'media':msg['document']['file_id'],'type':'document'})
    if 'photo' in msg:
        data.update({'media':msg['photo'][-1]['file_id'],'type':'photo'})
    if 'video' in msg:
        data.update({'media':msg['video']['file_id'],'type':'video'})
    if 'caption' in msg:
        data.update({'caption':msg['caption']})
    return data

"""find key"""
def _find_first_key(d, keys):
    for k in keys:
        if k in d:
            return k
    raise KeyError('No suggested keys %s in %s' % (str(keys), str(d)))

def handle(msg):
    global chatIds

    chatId = msg['chat']['id']
    chatTitle = msg['chat']['title']
    messageId = msg['message_id']

    """檢查並儲存chat id"""
    if str(chatId) not in chatIds:
        chatIds = saveChatId(BD.from_path,chatId,chatTitle)
    """轉傳"""
    # bot.forwardMessage(BD.targetChatId, chatId, message_id)
    """Media Group"""
    # bot.sendMediaGroup(BD.targetChatId, media=[{'media':"AgACAgUAAxkBAAOWYlZ-rQuHFx8KYAQ0QHSJWYZyWTcAAgKsMRuNf9BXjlwyHcayCC4BAAMCAANzAAMjBA",'type':'photo'}])

    if 'media_group_id' in msg:
        mediaGroupId = msg['media_group_id']
        gp = getGroup(mediaGroupId)
        gpArr = gp['media']
        gpArr.append(genMedia(msg))
    else:
        key = _find_first_key(msg,['text','audio','document','photo','video'])
        if key == 'text':
            BD.bot.forwardMessage(BD.targetChatId, chatId, messageId)
        else:
            BD.bot.sendMediaGroup(BD.targetChatId, media=[genMedia(msg)])
    
"""取得留存chat id紀錄"""
chatIds = saveChatId(BD.from_path)

MessageLoop(BD.bot, handle).run_as_thread()
print("I'm listening...")

while 1:
    now = time.mktime(time.localtime())
    for gp in mediaGroup:
        if now - gp['timestamp'] >= 2:
            BD.bot.sendMediaGroup(BD.targetChatId, media=gp['media'])
            mediaGroup.remove(gp)
    time.sleep(1)
