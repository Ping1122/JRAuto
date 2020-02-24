import React, { Component } from "react";
import TaskQueueCard from "./taskQueueCard";
import planning from "../images/planning.gif";
import performing from "../images/performing.gif";

class TaskQueue extends Component {
  renderTaskQueueCards() {
    return this.props.tasks.map((task, index) => {
      const colorCode = index * 0.1;
      const style = {
        backgroundColor: `rgba(34, 140, 202, ${colorCode})`
      };
      return (
        <div className="col-1 p-1 task-queue-col" style={style} key={task.id}>
          <TaskQueueCard
            task={task}
            index={index}
            handleRemove={this.props.handleRemove}
          />
        </div>
      );
    });
  }

  render() {
    return (
      <div className="container queue-container">
        <div className="row">
          <div className="col-1 p-1 ">
            <img
              src={planning}
              alt="planning"
              style={{ maxWidth: "100%", maxHeight: "100%" }}
            />
          </div>
          {this.renderTaskQueueCards()}
          <div className="col-1 p-1">
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
