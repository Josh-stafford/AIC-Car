import socket
from time import sleep

HOST = '172.20.12.187'
PORT = int(input(">> "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))


def asciiDisplay(arr, width, height):
    line = ''
    for i in range(0, len(arr)):
        val = arr[i]
        if val < 85:
            line += '. '
        elif val < 170:
            line += '\\ '
        else:
            line += '% '
        if i % width == 0:
            print(line)
            line = ''


recv_array = False
img_data = ""
count = 0

while True:
    data = s.recv(1)
    count += 1
    data = data.decode('utf-8')
    if data == "*":
        print("Start array")
        recv_array = True
        img_data = ""
    elif data == ".":
        print("End array")
        recv_array = False
        print(img_data)
        print(count)
        print(len(img_data))
        #  asciiDisplay(img_data, 32, 32)
    else:
        print(data)
        img_data += data
        print(img_data)
