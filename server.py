import socket 
import sys
from _thread import *

def ClientThread(connection):
    connection.send("Welcome to the server.You can send data and get it back :| ;)\n".encode())
    while True:
        data = connection.recv(1024)
        if not data:
            break
        connection.send(data)
    connection.close()

HOST = 'localhost'
PORT = 8888

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except OSError:
    print('Failed to create socket.')
    sys.exit()
print('Socket Created')

try:
    s.bind((HOST,PORT))
except OSError:
    print('Bind failed.')
    sys.exit()
print("Socket bind completed")

s.listen(10)
print("Socket is now listening")

while True:
    connection, address = s.accept()
    print("Connection with " + address[0] + ":"+str(address[1]))
    start_new_thread(ClientThread,(connection,))    
   

s.close()