import React, { Component } from "react";

class MainBackground extends Component {
  render() {
    return (
      <div className="main-background w-100 p-4 text-left">
        <this.props.content />
      </div>
    );
  }
}

export default MainBackground;
