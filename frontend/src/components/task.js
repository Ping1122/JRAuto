import React, { Component } from "react";
import TaskScrollContainer from "./taskScrollContainer";
import TaskQueue from "./taskQueue";
import taskService from "../services/taskService";
import { toast } from "react-toastify";

class Task extends Component {
  constructor() {
    super();
    this.state = {
      supportedTasks: [],
      showNewTask: [],
      taskQueue: []
    };
    this.updateTaskQueue = this.updateTaskQueue.bind(this);
    this.openNewTask = this.openNewTask.bind(this);
    this.closeNewTask = this.closeNewTask.bind(this);
    this.handlePut = this.handlePut.bind(this);
    this.handleInsert = this.handleInsert.bind(this);
    this.handleRemove = this.handleRemove.bind(this);
  }

  openNewTask(index) {
    const showNewTask = { ...this.state.showNewTask };
    showNewTask[index] = true;
    this.setState({ showNewTask });
  }

  closeNewTask(index) {
    const showNewTask = { ...this.state.showNewTask };
    showNewTask[index] = false;
    this.setState({ showNewTask });
  }

  async handlePut(index) {
    const response = await taskService.putTask({
      key: this.state.supportedTasks[index].key
    });
    if (response && response.status === 201) {
      toast.info("Unable to assig. Task Queue is Full");
    }
    this.closeNewTask(index);
    this.updateTaskQueue();
  }

  async handleInsert(index) {
    const response = await taskService.insertTask(0, {
      key: this.state.supportedTasks[index].key
    });
    if (response && response.status === 201) {
      toast.info("Unable to assign. Task Queue is Full");
    }
    this.closeNewTask(index);
    this.updateTaskQueue();
  }

  async handleRemove(index) {
    const task = this.state.taskQueue[index];
    await taskService.removeTask(task);
    this.updateTaskQueue();
  }

  async componentDidMount() {
    let { data: taskQueue } = await taskService.getTaskQueue();
    let emptyId = Number.MAX_SAFE_INTEGER;
    while (taskQueue.length < 10) {
      taskQueue.push({ type: "empty", id: emptyId });
      emptyId -= 1;
    }
    taskQueue = taskQueue.reverse();
    const { data: supportedTasks } = await taskService.getSupportedTasks();
    const showNewTask = Array(supportedTasks.length).fill(false);
    this.setState({ supportedTasks, showNewTask, taskQueue });
    setInterval(this.updateTaskQueue, 20000);
  }

  async updateTaskQueue() {
    let { data: taskQueue } = await taskService.getTaskQueue();
    let emptyId = Number.MAX_SAFE_INTEGER;
    while (taskQueue.length < 10) {
      taskQueue.push({ type: "empty", id: emptyId });
      emptyId -= 1;
    }
    taskQueue = taskQueue.reverse();
    this.setState({ taskQueue });
  }

  render() {
    return (
      <div className="pl-5 pr-2 py-5">
        <h5 className="mb-2"> Supported Tasks </h5>
        <TaskScrollContainer
          tasks={this.state.supportedTasks}
          showNewTask={this.state.showNewTask}
          openNewTask={this.openNewTask}
          closeNewTask={this.closeNewTask}
          handlePut={this.handlePut}
          handleInsert={this.handleInsert}
        />
        <br />
        <h5 className="mb-2"> Current Task Queue </h5>
        <TaskQueue
          tasks={this.state.taskQueue}
          handleRemove={this.handleRemove}
        />
      </div>
    );
  }
}

export default Task;
