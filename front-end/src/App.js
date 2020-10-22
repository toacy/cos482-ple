import React from "react";
import logo from "./assets/logo.png";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <a className="App-link" href="./home">
          Entrar
        </a>
      </header>
    </div>
  );
}

export default App;
