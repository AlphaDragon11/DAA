from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    name = "World"
    return render_template("index.html", name=name)

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)