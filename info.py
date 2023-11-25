import json, requests, traceback, sys, sqlite3, threading
from config import db_ID, load_json, save_json
from KPAPI import seen, sendMessage
from Module.save_user_for_upd import save_user_for_upd
from mtranslate import translate
from NAPI import saveMsg

#____________________________________info_real_______________________________
def info(data_user):
  print(data_user)
  tools = load_json("tools.json") or {}
  tools["total_mes"] += 1
  save_json(file_name="tools.json", data=tools)

  try:
    print(tools)
    sender_id = data_user['entry'][0]['messaging'][0]['sender']["id"]
    seen(send_to_id=sender_id)

    if not db_ID.select(value_table="id", value_select=sender_id):
      sendMessage(sender_id, 'SSBot chào bạn, SSBot được lập trình ra để hỗ trợ bạn học tập và giải đáp thắc mắc của bạn. SSBot có các tính năng nữa nhé   ❤️❤️\n\nBạn cần biết những chức năng gì hãy ấn ".list"  để xem câu lệnh và công dụng các tính năng đó. Cha đẻ trẻ tuổi của SSBot gồm: Duy Khang, Hoàng Nguyên, Minh Tuấn.')

      db_ID.insert(value_table="id", value_insert=sender_id) # lưu id vào db

    for data in data_user['entry'][0]['messaging']:
      timestamp = data["timestamp"]

      if tools["update_bot"] and sender_id not in ["6248280891946621", "6312817428801561", "6169255926506657"]:
        save_user_for_upd(sender_id)
      elif sender_id in tools["Creating_QR"]:
        from Commands.qr import Prompt_QR_Code
        Prompt_QR_Code(sender_id, data["message"]["text"], None)
      elif sender_id in tools["online_noitu"]:
          if data.get('postback'):
            return json.dumps({"postback": [sender_id, data['postback']['payload']]})
          elif data["message"].get("quick_reply"):
            payload = data['message']['quick_reply']['payload']
            return json.dumps({"postback": [sender_id, payload]})
          elif data["message"].get("text"):
            from Commands.conjunction import conjunction
            conjunction(sender_id, data["message"]["text"])

      elif data.get('postback'):
          return json.dumps({"postback": [sender_id, data['postback']['payload']]})

      elif data["message"].get("text"):
          message_text = data['message']["text"]
          return json.dumps({"message": [sender_id, message_text, ""]})

      elif data["message"].get("attachments"):
          message_id = data['message']['mid']
          url = data['message']['attachments'][0]['payload']['url']
          threading.Thread(target=saveMsg, args=(timestamp, message_id, url)).start()
          type = data['message']['attachments'][0]['type']
          return json.dumps({"attachments": [sender_id, url, type]})

      else: pass

  except Exception as e:
    name_error=str(sys.exc_info()[1])
    tb = sys.exc_info()[2]
    line_number = traceback.extract_tb(tb)[-1][1]
    print(f"ĐÃ CÓ LỖI XÃY RA!!!\n\nTên Lỗi: {name_error}\n\nTạm dịch: {translate(name_error,'vi')}\n\nTên file: {__name__} | Vị trí: dòng thứ {line_number}\n\nTham khảo: https://www.google.com/search?q=how+to+fix+{name_error.replace(' ','+')}+in+python")
