import timm
import torch
import torchvision.transforms as transforms
from PIL import Image
import io
UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

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