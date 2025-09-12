# manage_vm – Performs the Manage operations on the Virtual Machine.

## Synopsis
This playbook helps in performing the Manage operations on the VM provided.

## Parameters
- id (optional, str, None) — ID of the VM
- host (optional, str, None) — Host of the VM

## Examples
```yaml
---
- name: VM Manage Playbook
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
    - name: Perform VM Manage Operations
      ibm.powervc.manage_vm:
        auth: "{{ auth }}"
        id: "VM_ID"
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