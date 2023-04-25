import json
import os

import flask
import requests
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
    if len(content) < 750:
        msg = format_sse(data=content)
        announcer.announce(msg=msg)
    return {}, 200


@app.route('/api/data-feed-receive', methods=['GET'])
def listen():
    def stream():
        messages = announcer.listen()  # returns a queue.Queue
        while True:
            msg = messages.get()  # blocks until a new message arrives
            yield msg
    return flask.Response(stream(), mimetype='text/event-stream')


@app.route('/test', methods=['GET'])
def test():
    controller_json = r'{"controller-log": {"left_stick_coords:": [0.032227545976638794, 0.018768884241580963], ' \
                      r'"left_stick_down": false, "right_stick_coords": [0.027527695521712303, 0.0], ' \
                      r'"right_stick_down": false, "axis_left_trigger": 0.016418958082795143, "axis_right_trigger": ' \
                      r'0.0, "left_bumper": false, "right_bumper": false, "button_a": false, "button_b": false, ' \
                      r'"button_x": false, "button_y": false, "start": false, "select": false, "menu": false}} '
    headers = {"Content-Type": 'application/json'}

    # Once it's fully JSON'd
    requests.post("http://george-env.eba-trrm37cn.us-east-2.elasticbeanstalk.com/api/data-feed", headers=headers, data=json.dumps(controller_json))
    return {}, 200

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


@app.route('/api/2d-image', methods=['GET'])
def get_img_two():
    return send_file(os.path.join(app.root_path, '2d.png'))

