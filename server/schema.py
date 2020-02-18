from task.taskKey import TaskKey

taskSchema = {
    "type" : "object",
    "properties" : {
        "id" : {
            "type" : "number",
            "minimum" : 0,
            "maximum" : len(TaskKey)-1,
        },
        "maxRound" : {
            "type" : "number",
            "minimum" : 1,
            "maximum" : 100,
        },
        "duration" : {
            "type" : "number",
            "minimum" : 0,
            "maximum" : 7200,
        },
    },
    "required" : ["id", ]
}
schema = {
     "type" : "object",
     "properties" : {
         "price" : {"type" : "number"},
         "name" : {"type" : "string"},
     },
 }
