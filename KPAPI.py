import requests, json
from config import config

def seen(send_to_id):
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({
    "recipient": {"id": send_to_id},
    "sender_action": "mark_seen"
  })
  requests.post("https://graph.facebook.com/v3.0/me/messages", params=params, headers=headers, data=data)

def sendMedia(send_to_id, type_img, url):
  typingon(send_to_id=send_to_id)
  
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({
    "recipient": {
      "id": send_to_id
    },
    "message": {
      "attachment": {
        "type": type_img,
        "payload": {
          "is_reusable": True,
          "url": url
        }
      }
    }
  })
  requests.post("https://graph.facebook.com/v3.0/me/messages", params=params, headers=headers, data=data)
  typingon(send_to_id=send_to_id)

def sendMessage(send_to_id, message_text):
  seen(send_to_id)
  typingon(send_to_id)
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({
    "recipient": {"id": send_to_id},
    "message": {"text": message_text}
  })
  return requests.post("https://graph.facebook.com/v3.0/me/messages", params=params, headers=headers, data=data).json()  #["message_id"]
  
  typingoff(send_to_id)

def typingoff(send_to_id):
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({
    "recipient": {"id": send_to_id},
    "sender_action": "typing_off"
  })
  requests.post("https://graph.facebook.com/v3.0/me/messages", params=params, headers=headers, data=data)

def typingon(send_to_id):
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({
    "recipient": {"id": send_to_id},
    "sender_action": "typing_on"
  })

  requests.post("https://graph.facebook.com/v3.0/me/messages", params=params, headers=headers, data=data)
