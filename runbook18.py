import json
from nornir import InitNornir
from nornir_http.tasks import http_method
from nornir_utils.plugins.functions import print_result 

nr = InitNornir(config_file="config.yaml")

headers = {
    "Accept": "application/yang-data+json"}

def restconfig(task):
    response = task.run(
        task=http_method, 
        method="get", 
        verify=False, 
        auth=(f"{task.host.username}", f"{task.host.password}"),
        headers=headers,
        url=f"https://{task.host.hostname}:443/restconf/data/native/interface",
    )
    task.host["facts"] = json.loads(response.result)

results = nr.run(task=restconfig)
print_result(results)   
