import React, { Component } from "react";
import TaskScrollContainer from "./taskScrollContainer";
import TaskQueue from "./taskQueue";
import taskService from "../services/taskService";

class Task extends Component {
  state = {
    supportedTasks: [],
    taskQueue: []
  };

  async componentDidMount() {
    let { data: taskQueue } = await taskService.getTaskQueue();
    let emptyId = Number.MAX_SAFE_INTEGER;
    while (taskQueue.length < 10) {
      taskQueue.push({ type: "empty", id: emptyId });
      emptyId -= 1;
    }
    taskQueue = taskQueue.reverse();
    const { data: supportedTasks } = await taskService.getSupportedTasks();
    this.setState({ supportedTasks, taskQueue });
  }

  render() {
    return (
      <div className="pl-5 pr-2 py-5">
        <h5 className="mb-3"> Supported Tasks </h5>
        <TaskScrollContainer tasks={this.state.supportedTasks} />
        <br />
        <h5 className="mb-3"> Current Task Queue </h5>
        <TaskQueue tasks={this.state.taskQueue} />
      </div>
    );
  }
}

export default Task;
