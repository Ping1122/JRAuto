import React, { Component } from "react";
import TaskScrollCard from "./taskScrollCard";
import taskService from "../services/taskService";

class TaskScrollContainer extends Component {
  state = {
    tasks: []
  };

  async componentDidMount() {
    console.log("hello");
    const { data: tasks } = await taskService.getSupportedTasks();
    this.setState({ tasks });
  }

  renderTaskScrollCards() {
    return this.state.tasks.map(task => {
      return <TaskScrollCard task={task} key={task.key} />;
    });
  }

  render() {
    return (
      <section className="scroll-container px-1">
        {this.renderTaskScrollCards()}
      </section>
    );
  }
}

export default TaskScrollContainer;
