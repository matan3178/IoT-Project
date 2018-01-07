
import socket
import sys
import traceback
import netifaces

def log(log_info):         
	
	gws = netifaces.gateways()
	ip_add = gws['default'][netifaces.AF_INET][0]
	port = 2525
	client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	client_sock.sendto(log_info, (ip_add, port))

