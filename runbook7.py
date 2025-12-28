from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_ping
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def napalm_ip_ping(task):
    task.run(task=napalm_ping, dest="192.168.137.128", count=10, size=1500)

results = nr.run(task=napalm_ip_ping)
print_result(results)
