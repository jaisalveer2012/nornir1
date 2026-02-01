from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

target = input("Enter the mac address want to search for: ")

def find_mac_address(task):
    interface_result = task.run(task=send_command, command="show interfaces")
    task.host["facts"] = interface_result.scrapli_response.genie_parse_output()
    interfaces = task.host["facts"]
    for interface in interfaces:
        mac_addr = interfaces[interface]["mac_address"]
        if target == mac_addr:
            print(f"{task.host}'s {interface} has the mac address {mac_addr}")

nr.run(task=find_mac_address)
# import ipdb
# ipdb.set_trace()
