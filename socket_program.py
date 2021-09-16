import network
import socket
import time

wlan=None
soc=None


def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)                    
  wlan.active(True)                                     
  wlan.disconnect()                                   
  wlan.connect(ssid,passwd)                           
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
  print(wlan.ifconfig())
  return True


def Hello_farm():
  global soc
  soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
  soc.bind((wlan.ifconfig()[0], 80))                   
  soc.listen(1)                                         
  while True:
    conn, addr = soc.accept()                            
    print("Connection from %s" % str(addr))
    request = conn.recv(1024)                          
    conn.sendall('HTTP/1.1 200 OK\nContent-Type: text/html\nConnection: close\n\n')
    
    with open('Hello_smart_farm.html', 'r') as html:           
        conn.sendall(html.read())         
    conn.sendall('\r\n')
    conn.close()                                       
    print("Connection from %s closed" % str(addr))

connectWifi("username", "password")
Hello_farm()
