from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") #This assumes index.html is in your templates folder

if __name__ == "__main__":
    app.run(debug=True)