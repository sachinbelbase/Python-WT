from flask import Flask, render_template,request
from form import NameForm

app = Flask(__name__)
app.secret_key = "sachinbelbase"

@app.route("/", methods=['GET', 'POST'])
def home():
    form = NameForm()
    if form.validate_on_submit():
        return f"Hello {form.name.data}"
        
    return render_template("index.html",form = form)



# @app.route("/", methods=['GET', 'POST'])
# def home():
#     error = None
#     if request.method== 'POST':
#           name = request.form['name'].strip()
          
#           if not name:
#               error = "Name cannot be empty"
            
#           else:  
#             return f"Hello, {name}"
        
#     return render_template("index.html",error=error)
  
  
# @app.route('/about-me')
# def about():
#     return "Hello its me Sachin Belbase"


# @app.route("/greet")
# def greet():
#         name = request.args.get('name', "Guest")
#         return f"Hello, {name}"
    
    
if __name__ == '__main__':
    app.run(debug=True)