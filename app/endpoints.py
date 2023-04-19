import json
import os

import flask
from flask import request, jsonify, send_file
from flask_cors import cross_origin
from . import app
from .sse_helper import announcer, format_sse
from .database import execute_sql, temp_store


@app.route('/')
@cross_origin()
def index_client():
    return app.send_static_file('index.html')


@app.route('/api/lidar', methods=['POST'])
@cross_origin()
def lidar_receive() -> json:
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


@app.route('/api/data-feed', methods=['POST'])
@cross_origin()
def data_receive():
    content = request.json
    if "controller-log" in content or "ros-log" in content:
        content = str(content).replace("\'", "\"")
        if len(content) < 750:
            msg = format_sse(data=content)
            announcer.announce(msg=msg)
    return {}, 200


@app.route('/api/data-feed', methods=['GET'])
def listen():
    def stream():
        messages = announcer.listen()  # returns a queue.Queue
        while True:
            msg = messages.get()  # blocks until a new message arrives
            yield msg
    return flask.Response(stream(), mimetype='text/event-stream')


@app.route('/api/top', methods=['GET'])
def ten_most_recent():
    temp_store()
    res = execute_sql("SELECT stamp FROM frames ORDER BY stamp DESC LIMIT 10", 'select').fetchall()
    return str(res)


@app.route('/api/2d-image', methods=['POST'])
def post_img_two():
    if request.files:
        image = request.files['']
        image.save(os.path.join(app.root_path, '2d.png'))
    return {}, 200

