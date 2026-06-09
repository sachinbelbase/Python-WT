from flask import Flask, render_template,request, jsonify, redirect
from flask_mail import Mail, Message
from form import RegistrationForm
# from dotenv import load_dotenv
import os

app = Flask(__name__)
app.secret_key = "sachinbelbase"

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = "sachinbelbase818@gmail.com"  
app.config['MAIL_PASSWORD'] = "zpjw abie aozn pqem"
app.config['MAIL_DEFAULT_SENDER'] = "sachinbelbase818@gmail.com"

mail = Mail(app)

@app.route('/')
def home():
    return "Welcome!"

@app.route('/send-email', methds = ["GET", "POST"])
def send_email():
    form = RegistrationForm()
    if form.validate_on_submit():
        to = form.to.data
        From = form.From.data
        subject = form.subject.data
        recipients = form.recipients.data
        submit = form.submit.data
        return (
            f"TO {to}!<br>"
            f"From{From}<br>"
            f"Subject{subject}<br>"
            f"Recipients{recipients}<br>" 
            f"Submit{submit}<br>" 
        )
        
    return render_template("index.html",form = form)

    
if __name__ == '__main__':
    app.run(debug=True)
    
