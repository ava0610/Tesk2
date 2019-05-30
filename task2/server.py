from socket import*
from struct import*
serversock = socket(AF_INET, SOCK_DGRAM)
serversock.bind(('127.0.0.1', 12391))
while True:
    a, addr = serversock.recvfrom(1024)
    b = unpack('ii', a)
    if b[0] == 1:
        b = (b[0],) + (1,)
        print(b)
    if b[0] == 2:
        b = b*3
        print(b)
    if b[0] == 3:
        serversock.sendto(pack('ii', b[0], b[1]), addr)
        print('success')
    if b[0] == 4:
        b = b + (1,2,3)
        print(b)
    if b[0] == 5:
        b = b[1:]
        print(b)
    if b[0] == 6:
        print(b[1])
    if b[0] == 7:
        L = len(b)
        print(L)
    if b[0] == 8:
        print(type(b))
    if b[0] == 9:
        for i in b:
            print(i)
    if b[0] == 10:
        pass
    if b[0] == 11:
        break






