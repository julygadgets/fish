import requests

def send_msg(text):
   token = "5676519330:AAFRP3MvFZR6DSpFokylpg5_3gqDJAPPcrY"
   chat_id = "945684728"
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
   results = requests.get(url_req)
   print(results.json())

 