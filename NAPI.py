import requests

def saveMsg(timestamp, message_id, message_text):
  data = {
    "timestamp": timestamp, 
    "mid": message_id, 
    "message": message_text
  }
  requests.post("https://save-message-id-for-bot.nguyen3006-it.repl.co/save", json=data)

def getMsg(message_id):
  data = {"id": message_id}
  return requests.get(
    "https://save-message-id-for-bot.nguyen3006-it.repl.co/get_message",
    params=data
  ).json()

def search_irregular(verb):
  url = "https://data-for-ssbot.nguyen3006-it.repl.co/irregular"
  try: 
    return requests.get(url, params={"verb": verb}).json()
  except:
    return
  