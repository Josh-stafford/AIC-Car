import socket, sys
from time import sleep
import imgProcessor
import numpy as np
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

HOST = ''
PORT = 7776
framerate = 60


try:
    s.bind((HOST, PORT))
except:
    PORT += 1
    print(PORT)
    s.bind((HOST, PORT))

s.listen(10)
conn, addr = s.accept()


data = ''
sending = True

def send_data():
    threading.Timer(1/framerate, send_data).start ()
    if data != '':
        conn.send(bytes('*'+data+'.', 'utf-8'))

send_data()

while 1:
    img = imgProcessor.frame()
    data = (','.join(str(x) for x in img.flatten().tolist()))
    print('End')
