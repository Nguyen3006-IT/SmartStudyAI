import requests, json
from config import config

PAGE_ACCESS_TOKEN = config["Token"]

def send_photo(sender_id, url):
  params = {"access_token": PAGE_ACCESS_TOKEN}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({
    "recipient":{"id": sender_id},
      "message":{
        "attachment":{
          "type": "template",
          "payload":{
            "template_type": "generic",
            "elements":[{
              "title": f'Bạn muốn gửi {f"{len(url)} " if len(url) > 2 else ""}phương tiện này đến đâu ?',
              "subtitle": "Chọn phương thức gửi.",
              "image_url": url[0],
              "buttons":[{
                "type": "postback",
                "title":"Gửi ảnh cho người dùng",
                "payload": 'SEND_' + " ".join(url)
              },
              {
                "type": "postback",
                "title": "Gửi tất cả dưới dạng QR",
                "payload":"QR_" + " ".join(url)
              },
                         
              ]
            }]
          }
        }
      }
  })
  requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)



def photo(sender_id, url):
    params = {"access_token": PAGE_ACCESS_TOKEN}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({
        "recipient":{"id": sender_id},
          "message":{
            "attachment":{
              "type": "template",
              "payload":{
                "template_type": "generic",
                "elements":[
                {
                  "title": 'ảnh 1',
                  "subtitle": '...',
                  "image_url": url[0],
                  "buttons":[{
                    "type": "postback",
                    "title":".",
                    "payload": '.'
                  },
                  {
                    "type": "postback",
                    "title": "..",
                    "payload":".."
                  }
                             
                  ]
                },
                {
                  "title": 'ảnh 2',
                  "subtitle": '...',
                  "image_url": url[0],
                  "buttons":[{
                    "type": "postback",
                    "title":".",
                    "payload": '.'
                  },
                  {
                    "type": "postback",
                    "title": "..",
                    "payload":".."
                  }
                             
                  ]
                },
                {
                  "title": 'ảnh 3',
                  "subtitle": '...',
                  "image_url": url[0],
                  "buttons":[{
                    "type": "postback",
                    "title":".",
                    "payload": '.'
                  },
                  {
                    "type": "postback",
                    "title": "..",
                    "payload":".."
                  }
                             
                  ]
                },
                {
                  "title": 'ảnh 4',
                  "subtitle": '...',
                  "image_url": url[0],
                  "buttons":[{
                    "type": "postback",
                    "title":".",
                    "payload": '.'
                  },
                  {
                    "type": "postback",
                    "title": "..",
                    "payload":".."
                  }
                             
                  ]
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