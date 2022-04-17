import telepot
import os
 
encoding = "UTF-8"

bot = telepot.Bot('5121800363:AAFW06cDWT4-Ae9U_L__geQ1wLEPESlILxo')

path_data = os.path.join(os.path.expanduser("~"), 'Desktop')
from_path = os.path.join(path_data, "chatid.json")

targetChatId = "-771771446"

#TesSend = "-627525390"
#TestBotGroup = "-771771446"

"""
mediaGroup = [{'a':[],'timestamp':1},{'b':[],'timestamp':2}]

def getGroup(mediaGroupId):
    for jsonObj in mediaGroup:
        if str(mediaGroupId) in jsonObj:
            return jsonObj
    return {mediaGroupId:[],'timestamp':time.mktime(time.localtime())}

mediaGroupId = 'a'
gp = getGroup(mediaGroupId)
print(gp)
gpArr = gp[mediaGroupId]
print(gpArr)
gpArr.append({'123':'123'})
print(gpArr)
print(gp)
print(mediaGroup)
"""