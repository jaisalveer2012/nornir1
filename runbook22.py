from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.tasks.files import write_file
from nornir_utils.plugins.functions import print_result 

nr = InitNornir(config_file="config.yaml")

def config_backup(task):
    cmds = ["show run", "show version"]
    for cmd in cmds:
        r = task.run(task=send_command, command=cmd)
        task.run(task=write_file, content=r.result, filename=f"{cmd}-{task.host}.txt")

result = nr.run(name="config_backup", task=config_backup)
print_result(result)
