import axios from "axios";

const API_URL = "http://localhost:8080"

export default class SistemaAcademicoAPI {

    static login(email, password) {
        return axios.post(`${API_URL}/authenticate`, {
            email, password 
        });
    }


    static studentDetails(studentId) {
        return axios.get(`${API_URL}/discentes/${studentId}`)
    }


    static updateStudentDetails(studentId, chave, novoValor) {
        return axios.put(`${API_URL}/discentes/${studentId}?${chave}=${novoValor}`)
    }
}
