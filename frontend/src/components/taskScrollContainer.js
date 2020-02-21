import React, { Component } from "react";
import TaskScrollCard from "./taskScrollCard";

class TaskScrollContainer extends Component {
  state = {
    tasks: []
  };

  async componentDidMount() {
    const { tasks } = await getGenres();
    const genres = [{ _id: "", name: "All Genres" }, ...data];

    const { data: movies } = await getMovies();
    this.setState({ movies, genres });
  }

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
