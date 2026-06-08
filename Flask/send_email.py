from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587 
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "sachinbelbase818@gmail.com"  
app.config['MAIL_PASSWORD'] = "zpjw abie aozn pqem"
app.config['MAIL_DEFAULT_SENDER'] = "sachinbelbase818@gmail.com"

mail = Mail(app)

@app.route('/')
def home():
    return "Welcome!"

@app.route('/send')
def send_email():
    msg = Message(
        subject="Hello from Sachin using Flask",
        recipients=["roshankoirala660@gmail.com","secretgamer794@gmail.com"],
        body = "This is the test email sent using flask-mail and gmail SMTP!"
    )
    
    mail.send(msg)
    return "Email has sucessfully send"
    
        
if __name__ == '__main__':
    app.run(debug=True)