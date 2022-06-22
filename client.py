from socket import *

HOST = '127.0.0.1'
PORT = 3000
ADDR = (HOST, PORT)
BUFSIZE = 1024

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

input_record = input('Введите данные формата [BBBBxNNxHH:MM:SS.zhqxGGCR]: ')  # например 0002 C1 01:13:02.877 00[CR]
tcpCliSock.send(input_record.encode())
