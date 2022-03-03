import os
from flask import Flask, request, render_template
from io import BytesIO
from PIL import Image

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def carousel():
    if request.method == 'POST':
        f = request.files['file']
        image = Image.open(BytesIO(f.read()))
        image.save(f'static/img/{f.filename}')
    name_foto = os.listdir('static/img')
    return render_template('base.html', name_foto=name_foto)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
