import utime, machine
import random
import urequests as requests
import ujson
import random
import network

url_bkk = "http://worldtimeapi.org/api/timezone/Asia/Bangkok" 
# internal real time clock
rtc = RTC()

# connect wifi
def connect():   
    ssid = "ssid"
    password =  "password"
    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
      print("Already connected")
      return
    station.active(True)
    station.connect(ssid, password)

# get Bangkok time 
def get_bangkok_time():   '\darkcircle{2}'
    response = requests.get(url_bkk)
       
    if response.status_code == 200: 
        parsed = response.json()
        datetime_str = str(parsed["datetime"])
        year = int(datetime_str[0:4])
        month = int(datetime_str[5:7])
        day = int(datetime_str[8:10])
        hour = int(datetime_str[11:13])
        minute = int(datetime_str[14:16])
        second = int(datetime_str[17:19])
        subsecond = int(round(int(datetime_str[20:26]) / 10000))                
        rtc.datetime((year, month, day, 0, hour, minute, second, subsecond))

# get time 
def get_current_time():  '\darkcircle{3}'
    current_time = "{0:4d}-{1:02d}-{2:02d}T{4:02d}:{5:02d}:{6:02d}".format(*rtc.datetime())
    return current_time

connect()
get_bangkok_time()
while True:  
    print(get_current_time())
    utime.sleep(300)    
