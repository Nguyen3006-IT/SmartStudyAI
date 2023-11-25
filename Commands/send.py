from KPAPI import *
from config import config, commands
from Action.send_photo import *
import json, requests
from Action.Gv_AI import *
from Action.list_sub import list_sub
from Commands.sp_huy import *
from Commands.ungetsp import *

token = config["Token"]

def send(sender_id, message_text):
  with open("id_teacher.json", 'r') as file: id_gv_hs = json.load(file)
  with open("ids.json", 'r') as file: listId = json.load(file)
  connected = [id for id in id_gv_hs.values() if sender_id in id][0]
  if message_text.get('payload'):
    payload = message_text["payload"]
    if payload == "ChatWithAI":
      listId["Chat"].remove(sender_id)
      with open("ids.json", 'w') as save_fi: json.dump(listId, save_fi)
      menu_teacher(sender_id) if sender_id in [id[0] for id in id_gv_hs.values()] else menu_student(sender_id)
      sendMessage(token, sender_id, "Bạn vừa chuyển qua chế độ chat với Bot")
    elif payload == "un_support":
      sp_huy(sender_id)
    elif payload == "disconnect":
      ungetsp(sender_id)
    elif payload == "get_list_sub":
      list_sub(sender_id)
      
  elif message_text.get('text'):
    try:
      sendMessage(token, connected[0] if sender_id == connected[1] else connected[1], message_text["text"])
    except Exception as e: pass
      
  elif message_text.get('attachments'):
    try:
      urls = [requests.get(f'https://tinyurl.com/api-create.php?url={url["payload"]["url"]}').text for url in message_text['attachments']]
      sendMessage(token, connected[0] if sender_id == connected[1] else connected[1], "\n".join(urls)) if len(urls) > 3 else [sendMedia(token, connected[0] if sender_id == connected[1] else connected[1], "image", url) for url in urls]
      
      sendMessage(token, connected[0] if sender_id == connected[1] else connected[1], f"Người dùng đường dây bên kia vừa gửi cho bạn {len(urls)} ảnh.")
      
    except Exception as e: print(e)
    
  
def send_img(sender_id, urls):
  try:
    with open("id_teacher.json", 'r') as file:
      json_id = json.load(file)
  except:
    pass

  if sender_id in [user[0] for user in json_id.values()]:
    student_id = None
    for subject in json_id: 
      if json_id.get(subject)[0] == sender_id:
        if json_id[subject][1] != None:
          student_id = json_id[subject][1]
      
    if student_id != None:
      url = [url for url in urls]
      send_photo(sender_id, url)
    else:
      sendMessage(token, sender_id, "Hiện tại chưa có ai kết nối với bạn !")

  #chỗ này nói đến học sinh
  elif sender_id in [user[1] for user in json_id.values()]:
    url = [requests.get(f"https://tinyurl.com/api-create.php?url={url}").text for url in urls]
    send_photo(sender_id, url)
    
  else:
    sendMessage(token, sender_id, "Bạn chưa kết nối với ai !")