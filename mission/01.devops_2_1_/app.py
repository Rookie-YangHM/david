from flask import Flask, render_template
import socket

app = Flask(__name__)

@app.route('/')
def home():
    if app.debug:
        hostname = '컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname = ' '
    return render_template('index.html', computername=hostname)

"""
# 새로운 메뉴 라우트 추가
@app.route('/menu')
def menu():
    return render_template('menu.html')
"""

@app.route("/test1")
def test1():
    return render_template('test1.html')

if __name__ == "__main__":
	app.run('0.0.0.0',port=5000,debug=True)
