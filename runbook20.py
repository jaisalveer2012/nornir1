from nornir import InitNornir
from nornir_scrapli.tasks import send_configs
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.tasks.data import load_yaml

nr = InitNornir(config_file="config.yaml")

def load_variable(task):
    vars_data = task.run(task=load_yaml, file=f"./host_vars/{ task.host}.yaml")       # every host gets its own YAML file
    task.host["facts"] = vars_data.result
    push_some_configs(task)



def push_some_configs(task):
    template = task.run(task=template_file, template="snmp.j2", path="templates")
    task.host["snmp_config"] = template.result
    rendered = task.host["snmp_config"]
    configuration = rendered.splitlines()
    task.run(task=send_configs, configs=configuration)

results = nr.run(task=load_variable)
print_result(results)
