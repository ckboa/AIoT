import urequests as requests
import ujson
import random

def insert_my_data(cid, arg):
    post_data = ujson.dumps({ "x": cid, "value": arg})
    url = "https://esp32micropython-c827d.firebaseio.com/.json"
    res = requests.post(url, headers = {'content-type': 'application/json'},  data = post_data)
    text = res.text
    return text

x = 0
while x < 10:
    data = insert_my_data(x, random.randint(0,255) ) 
    x += 1