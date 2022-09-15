import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

# Front.reverse
def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_running_and_enabled(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled

def test_nginx_config(host):
    host.run("nginx -t")

# Back.db
def test_postgresql_running_and_enabled(host):
    postgresql = host.service("postgresql")
    assert postgresql.is_running
    assert postgresql.is_enabled

def test_nginx_config(host):
    host.run("sudo -u postgres psql postgres -c 'SELECT version();'")

# Back.django
def test_funkwhaleserver_running_and_enabled(host):
    funkwhaleserver = host.service("funkwhale-server")
    assert funkwhaleserver.is_running
    assert funkwhaleserver.is_enabled
