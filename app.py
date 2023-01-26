""" Written by: Masha + Yehyun"""
import base64

from controller.PictureController import getPicturePath, insertPictureClass
from controller.classificationController import get_prediction, allowed_file
from flask import flash, redirect, url_for, render_template, session
from werkzeug.utils import secure_filename
import os
import io
from PIL import Image
from flask import Flask, jsonify, request


UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

pathh = None#getPicturePath()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

#session['pathh']=getPicturePath()
@app.route('/welcome')
def welcome():
    session['pathh']=getPicturePath()
    return render_template('welcome.html')


@app.route('/image')
def image():
    pathh = session.get('pathh', None)
    path = pathh[1]
    print(path)
    img = Image.open(path)
    # create file-object in memory
    file_object = io.BytesIO()
    # write PNG in file-object
    img.save(file_object, 'JPEG')
    encoded_img_data = base64.b64encode(file_object.getvalue())
    return render_template("index.html", img_data=encoded_img_data.decode('utf-8'))

@app.route('/image', methods=["POST"])
def classific():
    pathh = session.get('pathh', None)
    text = request.form['text']
    processed_text = text.upper()
    print(processed_text)
    insertPictureClass(pathh[0], processed_text)
    return redirect(url_for('welcome')) #(request.url)
    #return processed_text

""" Renders template"""
@app.route('/')
def upload_form():
	return render_template('upload.html')

""" Classifies image"""
@app.route('/', methods=['GET','POST'])
def predict():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully uploaded and displayed below')

        with open('static/uploads/' + filename, 'rb') as f:
            img_bytes = f.read()
            print(img_bytes)
            n = get_prediction(image_bytes=img_bytes)
            return jsonify({'class_id': n })
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)


app.run()