import React, { Component } from "react";
import gameLogService from "../services/gameLogService";

class Log extends Component {
  constructor() {
    super();
    this.state = {
      screenshot: ""
    };
  }

  async componentDidMount() {
    let { data: screenshot } = await gameLogService.getScreenShot();
    this.setState({ screenshot });
    console.log(this.state);
  }

  render() {
    return (
      <div className="pl-5 pr-2 py-5">
        <div className="row">
          <div className="col-4">
            <h5 className="mb-2"> Log </h5>
            <div className="log-container"></div>
          </div>
          <div className="col-8">
            <h5 className="mb-2"> Screenshot </h5>
            <img
              src={`data:image/png;base64,${this.state.screenshot}`}
              alt="screenshot"
              className="screenshot"
            />
          </div>
        </div>
      </div>
    );
  }
}

export default Log;
