import socket
import sys
import os
import time
import bluetooth
import thread


port = 1
SIZE = 2048 # was 1024


def get_ESP32_addr():
	nearby_devices = bluetooth.discover_devices()
	print("Searching for ESP32 device!")
	for address in nearby_devices:
		if 'ESP32test' == bluetooth.lookup_name(address):
			return address
	return None


def send_data(s, to_send_data = ''):
	# send data
	to_send = str(to_send_data)
	s.send(to_send.encode())


def receive_data(s):
	# receive data
	data = s.recv(SIZE).decode("utf-8") # Assuming the data is formatted in UTF-8
	if data:
		print(data)

def socket_setup(): 
	s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
	return s
	
def main(to_send_data):
	try:
		addr = get_ESP32_addr()
		if not addr:
			raise Exception()
		socket_setup().connect((addr, port))
		print("We are now connected to ESP32")
		
		while True:
			thread.start_new_thread(receive_data, (socket_setup()))
			thread.start_new_thread(send_data, (socket_setup(), to_send_data))
	except:
		print('ERROR:', sys.exc_info(), '\n')
		s.close()
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)

