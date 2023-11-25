from KPAPI import sendMessage
import requests, json

def thoitiet(sender_id, message_text):
  sendMessage(sender_id, "Loading... ")
  text = message_text

  try:
    if text.lower() in ["phan rang", "phan rang tháp chàm"]:
      message_text = "phan rang - tháp chàm"
      text = "phan rang - tháp chàm"
    elif text.lower() in ["sài gòn", "sai gon", "saigon"]:
      message_text = "saigon"  #ở đây bằng "ho chi minh" được nhé!
      text = "thành phố - hồ chí minh"
    else:
      message_text = message_text.replace(' ', '%20').lower()

    api_weather = requests.get(
      f'https://api.openweathermap.org/data/2.5/weather?q={message_text}&units=metric&appid=a0999c58e5d99ab8bed47d4119f5f099'
    ).json()

    dic_weather = {"Rain": "Mưa", "Clouds": "Có mây", "Sunny": "Nắng", "clear sky": "Yên tĩnh"}
    weather = dic_weather.get(api_weather['weather'][0]['main'])
    nhiet_do = api_weather["main"]["temp"]
    do_am = api_weather["main"]["humidity"]
    wind_speed = f'{round(float(api_weather["wind"]["speed"])/3.6, 2)} (km/h)'
    wind_gust = "(không có)" if len(
      api_weather["wind"]
    ) < 3 else f'{round(float(api_weather["wind"]["gust"])/3.6,2)} (km/h)'
    clouds = int(api_weather["clouds"]["all"])

    sendMessage(
      token, sender_id,
      f'◆ Dự báo thời tiết ở {text.title()} là:\n- Thời tiết: {weather}\n- Nhiệt độ: {nhiet_do}°C\n- Tốc độ gió: {wind_speed} → Có thể giật: {wind_gust}\n- Độ ẩm: {do_am}%\n- Mật độ mây: {clouds}% '
    )

  except:
    sendMessage(
      sender_id,
      "Xin lỗi bạn. Có thể bạn nhập tên của một tỉnh hoặc bạn đã nhập sai tên thành phố. Xin vui lòng bạn nhập tên một thành phố. Xin cảm ơn"
    )
