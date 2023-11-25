from KPAPI import sendMessage
from config import config

token = config["Token"]

def integer(sender_id, message_text):
  try:
    message_text = str(message_text)
    value, integer  = 0
    for char in message_text.upper():
      for key, val in dict_lama.items():
        if char == val: 
          roman = key 
          if roman > value:
            integer += roman - 2*value
          else:
            integer += roman
        value = roman
    sendMessage(sender_id, f'Số nguyên của {message_text.upper()} là:\n→ {integer}') 
    
  except:
    sendMessage(sender_id, 'Có thể bạn nhập không đúng định dạng số La Mã. Hãy nhập lại.')

dict_lama = { 1000: 'M',      900: 'CM',      500: 'D',   
              400: 'CD',      100: 'C',       90: 'XC',
              50: 'L',        40: 'XL',       10: 'X',
              9: 'IX',        5: 'V',         4: 'IV',
              1: 'I'}
