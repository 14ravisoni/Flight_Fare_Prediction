from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello World'


if __name__ == '__main__':
    app.run()

