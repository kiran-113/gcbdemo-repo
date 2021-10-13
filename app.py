from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h1>This is Head </h> <br> <h3>Hello, World! This is new change, did through git hub </h3>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
