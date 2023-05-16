import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_is_git_installed(host):
   package_git = host.package('git')
   assert package_git.is_installed

def test_ownership_multidir(host):
    somedir = host.file('/tmp/')
    assert somedir.is_directory
