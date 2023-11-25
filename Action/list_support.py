import requests, json
from config import config
# nhận quyền hổ trợ môn học
PAGE_ACCESS_TOKEN = config["Token"]

def list_support(sender_id):
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
                  "text":"Chọn môn học hổ trợ",
                  "buttons":[
                  {
                    "type":"postback",
                    "title":"Toán học",
                    "payload":"sp_Math"
                  },
                  {
                    "type":"postback",
                    "title":"Hóa học",
                    "payload":"sp_Chemistry"
                  },
                  {
                    "type":"postback",
                    "title":"Vật Lý",
                    "payload":"sp_Physics"
                  }
                  
                  
                  ]
                }  
              }
            }
          })
      
        requests.post("https://graph.facebook.com/v2.6/me/messages",
                                  params=params,
                                  headers=headers,
                                  data=data)

def list_support2(sender_id):
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
                  "text":"Chọn môn học hổ trợ",
                  "buttons":[
                  {
                    "type":"postback",
                    "title":"Văn học",
                    "payload":"sp_Literature"
                  },
                  {
                    "type":"postback",
                    "title":"Lịch Sử",
                    "payload":"sp_History"
                  },
                  {
                    "type":"postback",
                    "title":"Địa Lí",
                    "payload":"sp_Geography"
                  }
                  
                  
                  ]
                }  
              }
            }
          })
      
        requests.post("https://graph.facebook.com/v2.6/me/messages",
                                  params=params,
                                  headers=headers,
                                  data=data)

def list_support3(sender_id):
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
                  "text":"Chọn môn học hổ trợ",
                  "buttons":[
                  {
                    "type":"postback",
                    "title":"Tin học",
                    "payload":"sp_IT"
                  },
                  {
                    "type":"postback",
                    "title":"Công nghệ",
                    "payload":"sp_Technicality"
                  },
                  {
                    "type":"postback",
                    "title":"Tiếng Anh",
                    "payload":"sp_English"
                  }
                  
                  
                  ]
                }  
              }
            }
          })
      
        requests.post("https://graph.facebook.com/v2.6/me/messages",
                                  params=params,
                                  headers=headers,
                                  data=data)