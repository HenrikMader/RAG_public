# power_system – PowerOn, PowerOff, modify_syscfg, modify_hwres, facts of the Managed system

## Synopsis
- Poweron specified managed system
- Poweroff specified managed system
- Modify System configuration of the specified managed system with specified configuration details
- Modify hardware resource of the specified managed system with specified hardware resource details
- Get the facts of the specified managed system
- Enable and Disable PCM metrics

## Parameters
- hmc_host (required, str, default: None)
  - The IP address or hostname of the HMC.

- hmc_auth (required, dict, default: None)
  - Username and Password credential of the HMC.
  - username (required, str, default: None)
    - Username of the HMC to login.
  - password (optional, str, default: None)
    - Password of the HMC.

- system_name (required, str, default: None)
  - The name or mtms (machine type model serial) of the managed system.

- new_name (optional, str, default: None)
  - The new name to be configured on specified system_name.
  - This option works with `modify_syscfg` action.

- power_off_policy (optional, int, default: None)
  - Power off policy to be configured on specified system_name.
  - This option works with `modify_syscfg` action.
  - Configuring this option to ‘1’ will power off the Managed System after all partitions are shutdown.

- power_on_lpar_start_policy (optional, str, default: None)
  - Power on partition start policy to be configured on specified system_name for the next system restart.
  - This option works with `modify_syscfg` action.

- requested_num_sys_huge_pages (optional, int, default: None)
  - Configures the number of pages of huge page memory.
  - User can change this value only when the managed system is powered off.
  - This option works with `modify_hwres` action.

- mem_mirroring_mode (optional, str, default: None)
  - Configures the memory mirroring mode on specified system_name for the next system poweron or system restart.
  - User can use this option only on managed systems which support memory mirroring.
  - This option works with `modify_hwres` action.

- pend_mem_region_size (optional, str, default: None)
  - Configures the memory region size setting on specified system_name.
  - Choices are in MB.
  - This option works with `modify_hwres` action.

- metrics (optional, list, default: None)
  - Provides five types of utilization data: Long Term Monitor (LTM), Short Term Monitor (STM), Aggregated metrics (AM), ComputeLTM (CLTM), EnergyMonitor (EM).
  - AM collects data from LTM and EM, hence when the AM is enabled automatically LTM and EM will be enabled.
  - When LTM or EM is disabled then automatically the AM will also get disabled.
  - This option works only with `enable_pcm` and `disable_pcm` action.

- action (optional, str, default: None)
  - `poweroff` poweroff a specified system_name.
  - `poweron` poweron a specified system_name.
  - `modify_syscfg` Makes system configurations of specified system_name.
  - `modify_hwres` Makes hardware resource configurations of specified system_name.
  - `enable_pcm` Enables the Performance and Capacity Monitoring for specified types of utilization data.
  - `disable_pcm` Disables the Performance and Capacity Monitoring for specified types of utilization data.

- state (optional, str, default: None)
  - `facts` fetch details of specified system_name
  - `pcm_facts` fetch Performance and Capacity Monitoring details of specified system_name

## Notes
- Note: All operations except facts support passwordless authentication.

## Examples
```yaml
- name: poweroff managed system
  power_system:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_system_name/mtms>
    action: poweroff

- name: poweron managed system
  power_system:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_sysystem_name/mtms>
    action: poweron

- name: modify managed system name, powerOn lpar start policy and powerOff policy
  power_system:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_system_name/mtms>
    new_name: <system_name_to_be_changed>
    power_off_policy: '1'
    power_on_lpar_start_policy: autostart
    action: modify_syscfg

- name: modify managed system memory settings
  power_system:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_system_name/mtms>
    requested_num_sys_huge_pages: <sys_huge_pages_to_be_set>
    mem_mirroring_mode: sys_firmware_only
    pend_mem_region_size: auto
    action: modify_hwres

- name: fetch the managed system details
  power_system:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_system_name/mtms>
    state: facts

- name: Fetch facts about monitoring metrics
  power_system:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_system_name/mtms>
    state: pcm_facts

- name: enable the long-term monitoring
  power_system:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_system_name/mtms>
    metrics:
      - LTM
    action: enable_pcm

- name: disable the short-term monitoring
  power_system:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_system_name/mtms>
    metrics:
      - STM
    action: disble_pcm
```

## Return Values
- system_info (always, dict)
  - Respective System information

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- Anil Vijayan (@AnilVijayan)
- Navinakumar Kandakur (@nkandak1)