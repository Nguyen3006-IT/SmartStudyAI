from KPAPI import sendMessage
import random
diem = 0

def ai_love(sender_id, message_text):  
  if "full môn" in message_text:
    subjects = ["môn lý", "môn toán", "môn hóa", "môn địa", "môn sử", "môn văn", "môn sinh", "môn KTPL", "môn anh", "môn tin"]
    for subject in subjects:
        sendMessage(sender_id, f"{subject} của bạn được {random.randint(1, 9)}đ")
  else: 
    sendMessage(sender_id, f"{message_text.title()} của bạn được {random.randint(1, 9)}đ")