import requests, json
from config import config
from KPAPI import *
PAGE_ACCESS_TOKEN=config["Token"]
def student(sender_id):
  params = {"access_token": PAGE_ACCESS_TOKEN}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({"psid": sender_id, "persistent_menu": [
    {"locale": "default","composer_input_disabled": False,"call_to_actions": [
      {"type": "postback", "title": "Danh sách chức năng", "payload": "/list"},
      {"type": "postback", "title": "Kết nối với giáo viên", "payload": "connect"},
      {"type": "postback", "title": "Ngắt kết nối với giáo viên", "payload": "disconnect"},
      {"type": "postback", "title": "Danh sách các môn hổ trợ", "payload": "get_list_sub"}
  ]}]})
  print(requests.post("https://graph.facebook.com/v17.0/me/custom_user_settings", params=params, headers=headers, data=data))
