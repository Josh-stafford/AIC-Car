import socket, pickle
from time import sleep

HOST = '172.20.12.187'
PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

def asciiDisplay(arr, width, height):
    line = ''
    for i in range(0, len(arr)):
        val = arr[i]
        if val < 85:
            line += '.'
        elif val < 170:
            line += '\\'
        else:
            line += '%'
        if i % width == 0:
            print(line)
            line = ''


while 1:
    data = s.recv(58000)
    img = pickle.loads(data)
    asciiDisplay(img, 32, 32)
