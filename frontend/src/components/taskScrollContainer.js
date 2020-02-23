import React, { Component } from "react";
import TaskScrollCard from "./taskScrollCard";

class TaskScrollContainer extends Component {
  renderTaskScrollCards() {
    return this.props.tasks.map(task => {
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
