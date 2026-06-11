from flask import Flask, render_template, flash, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "Sachin"
    
    
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get('username')
    
        if username:
            flash(f"welcome {username}")
            flash(f"Good morning {username}")
            return redirect(url_for('index'))
        else:
            flash("Please enter your name!")
        
    return render_template("flash_message.html")

if __name__ == '__main__':
    app.run(debug=True)