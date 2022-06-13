from socket import *

clientSocket=socket(AF_INET,SOCK_DGRAM)
for i in range(10):
    message="PING {}".format(i)
    clientSocket.sendto(message.encode(),(gethostbyname(gethostname()),12000))
    try:
        clientSocket.settimeout(1)
        resp=clientSocket.recv(1024)
        print(resp.decode())
        clientSocket.settimeout(None)
    except:
        print("Packet Lost")

print("Done")
i=input()
print(i)
