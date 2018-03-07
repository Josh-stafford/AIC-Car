import socket
from time import sleep
import pygame
import numpy
import threading

pygame.init()

resolution = 32;

size = width, height = 480, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

HOST = '127.0.0.1'#'172.20.12.187'
PORT = int(input(">> "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

def asciiDisplay(arr, width, height):
	line = ''
	for i in range(0, len(arr)):
		val = arr[i]
		if val < 63:
			line += '  '
		elif val < 127:
			line += '░░'
		elif val < 191:
			line += '▒▒'
		else:
			line += '▓▓'
		if i % width == 0:
			print(line)
			line = ''

recv_array = False
img_data = ""
count = 0

data_array = [];

def process():
	threading.Timer(1/30, process).start ()
	if data_array != []:
		arr = [ (int(x),int(x),int(x)) for x in data_array ]
		twod_array = numpy.reshape( arr, (resolution,resolution,3) )

		new_surface = pygame.surfarray.make_surface(twod_array)
		new_surface_rotate = pygame.transform.rotate(new_surface, 270)
		new_surface_scale = pygame.transform.scale(new_surface_rotate, size)
		rect = screen.blit( new_surface_scale, (0,0) )
		pygame.display.update(rect)

process()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	data = s.recv(1)
	count += 1
	data = data.decode('utf-8')
	if data == "*":
		recv_array = True
		img_data = ""
	elif data == ".":
		recv_array = False
		count = 0
		data_array = img_data.split(',')
	else:
		img_data += data
