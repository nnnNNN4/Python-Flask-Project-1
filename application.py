from flask import Flask, url_for
from markupsafe import escape
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #ログイン状態によって処理を分けるようにする
        if request.form['username'] and request.form['password']:
            #入力したpasswordとusernameが表示されるようにする
            return render_template('in.html',
            	username=request.form['username'],
            	password=request.form['password'])
    #フォームに何も入力しなかった場合は元のページに戻る
    return render_template('login.html')