from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result
from rich import print as rprint

nr = InitNornir(config_file="config.yaml")

def routing_table(task):
    show_result = task.run(task=send_command, command="show ip route")
    task.host["facts"] = show_result.scrapli_response.genie_parse_output()
    routes = task.host["facts"]["vrfs"]["default"]["address_family"]["ipv4"]["routes"]
    for key in routes:
        try:
            next_hop_list = routes[key]['next_hop']['next_hop_list']
            rprint(f"{task.host} Next hop info: {next_hop_list}")

        except KeyError:
            pass


result = nr.run(task=routing_table)
print_result(result)
# import ipdb
# ipdb.set_trace()

