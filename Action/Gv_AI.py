import requests, json
from config import config

PAGE_ACCESS_TOKEN=config["Token"]
def menu_student(sender_id):
  params = {"access_token": PAGE_ACCESS_TOKEN}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({"psid": sender_id,
    "persistent_menu": [{
        "locale": "default",
        "composer_input_disabled": False,
        "call_to_actions": [{
              "type": "postback",
              "title": "Chế độ Chat với Giáo Viên",
              "payload": "ChatWithTeacher"
            },
            {
              "type": "postback",
              "title": "Danh sách chức năng",
              "payload": "/list"
            },
            {
              "type": "postback",
              "title": "Ngắt kết nối với giáo viên",
              "payload": "disconnect"
            },
            {
              "type": "postback",
              "title": "Danh sách các môn hổ trợ",
              "payload": "get_list_sub"
            }
            
            ]
      }]
  })
  requests.post("https://graph.facebook.com/v17.0/me/custom_user_settings", params=params, headers=headers, data=data)
  
def menu_ChatWithTeacher(sender_id):
  params = {"access_token": PAGE_ACCESS_TOKEN}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({"psid": sender_id,
    "persistent_menu": [{
        "locale": "default",
        "composer_input_disabled": False,
        "call_to_actions": [{
              "type": "postback",
              "title": "Chế độ Chat với AI",
              "payload": "ChatWithAI"
            },
            {
              "type": "postback",
              "title": "Ngắt kết nối với giáo viên",
              "payload": "disconnect"
            },
            {
              "type": "postback",
              "title": "Danh sách các môn hổ trợ",
              "payload": "get_list_sub"
            }
            ]
      }]
  })
  requests.post("https://graph.facebook.com/v17.0/me/custom_user_settings", params=params, headers=headers, data=data)

def menu_teacher(sender_id):
  params = {"access_token": PAGE_ACCESS_TOKEN}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({"psid": sender_id,
    "persistent_menu": [{
        "locale": "default",
        "composer_input_disabled": False,
        "call_to_actions": [{
              "type": "postback",
              "title": "Chế độ Chat với Học Sinh",
              "payload": "ChatWithStudent"
            },
            {
              "type": "postback",
              "title": "Danh sách chức năng",
              "payload": "/list"
            },
            {
              "type": "postback",
              "title": "Hủy hổ trợ",
              "payload": "un_support"
            },
            {
              "type": "postback",
              "title": "Ngắt kết nối với học sinh", 
              "payload": "disconnect"
            },
            {
              "type": "postback",
              "title": "Xem danh sách các môn hổ trợ",
              "payload": "get_list_sub"
            }
            ]
      }]
  })
  requests.post("https://graph.facebook.com/v17.0/me/custom_user_settings", params=params, headers=headers, data=data)
  
def menu_ChatWithStudent(sender_id):
  params = {"access_token": PAGE_ACCESS_TOKEN}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({"psid": sender_id,
    "persistent_menu": [{
        "locale": "default",
        "composer_input_disabled": False,
        "call_to_actions": [{
              "type": "postback",
              "title": "Chế độ Chat với AI (Bot)",
              "payload": "ChatWithAI"
            },
            {
              "type": "postback",
              "title": "Hủy hổ trợ",
              "payload": "un_support"
            },
            {
              "type": "postback",
              "title": "Ngắt kết nối với học sinh", 
              "payload": "disconnect"
            },
            {
              "type": "postback",
              "title": "Xem danh sách các môn hổ trợ",
              "payload": "get_list_sub"
            },
            
            ]
      }]
  })

  requests.post("https://graph.facebook.com/v17.0/me/custom_user_settings", params=params, headers=headers, data=data)