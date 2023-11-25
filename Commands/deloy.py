from KPAPI import sendMessage
from requests import post

def deloy(sender_id, message_text):
  url = 'https://deloy.communityvn.repl.co/generate_code'
  data = {'text': message_text}
  sendMessage(
    sender_id,
    "Đây là link web của bạn: " + post(url, json=data).json()["link"])
