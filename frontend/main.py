from flask import Flask

app = Flask(__name__)

@app.route("/")
def upload():
    return "Coming Soon"