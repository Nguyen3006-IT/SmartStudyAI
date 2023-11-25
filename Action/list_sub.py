from KPAPI import sendMessage
from config import dic_subject, load_json

def list_sub(sender_id):
  try:
    message= ""
    gv= ""
    hs= ""
    
    lst = load_json("id_teacher.json") or {}
      
    for x, y in lst.items():
      gv = "Có"
      hs = "Có"
      if y[0] == None:
        gv = "không có"
      if y[1] == None:
        hs="không có"

      message += f"""
◆ {dic_subject.get(x)}:
- Giáo viên: {gv}
- Học sinh: {hs}\n {"_"*30}"""
    sendMessage(sender_id, message)
      
  except Exception as e:
    print(e)
