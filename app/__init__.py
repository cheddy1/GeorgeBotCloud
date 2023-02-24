from flask import Flask
from flask_cors import CORS

app = Flask(__name__, static_url_path='')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
from .endpoints import *


@app.route('/')
@cross_origin()
def index_client():
    return app.send_static_file('index.html')


@app.route('/api/lidar', methods=['POST'])
@cross_origin()
def lidar_receive():
    content = request.json
    with open('lidar.txt', 'w') as f:
        f.write(str(content))
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@app.route('/api/lidar', methods=['GET', 'OPTIONS'])
@cross_origin()
def lidar_display():
    with open('lidar.txt', 'r') as f:
        data = f.read()
    response = jsonify(data)
    response.content_type = 'application/json'
    return response
