from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test")
def testroute():
    return "test routed"


@app.route("/profile/<username>")
def varroute(username):
    return f"profile of {username}"


if __name__ == "__main__":
    app.run(debug=True)
