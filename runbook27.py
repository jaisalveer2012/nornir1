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
           source_proto = prefixes[prefix]["source_protocol"]
           if source_proto == "connected":
               try:
                   outgoing_intf = prefixes[prefix]["next_hop"]["outgoing_interface"]
                   for intf in outgoing_intf:
                       exit_inf = intf
                       print (f"{task.host} is connected to {target} via interface {exit_inf}")
               except KeyError:
                   pass
        else:
            try:
                next_hop_list = prefixes[prefix]["next_hop"]["next_hop_list"]
                for key in next_hop_list:
                    next_hop = next_hop_list[key]["next_hop"]
                    print (f"{task.host} can reach {target} via next hop {next_hop} {source_proto}")
            except KeyError:
                pass


nr.run(task=get_routes)
# import ipdb
# ipdb.set_trace()


