import requests, json
from config import config

def list_for_admin(sender_id):
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({
    "recipient":{"id": sender_id},
    "message":{"attachment":{"type":"template", "payload":
      {"template_type":"button", "text":"Bật/tắt Bot trong việc bảo trì Bot", "buttons":[
        {"type":"postback", "title":"Bật chế độ update Bot", "payload": "on update bot"},
        {"type":"postback", "title":"Tắt chế độ update Bot", "payload": "off update bot"},
      ]}}}})
  requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data).json()
  
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({
    "recipient":{"id": sender_id},
    "message":{"attachment":{"type":"template", "payload":
      {"template_type":"button", "text": "Chế độ dưới quyền Admin", "buttons":[
        {"type":"postback", "title":"Chế độ Giáo Viên", "payload": "admin teacher"},
        {"type":"postback", "title":"Chế độ Học Sinh", "payload": "admin student"},
      ]}}}})
  requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)


