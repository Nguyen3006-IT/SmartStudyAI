import requests, json
from config import config
from KPAPI import *

PAGE_ACCESS_TOKEN = config["Token"]

def menu_noitu(sender_id):
  params = {"access_token": PAGE_ACCESS_TOKEN}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({"psid": sender_id, "persistent_menu": [
    {"locale": "default", "composer_input_disabled": False, "call_to_actions": [
      {"type": "postback", "title": "Hướng dẫn chơi", "payload": "helpplay"},
      {"type": "postback", "title": "Kết thúc trò chơi", "payload": "offgame"}
    ]}]})
  requests.post("https://graph.facebook.com/v17.0/me/custom_user_settings", params=params, headers=headers, data=data)
  sendMessage(PAGE_ACCESS_TOKEN, sender_id, "Kết nối trò chơi thành công")
  
  data1 = json.dumps({
    "recipient": {"id": sender_id},
    "messaging_type": "RESPONSE",
    "message":{"text": "Bạn có thể ấn bắt đầu để bắt đầu chơi.", "quick_replies":[
        {"content_type":"text", "title": "Bắt đầu", "payload": "start"},
        
      ]}})
  requests.post("https://graph.facebook.com/v17.0/me/messages", params=params, headers=headers, data=data1)
