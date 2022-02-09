# from flask import Flask, url_for, g
# from markupsafe import escape
# from flask import request
# from flask import render_template
# from flask import request, after_this_request
# from flask import make_response
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         #ログイン状態によって処理を分けるようにする
#         if request.form['username'] and request.form['password']:
#             #入力したpasswordとusernameが表示されるようにする
#             return render_template('in.html',
#             	username=request.form['username'],
#             	password=request.form['password'])
#     #フォームに何も入力しなかった場合は元のページに戻る
#     return render_template('login.html')

# from werkzeug.utils import secure_filename

# @app.route('/uploads', methods=['POST', 'GET'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files["the_file"]
#         #任意の階層をフルパスで指定
#         f.save('/Users/<任意のユーザー名>/python/myproject/uploads/' + secure_filename(f.filename))
#         #サーバーにファイルが保存されたらfinished.htmlと表示
#         return render_template('finished.html')
#     else:
#     	#GETでアクセスされた時、uploadsを表示
#     	return render_template('uploads.html')

# #cookieを保存する
# @app.route('/')
# def index():
#     resp = make_response(render_template(...))
#     resp.set_cookie('username', 'the username')
#     return resp

# @app.route('/')
# def index():
#     username = request.cookies.get('username')

# #before_requestを指定するとリクエストの前処理
# @app.before_request
# def detect_user_language():
#     #「language」変数をcookieから取得する
#     language = request.cookies.get('user_lang')
    
#     #cookieに「language」変数がない場合
#     if language is None:
#         #「language」を取得
#         language = guess_language_from_request()

#         # when the response exists, set a cookie with the language
#         @after_this_request
#         def remember_language(response):
#             response.set_cookie('user_lang', language)
#             return response

#     #gに「language」変数を代入(この処理は必ず実行される)
#     g.language = language

# #before_requestを指定するとリクエストの前処理
# @app.before_request
# def detect_user_name():
#     #「u_name」変数をcookieから取得する
#     print("before_request")
#     u_name = request.cookies.get('username')
#     print(u_name)
#     #cookieに「u_name」変数がない場合
#     if u_name is None:
#         print("uname is none")
#         u_name = "panda"
#         @after_this_request
#         def remember_uname(response):
#             print("after_this_request")
#             response.set_cookie('username', u_name)
#             return response

#     g.u_name = u_name

# #indexページ
# @app.route('/')
# def index():
#     print("Index")
#     return "Index"

# #テスト用にアクセスするためのURL
# @app.route('/test/')
# def test():
#     print("test")
#     return "TEST"

from flask import Flask, url_for, g
from markupsafe import escape
from flask import request
from flask import render_template
from flask import request, after_this_request
from flask import make_response
app = Flask(__name__)

#before_requestを指定するとリクエストの前処理
@app.before_request
def detect_user_name():
    #「u_name」変数をcookieから取得する
    print("before_request")
    u_name = request.cookies.get('testuser')
    print(u_name)
    #cookieに「u_name」変数がない場合
    if u_name is None:
        print("uname is none")
        u_name = "testuser"
        @after_this_request
        def remember_uname(response):
            print("after_this_request")
            response.set_cookie('testuser', u_name)
            return response

    g.u_name = u_name

#indexページ
@app.route('/')
def index():
    resp = make_response(render_template("index.html", testuser=request.cookies.get('testuser')))
    return resp

#テスト用にアクセスするためのURL
@app.route('/test/')
def test():
    print("test")
    return "TEST"