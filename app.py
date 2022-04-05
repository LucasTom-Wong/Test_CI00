from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Aw 0oo-0"

if __name__ = "__main__":
    app.debug = True
    app.run()
