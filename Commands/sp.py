from KPAPI import *
from config import config, commands
import json

token = config["Token"]

def sp(sender_id, message_text):
  try:
    with open("id_teacher.json", 'r') as open_file: list_id = json.load(open_file)
  except:
    list_id = {}
    
  if sender_id in [x[0] for x in list_id.values()]:
    sendMessage(token, sender_id, "Bạn đã nhận support rồi!")
  else:
    if list_id.get(message_text):
      if list_id.get(message_text)[0] != None and list_id.get(message_text)[0] != sender_id:
        sendMessage(token,sender_id,"Đã có người nhận môn này rồi!")
        
      elif list_id.get(message_text)[0] == None :
        list_id.get(message_text)[0] = sender_id
        with open("id_teacher.json", 'w') as save_file:
          json.dump(list_id, save_file, indent = 2)
        sendMessage(token,sender_id,"Nhận support thành công!")
    
    else:
      try:
        with open("id_teacher.json", 'r') as open_file:
            list_id = json.load(open_file)
      except:
        list_id={}
        
      try:
        with open("id_teacher.json", 'w') as save_file:
            list_id[message_text] = [sender_id, None]
            json.dump(list_id, save_file, indent = 2)
        sendMessage(token,sender_id,"Nhận support thành công!")
        
      except Exception as e:
          print(e)
        