import requests
from bardapi import Bard
from KPAPI import sendMessage, sendMedia
from Commands.translate_text import translate_text
from config import config, load_json, save_json
from PIL import Image
from io import BytesIO

token_Bard = config["Token_Bard"]

def bard(sender_id, message_text, reply_message):
  try:
    read_data = load_json("accounts.json") or {}
    
    if sender_id in read_data and "https://scontent.xx.fbcdn.net/" in read_data[sender_id]: 
      message_to_user, result = read_image(sender_id, message_text, read_data[sender_id])
    elif reply_message:
      if "https://scontent.xx.fbcdn.net/" in reply_message:
        message_to_user, result = read_image(sender_id, message_text, reply_message[13:])
        
    else:     
      message_to_user, result = get_answer_text(sender_id, message_text) 

    read_data[sender_id] = message_text
    save_json("accounts.json", read_data)
    
    if len(message_to_user) < 2000:
        sendMessage(sender_id, message_to_user)
    else:
      answer = message_to_user.split()
      # cắt từ đầu chuỗi đến giữa chuỗi
      half1 = message_to_user[: (len(answer)//2)] 
      # cắt từ giữa chuỗi đến cuối chuỗi
      half2 = message_to_user[(len(answer)//2):]  
      sendMessage(sender_id, " ".join(half1))
      sendMessage(sender_id, " ".join(half2))
    if result.get("links"):
      sendMedia(sender_id, "image", result["links"][0])
  
  except: 
    import traceback, sys
    from Admin.block_user_on_update import on_block_user_on_update
    name_error=str(sys.exc_info()[1])
    tb=sys.exc_info()[2]
    line_number = traceback.extract_tb(tb)[-1][1]
    text = f"ĐÃ CÓ LỖI XÃY RA!!!\n\nTên Lỗi: {name_error}\n\nTạm dịch: {translate_text(name_error,'vi')}\n\nTên file: {__name__} | Vị trí: dòng thứ {line_number}\n\nTham khảo: https://www.google.com/search?q=how+to+fix+{name_error.replace(' ','+')}+in+python"
    #sendMessage("6248280891946621", "Xuất hiện lỗi -> " + str(e))
    sendMessage("6312817428801561", text)
    sendMessage("6169255926506657", text)
    on_block_user_on_update("6312817428801561")


def get_answer_text(id_user, text):
  #try:
    bard = Bard(token=token_Bard)
    result = bard.get_answer(text)
  #except Exception as e: print(e)
    return result["content"], result

 
def read_image(user_id, user_text, url_image):
  print("read img")
  bard = Bard(token=token_Bard)
  response = requests.get(url_image)
  if response.status_code == 200:
    image = Image.open(BytesIO(response.content))
  else:
     print("404")
  image_bytes = BytesIO()
  image.save(image_bytes, format="png")
  
  data_img_url = image_bytes.getvalue()
  text_eng = translate_text(text=user_text, target_lang='en')
  bard_answer = bard.ask_about_image(text_eng, data_img_url)
  
  find_markdown = [i for i in __import__('re').findall(r'```.*```', bard_answer["content"], __import__('re').DOTALL) if i[0]]

  text = translate_text(text=bard_answer["content"], target_lang='vi') if find_markdown == [] else bard_answer["content"]

  return text, bard_answer

def save_image_to_Bard(sender_id, url_image):
  accounts = load_json("accounts.json")
  accounts[sender_id] = url_image
  save_json("accounts.json", accounts)
  sendMessage(sender_id, "Bạn muốn tôi giúp gì về bức tranh này ?")


