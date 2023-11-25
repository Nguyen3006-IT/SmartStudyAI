from KPAPI import sendMessage
from requests import post

def encode(sender_id):
  url = f'https://smartstudyai.nguyen3006-it.repl.co/enc?id={sender_id}'
  sendMessage(
    sender_id,
    "Vào đây nhập code hoặc tải lên file code của bạn: " + url)
