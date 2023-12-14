from flask import Flask  # Flaskをインポート(導入)
from markupsafe import escape  # escapeをインポート
from flask import url_for  # url_forをインポート
from flask import request  # requestをインポート
from flask import render_template  # render_templateをインポート

app = Flask(__name__)  # クラス(設計図)をインスタンス(実体)化


@app.route("/")  # どのURLを引数にするか
def index():  # 関数名
    return "Index Page"  # 返す値


# @app.route("/<name>")  # /xxxにアクセス
# def hello(name):  # hello関数
#     return f"Hello, {escape(name)}!"  # 関数の値をエスケープ処理して返す(インジェクション対策)


@app.route("/user/<username>")  # /user/<username>にアクセス
def show_user_profile(username):  # show_user_profile関数(username)
    return f"User {escape(username)}"  # 返り値


@app.route("/post/<int:post_id>")  # /post/<post_id>にアクセス。int型のみ対応する(それ以外エラーで返す)
def show_post(post_id):  # show_post関数
    return f"Post {post_id}"  # 返り値


@app.route("/login", methods=["GET", "POST"])  # 異なるHTTPメソッドを処理するためにmethods引数を使用する
def login():
    if request.method == "POST":
        return "POST"  # 返す値
    else:
        return "GET"  # 返す値


# url_for一旦スルー。わからん。
# with app.test_request_context():
#     print(url_for("index"))
#     print(url_for("login"))
#     print(url_for("login", next="/"))
#     print(url_for("profile", username="John Doe"))

# url_for("static", filename="style.css")  # 静的ファイル(JS.CSS)の使用


@app.route("/hello/")
@app.route("/hello/<name>")  # 変数を設定
def hello(name=None):  # hello関数
    return render_template("hello.html", name=name)  # 変数nameをhello.htmlに渡す
