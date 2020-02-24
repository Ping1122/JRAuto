import React, { Component } from "react";
import { BrowserRouter, Route, Redirect, Switch } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";
import "react-toastify/dist/ReactToastify.css";
import Header from "./components/header";
import Tasks from "./components/tasks";
import Logs from "./components/logs";
import Footer from "./components/footer";
import NotFound from "./components/notFound";

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
          <ToastContainer />

          <BrowserRouter>
            <Route path="/" component={Header} />
            <Switch>
              <Route path="/tasks" component={Tasks} />
              <Route path="/logs" component={Logs} />
              <Route path="/not-found" component={NotFound} />
              <Redirect from="/" exact to="/tasks" />
              <Redirect to="/not-found" />
            </Switch>
          </BrowserRouter>
          <Footer />
        </div>
      </div>
    );
  }
}

export default App;
