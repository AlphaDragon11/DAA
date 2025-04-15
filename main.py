from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    dummy_variable = 10
    if dummy_variable > 5:
        dummy_variable += 5
    else:
        dummy_variable -= 5
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)