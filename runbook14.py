from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
def structured_output(task):
    output = task.run(task=netmiko_send_command, command_string="show clock", use_textfsm=True)
    structured_result = output.result
    print(structured_result)

results = nr.run(task=structured_output)
# print_result(results)