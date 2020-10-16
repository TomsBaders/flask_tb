from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("Contact.html")

@app.route("/test")
def test():
    return render_template("Test.html")


app.run(host="0.0.0.0", port=80, debug=True)