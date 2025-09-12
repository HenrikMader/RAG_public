# vios_maintenance – Manage the vios backup

## Synopsis
- Create a VIOS backup file
- List VIOS backup file details
- Modify the name of the VIOS backup file
- Remove a VIOS backup file
- Restore a VIOS backup

## Parameters
- hmc_host (required, str)
  - The IP address or hostname of the HMC.

- hmc_auth (required, dict)
  - username (required, str): Username of the HMC to login.
  - password (optional, str): Password of the HMC.

- attributes (required, dict)
  - types (required, str): The type of VIOS backup to create.  
    Valid values are `viosioconfig` for a VIOS I/O configuration backup, `vios` for a full VIOS backup, `ssp` for a Shared Storage Pool configuration backup.
  - system (optional, str): The name of the managed system which has the VIOS to back up.
  - vios_id (optional, str): The ID of the VIOS to back up. `vios_id`, `vios_uuid`, `vios_name` are mutually exclusive.
  - vios_uuid (optional, str): The UUID of the VIOS to back up. `vios_id`, `vios_uuid`, `vios_name` are mutually exclusive.
  - vios_name (optional, str): The name of the VIOS to back up. `vios_id`, `vios_uuid`, `vios_name` are mutually exclusive.
  - backup_name (optional, str): The name of the file where the backup will be saved.
  - file_list (optional, list): The list of backup files that need to be removed. This option is for `remove` state only. Add backup file names as comma-separated values.
  - nimol_resource (optional, int): Include NIMOL resources (`1` to include, `0` to exclude). Valid only when creating a full VIOS backup.
  - media_repository (optional, int): Include contents of the media repository (`1` to include, `0` to exclude). Valid only when creating a full VIOS backup.
  - volume_group_structure (optional, int): Include the volume group structure of user (`1` to include, `0` to exclude). Valid only when creating a full VIOS backup.
  - restart (optional, bool): Restart the VIOS if required (`True` to restart, `False` to not restart). Valid for `restore` state only.
  - new_name (optional, str): New name of the backup file. Valid for `modify` state only.

- state (optional, str)
  - `facts`: Does not change anything on the HMC and returns list of backup files of a VIOS.
  - `present`: Ensures a new backup file is created for the specified VIOS.
  - `absent`: Ensures the specified backup file(s) are removed from the HMC.
  - `restore`: Ensures the backup file is restored.
  - `modify`: Ensures that the name of the backup file is changed in the HMC.

## Notes
- All operations support passwordless authentication.

## Examples
```yaml
- name: Create a viosioconfig backup file
  vios_maintenance:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    attributes:
      vios_name: <vios name>
      backup_name: test
      system: <sys>
      types: viosioconfig
    state: present

- name: Restore a vios from test backup file
  vios_maintenance:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    attributes:
      vios_name: <vios name>
      backup_name: test.tar.gz
      system: <sys>
      types: viosioconfig
    state: restore

- name: Remove a backup file
  vios_maintenance:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    attributes:
      vios_name: <vios name>
      backup_name: test.tar.gz
      system: <sys>
      types: viosioconfig
    state: absent

- name: Rename the backup file
  vios_maintenance:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    attributes:
      vios_name: <vios name>
      backup_name: test.tar.gz
      new_name: new.tar.gz
      system: <sys>
      types: viosioconfig
    state: modify
```

## Return Values
- Command_output (dict, on success of all states except `absent`): Respective user configuration.

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- Sreenidhi S (@SreenidhiS1)