# volume_detach – Detaches the Volume to the Virtual Machine.

## Synopsis
This playbook helps in performing the Volume detach operations on the VM provided.

## Parameters
- name (required, str, default: None): Name of the VM
- volume_name (optional, list, default: None): Name of the volumes want to be detached

## Examples
```yaml
---
- name: VM Volume Detach Playbook
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
    - name: Perform VM Volume Attach Operations
      ibm.powervc.volume_detach:
        auth: "{{ auth }}"
        name: "NAME"
        volume_name: ["VOL_NAME1", "VOL_NAME2", "VOL_NAME3"]
        validate_certs: no
      register: result
    - debug:
        var: result

- name: VM Volume Detach Playbook
  hosts: localhost
  gather_facts: no
  tasks:
    - name: Perform VM Volume Attach Operations
      ibm.powervc.volume_detach:
        cloud: "CLOUD_NAME"
        name: "NAME"
        volume_name: ["VOLUME_NAME1", "VOLUME_NAME2", "VOLUME_NAME3"]
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