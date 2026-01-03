from nornir import InitNornir
from nornir_scrapli.tasks import send_command
import ipdb
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def structured_output(task):
    output = task.run(task=send_command, command="show ip int brief")
    task.host["facts"] = output.scrapli_response.genie_parse_output()
    print(task.host["facts"])

results = nr.run(task=structured_output)
# print_result(results)
ipdb.set_trace()

