from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yaml")

def show_version(task):
    task.run(task=send_command, command="show version")

results = nr.run(task=show_version)
print_result(results)
