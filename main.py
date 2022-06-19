'''
Author: G Suman Achary
Date: 18-06-2022
Project:
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run()
