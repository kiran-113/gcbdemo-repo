from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h1>Kedar</h1> <br> <h2> RAJI </h2> <br> <h1> Kiran </h1> <br> <h1> This is DEMO </h1> <br> <h1> AFFINE </h1>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
