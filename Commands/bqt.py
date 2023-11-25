from KPAPI import sendMessage
from NAPI import search_irregular

# hàm tra cứu động từ bất quy tắt tiếng anh
def bqt(sender_id, message_text):
  result = search_irregular(verb=message_text)
  if result:
    sendMessage(
      send_to_id=sender_id,
      message_text=f'''● Động từ bất quy tắc của "{message_text.title()}" là:
    ☞ V1:  {result["v1"]}
    ☞ V2:  {result["v2"]}
    ☞ V3:  {result["v3"]}
    ☞ Nghĩa:  {result["means"]}
      ''')

  else:
    sendMessage(sender_id, "Thông báo, có thể từ này không tồn tại trong từ điển bất quy tắc.")