import socket
import sys
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except OSError as msg:
    print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
    sys.exit()


print('Socket Created')
print("send empty message to exit!")
host = "localhost"
port = 8888

s.connect((host,port))

try:
    
    message = input("Enter Your message: ")
    while True:
        s.sendall(message.encode())
        reply = s.recv(4096)
        print(reply.decode('utf-8'))
        message = input("Enter Your message: ")
        if not message: 
            sys.exit()
except socket.error:
    print("Send Failed")
    sys.exit()
print("Message Sent successfully")

s.close()