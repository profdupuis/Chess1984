from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Chessforce 1984!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
