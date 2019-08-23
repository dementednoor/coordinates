from flask import Flask
import re
import socket

app = Flask(__name__)

fixed_latitude = 0.0
fixed_longitude = 0.0
fixed_height = 0
rtk_port = 11111

@app.route('/')  # opening the url http://*port_number*/ will call the data_print function:
def data_print():
    # conf = _config_data_print()
    conf = 'Config data: <br/> <br/>Latitude: {} <br/>Longitude: {} <br/>Height: {}'.\
      format(fixed_latitude, fixed_longitude, fixed_height)
    port = _port_data_print()
    return conf + '<br/>'*2 + port


#  getting data from config:
def _config_data_read():
    with open('config.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        space = re.compile('\n')  # regexp for one or more spaces to separate numbers form text file

        config_list = space.split(text)[0:3]  # 2:5 are the only numbers we need (0 - date, 1 - time)
        fixed_latitude = config_list[0]
        fixed_longitude = config_list[1]
        fixed_height = config_list[2]
        rtk_port = config_list[3]
    return true


# getting data from port:
def _port_data_print():
    host = socket.gethostname()
    port = rtk_port
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
    if (_config_data_read() != true)
      print('Error reading config')
    app.run()
