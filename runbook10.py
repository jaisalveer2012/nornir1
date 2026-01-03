from nornir import InitNornir
from nornir_scrapli.tasks import send_command
import ipdb
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def structured_output(task):
    output = task.run(task=send_command, command="show ip interface")
    task.host["facts"] = output.scrapli_response.genie_parse_output()
    interfaces = task.host["facts"]["Loopback111"]
    print(interfaces)

results = nr.run(task=structured_output)
# print_result(results)
# ipdb.set_trace()

