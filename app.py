import base64
from controller.PictureController import getPicturePath, insertPictureClass
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os
import io
import json

import timm
import torch
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request


UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

pathh = getPicturePath()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/image')
def image():
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
    text = request.form['text']
    processed_text = text.upper()
    print(processed_text)
    insertPictureClass(pathh[0], processed_text)
    return processed_text


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = timm.create_model('resnet18', pretrained=False, num_classes=3)
model = model.to(device)
model.eval()
model.load_state_dict(torch.load("best.pth", map_location=torch.device('cpu')))

def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    if predicted_idx == '0': return 'dog'
    elif predicted_idx == '1': return 'squirrel'
    elif predicted_idx == '2': return 'cat'
    else: return 'neither'

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def upload_form():
	return render_template('upload.html')

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
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')

        with open('static/uploads/' + filename, 'rb') as f:
            img_bytes = f.read()
            print(img_bytes)
            n = get_prediction(image_bytes=img_bytes)
            return jsonify({'class_id': n }) #class_id, 'class_name': class_name})

        # return render_template('upload.html', filename=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/test')
def test():
    return 'Hello World! I am from docker!'


app.run()