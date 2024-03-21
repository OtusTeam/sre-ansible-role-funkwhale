import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

@pytest.mark.parametrize('pkg', [
'nginx',
'redis'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed

@pytest.mark.parametrize('file, content', [
("/etc/nginx/conf.d/funkwhale.conf", "upstream funkwhale-api"),
("/etc/systemd/system/funkwhale-server.service", "User=funkwhale")
])
def test_files(host, file, content):
    file = host.file(file)
    assert file.exists
    assert file.contains(content)
