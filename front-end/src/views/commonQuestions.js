import React from "react";
import "./commonQuestions.css";

const CommonQuestions = () => {
  return (
    <div className="common-questions-container">
      <h1>Dúvidas frequentes</h1>
      <ul>
        <li>
          <h2>Como me inscrever em uma disciplina?</h2>
        </li>
        <p>
          Durante o período de inscrição em disciplinas o aluno poderá se inscrever nas disciplinas que tiver interesse
          através do Sistema Acadêmico
        </p>
        <li>
          <h2>Como iniciar um estágio?</h2>
          <p>
            O aluno apenas poderá iniciar um estágio após ter cumprido pelo menos 50% dos créditos de seu curso. Caso o
            estágio seja de 6h diárias é exigido que o aluno tenha pelo menos 85% do curso completo
          </p>
        </li>
        <li>
          <h2>Como trancar uma disciplina?</h2>
          <p>
            Trancamentos podem ser efetuados apenas durante o período de trancamento (verificar o calendário letivo). As
            solicitações de trancamento devem ser feitas através do Sistema Acadêmico
          </p>
        </li>
      </ul>
    </div>
  );
};

export { CommonQuestions };
