from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def send_netmiko_command(task):
    task.run(task=netmiko_send_command, command_string="show version")

results = nr.run(task=send_netmiko_command)
print_result(results)
