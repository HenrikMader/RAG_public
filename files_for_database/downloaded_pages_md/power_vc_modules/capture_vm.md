# capture_vm – Capturing the Image out of the Virtual Machine.

## Synopsis
This playbook helps in performing the Image Create/Capture operations on the VM provided.

## Parameters
- name (optional, str, default: None): Name of the VM

## Examples
```yaml
---
- name: VM Capture Playbook
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
    - name: Perform VM Capture Operations
      ibm.powervc.capture_vm:
        auth: "{{ auth }}"
        name: "NAME"
        image_name: "IMAGE_NAME"
        validate_certs: no
      register: result
    - debug:
        var: result

- name: VM Capture Playbook
  hosts: localhost
  gather_facts: no
  tasks:
    - name: Perform VM Capture Operations
      ibm.powervc.capture_vm:
        cloud: "CLOUDNAME"
        name: "NAME"
        image_name: "IMAGE_NAME"
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