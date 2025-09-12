# powervm_dlpar – Dynamically managing resources of partition

## Synopsis

Managing processor resources dynamically

Managing memory resources dynamically

Managing Storage resources dynamically

## Parameters

- hmc_host (required, str, default: None)
  - The IP Address or hostname of the HMC.

- hmc_auth (required, dict, default: None)
  - Username and Password credential of the HMC.
  - Fields:
    - username (required, str, default: None)
      - Username of the HMC to login.
    - password (optional, str, default: None)
      - Password of the HMC.

- system_name (required, str, default: None)
  - The name or mtms (machine type model serial) of the managed system.

- vm_name (required, str, default: None)
  - The name of the powervm partition.

- proc_settings (optional, dict, default: None)
  - Processor related settings.
  - Fields:
    - proc (optional, int, default: None)
      - The number of dedicated processors to create a partition.
      - If `proc_unit` parameter is set, then this value will work as virtual processors for shared processor setting.
    - proc_unit (optional, float, default: None)
      - The number of shared processing units to create a partition.
    - sharing_mode (optional, str, default: None)
      - The sharing mode of the partition.
      - Valid values for partitions using dedicated processors are `keep_idle_procs`, `share_idle_procs`, `share_idle_procs_active`, `share_idle_procs_always`.
      - Valid values for partitions using shared processors are `capped`, `uncapped`.
    - uncapped_weight (optional, int, default: None)
      - The uncapped weight of the partition.
    - pool_id (optional, int, default: None)
      - Shared Processor Pool ID to be set.

- mem_settings (optional, dict, default: None)
  - Memory related settings.
  - Fields:
    - mem (optional, int, default: None)
      - The value of dedicated memory value in megabytes to create a partition.

- timeout (optional, int, default: None)
  - The maximum time, in minutes, to wait for partition operating system to complete dlpar.
  - This option is valid for following actions `update_proc_mem`, `update_pv`, `update_npiv` and `update_vod`.

- pv_settings (optional, list, default: None)
  - List of Physical Volumes settings to be configured.
  - This option is valid only for `update_pv` action.
  - Item fields:
    - disk_name (required, str, default: None)
      - Name of the Disk.
    - vios_name (required, str, default: None)
      - Virtual IO Server name of the Disk belongs to.
    - target_name (optional, str, default: None)
      - Target Device name.
      - Optional, if not provided auto assigns `vtscsi*`.
    - server_adapter_id (optional, int, default: None)
      - The Server adapter slot number to be configured with SCSI adapter.
      - Optional, if not provided next available value will be assigned.
    - client_adapter_id (optional, int, default: None)
      - The client adapter slot number to be configured with SCSI adapter.
      - Optional, if not provided next available value will be assigned.

- npiv_settings (optional, list, default: None)
  - List of Virtual Fibre Channel port settings to be configured.
  - This option is valid only for `update_npiv` action.
  - Item fields:
    - fc_port_name (required, str, default: None)
      - Fibre Channel Port name.
    - vios_name (required, str, default: None)
      - Virtual IO Server name of the Fibre Channel Port belongs to.
    - wwpn_pair (optional, str, default: None)
      - The WWPN pair value to be configured with client FC adapter.
      - Both the WWPN value should be separated by semicolon delimiter example ‘c0507607577aefc0;c0507607577aefc1’.
      - Optional, if not provided the value will be auto assigned.
    - server_adapter_id (optional, int, default: None)
      - The Server adapter slot number to be configured with FC adapter.
      - Optional, if not provided next available value will be assigned.
    - client_adapter_id (optional, int, default: None)
      - The client adapter slot number to be configured with FC adapter.
      - Optional, if not provided next available value will be assigned.

- vod_settings (optional, list, default: None)
  - List of Virtual optical device settings to be configured.
  - This option is valid only for `update_vod` action.
  - Item fields:
    - device_name (required, str, default: None)
      - Name of the device.
    - vios_name (required, str, default: None)
      - Virtual IO Server name.
    - server_adapter_id (optional, int, default: None)
      - The Server adapter slot number to be configured.
      - Optional, if not provided next available value will be assigned.
    - client_adapter_id (optional, int, default: None)
      - The client adapter slot number to be configured.
      - Optional, if not provided next available value will be assigned.
    - media_name (optional, str, default: None)
      - Name of the media to be loaded.
      - Optional, if not provided no media will be loaded.

- action (required, str, default: None)
  - `update_proc_mem` updates the processor and memory resources of the partition.
  - `update_pv` Attach Physical Volumes via Virtual SCSI.
  - `update_npiv` Attach FC Port.
  - `update_vod` Attach Virtual Optical Device.

## Notes

- If the updating of settings for at least one VIOS is successful during the execution of the “update_pv” action, the changed status will be displayed as 1, and any failed updates will be shown as warnings. This behavior remains consistent for both the “update_npiv” and “update_vod” actions.
- Passwordless authentication is not supported.
- If the updating of settings for at least one VIOS is successful during the execution of the “update_pv” action, the changed status will be displayed as 1, and any failed updates will be shown as warnings. This behavior remains consistent for both the “update_npiv” and “update_vod” actions.

## Examples

```yaml
- name: Dynamically set the processor and memory values.
  powervm_dlpar:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <server name/mtms>
    vm_name: <vm name>
    proc_settings:
      proc: 3
      proc_unit: 2.5
      sharing_mode: 'uncapped'
      uncapped_weight: 131
      pool_id: 2
    mem_settings:
      mem: 3072
    action: update_proc_mem

- name: Dynamically configure Physical Volume settings on Lpar.
  powervm_dlpar:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <server name/mtms>
    vm_name: <vm name>
    pv_settings:
      - vios_name: <vios1>
        disk_name: <hdiskA>
      - vios_name: <vios2>
        disk_name: <hdiskB>
        target_name: <TargetName>
      - vios_name: <vios1>
        disk_name: <hdiskC>
        target_name: <TargetName>
        server_adapter_id: <Adapter_ID>
        client_adapter_id: <Adapter_ID>
    action: update_pv

- name: Dynamically configure NPIV settings on Lpar.
  powervm_dlpar:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <server name/mtms>
    vm_name: <vm name>
    npiv_settings:
      - vios_name: '<VIOS_NAME1>'
        fc_port_name: 'fcs0'
        wwpn_pair: <wwpn1>;<wwpn2>
        client_adapter_id: 6
        server_adapter_id: 9
      - vios_name: '<VIOS_NAME2>'
        fc_port_name: 'fcs0'
        client_adapter_id: 9
        server_adapter_id: 15
    action: update_npiv

- name: Dynamically configure Virtual Optical Disk settings on Lpar.
  powervm_dlpar:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <server name/mtms>
    vm_name: <vm name>
    vod_settings:
      - vios_name: '<VIOS_Name1>'
        device_name: '<device_name1>'
        media_name: '<media_name1>'
      - vios_name: '<VIOS_Name2>'
        device_name: '<device_name2>'
        client_adapter_id: 9
        server_adapter_id: 15
    action: update_vod
```

## Return Values

- partition_info (always, dict)
  - Return the attributes of the partition.

## Status

- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors

- Anil Vijayan (@AnilVijayan)
- Navinakumar Kandakur (@nkandak1)