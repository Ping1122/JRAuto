import React, { Component } from "react";
import boarder from "../images/boarder.png";

class MainBackground extends Component {
  render() {
    return (
      <div
        className="main-background w-100 h-75 p-4 text-left"
        style={{
          backgroundImage: `url(${boarder})`
        }}
      >
        <this.props.content />
      </div>
    );
  }
}

export default MainBackground;
