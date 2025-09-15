# unmanage_vm – Performs Unmanage operations on the Virtual Machine.

## Synopsis
This playbook helps in performing the Unmanage operations on the VM provided.

## Parameters
- name (required, string, default: None): Name of the VM

## Examples
```yaml
---
  - name: VM Unmanage Playbook
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
       - name: Perform VM Unmanage Operations
         ibm.powervc.unmanage_vm:
            auth: "{{ auth }}"
            name: "NAME"
            validate_certs: no
         register: result
       - debug:
            var: result

  - name: VM Unmanage Playbook
    hosts: localhost
    gather_facts: no
    tasks:
       - name: Perform VM Unmanage Operations
         ibm.powervc.unmanage_vm:
            cloud: "CLOUD_NAME"
            name: "NAME"
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