import requests, json
from config import config
# nhận sự hổ trợ từ giáo viên
PAGE_ACCESS_TOKEN = config["Token"]

def list_get_support(sender_id):
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
                    "payload":"get_sp_Math"
                  },
                  {
                    "type":"postback",
                    "title":"Hóa học",
                    "payload":"get_sp_Chemistry"
                  },
                  {
                    "type":"postback",
                    "title":"Vật Lý",
                    "payload":"get_sp_Physics"
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

def list_get_support2(sender_id):
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
                    "payload":"get_sp_Literature"
                  },
                  {
                    "type":"postback",
                    "title":"Lịch Sử",
                    "payload":"get_sp_History"
                  },
                  {
                    "type":"postback",
                    "title":"Địa Lí",
                    "payload":"get_sp_Geography"
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

def list_get_support3(sender_id):
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
                    "payload":"get_sp_IT"
                  },
                  {
                    "type":"postback",
                    "title":"Công nghệ",
                    "payload":"get_sp_Technicality"
                  },
                  {
                    "type":"postback",
                    "title":"Tiếng Anh",
                    "payload":"get_sp_English"
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