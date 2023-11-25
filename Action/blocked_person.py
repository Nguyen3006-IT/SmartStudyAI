import requests, json
from config import config

PAGE_ACCESS_TOKEN=config["Token"]
def blocked_person(sender_id):
  params = {"access_token": PAGE_ACCESS_TOKEN}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({"psid": sender_id,
    "persistent_menu": [{
        "locale": "default",
        "composer_input_disabled": False,
        "call_to_actions": [{
              "type": "postback",
              "title": "Gửi yêu cầu mở chặn",
              "payload": "Request"
            },
            ]
      }]
  })

  requests.post("https://graph.facebook.com/v17.0/me/custom_user_settings", params=params, headers=headers, data=data)
