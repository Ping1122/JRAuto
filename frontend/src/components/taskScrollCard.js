import React, { Component } from "react";
import NewTask from "./newTask";

class TaskScrollCard extends Component {
  render() {
    const { task } = this.props;
    let imageIndex;
    if (task.type === "Combat") {
      imageIndex = parseInt(task.stage.charAt(0)) - 1;
    } else if (task.type === "Exercise") {
      imageIndex = 8;
    } else if (task.type === "Campaign") {
      imageIndex = 9;
    }
    const images = [
      require("../images/stages/1.jpg"),
      require("../images/stages/2.jpg"),
      require("../images/stages/3.jpg"),
      require("../images/stages/4.jpg"),
      require("../images/stages/5.jpg"),
      require("../images/stages/6.jpg"),
      require("../images/stages/7.jpg"),
      require("../images/stages/8.jpg"),
      require("../images/stages/exercise.jpg"),
      require("../images/stages/campaign.jpg")
    ];
    return (
      <div className="card scroll-card my-2 mx-1 text-center">
        <a
          onClick={() => this.props.openNewTask(this.props.index)}
          className="stretched-link"
        >
          <img
            src={images[imageIndex]}
            className="card-img-top scroll-card-img round"
            alt="..."
          />
          <div className="card-img-overlay">
            <p className="card-title">{task.type}</p>
            <p className="card-text small">
              {typeof task.stage === "undefined"
                ? ""
                : `${task.stage} ${task.point}`}
            </p>
            <p className="card-text small">
              {typeof task.stage === "undefined" ? "" : task.description}
            </p>
          </div>
        </a>
        <NewTask
          show={this.props.showNewTask}
          handleClose={() => this.props.closeNewTask(this.props.index)}
          handleInsert={() => this.props.handleInsert(this.props.index)}
          handlePut={() => this.props.handlePut(this.props.index)}
        />
      </div>
    );
  }
}

export default TaskScrollCard;
