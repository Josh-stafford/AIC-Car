import socket, sys
from time import sleep
import imgProcessor
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = ''
PORT = 7776
data = ''
sending = True

try:
    s.bind((HOST, PORT))
except:
    PORT += 1
    print(PORT)
    s.bind((HOST, PORT))

s.listen(10)

while 1:
    conn, addr = s.accept()
    while sending:
        img = imgProcessor.frame()
        conn.send(bytes('*', 'utf-8'))
        data = (','.join(str(x) for x in img.flatten().tolist()))
        conn.send(bytes(data, 'utf-8'))
        conn.send(bytes('.', 'utf-8'))
        print('End')
        sleep(0.2)
