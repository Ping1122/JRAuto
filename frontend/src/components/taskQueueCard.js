import React, { Component } from "react";

class TaskQueueCard extends Component {
  render() {
    const { task } = this.props;
    let imageIndex;
    let displayText = "";
    if (task.type === "Combat") {
      imageIndex = parseInt(task.stage.charAt(0)) - 1;
      displayText = displayText.concat(task.stage, task.point);
      if (task.description) {
        displayText = displayText.concat(" ", task.description);
      }
    } else if (task.type === "Exercise") {
      displayText = "Exercise";
      imageIndex = 8;
    } else if (task.type === "Campaign") {
      displayText = "Campaign";
      imageIndex = 9;
    } else if (task.type === "empty") {
      displayText = "Empty";
      imageIndex = 10;
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
      require("../images/stages/campaign.jpg"),
      require("../images/stages/empty.png")
    ];
    return (
      <div className="card queue-card p-0 ">
        <img
          src={images[imageIndex]}
          className="card-img-top queue-card-img round"
          alt="..."
        />
        <div className="card-img-overlay p-0">
          <p style={{ fontSize: "2px" }}>{displayText}</p>
        </div>
      </div>
    );
  }
}

export default TaskQueueCard;
