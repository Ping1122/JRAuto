from os import path, getcwd
from flask import Flask, Response, request, jsonify, current_app, send_from_directory
from jsonschema import validate, ValidationError
from simplejson import dumps
from task.taskFactory import TaskFactory
from server.schema import taskSchema

app = Flask(__name__)
taskFactory = TaskFactory()
taskQueue = None

def init(tq):
    global taskQueue
    taskQueue = tq

@app.route('/', methods = ["GET", ])
def serveIndex():
    root_dir = path.dirname(getcwd())
    folderPath = path.join(root_dir, 'JRAuto', 'frontend', 'build')
    return send_from_directory(folderPath, "index.html")

@app.route('/static/<folder>/<file>', methods = ["GET", ])
def serveStatic(folder, file):
    root_dir = path.dirname(getcwd())
    folderPath = path.join(root_dir, 'JRAuto', 'frontend', 'build', 'static', folder)
    return send_from_directory(folderPath, file)

@app.route('/put', methods = ["POST", ])
def putTask():
    taskInfo = request.get_json()
    validate(taskInfo, taskSchema)
    task = taskFactory.makeTaskByKey(taskInfo["id"])
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
