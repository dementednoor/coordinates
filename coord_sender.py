import socket
from datetime import datetime

host = ''  # for all available interfaces
port = 11111
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 and reliable thread socket relatively
s.bind((host, port))
print(host, port)
s.listen(1)  # parameter is the number of unaccepted connections which system will allow
conn, addr = s.accept()
print('Connected by {}'.format(addr))
while True:
    try:
        data = '{} 55.146483884   37.938707328   196.8384   ' \
               '2  15   0.1168   0.1080   0.2248   0.0291  -0.0273   0.0517   1.00    1.5'.format(datetime.now())
        if not data: break
        conn.sendall(str.encode(data))
    except socket.error:
        print('Error occurred. Please, try again')
        break
conn.close()
