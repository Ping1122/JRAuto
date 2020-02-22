import React, { Component } from "react";
import TaskQueueCard from "./taskQueueCard";
import planning from "../images/planning.gif";
import performing from "../images/performing.gif";

class TaskQueue extends Component {
  render() {
    return (
      <div className="container queue-container">
        <div className="row">
          <div className="col-1 p-1 task-queue-col">
            <img
              src={planning}
              alt="planning"
              style={{ maxWidth: "100%", maxHeight: "100%" }}
            />
          </div>
          <div className="col-1 p-1 task-queue-col">
            <TaskQueueCard />
          </div>
          <div className="col-1 p-1 task-queue-col">
            <TaskQueueCard />
          </div>
          <div className="col-1 p-1 task-queue-col">
            <TaskQueueCard />
          </div>
          <div className="col-1 p-1 task-queue-col">
            <TaskQueueCard />
          </div>
          <div className="col-1 p-1 task-queue-col">
            <TaskQueueCard />
          </div>
          <div className="col-1 p-1 task-queue-col">
            <TaskQueueCard />
          </div>
          <div className="col-1 p-1 task-queue-col">
            <TaskQueueCard />
          </div>
          <div className="col-1 p-1 task-queue-col">
            <TaskQueueCard />
          </div>
          <div className="col-1 p-1 task-queue-col">
            <TaskQueueCard />
          </div>
          <div className="col-1 p-1 task-queue-col">
            <TaskQueueCard />
          </div>
          <div className="col-1 p-1 task-queue-col">
            <img
              src={performing}
              alt="performing"
              style={{ maxWidth: "100%", maxHeight: "100%" }}
            />
          </div>
        </div>
      </div>
    );
  }
}

export default TaskQueue;
