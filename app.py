from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello, World! This is kiran kiran </h3>"
    html = '<h1>Hello This is Continues Build Demo</h1>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
