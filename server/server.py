from os import path, getcwd
from io import BytesIO
from base64 import b64encode
from flask import Flask, Response, request, jsonify, current_app, send_from_directory
from jsonschema import validate, ValidationError
from simplejson import dumps
from server.schema import taskSchema
from task.taskFactory import TaskFactory
from task.keyTaskMap import keyTaskMap
from components.monitor import Monitor

app = Flask(__name__)
taskFactory = TaskFactory()
monitor =  Monitor()
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
    task = taskFactory.makeTaskByKey(taskInfo["key"])
    taskId = taskQueue.put(task, False)
    if not taskId:
        response = Response("Task Queue is full", status=201, mimetype="application/json")
    else:
        response = Response(dumps(taskInfo), status=200, mimetype="application/json")
    return response

@app.route("/insert/<int:index>", methods = ["POST", ])
def insertTask(index):
    taskInfo = request.get_json()
    validate(taskInfo, taskSchema)
    task = taskFactory.makeTaskByKey(taskInfo["key"])
    taskId = taskQueue.insert(index, task, False)
    if not taskId:
        response = Response("Task Queue is full", status=201, mimetype="application/json")
    else:
        response = Response(dumps(taskInfo), status=200, mimetype="application/json")
    return response

@app.route("/remove/<int:id>", methods = ["POST", ])
def removeTask(id):
    global taskQueue
    taskQueue.removeById(id)
    return Response(status=200)

@app.route("/screenshot", methods = ["GET", ])
def takeScreenshot():
    screenshot = monitor.takeScreenshot()
    bytes = BytesIO()
    screenshot.save(bytes, format='PNG')
    response = Response(b64encode(bytes.getvalue()), status=200, mimetype="image/png")
    return response

@app.errorhandler(ValidationError)
def handle_invalid_usage(error):
    response = dict()
    response["message"] = error.message
    response = jsonify(response)
    response.status_code = 400
    return response
