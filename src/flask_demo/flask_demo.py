from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#  flask --app src/flask_demo/flask_demo.py  run
