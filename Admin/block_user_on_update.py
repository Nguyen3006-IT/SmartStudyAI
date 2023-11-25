from KPAPI import sendMessage
from config import load_json, save_json
from Module.save_user_for_upd import run_JsonUser

def on_block_user_on_update(admin_id):
  try:
    tool = load_json("tools.json") or {}
    tool["update_bot"] = True
    save_json("tools.json", tool)
    sendMessage(admin_id, "Bật CĐ update Bot thành công. admin Minh Tuấn, Hoàng Nguyên, Khang Phan")
  except:
    sendMessage(admin_id, "Bật chế độ update Bot không thành công")


def off_block_user_on_update(admin_id): 
  try:
    tool = load_json("tools.json") or {}
    tool["update_bot"] = False
    save_json("tools.json", tool)
    sendMessage(admin_id, "Tắt CĐ update Bot thành công")

    run_JsonUser()

  except:
    sendMessage(admin_id, "Tắt chế độ update Bot không thành công")

  
