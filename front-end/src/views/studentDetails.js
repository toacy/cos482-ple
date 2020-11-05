import React, { useState, useEffect } from "react";
import SistemaAcademicoAPI from "../services/sistemaAcademicoApi"
import "./welcomePage.css";

const StudentDetails = () => {
  const [dadosPessoais, setDadosPessoais] = useState({})


  useEffect(() => {
    SistemaAcademicoAPI.studentDetails(1)
      .then((response) => setDadosPessoais(response.data))
  }, [])

  const alterarInformacao = (chave) => {
    let novoValor = window.prompt(`Digite um novo valor para ${chave}`)
    SistemaAcademicoAPI.updateStudentDetails(1, chave, novoValor)
    window.location.reload()

  }


  return (
    <div className="welcome-page-container">
      <h1>Dados Pessoais</h1>
      <ul>
        {Object.keys(dadosPessoais)
          .filter(info => info !== "id")
          .map(info => <li style={{margin: "15px", maxWidth: "500px", display: "flex", justifyContent: "space-between"}}>
                          {info.replace("_", " de ").toUpperCase()}: 
                          
                          {dadosPessoais[info]}
                          <button 
                            onClick={() => alterarInformacao(info)} 
                            style={{fontSize: "18px", margin: "2px"}}>
                              Editar 
                              <i class="fa fa-pencil"></i>
                              </button>
                        </li>
          )
        }
      </ul>
    </div>
  );
};

export { StudentDetails };
