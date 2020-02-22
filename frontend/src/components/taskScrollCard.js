import React, { Component } from "react";

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
        <img
          src={images[imageIndex]}
          className="card-img-top scroll-card-img round"
          alt="..."
        />
        <div className="card-img-overlay">
          <h5 className="card-title">{task.type}</h5>
          <p className="card-text">
            {typeof task.stage === "undefined"
              ? ""
              : `${task.stage} ${task.point}`}
          </p>
          <p className="card-text">
            {typeof task.stage === "undefined" ? "" : task.description}
          </p>
        </div>
      </div>
    );
  }
}

export default TaskScrollCard;
