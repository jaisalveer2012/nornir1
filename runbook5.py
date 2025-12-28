from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def send_netmiko_configs(task):
    task.run(task=netmiko_send_config, config_commands=["do show version"])

results = nr.run(task=send_netmiko_configs)
print_result(results)
