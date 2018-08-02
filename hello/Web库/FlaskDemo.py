from flask import Flask, render_template, url_for, redirect, abort

# 创建一个Web应用
app = Flask(__name__, template_folder="templates")  # 更改模板路径，默认就是这个文件夹
app.config['DEBUG'] = True


# 定义路由
# @app.route("/") # 绑定到app.url_map属性上
# def hello():
#     return 'hello World 这是第一个页面'
@app.route("/index/")
def index():
    return render_template("index.html", name='Stronger')


@app.route('/user/<uid>')
def user(uid):
    return f"hellow user{uid}"


@app.route('/user/')
def user_url_for():
    print(url_for('index', id=10, name='hanxiaocu', age=16))
    return 'Test'


"""
跳转和重定向
跳转（状态码通常301） => 通常用于旧网址转移到了新网址
重定向(状态码通常302)  => 表示页面是暂时性的转移
"""


@app.route('/redirect/')
def redirect_():
    return redirect(url_for('user_url_for'))


@app.route('/score/', methods=['GET'])
def getScore():
    return redirect(url_for('login'))
    # return '100'


# 错误处理
@app.route('/login/')
def login():
    abort(401)
    return '请登录'


import time
from flask import request

users = []


@app.route('/say/', methods=['GET', 'POST'])
def say_list():
    if request.method == 'GET':
        return render_template('says.html', says=users)

    else:
        title = request.form.get('say_title')
        text = request.form.get('say')
        user = request.form.get('user')
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print()
        users.append({
            'title': title,
            'text': text,
            'user': user,
            'date': date
        })
        return redirect(url_for('say_list'))


"""
配置
"""
app.config.update(
    DEBUG=True,
)

from config import Main_Config

app.config.from_object(Main_Config)

# silent 当文件不存在时不会报错 返回false
app.config.from_pyfile('config.conf', silent=True)

"""
session
"""

from flask import session
import os

app.config.update(
    DEBUG=True,
    SECRET_KEY=os.urandom(24)
)


@app.route('/session/', methods=['GET', 'POST'])
def session_():
    if request.method == 'GET':
        return render_template('session.html', id=session.get('id'))

    session['id'] = request.form.get('id')
    return render_template('session.html', id=session.get('id'))


"""
自定义错误
"""


@app.errorhandler(404)
def error_404(error):
    return '404 Not Found', 404


"""
清理静态文件缓存
"""


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
    if filename:
        file_path = os.path.join(app.root_path, endpoint, filename)
        values['q'] = int(os.stat(file_path).st_mtime)
        return url_for(endpoint=endpoint, **values)


# 或者 直接修改Flask 配置 缓存最大时间
from datetime import timedelta
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)


if __name__ == '__main__':
    app.run('127.0.0.1', port=8050, debug=True)
