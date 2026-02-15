from ipaddress import ip_network, ip_address
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file = "config.yaml")

target = input ("Enter the target ip address : ")
ipaddr = ip_address(target)

def get_routes(task):

    route_table = task.run(task=send_command, command="show ip route")
    task.host["facts"]= route_table.scrapli_response.genie_parse_output()
    prefixes = task.host["facts"]["vrf"]["default"]["address_family"]["ipv4"]["routes"]
    for prefix in prefixes:
        net = ip_network(prefix)
        if ipaddr in net:
            print(f"{ipaddr} is present on device {task.host} (network: {net})")


nr.run(task=get_routes)
# import ipdb
# ipdb.set_trace()


