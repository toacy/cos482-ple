from services.camunda_service import CamundaService
from config import TestConfig

camunda_handler = CamundaService("alterar_dados_usuario", config=TestConfig)
process_data = camunda_handler.start_process()

print(process_data)


camunda_handler.claim_task(process_data["processInstanceId"])
camunda_handler.complete_task(process_data["processInstanceId"])
camunda_handler.claim_task(process_data["processInstanceId"])
camunda_handler.complete_task(process_data["processInstanceId"])
