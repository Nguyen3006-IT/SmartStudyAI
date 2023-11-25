from KPAPI import sendMessage, typingoff
from config import config, load_json, save_json
from Action.All_Menu import teacher, student
import requests, random, json

url = "https://gist.githubusercontent.com/Nguyen3006-IT/85ef6863ddbaaecb3c39d490bf7802b3/raw/f0553d0f2880e245479fa58083098ed0faf79d8d/text2len.json"
json_text = requests.get(url).json()

def conjunction(sender_id, message_text):
  collect_text(message_text.lower())
  try:
    dic_text = load_json("accounts.json") or {}
    texts_collect = load_json("textNoiTu.json") or {}
    
    if dic_text[sender_id] == "noitu_empty":
      text_user = message_text.split()[-1]
      text_true = [text for text in json_text if text_user == text.split()[0]]
      if text_true == []: 
        dic_text[sender_id] = "noitu_empty"
        sendMessage(sender_id, "Bot hết từ... Mong bạn cung cấp thêm giúp Bot.")
      else: 
        dic_text[sender_id] = random.choice(text_true) 
        sendMessage(sender_id, dic_text[sender_id]) 
  
    elif message_text.lower().split()[0] == dic_text[sender_id].lower().split()[-1] and len(message_text.split()) == 2:
      text_user = message_text.split()[-1]
      text_true = [text for text in json_text+texts_collect if text_user == text.split()[0]]
      if text_true == []:
        dic_text[sender_id] = "noitu_empty"
        sendMessage(sender_id, "Bot hết từ. Mời bạn đi trước.")
      else:
        dic_text[sender_id] = random.choice(text_true)
        sendMessage(sender_id, dic_text[sender_id])
  
    else:
      sendMessage(sender_id, "Bạn đã thua. Bot đi trước")
      dic_text[sender_id] = random.choice(json_text)
      sendMessage(sender_id, dic_text[sender_id])
      
    typingoff(sender_id)
    save_json("accounts.json", dic_text)
    
  except Exception as e:
        print(e)


def ongame(sender_id):
  dic_text = load_json("accounts.json")
  dic_text[sender_id] = json_text[random.randint(1,500)]
  save_json("accounts.json", dic_text)
  sendMessage(sender_id, dic_text[sender_id])

def offgame(sender_id):
  tool = load_json("tools.json")
  tool["online_noitu"].remove(sender_id)
  teacher(sender_id) if sender_id in tool["teacher"] else student(sender_id)
  save_json("tools.json", tool)
  sendMessage(sender_id, "Bạn đã rời trò chơi nối từ thành công.")

def collect_text(text):
  texts_collect = load_json("textNoiTu.json")
  texts_collect.append(text)
  with open("textNoiTu.json", 'w') as save:
    json.dump(texts_collect, save, ensure_ascii=False)


def rep_start_conjunction(sender_id):
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({
      "recipient":{"id": sender_id},
      "message":{
        "attachment":{
        "type":"template",
        "payload":{
            "template_type":"button",
            "text": "Chọn người đi trước",
            "buttons":[{
              "type":"postback",
              "title": "SSBot",
              "payload":"bot_start"
            },
            {
              "type":"postback",
              "title": "Tôi",
              "payload": "user_start"
            }
            ]}}}})
  requests.post("https://graph.facebook.com/v2.6/me/messages", params=params,headers=headers, data=data)