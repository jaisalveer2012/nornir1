from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def get_interfaces(task):
    task.run(task=napalm_get, getters=["get_interfaces"])

results = nr.run(task=get_interfaces)
print_result(results)