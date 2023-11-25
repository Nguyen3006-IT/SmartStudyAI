from KPAPI import *
from config import config
import json
import requests

token = config["Token"]

#hàm chuyển chữ có dấu sang không dấu
def change(strings): 
  new_string = ''
  for char in strings:
    for trade in char_vietnam.keys():
      if char in char_vietnam[trade]:
        char = trade
    new_string += char 
  return new_string
  
#hàm lấy mã thuê bao
def phone_codes(nation_code):
  url_json = requests.get("http://country.io/phone.json").json()
  return url_json.get(nation_code.upper())

# hàm chuyển đổi country -> code
def country_names(nation): 
  nation = nation if nation.lower() != "viet nam" else "vietnam"
  nations = requests.get("http://country.io/names.json").json()
  for code, country in nations.items():
    if nation.lower() == country.lower():
      return code 

#hàm dùng code country để lấy mã tiền tệ
def currencies(nation_code): 
  currency_api = requests.get(f'http://country.io/currency.json').json()
  return currency_api.get(nation_code.upper())


# hàm chính
def nation(sender_id, message_text): 
  typingon(token, sender_id)
  nation = change(message_text)
  
  sendMessage(token, sender_id, "Đang xử lý...")
  
  try: # khi tên quốc gia sai, phía dưới có kết quả gì thì bot sẽ không in ra
    nation_code = country_names(nation).lower() # code của của quốc gia hay viết tắt 
    currency = currencies(nation_code) # tiền tệ của quốc gia
  except:
    sendMessage(token, sender_id, "Xin lỗi, có thể bạn đã nhập không đúng tên quốc gia chuẩn kiểu quốc tế. Xin vui lòng nhập lại.")

  api = requests.get(f'https://restcountries.com/v3.1/alpha/{nation_code}').json()
  
  #name_nation, capitain, code_cca2, acreage, timezones, currency_name, currency_symbol, phone_code = api[0]["name"]["common"], api[0]["capital"][0], api[0]["cca2"], "{:,.3f}".format(api[0]["area"]).replace(',', '.').replace(".000",""), api[0]["timezones"][0], api[0]["currencies"][currency]["name"],  api[0]["currencies"][currency]["symbol"], phone_codes(nation_code)

  name_nation = api[0]["name"]["common"]
  capitain = api[0]["capital"][0]
  code_cca2 = api[0]["cca2"]
  acreage = "{:,.3f}".format(api[0]["area"]).replace(',','.').replace(".000","")
  timezones = api[0]["timezones"][0]
  currency_name = api[0]["currencies"][currency]["name"]
  currency_symbol =  api[0]["currencies"][currency]["symbol"]
  phone_code = phone_codes(nation_code)
  
  dic_region = {"Europe": "Châu Âu", "Americas": "Châu Mỹ", "Antarctic": "Châu Nam Cực", "Africa": "Châu phi", "Asia": "Châu Á", "Oceania": "Châu Đại Dương"}
  region = dic_region.get(api[0]["region"])
  
  map = api[0]["maps"]["googleMaps"] # chỗ này sẽ đưa ra link ggmap
  flag = api[0]["flags"]["png"] # link ảnh
  
  sendMessage(token, sender_id, f'Đây là cờ {nation.title()}... ')
  sendMedia(token, sender_id, 'image', flag)
  sendMessage(token, sender_id, f'Đây là thông tin của {nation.title()}:\n- Tên quốc gia: {name_nation}\n- Quốc gia (cca2): {code_cca2}\n- Khu vực: {region}\n- Thủ đô: {capitain}\n- Diện tích: {acreage} km²\n- Múi giờ: {timezones}\n- Tiền tệ (tên): {currency_name}\n- Kí hiệu tiền tệ: {currency_symbol}\n- Mã số thuê bao: {phone_code}\n- Vị trí trên bản đồ: {map} ')
  
  typingoff(token, sender_id)



char_vietnam = {
  'a': ['a', 'à', 'á', 'ả', 'ã', 'ạ', 'ă', 'ằ', 'ắ', 'ẳ', 'ẵ', 'ặ', 'â', 'ầ', 'ấ', 'ẩ', 'ẫ', 'ậ'],
  'd': ['đ'],
  'e': ['e', 'è', 'é', 'ẻ', 'ẽ', 'ẹ', 'ê', 'ề', 'ế', 'ể', 'ễ', 'ệ'],
  'i': ['i', 'ì', 'í', 'ỉ', 'ĩ', 'ị'],
  'o': ['o', 'ò', 'ó', 'ỏ', 'õ', 'ọ', 'ô', 'ồ', 'ố', 'ổ', 'ỗ', 'ộ', 'ơ', 'ờ', 'ớ', 'ở', 'ỡ', 'ợ'],
  'u': ['u', 'ù', 'ú', 'ủ', 'ũ', 'ụ', 'ư', 'ừ', 'ứ', 'ử', 'ữ', 'ự'],
  'y': ['y', 'ỳ', 'ý', 'ỷ', 'ỹ', 'ỵ']
}
  