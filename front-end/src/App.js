import React from "react";
import logo from "./assets/logo.png";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {/* <p>Plataforma de gestão acadêmica da Universidade Federal do Rio de Janeiro</p> */}
        <a className="App-link" href="https://reactjs.org" target="_blank" rel="noopener noreferrer">
          Entrar
        </a>
      </header>
    </div>
  );
}

export default App;
