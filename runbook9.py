from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

print("--- Inventory Report ---")
print(f"Total Hosts Found: {len(nr.inventory.hosts)}")
for name, host in nr.inventory.hosts.items():
    print(f"Host: {name} | IP: {host.hostname}")