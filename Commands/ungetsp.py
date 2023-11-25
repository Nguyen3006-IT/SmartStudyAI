from KPAPI import sendMessage
from config import load_json, save_json, dic_subject

def ungetsp(sender_id):
  json_id = load_json("id_teacher.json") or {}

  student_id = ""
  for subject, id in json_id.items():
    if sender_id == id[1]:
      teacher_id = id[0]
      student_id = id[1]
      id[1] = None
      sj_now = subject
      break
    elif sender_id == id[0]:
      teacher_id = id[0]
      student_id = id[1]
      id[1] = None
      break

  save_json("id_teacher.json", json_id)

  if student_id == "":
    sendMessage(sender_id, "Hiện bạn đang không kết nối với giáo viên nào !")
    #if sender_id not in [id[0] for id in json_id.values()]:

  elif student_id == None and teacher_id == sender_id:
    sendMessage(sender_id, "Không có học sinh nào !")
  elif sender_id == teacher_id:
    sendMessage(teacher_id, "Bạn đã đưa học sinh ra khỏi phòng thành công.")
    sendMessage(student_id, "Bạn đã được giáo viên đưa ra khỏi phòng.")

  else:
    sendMessage(teacher_id, "Học sinh đã ngắt kết nối với bạn.")
    sendMessage(sender_id, f"Bạn đang cần giúp đỡ ở bên môn {dic_subject.get(sj_now)}. Bạn đã ngắn kết nối thành công!")
  