import socket, pickle
from time import sleep
import imgProcessor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = ''
PORT = 6666
test_data = [0,1,2,3,4]
sending = True

s.bind((HOST, PORT))

s.listen(10)

while 1:
    conn, addr = s.accept()
    while sending:
        img = pickle.dumps(imgProcessor.frame())
        conn.send(img)
        input('>> ')
