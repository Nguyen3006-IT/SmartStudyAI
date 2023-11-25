import requests, json
import threading, time
from flask import Flask, request, render_template
from centre import centre
from KPAPI import sendMessage
from config import config, db_ID, load_json

app = Flask(__name__)
token=config["Token"]

@app.route('/', methods=['GET'])
def fbverify():
  # verify url call back
  try:
      count_ID = len(db_ID.all())
      count_mess = load_json("tools.json")["total_mes"] or 0
  except:
      pass
    
  if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
      if not request.args.get("hub.verify_token")=="verify_token":
          return "Verification token missmatch", 403
      return request.args['hub.challenge'], 200
  return render_template("index.html", listMes=count_mess, listId=count_ID), 200


@app.route("/", methods=['POST'])
def fbwebhook():
#    create thread for asynchronous execution
   threading.Thread(target=centre, args=(request.get_json(),)).start()
   return "Message Processed"

@app.route("/send", methods=['POST'])
def send():
    sender_id = request.form['sender_id']
    text = request.form['text']
    if sender_id and text:
        threading.Thread(target=sendMessage, args=(sender_id, text)).start()
        return "successfully"
    else:
        return "failed"
      
@app.route("/enc", methods=['GET'])
def UI_upload_code():
    return render_template("upload_code.html")

@app.route("/encode", methods=['POST'])
def encode():
    sender_id = request.form.get("id")
    lang =request.form.get("lang")
    mode=request.form.get("mode")
    if mode == "text":
      code = request.form.get("text")
    else:
      file = request.files['file']
      code=file.read().decode('utf-8')
    if lang =="python":
      content = requests.post("https://apiencode.phankhang2.repl.co/code",json={"code":code}).json()["processed_data"]
      file_name="encode.py"
      
    #----------------------------------api Github------------------------------
    headers = {
    "Authorization": f"token {config['Token_Github']}"#mes qd 2000 kí tự
    }
    payload = {
        "description": "Here is your code",
        "public": True,
        "files": {
            file_name: {
                "content": content
            }
        }
    }
    
    response = requests.post("https://api.github.com/gists", json=payload, headers=headers)

    gist_id = response.json()["id"]
    lang_code = "Python" if lang == "python" else "PHP"
    url=f"Code *{lang_code}* của bạn đã được encode tại: https://gist.github.com/SmartStudy-ChatBot/{gist_id}"
    threading.Thread(target=sendMessage, args=(sender_id, url)).start()
    return "Done"

def uptime():
  while True:
    requests.get("https://smartstudyai.nguyen3006-it.repl.co/")
    requests.get("https://send-day-to-bot.nguyen3006-it.repl.co/")
    
    time.sleep(60)


# run app
if __name__ == "__main__":
  threading.Thread(target=uptime).start()
  app.run(host='0.0.0.0', port=0000)