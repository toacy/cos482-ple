import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { WelcomePage } from "../views/welcomePage";
import { CommonQuestions } from "../views/commonQuestions";
import { StudentDetails } from "../views/studentDetails"
import App from "../App";

const defaultRoutes = (
  <BrowserRouter>
    <Switch>
      <Route exact path="/" component={App} />
      <Route exact path="/home" component={WelcomePage} />
      <Route exact path="/duvidas-frequentes" component={CommonQuestions} />
      <Route exact path="/dados-pessoais" component={StudentDetails} />
      <Route path="*"><h3 style={{color: "#fff", margin: "20px"}}>Em construção ...</h3></Route>
    </Switch>
  </BrowserRouter>
);

export { defaultRoutes };
