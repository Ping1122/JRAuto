import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";
import Header from "./components/header";
import Tasks from "./components/tasks";
import Footer from "./components/footer";

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
          <Header />
          <Tasks />
          <Footer />
        </div>
      </div>
    );
  }
}

export default App;
