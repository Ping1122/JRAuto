import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";
import Header from "./components/header";
import Tasks from "./components/tasks";
import Footer from "./components/footer";
function App() {
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

export default App;
