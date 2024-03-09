from flask import Flask
from flask import render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv
from resolver import check_image
load_dotenv()

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# app.config['UPLOAD_FOLDER'] = upload_folder


@app.route("/")
def func(text="data_text", status='status'):
    return render_template('index.html', text=text, status=status)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_image', methods=['POST'])
def upload_image():
    # Get the uploaded file
    image_file = request.files['image']
    # Check if a file was uploaded
    if image_file and allowed_file(image_file.filename):
        # Save the file
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(UPLOAD_FOLDER, filename))

        # You can further process the image here (e.g., resize, convert format)

        # Optional: Flash a success message
        flash('Image uploaded successfully!')
        return redirect('/process_image')
    else:
        # Flash an error message
        return redirect(url_for('upload_image'))

@app.route('/process_image', methods=['GET'])
def return_prediction():
    return render_template('index.html', text=check_image())