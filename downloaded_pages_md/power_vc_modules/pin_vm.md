# pin_vm – Performs the Pin VM operations.

## Synopsis
This playbook helps in performing the Pin operations on the VM provided.

## Parameters
- name (optional, str, None): Name of the Server
- pin_type (optional, str, None): Pin Type - Allowed values are no_pin, soft_pin, hard_pin

## Examples
```yaml
- name: Perform Soft Pin Operations on the VM
  hosts: all
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
     - name: Pin VM Task
       ibm.powervc.pin_vm:
          auth: "{{ auth }}"
          name: "NAME"
          pin_type: "PIN_TYPE"
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