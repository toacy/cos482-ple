import requests
import json
from requests.api import request
from config import ProductionConfig


class CamundaService:
    def __init__(self, process_name, config=ProductionConfig):
        self._camunda_server = config.CAMUNDA_SERVER
        self._camunda_user = config.CAMUNDA_USER
        self._process_name = process_name
        self._process_id = self._get_process_id()

    def _get_process_id(self):
        r = requests.get(self._camunda_server + "/process-definition")
        print(r.json())
        desired_process = [p for p in r.json() if p["key"] == self._process_name][0]
        print(desired_process)
        return desired_process["id"]

    def start_process(self):
        r = requests.post(self._camunda_server + f"/process-definition/{self._process_id}/start",
                          headers={"Content-Type": "application/json"},
                          data=json.dumps({"businessKey": 123}),
                          )
        if r.status_code != 200:
            print(r.text)
            raise f"Erro ao iniciar processo, {r.text}"

        response = r.json()
        return {
            "processInstanceId": response["id"],
            "processInstanceBusinessKey": response["businessKey"]
        }

    def find_task(self, processInstanceId):
        r = requests.get(self._camunda_server + f"/task")
        r = r.json()
        task_to_claim = [t for t in r if t["processInstanceId"] == processInstanceId][0]
        return task_to_claim["id"]

    def claim_task(self, processInstanceId):
        taskId = self.find_task(processInstanceId)
        r = requests.post(self._camunda_server + f"/task/{taskId}/claim",
                          headers={"Content-Type": "application/json"},
                          data=json.dumps({"userId": self._camunda_user}),
                          )

    def complete_task(self, processInstanceId):
        taskId = self.find_task(processInstanceId)
        r = requests.post(self._camunda_server + f"/task/{taskId}/complete",
                          headers={"Content-Type": "application/json"},
                          data={})
        return r.status_code
