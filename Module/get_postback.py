import json
from KPAPI import *
from config import config, commands
from Action.All_Menu import student, teacher
from Commands.list import list
from Action.student import student
from Action.teacher import teacher
from Commands.sp import *
from Commands.sp_huy import *
from Commands.getsp import *
from Commands.ungetsp import *
from Commands.send import *
from Commands.qr import *
from Action.list_get_support import *
from Action.list_support import *
from Action.Gv_AI import *
from Commands.list import *
from Action.list_sub import *
from Action.list_bang import *
from Commands.request import *
from Commands.conjunction import *
from Action.all_list import *
from Admin.block_user_on_update import *
from mtranslate import translate


def run_postback(sender_id, payload):
  try:
    if payload in ["cong_cu", "AI", "chuyen_van_ban"]:
      list(sender_id, payload)
  
    elif payload == "student":
      student(sender_id)
      sendMessage(sender_id, "Bạn đã nhận được menu của vai trò học sinh!") 
    elif payload == "teacher":
      list_admin_rep(
        sender_id="6312817428801561", user=f'_teacher_{sender_id}', 
        text="Một người vừa gửi yêu cầu chức vụ Giáo Viên đến bạn."
      )

    elif payload == "start":
      from Commands.conjunction import rep_start_conjunction
      rep_start_conjunction(sender_id)
    elif payload == "bot_start":
      from Commands.conjunction import ongame
      ongame(sender_id)
    elif payload == "user_start":
      data = load_json("accounts.json") or {}
      data[sender_id] = "noitu_empty"
      sendMessage(sender_id, "Mời bạn đi trước")
      save_json("accounts.json", data)
    elif payload == "offgame":
      sendMessage(sender_id, "Đang xử lý...")
      from Commands.conjunction import offgame
      offgame(sender_id)
      
    elif payload == "disconnect":
      ungetsp(sender_id)
    elif payload == "connect":
      bang(sender_id, char="student")
    elif payload == "support":
      bang(sender_id, char="teacher")
    elif payload == "un_support":
      sp_huy(sender_id)
    
    elif payload[:8] == "tu_nhien":
      list_support(sender_id) if payload[8:] == "teacher" else list_get_support(sender_id)
    elif payload[:6] == "xa_hoi":
      list_support2(sender_id) if payload[6:] == "teacher" else list_get_support2(sender_id)
    elif payload[:8] == "ung_dung":
      list_support3(sender_id) if payload[8:] == "teacher" else list_get_support3(sender_id)
  
    elif "get_sp" in payload:
      getsp(sender_id, payload[7:])
    elif "sp_" in payload:
      sp(sender_id, payload[3:])
  
    elif payload.split()[0] == "QR_Clear":
      qr_clear(sender_id, " ".join(payload.split()[1:]))
    elif payload.split()[0] == "AI_Art_QR":
      qr_AI(sender_id, " ".join(payload.split()[1:]), prompt=None)
    elif payload.split()[0] == "Prompt_QR":
      Prompt_QR_Code(sender_id, " ".join(payload.split()[1:]), prompt=True)
      tools = load_json("tools.json")
      tools["Creating_QR"] += [sender_id]
      save_json("tools.json", tools)
  
    elif payload == "/list":
      list(sender_id)
    elif payload == "get_list_sub":
      list_sub(sender_id)
    elif payload[:4] == "SEND":
      send(sender_id, payload[5:].split())
  
    elif payload == "ChatWithTeacher":
      tools = load_json("tools.json")
      tools["Chat"].append(sender_id)
      save_json("tools.json", tools)
      menu_ChatWithTeacher(sender_id)
      sendMessage(sender_id,"Bạn đã chuyển sang chế độ 'Chat với giáo viên'.")
      
    elif payload == "ChatWithStudent":
      tools = load_json("tools.json")
      tools["Chat"].append(sender_id)
      save_json("tools.json", tools)
      menu_ChatWithStudent(sender_id)
      sendMessage(sender_id,"Bạn đã chuyển sang chế độ 'Chat với học sinh'.")
  
    elif payload[:6] == "accept" and sender_id in ["6248280891946621", "6312817428801561", "6169255926506657"]:
      if payload[6:15] == "_teacher_":
        tools = load_json("tools.json")
        tools["teacher"].append(payload[15:])
        teacher(payload[15:])
        sendMessage(payload[15:],"Bạn đã được chấp nhận với vai trò giáo viên thành công.")
        sendMessage(payload[15:],"Bạn đã nhận được menu của vai trò giáo viên !")
        with open("ids.json", "w") as save: json.dump(ids, save) 
      else:
        user_id = payload[6:]; acp_request(user_id); student(user_id)
        sendMessage(sender_id, "Gỡ chặn người dùng thành công !")
    elif payload[:6] == "refuse" and sender_id in ["6248280891946621", "6312817428801561", "6169255926506657"]:
      if payload[6:15] == "_teacher_":
        student(payload[15:])
        sendMessage(payload[15:],"Bạn đã bị từ chối yêu cầu làm chức vụ Giáo Viên. Bạn sẽ là chức vụ Học Sinh. Bạn có thể sử dụng Bot.")
      else:
        sendMessage(payload[6:], 'Admin đã TỪ CHỐI yêu cầu "gỡ block" bạn.')
        sendMessage(sender_id, 'Gửi trả lời thành công.')
  
    elif sender_id in ["6248280891946621", "6312817428801561", "6169255926506657"]:
      if payload == "list admin":
        list_for_admin(sender_id)
      elif payload == "on update bot":
        on_block_user_on_update(sender_id)
      elif payload == "off update bot":
        off_block_user_on_update(sender_id)
      elif payload == "admin teacher":
        admin_teacher(sender_id)
        sendMessage(sender_id, "chuyển menu thành công")
      elif payload == "admin student":
        admin_student(sender_id)
        sendMessage(sender_id, "chuyển menu thành công")

  except Exception as e:
    print(e)