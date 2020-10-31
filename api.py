from flask import Flask, request, render_template,jsonify
import ssl
import requests
import torch
from torchvision import models
from torchvision import transforms
from PIL import Image


app = Flask(__name__)

ssl._create_default_https_context = ssl._create_unverified_context
LABELS_URL = 'https://s3.amazonaws.com/outcome-blog/imagenet/labels.json'
labels = {int(key):value for (key, value)
      in requests.get(LABELS_URL).json().items()}

def get_prediction(image):
    alexnet = torch.load('net.pkl')

    transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225]
    )])

    img = Image.open(image)

    img_t = transform(img)
    batch_t = torch.unsqueeze(img_t, 0)

    alexnet.eval()
    out = alexnet(batch_t)
    _, index = torch.max(out, 1)

    percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

    return labels[index[0].item()], percentage[index[0].item()].item()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recognize', methods=['GET','POST'])
def my_form_post():
    image = request.files.get('file')
    label, confidence = get_prediction(image)
    result = {
        "class": label,
        "confidence": confidence
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
