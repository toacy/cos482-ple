import React, { useState } from "react";
import logo from "./assets/logo.png";
import SistemaAcademicoAPI from "./services/sistemaAcademicoApi"
import { Redirect } from "react-router-dom";
import "./App.css";

function App() {
  const [pass, setPass] = useState("")
  const [email, setEmail] = useState("")
  const [loggedIn, setLoggedIn] = useState(false)


  const login = (event) => {
    event.preventDefault()
    SistemaAcademicoAPI.login(email, pass)
    .then((response) =>  {
      if (parseInt(response.status) === 200) {
        setLoggedIn(true)
      } else {
        window.alert("Credenciais inválidas")
      }
    })
    .catch(() => window.alert("Credenciais inválidas"))
  }



  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <div>
        <form onSubmit={login}>
        <label>
            {"Email: "}
            <input type="text" name="email" onChange={(event) => setEmail(event.target.value)} />
          </label><br/><br/>
          <label>
          {"Senha: "}
            <input type="password" name="password" onChange={(event) => setPass(event.target.value)}/>
          </label><br/><br/>
          <input type="submit" value="Entrar" />
        </form>
        </div>
      </header>
      {
        loggedIn ? (
        <Redirect
          to={{
            pathname: "/home",
            state: {
              email: email
            },
          }}
        />
        ) 
        : 
        <></>
      }
    </div>
  );
}

export default App;
