from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h1>kedar<h1> <br> <img src=https://www.bing.com/images/search?view=detailV2&ccid=Lpl2HSeD&id=2D7DB10D80A04FE5E30AD9B7CA32BBA0CE1C0854&thid=OIP.Lpl2HSeDisjQXt0-sOnDgQHaGI&mediaurl=https%3a%2f%2fdeverra.me%2fwp-content%2fuploads%2f2019%2f11%2fcareer-main.png&exph=589&expw=711&q=img&simid=608002519834769639&FORM=IRPRST&ck=26F1F082A70CEA150465E476537E6E48&selectedIndex=141""
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
