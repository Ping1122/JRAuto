import React, { Component } from "react";

class Header extends Component {
  render() {
    return (
      <header className="masthead mb-auto">
        <div className="inner">
          <h3 className="masthead-brand">JRAuto</h3>
          <nav className="nav nav-masthead justify-content-center">
            <a className="nav-link active" href="#">
              Tasks
            </a>
            <a className="nav-link" href="#">
              Logs
            </a>
            <a className="nav-link" href="#">
              Statistics
            </a>
          </nav>
        </div>
      </header>
    );
  }
}

export default Header;
