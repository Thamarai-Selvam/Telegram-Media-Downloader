from telethon import TelegramClient,events,sync
from hurry.filesize import size

def Reverse(list):
    list.reverse()
    return list

def getstickers(list):
    for msg in list:
        print(msg.id,msg.message,msg.media.document.attributes[1].alt,
                            msg.media.document.mime_type,size(msg.media.document.size))

def getimages(list):
    for msg in list:
         if(hasattr(msg.media,'document')):
             print(msg.id,msg.message,msg.media.document.attributes[1].file_name,
                            msg.media.document.mime_type,size(msg.media.document.size))
         elif(hasattr(msg.media,'photo')):
            print(msg.id,msg.message)

def getaudio(list):
    for msg in list:
        print("Under construction")

def getothers(list):
    for msg in list:
        print(msg.id,msg.message,msg.media.document.attributes[0].file_name,
                        msg.media.document.mime_type,size(msg.media.document.size))

def gettext(list):
    for msg in list:
        print(msg.id,msg.message)

# Use your own values from my.telegram.org
api_id = 'your api id'
api_hash = 'enter your api hash here'

# The first parameter is the .session file name (absolute paths allowed)


client = TelegramClient('mysession', api_id, api_hash)
client.start()

#print(client.get_me().stringify())

try:
    messages = client.get_messages('dr_stone',limit=20000)
except:
    print('Channel Not Found/Cannot Connect')
    
#print(messages[70])


#variables for holding different file types
#string vars
ltext =[]
laudio = []
lvideo = []
limages = []
lstickers = []
lothers = []



for i,msg in enumerate(Reverse(messages)):
    if(msg.media != ''):
        if(hasattr(msg.media,'document')):
            if(msg.media.document.mime_type == 'image/webp'):        
                lstickers.append(msg)
                   
            elif((msg.media.document.mime_type == 'image/jpeg') or 
                        (msg.media.document.mime_type == 'image/png')):
                    limages.append(msg)
            else:
                lothers.append(msg)

        elif(hasattr(msg.media,'photo')):
            limages.append(msg)

        elif(msg.media == None):
            ltext.append(msg)


#print vars

ptext=['Text Messages','Stickers','Images','Audios','Videos','Other Files']
plist = [ltext,lstickers,limages,laudio,lvideo,lothers]
#for x,i in enumerate(plist):
 #   print(ptext[x])
  #  for j in i:
   #     print(j)
        
print('Text Messages')
gettext(ltext)
print('Images')
getimages(limages)
print('Audio')
getaudio(laudio)
#print('Videos')
#getvideos(lvideos)
print('Other files')
getothers(lothers)
