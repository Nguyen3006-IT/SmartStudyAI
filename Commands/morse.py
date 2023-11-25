from KPAPI import sendMessage
from config import config

token = config["Token"]

# hàm chuyển đổi chữ có dấu sang chữ không dấu
def convert_telex(char): 
    for key in char_vietnam.keys(): 
        if char in char_vietnam[key]: # nếu nó là chữ có dấu thì sẽ bị đổi
            return key
    return char # Nếu không có dấu hay kí tự khác thì nó sẽ trả về lại ban đầu
  
def morse(sender_id, message_text):  
  if message_text == "{full}":
    list_Morse = []
    for key, value in dic_morse.items(): 
      list_Morse.append(f'" {key.upper()} " :  {value}')
    dictionary_morse = "\n".join(list_Morse)
    sendMessage(sender_id, f'Dưới đây là bảng mã Morse:\n{dictionary_morse} \n(với khoảng trắng là: " / ")' )

  else: 
    message_text = message_text.lower()
    list_message = list(message_text) 
    total = []
    for text in list_message:
      text_eng = convert_telex(text)
      if text_eng not in dic_morse.keys():
        total = None
        break
        
      for key, val in dic_morse.items():
        if text_eng == key:
          total.append(val)
    
    if total == None:
      sendMessage(sender_id, f'Kí tự " {text_eng} " không có trong bảng mã Morse')
    else:
      sendMessage(sender_id, "Đây là mã morse bạn cần:\n" + " ".join(total))  


dic_morse = {
  "a": ".-",  "b": "-...",  "c": "-.-.",  "d": "-..",  "e": ".",  "f": "..-.",   
  "g": "--.", "h": "....",  "i": "..",  "j": ".---",  "k": "-.-", "l":".-..",  
  "m":"--",  "n":"-.",  "o": "---",  "p": ".--.",  "q": "--.-",  "r": ".-.",  
  "s": "...",  "t": "-",   "u": "..-",  "v": "...-",  "w": ".--",  "x": "-..-",  
  "y": "-.--",  "z":"--..",

  "0": "-----",	 "1": ".----",	"2": "..---",  "3": "...--",  "4": "....-",  
  "5": ".....",  "6": "-....",  "7": "--...",	"8": "---..", "9": "----.",
  
  ".":  ".-.-.-",  ",":  "--..--",  "?":	"..--..",  "'":	 ".----.",  "!":  "-.-.--",
  "/":	"-..-.",   "(":  "-.--.",   ")":  "-.--.-",  "&":	 ".-...",   ":":  "---...",  	
  ";":  "-.-.-.",  "=":  "-...-",   "+":	".-.-.",   "-":  "-....-",  "_":	"..--.-",
  '"':	".-..-.",	 "$": "...-..-",	"@":	".--.-.",  "¿":	"..-.-",    "¡":  "--...-",
  " ":  "/"
}

char_vietnam = {
  'a': ['a', 'à', 'á', 'ả', 'ã', 'ạ', 'ă', 'ằ', 'ắ', 'ẳ', 'ẵ', 'ặ', 'â', 'ầ', 'ấ', 'ẩ', 'ẫ', 'ậ'],
  'd': ['đ'],
  'e': ['e', 'è', 'é', 'ẻ', 'ẽ', 'ẹ', 'ê', 'ề', 'ế', 'ể', 'ễ', 'ệ'],
  'i': ['i', 'ì', 'í', 'ỉ', 'ĩ', 'ị'],
  'o': ['o', 'ò', 'ó', 'ỏ', 'õ', 'ọ', 'ô', 'ồ', 'ố', 'ổ', 'ỗ', 'ộ', 'ơ', 'ờ', 'ớ', 'ở', 'ỡ', 'ợ'],
  'u': ['u', 'ù', 'ú', 'ủ', 'ũ', 'ụ', 'ư', 'ừ', 'ứ', 'ử', 'ữ', 'ự'],
  'y': ['y', 'ỳ', 'ý', 'ỷ', 'ỹ', 'ỵ']
}
