from flask import Flask, Response, request, jsonify
from jsonschema import ValidationError
from simplejson import dumps
from task.taskFactory import TaskFactory
from server.decorator import validateTask

app = Flask(__name__)
taskFactory = TaskFactory()
taskQueue = None

def init(taskQueue):
    global taskQueue = taskQueue

@app.route('/')
def index():
    return "Under development"

@app.route('/put')
@validateTask
def putTask():
    taskInfo = request.get_json()
    task = taskFactory.makeTaskByKey(taskInfo["taskId"])
    taskId = taskQueue.put(task, False)
    if not taskId:
        response = Response("Task Queue is full", status=201, mimetype='application/json')
    response = Response(dumps(taskInfo), status=200, mimetype='application/json')
    return response

@app.errorhandler(ValidationError)
def handle_invalid_usage(error):
    response = dict()
    response['message'] = error.message
    response = jsonify(response)
    response.status_code = 400
    return response
