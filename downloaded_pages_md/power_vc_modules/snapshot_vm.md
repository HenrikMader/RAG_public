# snapshot_vm – Takes the Snapshot of VM’s All/Boot/Specific volumes.

## Synopsis
This playbook helps in performing the Snapshot operations on the VM based on the inputs

## Parameters
- name (True, str, None): Name of the VM
- volume (True, dict, None): Name of the Volume type. Provide the Volume name if volume type is Specific
- snapshot_name (optional, str, None): Name of the Snapshot
- snapshot_description (optional, str, None): Description of the Snapshot

## Examples
```yaml
- name: VM Specific Volume Snapshot Playbook
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
    - name: Perform VM Snapshot Operations on Specific volumes
      ibm.powervc.snapshot_vm:
        auth: "{{ auth }}"
        vm_name: "VM_NAME"
        snapshot_name: "SNAPSHOT_NAME"
        snapshot_description: "SNAPSHOT_DESCRIPTION"
        volume:
          type: "Specific"
          name: ['VOLUME_NAME']
        validate_certs: no
      register: result
    - debug:
        var: result
```

```yaml
- name: VM All Volume Snapshot Playbook
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
    - name: Perform VM Snapshot Operations on All the volumes
      ibm.powervc.snapshot_vm:
        auth: "{{ auth }}"
        vm_name: "VM_NAME"
        snapshot_name: "SNAPSHOT_NAME"
        snapshot_description: "SNAPSHOT_DESCRIPTION"
        volume:
          type: "All"
        validate_certs: no
      register: result
    - debug:
        var: result
```

```yaml
- name: VM Boot Volume Snapshot Playbook
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
    - name: Perform VM Snapshot Operations on Boot volumes
      ibm.powervc.snapshot_vm:
        auth: "{{ auth }}"
        vm_name: "VM_NAME"
        snapshot_name: "SNAPSHOT_NAME"
        snapshot_description: "SNAPSHOT_DESCRIPTION"
        volume:
          type: "Boot"
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