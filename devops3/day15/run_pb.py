
#与执行ad-hoc命令一样,playbook的执行也需要相关模块

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor

Options = namedtuple(      ##创建元组
    'Options',
    [
        'connection',
        'remote_user',
        'ask_sudo_pass',
        'verbosity',
        'ask_pass',
        'module_path',
        'forks',
        'become',
        'become_method',
        'become_user',
        'check',
        'listhosts',
        'listtasks',
        'listtags',
        'syntax',
        'sudo_user',
        'sudo',
        'diff'
    ]
)

ops = Options(         ##创建元组
    connection='smart',
    remote_user=None,
    ask_pass=None,
    sudo_user=None,
    forks=5,
    sudo=None,
    ask_sudo_pass=False,
    verbosity=5,
    module_path=None,
    become=None,
    become_method=None,
    become_user=None,
    check=False,
    diff=False,
    listhosts=None,
    listtags=None,
    listtasks=None,
    syntax=None
)
loader = DataLoader()
passwords = dict()
inventory = InventoryManager(
    loader=loader,
    sources=['myansible/hosts']
)
variable_manager = VariableManager(
    loader=loader,
    inventory=inventory
)

def run_pb(pb_path):
    playbook = PlaybookExecutor(
        playbooks=pb_path,
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        options=ops,
        passwords=passwords
    )
    result = playbook.run()
    return result

if __name__ == '__main__':
    run_pb(pb_path=['myansi/lamp.yml'])
