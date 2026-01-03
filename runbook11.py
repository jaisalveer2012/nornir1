from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
import ipdb
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def structured_output(task):
    output = task.run(task=send_command, command="show cdp neighbors")
    task.host["facts"] = output.scrapli_response.genie_parse_output()
    cdp_index = task.host["facts"]["cdp"]["index"]
    for num in cdp_index:
        local_interface = cdp_index[num]["local_interface"]
        remote_device = cdp_index[num]["device_id"]
        remote_port = cdp_index[num]["port_id"]
        rprint(f"{task.host} {local_interface} is connected to {remote_device} {remote_port}")

results = nr.run(task=structured_output)
# print_result(results)
# ipdb.set_trace()
