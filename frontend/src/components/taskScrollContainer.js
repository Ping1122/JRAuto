import React, { Component } from "react";
import TaskScrollCard from "./taskScrollCard";

class TaskScrollContainer extends Component {
  render() {
    return (
      <section class="scroll-container px-1">
        <TaskScrollCard />
        <TaskScrollCard />
        <TaskScrollCard />
        <TaskScrollCard />
        <TaskScrollCard />
        <TaskScrollCard />
        <TaskScrollCard />
        <TaskScrollCard />
        <TaskScrollCard />
        <TaskScrollCard />
        <TaskScrollCard />
      </section>
    );
  }
}

export default TaskScrollContainer;
