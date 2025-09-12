# volume_attach – Attach the Volume to the Virtual Machine.

## Synopsis
This playbook helps in performing the Volume attach operations on the VM provided.

## Parameters
- name (required, str; default: None): Name of the VM.
- volume_name (optional, list; default: None): Names of the volumes to be attached.
- volume_id (optional, list; default: None): IDs of the volumes to be attached.

## Examples
```yaml
---
- name: VM Volume Attach Playbook
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
      ibm.powervc.volume_attach:
        auth: "{{ auth }}"
        name: "NAME"
        volume_name: ["VOL_NAME1", "VOL_NAME2", "VOL_NAME3"]
        validate_certs: no
      register: result

    - debug:
        var: result

- name: VM Volume Attach Playbook
  hosts: localhost
  gather_facts: no
  tasks:
    - name: Perform VM Volume Attach Operations
      ibm.powervc.volume_attach:
        cloud: "CLOUD_NAME"
        name: "NAME"
        volume_name: ["VOL_NAME1", "VOL_NAME2", "VOL_NAME3"]
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