from services.camunda_service import CamundaService
from config import TestConfig


def test_alterar_dados_usuario():
    camunda_handler = CamundaService("alterar_dados_usuario", config=TestConfig)
    process_data = camunda_handler.start_process()

    camunda_handler.claim_task(process_data["processInstanceId"])
    response_code = camunda_handler.complete_task(process_data["processInstanceId"])
    assert response_code >= 200 and response_code < 300
