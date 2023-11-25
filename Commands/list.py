import requests, json
from KPAPI import sendMessage
from config import config, commands

def list(sender_id, choice=None):
  if choice == None:
    params = {"access_token": config["Token"]}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({
      "recipient":{
        "id": sender_id
      },
      "message":{
        "attachment":{
        "type":"template",
        "payload":{
            "template_type":"button",
            "text":"Mục lục 📄",
            "buttons":[
            {
              "type":"postback",
              "title":"Công cụ",
              "payload":"cong_cu"
            },
            {
              "type":"postback",
              "title":"AI",
              "payload":"AI"
            },
            {
              "type":"postback",
              "title":"Chuyển đổi văn bản",
              "payload":"chuyen_van_ban"
            }
            
            ]
          }  
        }
      }
    })

    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
  else:
    try:
      list = ""
      for func, usage in commands.items():
        if usage[4]==choice:
          list += f"- Cú pháp: {func}\n- Cách dùng: {usage[2]}\n- Công dụng: {usage[3]}\n" + ("-"*50) + "\n"
      sendMessage(sender_id, list)
      
    except Exception as e:
      print("config sai kìa chú em. lỗi của chú đây:", e)

