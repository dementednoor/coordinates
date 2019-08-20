from flask import Flask
import re

app = Flask(__name__)


@app.route('/')  # opening the url http://*port_number*/ will call the data_print function:
def data_print():
    with open('config.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        space = re.compile('[ ]*')  # regexp for one or more spaces to separate numbers form text file
        config_list = space.split(text)[2:5]  # 2:5 are the only numbers we need (0 - date, 1 - time)
        result = 'Config data: <br/> <br/>Latitude: {} <br/>Longitude: {} <br/>Height: {}'.\
            format(config_list[0], config_list[1], config_list[2])
    return result


if __name__ == '__main__':
    app.run()
