from flask import Flask
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv
from resolver import check_image
import asyncio
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
    image_file = request.files['image']
    if image_file and allowed_file(image_file.filename):
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(UPLOAD_FOLDER, filename))
        return redirect('/process_image')
    else:
        return redirect(url_for('upload_image'))


@app.route('/process_image', methods=['GET'])
async def return_prediction():
    st = await check_image()
    asyncio.sleep(1)
    return render_template('succeed.html', text=st)