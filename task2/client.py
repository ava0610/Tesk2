from socket import*
from struct import*
clientsock = socket(AF_INET, SOCK_DGRAM)
clientsock.bind(('127.0.0.1', 12389))
N = 1
M = 3
while N < 12:
    number = pack('ii', N, M)
    clientsock.sendto(number, ('127.0.0.1', 12391))
    N = N + 1
    M = N*3


 



