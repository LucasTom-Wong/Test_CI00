from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/soo")
def new_world():
    return render_template("new.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
