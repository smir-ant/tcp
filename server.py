from socket import *

HOST = '127.0.0.1'
PORT = 3000
ADDR = (HOST, PORT)
BUFSIZE = 1024

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

tcpCliSock, addr = tcpSerSock.accept()

data = tcpCliSock.recv(BUFSIZE).decode('utf-8')
# print('data =', data)
separated_data = str(data).split(' ')
# print('separated_data ', separated_data)
line = f'Спортсмен, нагрудный номер {separated_data[0]} прошёл отсечку {separated_data[1]} в ' \
       f'«{separated_data[2][0:separated_data[2].index(".")+2]}»'  # +2 = сдвиг вправо от точки
if separated_data[3].split('[')[0] == '00':  # если группа == 00
    print(line)

# в любом случае записываем в лог
with open('log.txt', mode='a') as f:  # открыли в режиме append
    f.write(f'{line}\n')

tcpSerSock.close()
tcpCliSock.close()
