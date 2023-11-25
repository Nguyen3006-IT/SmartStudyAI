import requests
from KPAPI import typingoff, sendMessage
from config import config, load_json, save_json

def gpt(sender_id, message):
  try:
    account = load_json("accounts.json") or {}
    if sender_id in account :
      if "https://scontent.xx.fbcdn.net/" in account[sender_id]:
        from Commands.bard import read_image
        answer, content = read_image(sender_id, message, account[sender_id])
        account[sender_id] = answer
        save_json("accounts.json", account)
        return send_content(sender_id, answer)
      
    len_text_sender = len(account[sender_id]) < 2000
    text = account[sender_id] if len_text_sender else ""
  
    url = "https://api.openai.com/v1/chat/completions"
    header = {
      'Content-Type': 'application/json',
      'Authorization': f'Bearer {config["Token_OpenAI"]}'
    }
    
    data = {
      "model": "gpt-3.5-turbo-1106",
      "messages": [{
        "role": "system",
        "content": "Tên tôi là SmartStudy. Bạn có thể gọi tôi là AI hoặc Chat-Bot. Tôi được tạo ra bởi Duy Khang, Hoàng Nguyên, Minh Tuấn và Công Toại. Tôi được tạo ra nhằm mục đích giúp mọi người học tập và giải đáp các thắc mắc."
        },
        {"role": "assistant", "content": f'{text}'},
        {"role": "user", "content": f'{message}'}
      ]
    }
  
    response = requests.post(url, headers=header, json=data).json()
    #print(response)
    account[sender_id] = response['choices'][0]['message']['content']
    answer = account[sender_id]
    save_json("accounts.json", account)

    send_content(sender_id, answer)

  except Exception as e:
    from Commands.bard import bard
    bard(sender_id, message, None)
    print(e)


def send_content(sender_id, text):
  if len(text) < 2000:
    sendMessage(sender_id, text)
  else:
    answer = text.split() 
    sendMessage(sender_id, *answer[: len(answer)//2])
    sendMessage(sender_id, *answer[(len(answer)//2) :])

  typingoff(sender_id)
