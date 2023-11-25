import requests, json
import threading
from flask import Flask, request, render_template
from centre import centre

app = Flask(__name__)
from sanic import response
from KPAPI import sendMessage
from config import config

token = config["Token"]


@app.route('/', methods=['GET'])
def fbverify():
  # verify url call back
  try:
    with open("ids.json", 'r') as file:
      listId = json.load(file)
  except:
    pass
  if request.args.get("hub.mode") == "subscribe" and request.args.get(
      "hub.challenge"):
    if not request.args.get("hub.verify_token") == "verify_token":
      return "Verification token missmatch", 403
    return request.args['hub.challenge'], 200
  return render_template("index.html",
                         listMes="Undefined",
                         listId=len(listId['ids'])), 200


@app.route("/", methods=['POST'])
def fbwebhook():
  #    create thread for asynchronous execution
  threading.Thread(target=centre, args=(request.get_json(), )).start()
  return "Message Processed"


@app.route("/send", methods=['POST'])
def send():
  sender_id = request.form['sender_id']
  text = request.form['text']
  if sender_id and text:
    threading.Thread(target=sendMessage, args=(token, sender_id, text)).start()
    return "successfully"
  else:
    return "failed"


@app.route("/enc", methods=['GET'])
def UI_upload_code():
  return render_template("upload_code.html")


@app.route("/encode", methods=['POST'])
def encode():
  sender_id = request.form.get("id")
  lang = request.form.get("lang")
  mode = request.form.get("mode")
  if mode == "text":
    code = request.form.get("text")
  else:
    file = request.files['file']
    code = file.read().decode('utf-8')
  if lang == "python":
    content = requests.post("https://apiencode.phankhang2.repl.co/code",
                            json={
                              "code": code
                            }).json()["processed_data"]
    file_name = "encode.py"
  else:
    file_name = "encode.php"
    content = requests.post(
      "https://www.toolfk.com/toolfk-run-encrypt-php",
      headers={
        "Host": "www.toolfk.com",
        "Method": "POST",
        "Path": "/toolfk-run-encrypt-php",
        "Scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language":
        "vi,vi-VN;q=0.9,th-TH;q=0.8,th;q=0.7,en-PN;q=0.6,en;q=0.5,fr-FR;q=0.4,fr;q=0.3,en-US;q=0.2",
        "Content-Length": "147",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie":
        "fpestid=iOxmDcfYNtVKbwmY5oKpnljeOegbSt8N6VLNMLjPBcbRJlrE7At_0DhUKPtL1XNvMrHheA; _ga_PXTWREVGSC=GS1.1.1691742300.1.0.1691742300.0.0.0; Hm_lvt_9c8c79724749349076977e161a8ca09d=1691742301; Hm_lpvt_9c8c79724749349076977e161a8ca09d=1691742301; _ga=GA1.2.503977605.1691742301; _gid=GA1.2.1158444289.1691742301; _gat_gtag_UA_31321715_4=1; XSRF-TOKEN=eyJpdiI6IlVDTWFjcVlzRUJ2YlI4emNLSVFHSGc9PSIsInZhbHVlIjoiV0FOdzJzQXRLVW55VXBzbXRFOG1YOGkxUGZOQXp6YWNEY0NTTFhVOGdEUURHbHBEUmE0WDRuOTdvRWpxRHkwSiIsIm1hYyI6IjdiZDk0ZjgzMzc1YTRlYmVmY2Q0ZTI1YWE2ODY4NWMzMzY2MTNhMWEyZjdkYTVjMDE0NWY4MzJkMTg1YTBkNzQifQ%3D%3D; s_id=eyJpdiI6Ik9WRGtJXC81YmtpNzVkNldOUm9XaUFBPT0iLCJ2YWx1ZSI6IkV5endNMXg2VTBiaGM2ZnZQeU9MMWJhbGY1NFFZejBKZ1JmdnVXcHU2akNxYzQrYnRiNHMydkpTeTY5aXlKcmoiLCJtYWMiOiIzMTc5YjliNTlkZTExNGNmZmI5MDg4OGMwMjMxMjNhMmJlZDY2OTViN2Q0MTkxNmQ4ODFmMzczMDhmNzM0MTFjIn0%3D",
        "Origin": "https://www.toolfk.com",
        "Referer": "https://www.toolfk.com/tools/convert-php.html",
        "Sec-Ch-Ua":
        "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "X-Csrf-Token": "x9AQWLS5DQP6AtfqA6eqx0v236taj7ukLUUA3xwL",
        "X-Requested-With": "XMLHttpRequest"
      },
      data={
        "code": code
      }).json()["data"]

  headers = {"Authorization": f"token {config['Token_Github']}"}

  payload = {
    "description": "Here is your code",
    "public": True,
    "files": {
      file_name: {
        "content": content
      }
    }
  }

  response = requests.post("https://api.github.com/gists",
                           json=payload,
                           headers=headers)
  gist_id = response.json()["id"]
  lang_code = "Python" if lang == "python" else "PHP"
  url = f"Code {lang_code} của bạn: https://gist.github.com/SmartStudy-ChatBot/{gist_id}"
  threading.Thread(target=sendMessage, args=(token, sender_id, url)).start()
  return "Done"


# run app
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
