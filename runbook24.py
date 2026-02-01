from nornir import InitNornir
from nornir_scrapli.tasks import send_command
from nornir_utils.plugins.tasks.files import write_file
from nornir_utils.plugins.functions import print_result
from datetime import date
import pathlib

nr = InitNornir(config_file="config.yaml")

my_list = []
user_input = input("Enter the command: ")
while user_input:
    my_list.append(user_input)
    user_input = input("Enter the command: ")
    if user_input == "\n":
        break

def config_backup(task):
    for cmd in my_list:
        folder = cmd.replace(" ", "_")
        folder = folder.strip("\n")
        config_dir = "config-archive"
        date_dir = config_dir + "/" + str(date.today())
        command_dir = date_dir + "/" + folder
        pathlib.Path(config_dir).mkdir(exist_ok=True)
        pathlib.Path(date_dir).mkdir(exist_ok=True)
        pathlib.Path(command_dir).mkdir(exist_ok=True)
        r = task.run(task=send_command, command=cmd)
        task.run(
            task=write_file,
            content=r.result,
            filename= str(command_dir + f"/{task.host}.txt"))
results = nr.run(name="creating_backup", task=config_backup)
print_result(results)




