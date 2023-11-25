from KPAPI import *
from requests import get, post
import json
from config import config

token = config["Token"]

def getVideo(sender_id, message_text):
  sendMessage(sender_id,"Vui lòng đợi xử lý trong vài giây...")
  typingon(sender_id)

  try: # nếu nhập sai định dạng url video, api sẽ xảy ra lỗi
    video = post("https://api.letuan.edu.vn/", data = message_text).json()["link"]
    short_link = get(f"https://tinyurl.com/api-create.php?url={video}").text
  
    sendMessage(sender_id, f"Đây là url video của bạn:\n {short_link} ")

  except:
    sendMessage(sender_id, "Có vẻ như bạn gửi sai định dạng không phải là định dạng VIDEO. Xin vui lòng nhập lại.")

  typinoff(sender_id)

