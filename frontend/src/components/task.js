import React, { Component } from "react";
import TaskScrollContainer from "./taskScrollContainer";
import TaskQueue from "./taskQueue";

class Task extends Component {
  render() {
    return (
      <div className="pl-5 pr-2 py-5">
        <h5 className="mb-3"> Supported Tasks </h5>
        <TaskScrollContainer />
        <br />
        <h5 className="mb-3"> Current Task Queue </h5>
        <TaskQueue />
      </div>
    );
  }
}

export default Task;
