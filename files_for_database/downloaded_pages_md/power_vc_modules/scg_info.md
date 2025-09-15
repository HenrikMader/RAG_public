# scg_info – Fetches the Storage Connectivity Group Details.

## Synopsis
This playbook helps in performing the Get operations for the Storage Connectivity Groups.

## Parameters
- scg_name (string, optional): Name of the Storage Connectivity Group
- scg_id (string, optional): ID of the Storage Connectivity Group

## Examples
```yaml
- name: List all the SCG Details Playbook
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
    - name: Get All the SCG Details
      ibm.powervc.scg_info:
        auth: "{{ auth }}"
        validate_certs: no
      register: result
    - debug:
        var: result
```

```yaml
- name: List all the SCG Details Playbook
  hosts: all
  gather_facts: no
  tasks:
    - name: Get All the SCG Details
      ibm.powervc.scg_info:
        cloud: "CLOUD_NAME"
        validate_certs: no
      register: result
    - debug:
        var: result
```

```yaml
- name: List a Specific SCG Details Playbook
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
    - name: Get the specific SCG Details
      ibm.powervc.scg_info:
        auth: "{{ auth }}"
        scg_name: "SCG_NAME"
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