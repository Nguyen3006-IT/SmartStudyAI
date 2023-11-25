from KPAPI import sendMessage
from config import load_json, save_json, dic_subject

def sp_huy(sender_id):
  list_id = load_json("id_teacher.json") or {}
  
  subject = ""
  for id_user in list_id:
    if sender_id.strip() == list_id.get(id_user)[0]:
      subject = id_user
      list_id.get(id_user)[0] = None
      student_id = list_id.get(id_user)[1]
      list_id.get(id_user)[1] = None

  if subject != "":
      save_json("id_teacher.json", list_id)
        
      sendMessage(sender_id, f'Hiện tại bạn đang hỗ trợ môn {dic_subject.get(subject)}. Bạn đã hủy hỗ trợ thành công!\nCảm ơn bạn đã giúp hỗ trợ. ')
      sendMessage(student_id, "Giáo viên đã rời phòng. Vì thế bạn đã được đưa khỏi phòng.")
      
  else:
    sendMessage(sender_id, "Hiện tại bạn không có trong danh sách hỗ trợ.")

    
      
