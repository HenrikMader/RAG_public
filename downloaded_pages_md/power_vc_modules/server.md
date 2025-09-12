# server – Create/Delete the Virtual Machines from PowerVC.

## Synopsis
This playbook helps in performing the Create and Delete VM operations.

## Parameters
- name (optional, str, None): Name of the Server
- flavor (optional, str, None): Name of the flavor
- image (optional, str, None): Name of the image
- collocation_rule_name (optional, str, None): Name of the collocation_rule_name
- max_count (optional, str, None): The maximum number of servers to create.
- key_name (optional, str, None): The key pair name to be used when creating an instance.
- network (optional, str, None): Name or ID of a network to attach this instance to. A simpler version of the nics parameter; only one of network or nics should be supplied. This server attribute cannot be updated.
- nics (optional, list, []): A list of networks to which the instance’s interface should be attached. Networks may be referenced by network_id/network_name.
- image_volume_override (optional, list, []): A list of volume id and templated id which will be attached to the VM. Referenced by volume_id and template_id.
- volume_name (optional, list, []): A list of volumes that are to be attached to the VM.
- state (True, str, None): VM Operation to be perfomed.

## Examples
```yaml
---
- name: PowerVC Create VM Playbook
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
    - name: Create a new instance and attaches to a network
      ibm.powervc.server:
        auth: "{{ auth }}"
        name: "VM_NAME"
        image: "VM_IMAGE"
        timeout: 200
        max_count: "COUNT"
        collocation_rule_name: "COLLOCATION_RULE_NAME"
        nics:
          - network_name: "NETWORK_NAME"
            fixed_ip: "FIXED_IP" # "fixed_ip: 192.168.10.20"
        image_volume_override:
          - volume_id: "VOLUME_ID"
            template_id: "TEMPLATE_ID"
        flavor: "FLAVOR_NAME"
        volume_name: ["VOLUME_1", "VOLUME_2"]
        state: present
        validate_certs: no
      register: result

    - name: Disply server info
      debug:
        var: result
```

```yaml
- name: PowerVC Create VM Playbook
  hosts: localhost
  gather_facts: no
  tasks:
    - name: Create a new instance and attaches to a network
      ibm.powervc.server:
        cloud: "CLOUD_NAME"
        name: "VM_NAME"
        image: "VM_IMAGE"
        timeout: 200
        max_count: "COUNT"
        collocation_rule_name: "COLLOCATION_RULE_NAME"
        nics:
          - network_name: "NETWORK_NAME"
            fixed_ip: "FIXED_IP" # "fixed_ip: 192.168.10.20"
        image_volume_override:
          - volume_id: "VOLUME_ID"
            template_id: "TEMPLATE_ID"
        flavor: "FLAVOR_NAME"
        volume_name: ["VOLUME_1", "VOLUME_2"]
        state: present
        validate_certs: false
      register: result

    - name: Disply server info
      debug:
        var: result
```

```yaml
- name: PowerVC Delete VM Playbook
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
    - name: Delete the VM based on the input name provided
      ibm.powervc.server:
        auth: "{{ auth }}"
        name: "VM_NAME"
        state: absent
      register: result

    - name: Disply server info
      debug:
        var: result
```

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by PowerVC.

### Authors
- Karteesh Kumar Vipparapelli (@vkarteesh)