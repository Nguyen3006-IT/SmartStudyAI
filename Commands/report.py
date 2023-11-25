from KPAPI import *
from config import config
from Action.blocked_person import blocked_person
import json
import datetime

token = config["Token"]

def report_user(sender_id, message_text):
  print(sender_id)
  try:
    with open("ids.json", "r") as file:
      json_id = json.load(file)
  except :
    json_id = {"ids": [], "online": [], "total_id_1": [], "total_id_2": [], "block": []}
  sendMessage(token, sender_id, "có vẻ như bạn đang dùng từ ngữ thô tục.")

  
  if sender_id not in json_id["total_id_1"] and sender_id not in json_id["total_id_2"] and sender_id not in json_id["block"]:
    #with open("ids.json", "w") as save:
    json_id["total_id_1"].append(sender_id)
    sendMessage(token, sender_id, "Bạn đã được nhắc nhở 1 lần. Bạn còn tái phạm 2 lần nữa sẽ bị chặn, không được dùng bot.")
    
  elif sender_id in json_id["total_id_1"]:
    json_id["total_id_1"].remove(sender_id); json_id["total_id_2"].append(sender_id)
    sendMessage(token, sender_id, "Bạn đã được nhắc nhở 1 lần. Bạn còn tái phạm 1 lần nữa sẽ bị chặn, không được dùng bot.")
    
  elif sender_id in json_id["total_id_2"]:
    json_id["total_id_2"].remove(sender_id)
    json_id["block"].append(sender_id)
    sendMessage(token, sender_id, "Bạn đã bạn vào danh sách chặn. Bot sẽ không trả lời mọi câu hỏi của bạn. ")
    blocked_person(sender_id)
  
  

  
  try:
    with open("ids.json", "w") as save:
      json.dump(json_id, save)
  except Exception as e:
    print(e)
