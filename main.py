from flask import Flask
import re
import socket

app = Flask(__name__)


@app.route('/')  # opening the url http://*port_number*/ will call the data_print function:
def data_print():
    conf = _config_data_print()
    port = _port_data_print()
    return conf + '<br/>'*2 + port


#  getting data from config:
def _config_data_print():
    with open('config.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        space = re.compile('[ ]*')  # regexp for one or more spaces to separate numbers form text file
        config_list = space.split(text)[2:5]  # 2:5 are the only numbers we need (0 - date, 1 - time)
        result = 'Config data: <br/> <br/>Latitude: {} <br/>Longitude: {} <br/>Height: {}'.\
            format(config_list[0], config_list[1], config_list[2])  # gonna fix that a lil bit later
    return result


# getting data from port:
def _port_data_print():
    host = socket.gethostname()
    port = 11111
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # for ipv4 and reliable thread socket respectively
    s.connect((host, port))
    data = s.recv(1024)  # receiving up to 1024 bytes from our socket
    s.close()
    space = re.compile('[ ]*')
    port_list = space.split(repr(data))[2:5]
    print('Received message from port: {}'.format(repr(data)))  # repr is object string representation
    result = 'Port data: <br/> <br/>Latitude: {} <br/>Longitude: {} <br/>Height: {}'.\
        format(port_list[0], port_list[1], port_list[2])
    return result


if __name__ == '__main__':
    app.run()
