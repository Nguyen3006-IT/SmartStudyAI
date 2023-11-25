import requests, json
from config import config

PAGE_ACCESS_TOKEN = config["Token"]

def list_admin_rep(sender_id, user, text):
        params = {"access_token": PAGE_ACCESS_TOKEN}
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
                  "text": text,
                  "buttons":[
                  {
                    "type":"postback",
                    "title":"Chấp nhận",
                    "payload": f"accept{user}"
                  }, 
                  {
                    "type":"postback",
                    "title":"Từ chối",
                    "payload": f"refuse{user}"
                  }
                  ]
              }  
            }
          }
        })

        requests.post("https://graph.facebook.com/v2.6/me/messages",params=params, headers=headers, data=data)