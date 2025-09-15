# migrate_vm – Migrating the Virtual Machine from one host to the other

## Synopsis
This playbook helps in performing the Migrate operations on the VM provided.

## Parameters
- name (optional, str, None): Name of the VM
- host (optional, str, None): Name of the Host

## Examples
```yaml
---
  - name: VM Migrate Playbook
    hosts: localhost
    gather_facts: no
    vars:
     auth:
      auth_url: https://<POWERVC>:5000/v3
      project_name: PROJECT-NAME
      username: USERID
      password: PASSWORD
      project_domain_name: PROJECT_DOMAIN_NAME
      user_domain_name: USER_DOMAIN_NAME
    tasks:
       - name: Perform VM Migrate Operations
         ibm.powervc.migate_vm:
            auth: "{{ auth }}"
            name: "NAME"
            host: "HOST"
            validate_certs: no
         register: result
       - debug:
            var: result

  - name: VM Migrate Playbook
    hosts: localhost
    gather_facts: no
    tasks:
       - name: Perform VM Migrate Operations
         ibm.powervc.migate_vm:
            cloud: "CLOUD_NAME"
            name: "NAME"
            host: "HOST"
            validate_certs: no
         register: result
       - debug:
            var: result
```

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by PowerVC.

### Authors
- Karteesh Kumar Vipparapelli (@vkarteesh)