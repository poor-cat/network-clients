import socket 

target_port = "www.google.com"
target_port = 80

# create a socket object 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
