from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_save_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def send_netmiko_config_save(task):
    task.run(task=netmiko_save_config, cmd="write memory")

results = nr.run(task=send_netmiko_config_save)
print_result(results)
