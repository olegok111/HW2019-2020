from flask import Flask, render_template
import os
appw = Flask(__name__)


@appw.route('/<wrong_page>')
def hello_world(wrong_page):
    with open('404.html', encoding='utf8') as html_file:
        html_string = html_file.read()
        return html_string


@appw.route('/')
@appw.route('/index.html')
def greeting():
    with open('index.html', encoding='utf8') as html_file:
        html_string = html_file.read()
        return html_string


@appw.route('/time')
def time():
    with open('time.html', encoding='utf8') as html_file:
        html_string = html_file.read()
        return html_string


if __name__ == '__main__':
    appw.run()
    # appw.run(port=int(os.getenv('PORT',8123)))