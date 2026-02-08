from math import inf
from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")
# This script will search for a mac address across all devices in the inventory and print out the device name, interface, version and serial number if found. 
# If not found, it will print out a message saying the target was not found on any device.
target_list = []

target = input("Enter the mac address want to search for: ")

def find_mac_address(task):
    interface_result = task.run(task=send_command, command="show interfaces")
    task.host["facts"] = interface_result.scrapli_response.genie_parse_output()
    interfaces = task.host["facts"]
    for interface in interfaces:
        mac_addr = interfaces[interface]["mac_address"]
        if target == mac_addr:
            target_list.append(mac_addr)
            intf = interface
            print_info(task, intf)

def print_info(task, intf):
    print(f"MAC ADDRESS : {target} is present on {task.host} interface {intf}")
    
    cdp_response = task.run(task=send_command, command="show cdp neighbors")
    task.host["cdpinfo"] = cdp_response.scrapli_response.genie_parse_output()
    index = task.host["cdpinfo"]["cdp"]["index"]
    for num in index:
        local_intf = index[num]["local_interface"]
        if local_intf == intf:
            dev_id = index[num]["device_id"]
            port_id = index[num]["port_id"]
    # Get version and serial number
    ver_result = task.run(task=send_command, command="show version")
    task.host["verinfo"] = ver_result.scrapli_response.genie_parse_output()
    version = task.host["verinfo"]["version"]
    serial_num = version["chassis_sn"]
    version_short = version["version_short"]
    print(f"DEVICE VERSION : {version_short}")
    print(f"DEVICE SERIAL NUMBER : {serial_num}")
    


nr.run(task=find_mac_address)
if target not in target_list:
    print("TARGET NOT FOUND ON ANY DEVICE")
# nr.run(task=cdp_neighbors)
# import ipdb
# ipdb.set_trace()