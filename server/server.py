from os import path, getcwd
from flask import Flask, Response, request, jsonify, current_app, send_from_directory
from jsonschema import validate, ValidationError
from simplejson import dumps
from server.schema import taskSchema
from task.taskFactory import TaskFactory
from task.keyTaskMap import keyTaskMap

app = Flask(__name__)
taskFactory = TaskFactory()
taskQueue = None

def init(tq):
    global taskQueue
    taskQueue = tq

@app.route("/", methods = ["GET", ])
def serveIndex():
    root_dir = path.dirname(getcwd())
    folderPath = path.join(root_dir, "JRAuto", "frontend", "build")
    return send_from_directory(folderPath, "index.html")

@app.route("/static/<folder>/<file>", methods = ["GET", ])
def serveStatic(folder, file):
    root_dir = path.dirname(getcwd())
    folderPath = path.join(root_dir, "JRAuto", "frontend", "build", "static", folder)
    return send_from_directory(folderPath, file)

@app.route("/supportedtasks", methods = ["GET", ])
def serveSupportedTasks():
    tasks = []
    for task in keyTaskMap.values():
        tasks.append(taskToJson(task()))
    response = Response(dumps(tasks), status=200, mimetype="application/json")
    return response

@app.route("/taskqueue", methods =["GET", ])
def serveTaskQueue():
    global taskQueue
    tasks = []
    taskList = taskQueue.toList()
    for task in taskList:
        tasks.append(taskToJson(task))
    response = Response(dumps(tasks), status=200, mimetype="application/json")
    return response

def taskToJson(task):
    name = task.name.split()
    temp = {"key" : task.key, "type" : name[0]}
    if task.id:
        temp["id"] = task.id
    if len(name) > 1:
        temp["stage"] = name[1]
    if len(name) > 2:
        temp["point"] = name[2]
    if len(name) > 3:
        temp["description"] = name[3]
    return temp


@app.route("/put", methods = ["POST", ])
def putTask():
    taskInfo = request.get_json()
    validate(taskInfo, taskSchema)
    task = taskFactory.makeTaskByKey(taskInfo["id"])
    taskId = taskQueue.put(task, False)
    if not taskId:
        response = Response("Task Queue is full", status=201, mimetype="application/json")
    response = Response(dumps(taskInfo), status=200, mimetype="application/json")
    return response

@app.errorhandler(ValidationError)
def handle_invalid_usage(error):
    response = dict()
    response["message"] = error.message
    response = jsonify(response)
    response.status_code = 400
    return response
