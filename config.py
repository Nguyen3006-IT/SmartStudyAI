import os, json, sqlite3

config = {
  "Token": os.environ['Token'],
  "Token_OpenAI": os.environ['Token_OpenAI'],
  "Token_Github": os.environ['Token_Github'],
  "Token_Bard": os.environ['Token_Bard']
}

# -------------------------------define commands----------------------------------
commands = {
  "không có": [None, True, "Gửi tin nhắn", "Trò chuyện với ChatGPT (dữ liệu tính đến 2021)","AI"],

  ".bard": ["bard", True, "Gửi .bard <Tin_nhắn>", "Trò chuyện cùng Bard AI (không dùng để viết code. Dữ liệu cập nhật realtime)","AI"],

  ".bqt": ["bqt", True, "Gửi .bqt <Verd>", "Tra cứu bảng động từ bất quy tắc.","cong_cu"],

  ".morse": ["morse", True, "Gửi .morse <Văn_bản>", "Chuyển VĂN BẢN sang mã morse.", "chuyen_van_ban"],

  ".text": ["textMorse", True, "Gửi .text <Morse_của_bạn>", "Chuyển mã Morse sang VĂN BẢN.", "chuyen_van_ban"],

  ".roman": ["lama", True, "Gửi .roman <Số_tự_nhiên>", "Chuyển số tự nhiên sang số La Mã.", "chuyen_van_ban"],

  ".integer": ["integer", True, "Gửi .integer <La_mã>", "Chuyển đổi số La mã sang số nguyên.", "chuyen_van_ban"],

  ".qr": ["qr", True, "Gửi .qr <văn_bản>", "Chuyển văn bản bất kì sang QR Code.", "chuyen_van_ban"],

  ".wtof": ["thoitiet", True, "Gửi .wtof + <địa điểm>", "Xem thời tiết tỉnh/thành phố", "cong_cu"],

  ".nation": ["nation", True, "Gửi .infor <Tên_quốc_gia>", "Xem thông tin của quốc gia (yêu cầu nhập tên quốc gia bằng Tiếng Anh)","cong_cu"],

  ".list": ["list", False, "Gửi .list", "Xem các chức năng", ""],

  ".download": ["getVideo", True, "Gửi .download <URL_video>", "Tải xuống video từ các mạng xã hội như Facebook, Tiktok, Douyin, Youtube thông qua link","cong_cu"],

  ".error": ["error", True, "Gửi .error <Nội_dung_cần_báo> ", "Báo lỗi đến cho Admin.", "cong_cu"],

  ".send": ["send", True, "Gửi .send <tin nhắn>", "Gửi tin nhắn đến Giáo Viên và ngược lại (chỉ khi kết nối với giáo viên)", "cong_cu"],
  
  "/sendall": ["sendall", True, "admin", "admin", ""],
  
  ".in4": ["chemistry", True, "Gửi .in4 <nguyên tố>", "Tra cứu thông tin nguyên tố Hóa học", "cong_cu"],

  ".word": ["EnWords", True, "Gửi .word <từ vựng>", "Tra từ vựng tiếng Anh (hiện đang có )", ""],
  
  ".deloy": ["deloy", True, "Gửi .deloy <code HTML của bạn>", "Deloy code HTML của bạn và nhận link trang web vừa deloy", "cong_cu"],
  
  "play.noitu": ["menu_noitu", None, "Gửi .rep <text>", "Trò chơi nối chữ ", "AI"],
  
  ".encode": ["encode", False, "Gửi .encode", "Mã hóa code python", "cong_cu"],

  ".tientri" : ["ai_love", True, "Gửi .tientri <text>", "đoán điểm số giữa kì của bạn","AI"]
}


class Database:
  def __init__(self, db_name:str, table_name:str, build_table:str):
    self.connection = sqlite3.connect(db_name, check_same_thread=False)
    self.cur = self.connection.cursor()
    self.table = table_name
    try:
      self.cur.execute(f"""CREATE TABLE {self.table} ({build_table})""")
    except: 
      pass
    
  def insert(self, value_table:str, value_insert:str):
    try:
      self.cur.execute(f"INSERT INTO {self.table} ({value_table}) VALUES ({value_insert});")
      self.connection.commit()
    except: print("ERROR !!!!!!!!!!!!")

  def select(self, value_table:str, value_select:str):
    try:
      self.cur.execute(f"SELECT * FROM {self.table} WHERE {value_table}={value_select}")
      return self.cur.fetchone() 
    except: print("ERROR !!!!!!!!!!!!")
  
  def selectAll(self, value_table) -> list:
    try:
      self.cur.execute(f"SELECT * FROM {self.table} WHERE {value_table}")
      return self.cur.fetchall()
    except:  
      print("ERROR !!!!!!!!!!!!")

  def all(self) -> list:
    self.cur.execute(f"SELECT * FROM {self.table}")
    return self.cur.fetchall()
    
      
db_ID = Database("IDs.db", "ids", "id TEXT")

  
def load_json(file_name):
  try:
    with open(file_name, "r") as file:
      return json.load(file)
  except:
    print("Open Json Error")
    return 

def save_json(file_name, data):
  try:
    with open(file_name, "w") as save:
      json.dump(data, save, ensure_ascii=False, indent=2)
  except: 
    print("Save Json Error!")


dic_subject = {
  "Math": "Toán học", 
  "Physics": "Vật Lý", 
  "Chemistry": "Hóa học", 
  "Literature": "Văn học", 
  "History": "Lịch Sử", 
  "Geography": "Đại Lí", 
  "Technicality": "Công Nghệ", 
  "IT": "Tin Học", 
  "English": "Tiếng Anh"
}
