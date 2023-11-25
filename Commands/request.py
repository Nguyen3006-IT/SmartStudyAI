from KPAPI import *
from config import config
from Action.list_admin_rep import *
import datetime

token = config["Token"]

def request(sender_id, message_text):
  Admin_id = ["6248280891946621", "6312817428801561", "6169255926506657"]

  date_now = datetime.datetime.today()
  #hour + 7 vì việt nam có múi giờ số 7
  date = f'{date_now.hour + 7}:{date_now.minute}:{date_now.second} - {date_now.day}/{date_now.month}/{date_now.year}'
    
  text = f'- Người dùng có ID "{sender_id}" vừa gửi yêu cầu gỡ block lúc ({date}) với nội dung:\n→ {message_text} '
  if text != "":
    list_admin_rep(Admin_id[0], sender_id, text)
    list_admin_rep(Admin_id[1], sender_id, text)
    list_admin_rep(Admin_id[2], sender_id, text)
  
  sendMessage(token, sender_id, 'Gửi yêu cầu thành công !') 



def acp_request(sender_id):
  try:
    with open("ids.json", "r") as file:
      block_ids = json.load(file)
  except:
    pass 

  if sender_id in block_ids["block"]:
    block_ids["block"].remove(sender_id)
    with open("ids.json", "w") as save:
      json.dump(block_ids, save)

    time = datetime.datetime.today()
    date = f'{time.hour + 7}:{time.minute}:{time.second} - {time.day}/{time.month}/{time.year}'

    sendMessage(token, sender_id, f"Bạn đã được gỡ block lúc ({date}) thành công !")



    

    