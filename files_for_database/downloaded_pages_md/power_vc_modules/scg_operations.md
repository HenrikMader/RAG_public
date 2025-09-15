# scg_operations – Performs the Create, Delete, Update on the Storage Connectivity Group.

## Synopsis
This playbook helps in performing the Create, Delete and Update operations for the Storage Connectivity Groups.

## Parameters
- state (required, str): SCG Operation to be performed
- name (optional, str): Name of the Storage Connectivity Group
- scg_id (optional, str): ID of the Storage Connectivity Group

## Examples
```yaml
- name: Storage Connectivity Group Operations from PowerVC Server
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
    - name: Performing the DELETE SCG Operation
      ibm.powervc.scg_operations:
        auth: "{{ auth }}"
        state: "absent"
        name: "NAME"
        validate_certs: no
      register: result
    - debug:
        var: result
```

```yaml
- name: Storage Connectivity Group Operations from PowerVC Server
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
    - name: Performing the Create SCG Operation
      ibm.powervc.scg_operations:
        auth: "{{ auth }}"
        state: "present"
        display_name: <DISPLAY_NAME>
        vios_ids: <VIOS_ID>
        boot_connectivity: <BOOT_CONNECTIVITY_VAL>
        data_connectivity: <DATA_CONNECTIVITY_VAL>
      register: result
    - debug:
        var: result
```

```yaml
- name: Storage Connectivity Group Operations from PowerVC Server
  hosts: all
  gather_facts: no
  tasks:
    - name: Performing the Create SCG Operation
      ibm.powervc.scg_operations:
        cloud: "{{ CLOUD_NAME }}"
        state: "present"
        display_name: <DISPLAY_NAME>
        vios_ids: <VIOS_ID>
        boot_connectivity: <BOOT_CONNECTIVITY_VAL>
        data_connectivity: <DATA_CONNECTIVITY_VAL>
      register: result
    - debug:
        var: result
```

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by PowerVC.

### Authors
- Karteesh Kumar Vipparapelli (@vkarteesh)