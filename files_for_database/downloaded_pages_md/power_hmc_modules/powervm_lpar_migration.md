# powervm_lpar_migration – validate, migrate and recover of the LPAR

## Synopsis
- Validate provided LPAR/s for migration
- Migrate provided LPAR/s
- Recover provided LPAR
- Authenticate HMC

## Parameters
- hmc_host (required, str)
  - The IP Address or hostname of the HMC.
- hmc_auth (required, dict)
  - Username and Password credential of the HMC.
  - username (required, str) – Username of the HMC to login.
  - password (optional, str) – Password of the HMC.
- src_system (optional, str)
  - The name of the source managed system.
- dest_system (optional, str)
  - The name of the destination managed system.
  - Valid only for `validate` and `migrate` action.
- vm_names (optional, list)
  - Name of the partition/s to be migrated/validated.
  - To perform action on multiple partitions, provide comma-separated partition names or in list form.
  - For `recover` action only one partition name is allowed.
- vm_ids (optional, list)
  - ID/s of the partition to be migrated/validated.
  - To perform action on multiple partitions, provide comma-separated partition IDs or in list form.
  - For `recover` action only one partition ID is allowed.
- all_vms (optional, bool)
  - All the partitions of the `src_system` to be migrated.
  - Valid only for `migrate` action.
- remote_ip (optional, str)
  - If the destination managed system is not managed by the same management console that is managing the source managed system, specify the IP address or host name of the management console that is managing the destination managed system.
  - This option is mandatory for `authenticate` action and optional for other actions.
- remote_username (optional, str)
  - Username of the remote HMC.
  - Can be used only with `authenticate` action.
- remote_passwd (optional, str)
  - Password of the remote HMC.
  - Can be used only with `authenticate` action.
- wait (optional, int)
  - The maximum time, in minutes, to wait for operation to complete.
  - Can be used only with `migrate` and `validate` actions.
- shared_proc_pool (optional, list)
  - List of the details of the shared processor pools to use on the destination managed system.
  - Supports single and multiple pools.
  - Can be used only with `migrate`.
  - Fields:
    - lpar_name (optional, str) – Name of the partition to be migrated. Mutually exclusive with lpar_id.
    - lpar_id (optional, int) – ID of the partition to be migrated. Mutually exclusive with lpar_name.
    - pool_id (optional, int) – ID of the shared processor pool to use on the destination managed system. Mutually exclusive with pool_name.
    - pool_name (optional, str) – Name of the shared processor pool to use on the destination managed system. Mutually exclusive with pool_id.
- action (required, str)
  - `validate` – Validate a specified partition/s.
  - `migrate` – Migrate a specified partition/s from `src_system` to `dest_system`.
  - `recover` – Recover a specified partition.
  - `authenticate` – Add SSH authentication key of remote management console.

## Notes
- All the actions support passwordless authentication.

## Examples
```yaml
- name: Validate that the input partitions can be migrated to the destination
  powervm_lpar_migration:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    src_system: <managed_system_name>
    dest_system: <destination_managed_system>
    vm_names:
      - <vm_name1>
      - <vm_name2>
    action: validate

- name: Recover specifed vm_id from migration failure
  powervm_lpar_migration:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    src_system: <managed_system_name>
    vm_ids:
      - <id1>
    action: recover

- name: Migrate all partitions of the cec to remote HMC
  powervm_lpar_migration:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    src_system: <managed_system_name>
    dest_system: <destination_system_name>
    remote_ip: <ipaddress of the remote HMC>
    all_vms: true
    action: migrate

- name: Migrate 2 partitions of the cec to another
  powervm_lpar_migration:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    src_system: <managed_system_name>
    dest_system: <destination_system_name>
    vm_ids:
      - <id1>
      - <id2>
    shared_proc_pool:
      - lpar_id: <id1>
        pool_id: <poolid1>
      - lpar_id: <id2>
        pool_id: <poolid2>
    action: migrate

- name: Adds SSH authentication key of remote HMC.
  powervm_lpar_migration:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    remote_ip: <IP Address of the remote HMC>
    remote_username: <Username of the remote HMC>
    remote_passwd: <Password of the remote HMC>
    action: authenticate
```

## Return Values
- system_info (always, dict)
  - Respective partition migration information.

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- Navinakumar Kandakur (@nkandak1)