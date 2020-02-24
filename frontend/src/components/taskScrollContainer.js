import React, { Component } from "react";
import TaskScrollCard from "./taskScrollCard";

class TaskScrollContainer extends Component {
  renderTaskScrollCards() {
    return this.props.tasks.map((task, index) => {
      const showNewTask = this.props.showNewTask[index];
      return (
        <TaskScrollCard
          index={index}
          task={task}
          showNewTask={showNewTask}
          key={task.key}
          openNewTask={this.props.openNewTask}
          closeNewTask={this.props.closeNewTask}
          handlePut={this.props.handlePut}
          handleInsert={this.props.handleInsert}
        />
      );
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
