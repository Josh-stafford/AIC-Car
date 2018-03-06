import socket, sys
from time import sleep
import imgProcessor
import numpy as np
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = ''
PORT = 7776


try:
    s.bind((HOST, PORT))
except:
    PORT += 1
    print(PORT)
    s.bind((HOST, PORT))

s.listen(10)

class send(threading.Thread):

    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        data = ''
        sending = True

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

sendThread = send(1, 'sendThread')
sendThread.start()
