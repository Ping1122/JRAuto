import React, { Component } from "react";
import { Link, NavLink } from "react-router-dom";

class Header extends Component {
  getActiveClass(pathname) {
    return this.props.location.pathname === pathname
      ? "nav-link active"
      : "nav-link";
  }

  render() {
    const tasksActive = this.getActiveClass("/tasks");
    const logsActive = this.getActiveClass("/logs");
    const statisticActive = this.getActiveClass("/statistics");
    return (
      <header className="masthead mb-auto">
        <div className="inner">
          <Link to="/">
            <h3 className="masthead-brand">JRAuto</h3>
          </Link>
          <nav className="nav nav-masthead justify-content-center">
            <NavLink className={tasksActive} to="/tasks">
              Tasks
            </NavLink>
            <NavLink className={logsActive} to="/logs">
              Logs
            </NavLink>
            <NavLink className={statisticActive} to="/statistics">
              Statistics
            </NavLink>
          </nav>
        </div>
      </header>
    );
  }
}

export default Header;
