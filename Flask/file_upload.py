from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
     file = request.files["file"]
     if file.filename != '':
         filename = secure_filename(file.filename)
         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
         return "File Uploaded Sucessfully!"
        
    return render_template("file_upload.html")


@app.route("/")
def home():
    return "Home Page"


if __name__ == '__main__':
    app.run(debug=True)