from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, lets deploy an even newer newer newer version!</p>"


app.run(host="0.0.0.0", port=8080)
