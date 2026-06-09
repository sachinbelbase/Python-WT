from flask import Flask, make_response, request, render_template

app = Flask(__name__)


# Defination of Cookie
# -> A cookie is a small piece of data stored in the user's browser. Flask lets you set, read, and delete cookies easily.

### Setting a Cookie ###
@app.route("/setcookie")
def set_cookies():
    resp = make_response("Cookies has been sent!")
    ###  username is the name and Sachin is the value also max_age= 3600 means cookies expire in 3600 seconds ###
    resp.set_cookie("username","Sachin", max_age=3600)
    return resp

### Reading a Cookie ###
@app.route("/getcookie")
def get_cookie():
    # Browser automatically sends all stored cookies in the request headers
    #        ↓
    # request.cookies.get('username') → looks up the cookie by name → "Sachin"
    #        ↓
    # Returns "Hello Sachin"
    
    username = request.cookies.get('username')
    return f"Hello {username}"

### Delete a Cookie ###
@app.route("/delcookie")
def delete_cookie():
   resp = make_response("Cookies has been deleted!")
    # Flask sets the cookie "username" to empty string ""
    # AND sets expires=0 (meaning: expired immediately in the past)
   resp.set_cookie("username", "", expires=0)
   return resp


### Delete a Cookie in Alternative Way ###
@app.route("/delcookie1")
def delete_cookie1():
    resp = make_response("Cookies has been deleted!")
    # Flow: Same as above, but Flask's built-in delete_cookie() does the expiry trick for you internally.
    # Both methods achieve the exact same result — this is just cleaner.
    resp.delete_cookie("username")
    return resp

### Home Page ###
@app.route("/")
def home():
    return render_template("cookies.html")

if __name__ == "__main__":
    app.run(debug=True)
    