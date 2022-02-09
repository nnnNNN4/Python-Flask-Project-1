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

from werkzeug.utils import secure_filename

@app.route('/uploads', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files["the_file"]
        #任意の階層をフルパスで指定
        f.save('/Users/<任意のユーザー名>/python/myproject/uploads/' + secure_filename(f.filename))
        #サーバーにファイルが保存されたらfinished.htmlと表示
        return render_template('finished.html')
    else:
    	#GETでアクセスされた時、uploadsを表示
    	return render_template('uploads.html')