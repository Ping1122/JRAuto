from functools import wraps
from flask import request
from jsonschema import validate
from server.schema import taskSchema

def validateTask(viewFunction):
    @wraps(viewFunction)
    def decoratedFunction(*args, **kwargs):
        validate(taskSchema, request.get_json())
        return viewFunction(*args, **kwargs)
    return decoratedFunction
