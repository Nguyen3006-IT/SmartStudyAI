import requests, re
from config import config, commands
from KPAPI import *
from Commands.translate_text import *

token = config["Token"]


def EnWords(sender_id, message_text):
  typingon(sender_id)
  if message_text[0].lower() in ["t", "u", "v", "w", "y", "z"]:
    data_words = requests.get(url1).text
  elif message_text[0].lower() in ["n", "o", "p", "q", "r"]:
    data_words = requests.get(url2).text
  elif message_text[0].lower() in ["h", "i", "j", "k", "m"]:
    data_words = requests.get(url3).text
  elif message_text[0].lower() in ["d", "e", "f"]:
    data_words = requests.get(url4).text
  elif message_text[0].lower() == "s":
    data_words = requests.get(url1).text + "\n" + requests.get(url2).text
  elif message_text[0].lower() == "n":
    data_words = requests.get(url2).text + "\n" + requests.get(url3).text
  elif message_text[0].lower() == "g":
    data_words = requests.get(url3).text + "\n" + requests.get(url4).text
  elif message_text[0].lower() == "c":
    data_words = requests.get(url4).text + "\n" + requests.get(url5).text
  else:
    data_words = requests.get(url5).text

  user_word, word_vie = xuly(x=data_words, user_word=message_text)
  if word_vie != None:
    word_vie = splitMean(word_vie)
    [
      sendMessage(sender_id,
                  f"*{message_text.capitalize()}*  \n```{word_vi}```")
      for word_vi in word_vie
    ]
  else:
    #vie = translate_text(text=message_text, target_lang="vi")
    sendMessage(
      sender_id,
      translate_text(text=message_text, target_lang="vi")
    )

  typingoff(sender_id)


def xuly(x, user_word):
  string = None
  for i in x.split("\n"):
    word_en = re.sub('\W+?', "",
                     re.sub(r'\((.*?)\)', r'',
                            i.split("\t")[0]).strip())
    if re.sub('\W+?', "", user_word.lower()) == word_en.lower():
      mean = eval('"""' + '\n' + i.split("\t")[1] + '\n' + '"""')
      mean = mean.split("\n")
      string = ""
      for j in mean:
        if "*" in j:
          j = j.title()
        string += j + "\n"
  return word_en, string


def splitMean(string):
  if len(string) < 2000:
    return [string]
  elif 2000 < len(string) < 4000:
    half1 = string[:len(string) // 2]
    half2 = string[len(string) // 2:]
    return [half1, half2]
  else:
    half1 = string[:(len(string) // 4)]
    half2 = string[(len(string) // 4):(len(string) // 4) * 2]
    half3 = string[(len(string) // 4) * 2:(len(string) // 4) * 3]
    half4 = string[(len(string) // 4) * 3:]
    return [half1, half2, half3, half4]


url1 = "https://gist.githubusercontent.com/Nguyen3006-IT/cdba6c7750de29d47f23a29a06ea1fa2/raw/a68f4e7cbb9eade9513702bf3b0ee6ef5671abc0/en-vi1.txt"
url2 = "https://gist.githubusercontent.com/Nguyen3006-IT/a22342b15025876068d9e9a88e903fda/raw/4eea4f93c0d2f3ca9887cdcb7415e276465aed6e/gistfile1.txt"
url3 = "https://gist.githubusercontent.com/Nguyen3006-IT/2504a6a981ea49b0ec18855901c58eb9/raw/0ce63dc3afd79d1cc6e1b88f02835bc9ffdb3d25/en-vi3.txt"
url4 = "https://gist.githubusercontent.com/Nguyen3006-IT/95c1c47aad4a3ac0a7197b7c67a3a3cd/raw/05f7cbdab02a5b5244bd6f5b0af5c46b5292bda6/gistfile1.txt"
url5 = "https://gist.githubusercontent.com/Nguyen3006-IT/67877c551eb198c57acbfb28b1e869be/raw/98d18ec740e3eb216032270ed5b0abcfd9d0539a/gistfile1.txt"
