from KPAPI import sendMessage
from config import config

token = config["Token"]

#hàm chuyển mã Morse sang văn bản
def textMorse(sender_id, message_text):
  list_message_text = message_text.split()

  total = ""
  char = 0
  for Morse in list_message_text:
    for key, val in dic_morse.items():
      if Morse == val:
        total += key 
      else: 
        total += ""
        

  if total != "":        
    sendMessage(token, sender_id, "Đây là văn bản bạn cần:\n" + total.upper())
  else: 
    sendMessage(token, sender_id, 'Có vẻ bạn nhập không đúng định dạng mã Morse. Nếu bạn muốn chuyển đổi VĂN BẢN sang MÃ MORSE hãy dùng cú pháp ".morse + văn_bản". Xin cảm ơn')

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