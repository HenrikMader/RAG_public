# resize_vm – Resizes the VM based on the compute templates parameter.

## Synopsis
This playbook helps in performing the Resize operations on the VM based on the compute templates parameter.

## Parameters
- name (True, str, None): Name of the VM
- template_type (True, str, None): Name of the Compute Template

## Examples
```yaml
- name: VM Resize Playbook
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
    - name: Performing the DELETE SCG Operation
      ibm.powervc.resize_vm:
        auth: "{{ auth }}"
        vm_name: "VM_NAME"
        template_type: "TEMPLATE_TYPE"
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