# clone_vm – Takes Clone of the Virtual Machine.

## Synopsis
This playbook helps in performing the Clone operations on the VM provided.

## Parameters
- name (True, str, None): Name of the VM
- clonevm_name (True, str, None): Name of the Cloned VM
- nics (True, list, None): A list of networks to which the instance’s interface should be attached.

## Examples
```yaml
- name: VM Clone Playbook with Network
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
    - name: Perform VM Clone Operation on VM with network
      ibm.powervc.clone_vm:
        auth: "{{ auth }}"
        vm_name: "VM_NAME"
        clonevm_name: "CLONEVM_NAME"
        nics:
          - net-name: "NET-NAME"
        validate_certs: no
      register: result
    - debug:
        var: result
```

```yaml
- name: VM Clone Playbook with Network and providing a fixed_ip
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
    - name: Perform VM Clone Operation on VM with network and IP details
      ibm.powervc.clone_vm:
        auth: "{{ auth }}"
        vm_name: "VM_NAME"
        clonevm_name: "CLONEVM_NAME"
        nics:
          - net-name: "NET-NAME"
            fixed_ip: "FIXED_IP"
        validate_certs: no
      register: result
    - debug:
        var: result
```

```yaml
- name: VM Clone Playbook with Network and providing a fixed_ip
  hosts: localhost
  gather_facts: no
  tasks:
    - name: Perform VM Clone Operation on VM with network and IP details
      ibm.powervc.clone_vm:
        cloud: "CLOUD_NAME"
        vm_name: "VM_NAME"
        clonevm_name: "CLONEVM_NAME"
        nics:
          - net-name: "NET-NAME"
            fixed_ip: "FIXED_IP"
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