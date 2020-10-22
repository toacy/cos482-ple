import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { WelcomePage } from "../views/welcomePage";
import { CommonQuestions } from "../views/commonQuestions";
import App from "../App";

const defaultRoutes = (
  <BrowserRouter>
    <Switch>
      <Route exact path="/" component={App} />
      <Route exact path="/home" component={WelcomePage} />
      <Route exact path="/duvidas-frequentes" component={CommonQuestions} />
      <Route path="*">Em construção ...</Route>
    </Switch>
  </BrowserRouter>
);

export { defaultRoutes };
