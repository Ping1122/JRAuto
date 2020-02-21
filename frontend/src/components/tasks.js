import React, { Component } from "react";
import MainBackground from "./mainBackground";
import Task from "./task";

class Tasks extends Component {
  render() {
    return <MainBackground content={Task} />;
  }
}

export default Tasks;
