from flask import Flask, make_response, request, render_template

app = Flask(__name__)

### Setting a Cookie ###
@app.route("/setcookie")
def set_cookies():
    resp = make_response("Cookies has been sent!")
    resp.set_cookie("username","Sachin", max_age=3600)
    return resp

### Reading a Cookie ###
@app.route("/getcookie")
def get_cookie():
    username = request.cookies.get('username')
    return f"Hello {username}"

### Delete a Cookie ###
@app.route("/delcookie")
def delete_cookie():
   resp = make_response("Cookies has been deleted!")
   resp.set_cookie("username", "", expires=0)
   return resp

### Delete a Cookie in Alternative Way ###
@app.route("/delcookie1")
def delete_cookie1():
    resp = make_response("Cookies has been deleted!")
    resp.delete_cookie("username")
    return resp

### Home Page ###
@app.route("/")
def home():
    return render_template("cookies.html")

if __name__ == "__main__":
    app.run(debug=True)
    