import React, { Component } from "react";
import MainBackground from "./mainBackground";
import Log from "./log";

class Logs extends Component {
  render() {
    return <MainBackground content={Log} />;
  }
}

export default Logs;
