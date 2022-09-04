Funkwhale.audio Ansible Role
=========
[![Galaxy](https://img.shields.io/badge/galaxy-kevit.ansible-role-funkwhale-blue.svg?style=flat)](https://galaxy.ansible.com/kevit/ansible-role-funkwhale)
[![Build Status](https://travis-ci.org/kevit/ansible-role-funkwhale.svg?branch=master)](https://travis-ci.org/kevit/ansible-role-funkwhale)

A brief description of the role goes here.

Requirements
------------
Recommend by ansible host to use:
- Molecule ver. 3+ (syntax of files)
- Ansible-galaxy collection:
  - community.docker

Recommend by ansible aims by OS to use:
- Python ver. 3.7+ (python modules)

Role Variables
--------------

| Name              | Default Value       | Description          |
|-------------------|---------------------|----------------------|
| `` | `` |  |


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

    - hosts: all 
      gather_facts: true
      become: yes
      roles:
      - { role: ansible-role-funkwhale }

License
-------

MIT
