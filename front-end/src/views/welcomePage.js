import React from "react";
import "./welcomePage.css";

const WelcomePage = () => {
  return (
    <div className="welcome-page-container">
      <h1>Bem vindo!</h1>
      <div>
        <div className="menu-option" onClick={() => (window.location.href = "./inscricao")}>
          Inscrição em disciplinas
        </div>
        <div className="menu-option" onClick={() => (window.location.href = "./duvidas-frequentes")}>
          Dúvidas frequentes
        </div>
        <div className="menu-option" onClick={() => (window.location.href = "./dados-pessoais")}>
          Alteração de dados pessoais
        </div>
      </div>
    </div>
  );
};

export { WelcomePage };
