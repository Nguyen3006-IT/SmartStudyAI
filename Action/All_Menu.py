import requests, json
from config import config

def admin_teacher(sender_id):
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({"psid": sender_id, "persistent_menu": [
    {"locale": "default", "composer_input_disabled": False, "call_to_actions":[
      {"type": "postback", "title": "List Quyền Admin", "payload": "list admin"},
      {"type": "postback", "title": "Danh sách chức năng", "payload": "/list"},
      {"type": "postback", "title": "Nhận hổ trợ", "payload": "support"},
      {"type": "postback", "title": "Hủy hổ trợ", "payload": "un_support"},
      {"type": "postback", "title": "Ngắt kết nối với học sinh",  "payload": "disconnect"},
      {"type": "postback", "title": "Xem danh sách các môn hổ trợ", "payload": "get_list_sub"}
  ]}]})
  requests.post("https://graph.facebook.com/v17.0/me/custom_user_settings", params=params, headers=headers, data=data).json()
def admin_student(sender_id):
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({"psid": sender_id, "persistent_menu": [
    {"locale": "default","composer_input_disabled": False,"call_to_actions": [
      {"type": "postback", "title": "List Quyền Admin", "payload": "list admin"},
      {"type": "postback", "title": "Danh sách chức năng", "payload": "/list"},
      {"type": "postback", "title": "Kết nối với giáo viên", "payload": "connect"},
      {"type": "postback", "title": "Ngắt kết nối với giáo viên", "payload": "disconnect"},
      {"type": "postback", "title": "Danh sách các môn hổ trợ", "payload": "get_list_sub"}
  ]}]})
  requests.post("https://graph.facebook.com/v17.0/me/custom_user_settings", params=params, headers=headers, data=data)
  
#admin_teacher('6312817428801561')
  
def teacher(sender_id):
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({"psid": sender_id, "persistent_menu": [
    {"locale": "default", "composer_input_disabled": False, "call_to_actions":[
      {"type": "postback", "title": "Danh sách chức năng", "payload": "/list" },
      {"type": "postback", "title": "Nhận hổ trợ", "payload": "support" },
      {"type": "postback", "title": "Hủy hổ trợ", "payload": "un_support"},
      {"type": "postback", "title": "Ngắt kết nối với học sinh",  "payload": "disconnect"},
      {"type": "postback", "title": "Xem danh sách các môn hổ trợ", "payload": "get_list_sub"}
  ]}]})
  requests.post("https://graph.facebook.com/v17.0/me/custom_user_settings", params=params, headers=headers, data=data)

#teacher("6456701047755792")

def student(sender_id):
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({"psid": sender_id, "persistent_menu": [
    {"locale": "default","composer_input_disabled": False,"call_to_actions": [
      {"type": "postback", "title": "Danh sách chức năng", "payload": "/list"},
      {"type": "postback", "title": "Kết nối với giáo viên", "payload": "connect"},
      {"type": "postback", "title": "Ngắt kết nối với giáo viên", "payload": "disconnect"},
      {"type": "postback", "title": "Danh sách các môn hổ trợ", "payload": "get_list_sub"}
  ]}]})
  requests.post("https://graph.facebook.com/v17.0/me/custom_user_settings", params=params, headers=headers, data=data)

def menu_noitu(sender_id):
  from KPAPI import sendMessage
  from config import load_json, save_json 
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({"psid": sender_id, "persistent_menu": [
    {"locale": "default", "composer_input_disabled": False, "call_to_actions": [
      {"type": "postback", "title": "Hướng dẫn chơi", "payload": "helpplay"},
      {"type": "postback", "title": "Kết thúc trò chơi", "payload": "offgame"}
    ]}]})
  requests.post("https://graph.facebook.com/v17.0/me/custom_user_settings", params=params, headers=headers, data=data)
  
  sendMessage(sender_id, "Kết nối trò chơi thành công")
  tool = load_json("tools.json")
  tool["online_noitu"]+=[sender_id]
  save_json("tools.json", tool)
  
  data1 = json.dumps({
    "recipient": {"id": sender_id},
    "messaging_type": "RESPONSE",
    "message":{"text": "Bạn có thể ấn bắt đầu để bắt đầu chơi.", "quick_replies":[
        {"content_type":"text", "title": "Bắt đầu", "payload": "start"},
    ]}})
  requests.post("https://graph.facebook.com/v17.0/me/messages", params=params, headers=headers, data=data1)