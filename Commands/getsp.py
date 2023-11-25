from KPAPI import sendMessage
from config import load_json, save_json, dic_subject
from Action.Gv_AI import menu_student, menu_teacher


def getsp(sender_id, message_text):
  json_id = load_json("id_teacher.json") or {}
    
  teacher_id = json_id[message_text][0]
  if json_id.get(message_text):
    if teacher_id == None:
      sendMessage(sender_id, "Hiện tại môn này chưa có người hỗ trợ.")
      
    elif json_id[message_text][1]:
      if sender_id == json_id[message_text][1]:
        sendMessage(sender_id, "Hiện tại bạn đã được nhận trợ giúp.")
      else:
        sendMessage(sender_id, "Đang có người hỏi. Vui lòng quay lại sau.")

    elif sender_id == json_id[message_text][0]:
      sendMessage(sender_id, "Hiện tại bạn đang hỗ trợ môn này")
    
    #elif sender_id in [id[0] for id in json_id.values()]:
     # sendMessage(sender_id, "Bạn đang là người hỗ trợ bạn không thể cần trợ giúp")

    else:
      json_id[message_text][1] = sender_id
      save_json("id_teacher.json", json_id)
          
      menu_student(sender_id)
      sendMessage(sender_id, f"Bạn đã nhận hỗ trợ môn {dic_subject.get(message_text)} thành công!")
      menu_teacher(sender_id=teacher_id)
      sendMessage(teacher_id, "Có 1 học sinh vừa mới kết nối.")
