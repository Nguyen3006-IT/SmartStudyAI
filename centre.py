import json, requests, traceback, sys
from info import info
from Commands.gpt import gpt
from config import commands, load_json, save_json
from KPAPI import sendMessage
#from Action.All_Menu import *

def centre(data_user):
  try:
    data = json.loads(info(data_user))
    # gọi hàm get info xem nó trả về key và message hay attachments
    if data.get("message"):
      # lấy thông tin
      sender_id = data["message"][0]
      message = data["message"][1]
      reply = data["message"][2] 
      
      cmd = message.split()[0].lower()
      if commands.get(cmd):
        if commands[cmd][1]:
          exec(f"""
from Commands.{commands[cmd][0]} import {commands[cmd][0]}
{commands[cmd][0]}("{sender_id}","{" ".join(message.split()[1:])}")
          """)
        elif commands[cmd][1] == False:
          exec(f"""
from Commands.{commands[cmd][0]} import {commands[cmd][0]}
{commands[cmd][0]}("{sender_id}")
          """)
        else:
          exec(f"""
from Action.All_Menu import {commands[cmd.lower()][0]}
{commands[cmd.lower()][0]}("{sender_id}")
          """)
        
      else:
        gpt(sender_id, message)
        #bard(sender_id, message, rep_mess)
    
    elif data.get("attachments"):
      # còn nếu người dùng gửi ảnh nó sẽ lấy url ảnh 
      if data["attachments"][2] == "image":
        from Commands.bard import save_image_to_Bard
        sender_id = data["attachments"][0]
        url_img = data["attachments"][1]
        accounts = load_json("accounts.json")
        accounts[sender_id] = url_img
        save_json("accounts.json", accounts)
        sendMessage(sender_id, "Bạn muốn tôi giúp gì về bức tranh này ?")   
    
    elif data.get("postback"):
      from Module.get_postback import run_postback
      run_postback(sender_id=data["postback"][0], payload=data["postback"][1])
      
      
        
  except Exception as e :
    print(e)
    pass
    #name_error=str(sys.exc_info()[1])
    #tb=sys.exc_info()[2]
    #line_number = traceback.extract_tb(tb)[-1][1]
    #print(f"ĐÃ CÓ LỖI XÃY RA!!!\n\nTên Lỗi: {name_error}\n\nTạm dịch: {translate(name_error,'vi')}\n\nTên file: {__name__} | Vị trí: dòng thứ {line_number}\n\nTham khảo: https://www.google.com/search?q=how+to+fix+{name_error.replace(' ','+')}+in+python")


