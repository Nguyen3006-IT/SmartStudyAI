import requests, json
from config import config

PAGE_ACCESS_TOKEN = config["Token"]

def bang(sender_id, char):
  params = {"access_token": PAGE_ACCESS_TOKEN}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({
    "recipient":{"id": sender_id},
    "message":{"attachment":{"type":"template", "payload":
      {"template_type":"button", "text": "Chọn Bang", "buttons":[
        {"type":"postback", "title":"Tự Nhiên", "payload": f"tu_nhien{char}" },
        {"type":"postback", "title":"Xã Hội", "payload": f"xa_hoi{char}" },
        {"type":"postback", "title":"Ứng Dụng", "payload": f"ung_dung{char}" }
          
      ]}}}})
  requests.post("https://graph.facebook.com/v2.6/me/messages",
                            params=params,
                            headers=headers,
                            data=data)