from KPAPI import sendMedia, sendMessage, typingoff
from config import config, load_json, save_json
import json, requests, os, random

gooey_api_key = os.environ['gooey_api_key']

def qr(sender_id, message_text):
  params = {"access_token": config["Token"]}
  headers = {"Content-Type": "application/json"}
  data = json.dumps({
    "recipient":{"id": sender_id},
    "message":{"attachment":{"type":"template", "payload":
      {"template_type":"button", "text": "Chọn kiểu QR", "buttons":[
        {"type":"postback", "title":"QR truyền thống", "payload": f"QR_Clear {message_text}"},
        {"type":"postback", "title":"AI tự vẽ QR", "payload": f"AI_Art_QR {message_text}"},
        {"type":"postback", "title":"Tạo chủ đề QR", "payload": f"Prompt_QR {message_text}"}
      ]}}}})
  requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)


def qr_clear(sender_id, message_text):
  from urllib.parse import quote
  sendMessage(sender_id, "Vui lòng đợi trong giấy lát...")
  sendMedia(
    sender_id, "image",
    f"https://api.qrserver.com/v1/create-qr-code/?size=500x500&data={quote(message_text)}"
  )

def Prompt_QR_Code(sender_id, message_text, prompt):
  accounts = load_json("accounts.json") or {}
    
  if prompt:
    sendMessage(sender_id, 'Bạn nhập chủ đề bất kì cần vẽ QR Code. Bạn có thể gửi "not" để tôi tự tạo chủ đề.')
    accounts[sender_id] = f"Prompt_to_AI_ART_QR {message_text}"
  else:
    prompt = message_text
    if message_text.lower() == "not":
      prompt = None
    message_text = " ".join(accounts[sender_id].split()[1:])
    qr_AI(sender_id, message_text, prompt=prompt)
    accounts[sender_id] = "creat qr complete!"
    tools = load_json("tools.json") or {}
    tools["Creating_QR"].remove(sender_id)
    save_json("tools.json", tools)
    
  save_json("accounts.json", accounts)
    

def qr_AI(sender_id, message_text, prompt=None):
  sendMessage(sender_id, "Xin đợi tôi trong vòng 15-30 giây...")
  lst_seed = [4268277630, 1858283311, 1599532306, 1355020499, 1848776043, 843891565, 440482501, 3223249209, 4072185744, 2746317213, 3009170676, 679178490]
  payload = {
    "qr_code_data": message_text,
    "qr_code_input_image": None,
    "use_url_shortener": False,
    "text_prompt": "technology 3D, 8k, UHD" if prompt == None else prompt,
    "negative_prompt": "ugly, disfigured, low quality, blurry, nsfw, text, words",
    "selected_model": "dream_shaper",
    "selected_controlnet_model": ["sd_controlnet_brightness", "sd_controlnet_tile"],
    "output_width": 512,
    "output_height": 512,
    "guidance_scale": 10,
    "controlnet_conditioning_scale": [0.4, 0.4],
    "num_outputs": 1,
    "quality": random.randint(100, 200),
    "scheduler": "euler_ancestral",
    "seed": random.choice(lst_seed),
    "obj_scale": 0.65,
    "obj_pos_x": 0.5,
    "obj_pos_y": 0.5,
  }
  response = requests.post(
    "https://api.gooey.ai/v2/art-qr-code/",
    headers={"Authorization": "Bearer " + gooey_api_key},
    json=payload,
  )
  assert response.ok, response.content
  result = response.json()
  print(result)
  sendMedia(sender_id, "image", result["output"]["output_images"][0])
  sendMessage(sender_id, "Xin lỗi đã để bạn đợi 🥺.")
  typingoff(sender_id)
  
  if result.get("detail"):
    print("Error qr status:", response.status_code)
    sendMessage(sender_id, "Có vẻ có lỗi nên tạo QR Code không thành công, dùng lệnh .erorr <nội dung> để báo với admin")
