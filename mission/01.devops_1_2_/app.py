from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>떼스토</h1>\n<a href='/menu'><strong>/menu</strong> 로 이동</a> "

# 새로운 메뉴 라우트 추가
@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == "__main__":
	app.run('0.0.0.0',port=5000,debug=True)
