from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

    
    
@app.route('/old')
def old():
    return redirect(url_for('new'))

@app.route("/new")
def new():
    return "Welcome to new Page"

@app.route("/")
def home():
    return render_template("redirect.html")

if __name__ == '__main__':
    app.run(debug=True)