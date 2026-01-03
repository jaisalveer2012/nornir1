from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_scrapli.functions import print_structured_result
from nornir_utils.plugins.functions import print_result
import ipdb

nr = InitNornir(config_file="config.yaml")
def structured_output(task):
    output = task.run(task=send_command, command="show ip interface")
    # task.host["facts"] = output.scrapli_response.genie_parse_output()      #no need if want to use genie structured output directly using print_structured_result

results = nr.run(task=structured_output)
print_structured_result(results, parser="genie")
# ipdb.set_trace()