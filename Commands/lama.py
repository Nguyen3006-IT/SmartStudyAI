from KPAPI import sendMessage
from config import config

token = config["Token"]

def lama(sender_id, message_text):
  message_text = str(message_text)
  
  try:
    message_text = int(message_text) # nếu người dùng này nhập số la mã line này sẽ sai và xét hàm except
    val = message_text
      
    lama = ''  # tạo string rỗng để lưu số La Mã
    for value, num in dict_lama.items():
        count = int(message_text) // value # đếm giá trị số La Mã hiện tại trong số number
        lama += num * count  # add vào string lượng gtrị số La Mã theo số lần xuất hiện trong number
      
        message_text = int(message_text) - (count * value)  # Trừ đi giá trị số la Mã hiện tại tính được từ number
        
    sendMessage(sender_id, f'Số La Mã của {val} là:\n→ {lama}')  

  except:
    sendMessage(sender_id, 'Có thể bạn nhập không đúng định dạng số. Vui lòng nhập lại') 
    
# Tạo một dictionary để lưu giá trị tương ứng giữa các số La Mã và các giá trị thập phân tương ứng
dict_lama = { 1000: 'M',      900: 'CM',      500: 'D',   
              400: 'CD',      100: 'C',       90: 'XC',
              50: 'L',        40: 'XL',       10: 'X',
              9: 'IX',        5: 'V',         4: 'IV',
              1: 'I'}

  