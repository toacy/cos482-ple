import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import { defaultRoutes as routes } from "./routes/index";
import { BrowserRouter as Router } from "react-router-dom";
import * as serviceWorker from "./serviceWorker";
import { Header } from "./components/header";

ReactDOM.render(
  <React.StrictMode>
    {window.location.pathname === "/" ? <></> : <Header />}

    <Router>{routes}</Router>
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
