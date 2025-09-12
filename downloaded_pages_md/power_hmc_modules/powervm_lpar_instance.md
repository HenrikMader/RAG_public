# powervm_lpar_instance – Create, Delete, Shutdown, Activate, Restart, Facts and Install of PowerVM Partitions

## Synopsis
- Creates AIX/Linux or IBMi partition with specified configuration details on a system
- Deletes specified AIX/Linux or IBMi partition on a system
- Shutdown specified AIX/Linux or IBMi partition on a system
- Power on/Activate specified AIX/Linux or IBMi partition, with provided configuration details on a system
- Restart specified AIX/Linux or IBMi partition on a system
- Facts of the specified AIX/Linux or IBMi partition on a system
- Install of PowerVM Partition

## Requirements
The below requirements are needed on the host that executes this module.
- Python >= 3
- lxml

## Parameters
- hmc_host (required, str)
  - IP address or hostname of the HMC.

- hmc_auth (required, dict)
  - Username and Password credential of the HMC.
  - username (required, str): HMC username.
  - password (optional, str): HMC password.

- system_name (optional, str)
  - The name or mtms (machine type model serial) of the managed system.
  - Optional for state=absent, state=facts, action=poweron, action=shutdown and action=restart.

- vm_name (required, str)
  - The name of the powervm partition.

- force (optional, bool)
  - Force deletion of a partition.
  - Delete a partition that is not in off state.

- vm_id (optional, int)
  - The partition ID to be set while creating a Logical Partition.
  - Optional; if not provided, next available value will be assigned.

- proc (optional, int)
  - The number of dedicated processors to create a partition.
  - If `proc_unit` is set, then this value will work as virtual processors for shared processor setting.
  - Default: 2. This will not work during shared processor setting.

- max_proc (optional, int)
  - The maximum number of dedicated processors to create a partition.
  - If `proc_unit` is set, then this value will work as max virtual processors for shared processor setting.
  - Default: proc.
  - Must be >= proc.

- min_proc (optional, int)
  - The minimum number of dedicated processors to create a partition.
  - If `proc_unit` is set, then this value will work as min virtual processors for shared processor setting.
  - Default: 1.
  - Must be <= proc.

- proc_unit (optional, float)
  - The number of shared processing units to create a partition.

- shared_proc_pool (optional, str)
  - Shared Processor Pool ID or Name.
  - If a numeric value is provided, it is considered as Shared Processor Pool ID.
  - Use only with `proc_unit`.
  - Default: DefaultPool.

- max_proc_unit (optional, float)
  - The maximum number of shared processing units to create a partition.
  - Must be >= `proc_unit`.
  - Use only with `proc_unit`.
  - Default: proc_unit.

- min_proc_unit (optional, float)
  - The minimum number of shared processing units to create a partition.
  - Must be <= `proc_unit`.
  - Use only with `proc_unit`.
  - Default: 0.1.

- proc_mode (optional, str)
  - The processor mode to be used to create a partition with shared processor settings.
  - Use only with `proc_unit`.
  - Default: uncapped.

- weight (optional, int)
  - The weight to be used for uncapped proc mode while creating a partition with shared processor settings.
  - Default: 128.
  - Ignored if `proc_mode` is capped.
  - Use only with `proc_mode`.

- proc_compatibility_mode (optional, str)
  - The processor compatibility mode to be configured while creating a partition.

- mem (optional, int)
  - Dedicated memory in MB to create a partition.
  - Default: 2048.

- max_mem (optional, int)
  - Maximum dedicated memory in MB to create a partition.
  - Default: 2048.
  - Can only be used with `mem`.

- min_mem (optional, int)
  - Minimum dedicated memory in MB to create a partition.
  - Default: 1024.
  - Can only be used with `mem`.

- os_type (optional, str)
  - Type of logical partition to be created.
  - `aix_linux` or `linux` or `aix` for AIX or Linux operating system.
  - `ibmi` for IBMi operating system.

- prof_name (optional, str)
  - Partition profile to be used to activate a partition.
  - If not provided, the current configuration of the partition will be used for activation.
  - Only for action=poweron.

- keylock (optional, str)
  - The keylock position to be set while activating a partition.
  - If not provided, the current setting will be used.
  - Only for action=poweron.

- iIPLsource (optional, str)
  - The initial program load (IPL) source to be used while activating an IBMi partition.
  - If not provided, current setting will be used.
  - If provided for AIX/Linux partition, it will warn and ignore.
  - Only for action=poweron.

- volume_config (optional, list)
  - Storage volume configurations of a partition.
  - Attach Physical Volumes via Virtual SCSI.
  - Redundant paths created by default if the physical volume is visible in more than one VIOS.
  - Provide either volume_size or both volume_name and vios_name. If volume_size is provided, an available physical volume matching or greater than specified size will be attached.
  - Suboptions:
    - volume_name (optional, str): Physical volume name visible through VIOS. Mutually exclusive with volume_size.
    - vios_name (optional, str): VIOS name where volume_name is present. Mutually exclusive with volume_size.
    - volume_size (optional, int): Physical volume size in MB.

- virt_network_config (optional, list)
  - Virtual Network configuration of the partition.
  - Implicitly adds a Virtual Ethernet Adapter with given virtual network to the partition.
  - Ensure provided Virtual Network is attached to an active Network Bridge for external communication.
  - Suboptions:
    - network_name (required, str): Name of the Virtual Network to attach.
    - slot_number (optional, int): Virtual slot number to attach the virtual network. If not provided, next available is assigned.

- npiv_config (optional, list)
  - Configure NPIV (Virtual Fibre) for the partition.
  - You can provide two FC port configurations and mappings will be created with VIOS implicitly.
  - Suboptions:
    - vios_name (required, str): Name of the VIOS in which FC port is available.
    - fc_port (required, str): Port to be used for NPIV. Port name or fully qualified location code.
    - wwpn_pair (optional, str): WWPN pair for the client FC adapter. Two WWPNs separated by semicolon. If not provided, auto-assigned.
    - client_adapter_id (optional, int): Client adapter slot number. If not provided, next available is assigned.
    - server_adapter_id (optional, int): Server adapter slot number. If not provided, next available is assigned.

- all_resources (optional, bool)
  - Create a partition with all the resources available in the managed system.
  - If true, ensure all partitions are shutdown (if any exist on the system).
  - Default: false.

- max_virtual_slots (optional, int)
  - Maximum virtual slot configuration of the partition.
  - Default: 20 (if not provided).

- physical_io (optional, list)
  - Physical IO adapter(s) to be added to the partition.
  - Example IO location code pattern: XXXXX.XXX.XXXXXXX-P1-T1 or P1-T1.

- retain_vios_cfg (optional, bool)
  - Do not remove VIOS configuration (server adapters, storage mappings associated with the partition) when deleting the partition.
  - Applicable only for state=absent.
  - Default: false (remove associated VIOS config on delete).

- delete_vdisks (optional, bool)
  - Delete the Virtual Disks associated with the partition when deleting the partition.
  - Default: false.

- advanced_info (optional, bool)
  - Display advanced information of the logical partition.
  - Applicable only for state=facts.
  - Default: false.
  - Currently shows only NPIV storage details.

- install_settings (optional, dict)
  - Settings for installing Operating System on a logical partition.
  - Requires NIM Server with pull install configuration.
  - Suboptions:
    - vm_ip (required, str): IP address to configure on the Logical Partition.
    - nim_ip (required, str): IP address of the NIM Server.
    - nim_gateway (required, str): Gateway IP address for the Logical Partition.
    - nim_subnetmask (required, str): Subnet mask IP address for the Logical Partition.
    - location_code (optional, str): Network adapter location code to use while installing AIX OS. If not provided, automatically picks the first pingable adapter attached to the partition.
    - vm_mac (optional, str): MAC address of LPAR. Used when installing Linux OS on LPAR.
    - nim_vlan_id (optional, str): VLAN ID (0–4094) for tagging during network install. Default: 0.
    - nim_vlan_priority (optional, str): VLAN priority (0–7) for tagging during network install. Default: 0.
    - timeout (optional, int): Max waiting time in minutes for OS to fully boot. Minimum > 10. Default: 60.

- vnic_config (optional, list)
  - Virtual NIC configuration of the partition.
  - Suboptions:
    - vnic_adapter_id (optional, int): VNIC Adapter ID. If not provided, next available is assigned.
    - allowed_vlanids (optional, str):
      - Controls whether the virtual NIC accepts packets with any VLAN ID.
      - Values: `All`, `None`, or comma-separated VLAN IDs (2–4094). Max 20 VLAN IDs.
      - Default: `All`.
      - If `allowed_vlanids` is `All`, `allowed_macaddr` must also be `All`. If `None`, `allowed_macaddr` must be `None` or a comma-separated list of MAC addresses.
    - allowed_macaddr (optional, str):
      - Controls whether the virtual NIC accepts packets with any valid MAC address.
      - Values: `All`, `None`, or comma-separated MAC addresses. Max 4 MAC addresses.
      - Default: `All`.
      - Must align with `allowed_vlanids` as described above.
    - port_vlan_id (optional, int):
      - Port VLAN ID within range supported by the SR-IOV physical port backing device.
      - Value 0 or 2–4094.
      - Default: 0.
    - port_vlan_priority (optional, int):
      - Priority for frames in a VLAN network, 0–7.
      - Default: 0.
    - backing_devices (optional, list):
      - SR-IOV physical ports used as backing devices for VNIC.
      - If not provided, selects an SR-IOV physical port with link status up by default; otherwise randomly picks a port with capacity > 2.0%.
      - Suboptions:
        - location_code (required, str): SR-IOV physical port location code (e.g., XXXXX.XXX.XXXXXXX-P1-T1 or P1-T1).
        - capacity (optional, float): Capacity for VNIC backing device. Default: 2.0%.
        - hosting_partition (optional, str): VIOS name on which SR-IOV physical port location code is configured. Default: random VIOS with RMC state active.

- shutdown_option (optional, str)
  - Option to shutdown Logical Partition.
  - Only for action=shutdown.
  - Default: Delayed.

- restart_option (optional, str)
  - Option to reboot Logical Partition.
  - Only for action=restart.
  - Default: Immediate.

- state (optional, str)
  - `present`: creates a partition of the specified os_type, vm_name, proc and memory on specified system_name.
  - `absent`: deletes a partition of the specified vm_name.
  - `facts`: fetches the details of the specified vm_name on specified system_name.

- action (optional, str)
  - `shutdown`: shutdown a partition of the specified vm_name on specified system_name.
  - `poweron`: power on a partition of the specified vm_name with specified prof_name, keylock, iIPLsource on specified system_name.
  - `restart`: restart a partition of the specified vm_name on specified system_name.
  - `install_os`: install AIX/Linux OS through NIM Server on specified vm_name.

## Notes
- The network configuration currently does not support SR-IOV configurations.
- retain_vios_cfg and delete_vdisks are supported only from HMC V9 R1 M930 or later.
- Partition creation is not supported for resource role-based users in HMC versions prior to 951.
- action=install_os does not support installation of IBMi OS.
- Only state=absent and action=install_os operations support passwordless authentication.
- install_settings suboption “location_code” supports AIX installation; “vm_mac” supports Linux installation on LPAR.

## Examples
```yaml
- name: Create an IBMi logical partition instance with shared proc, volume_config's vios_name and volume_name values, PhysicaIO and
        max_virtual_slots.
  powervm_lpar_instance:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      system_name: <system_name/mtms>
      vm_name: <vm_name>
      vm_id: <lpar_id>
      proc: 4
      proc_unit: 4
      mem: 20480
      volume_config:
          - vios_name: <viosname1>
            volume_name: <volumename1>
          - vios_name: <viosname2>
            volume_name: <volumename2>
      physical_io:
          - <physicalIO location code>
          - <physicalio location code>
      max_virtual_slots: 50
      os_type: ibmi
      state: present

- name: Create an AIX/Linux logical partition instance with default proc, mem, virt_network_config, volume_config's volumes_size and
        npiv_config, vnic_config.
  powervm_lpar_instance:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      system_name: <system_name/mtms>
      vm_name: <vm_name>
      volume_config:
          - volume_size: <disk_size>
          - volume_size: <disk_size>
      virt_network_config:
          - network_name: <virtual_nw_name>
            slot_number: <client_slot_no>
      npiv_config:
          - vios_name: <viosname>
            fc_port: <fc_port_name/loc_code>
            wwpn_pair: <wwpn1;wwpn2>
      vnic_config:
          - vnic_adapter_id: <vnic_adapter_id>
            backing_devices:
                - location_code: XXXXX.XXX.XXXXXXX-P1-T1
                  capacity: <capacity>
                  hosting_partition: <vios_name>
                - location_code: P1-T2
          - backing_devices:
                - location_code: P1-T3
                  hosting_partition: <vios_name>
                - location_code: P1-T4
                  capacity: <capacity>
          - vnic_adapter_id: <vnic_adapter_id>
      os_type: aix_linux
      state: present

- name: Delete a logical partition instance with retain_vios_cfg and delete_vdisk options.
  powervm_lpar_instance:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      system_name: <system_name/mtms>
      vm_name: <vm_name>
      retain_vios_cfg: true
      delete_vdisks: true
      state: absent

- name: Shutdown a logical partition.
  powervm_lpar_instance:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      system_name: <system_name/mtms>
      vm_name: <vm_name>
      action: shutdown

- name: Activate an AIX/Linux logical partition with user defined profile_name.
  powervm_lpar_instance:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      system_name: <system_name/mtms>
      vm_name: <vm_name>
      prof_name: <profile_name>
      action: poweron

- name: Activate IBMi based on its current configuration with keylock and iIPLsource options.
  powervm_lpar_instance:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      system_name: <system_name/mtms>
      vm_name: <vm_name>
      keylock: 'normal'
      iIPLsource: 'd'
      action: poweron

- name: Create a partition with all resources.
  powervm_lpar_instance:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      system_name: <system_name/mtms>
      vm_name: <vm_name>
      all_resources: true
      os_type: aix_linux
      state: present

- name: Install Aix OS on LPAR from NIM Server.
  powervm_lpar_instance:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth: "{{ curr_hmc_auth }}"
      system_name: <system_name/mtms>
      vm_name: <vm_name>
      install_settings:
          vm_ip: <IP_address of the lpar>
          nim_ip: <IP_address of the NIM Server>
          nim_gateway: <Gateway IP_Addres>
          nim_subnetmask: <Subnetmask IP_Address>
      action: install_os

- name: Install Linux OS on LPAR from NIM Server.
  powervm_lpar_instance:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth: "{{ curr_hmc_auth }}"
      system_name: <system_name/mtms>
      vm_name: <vm_name>
      install_settings:
          vm_ip: <IP_address of the lpar>
          nim_ip: <IP_address of the NIM Server>
          nim_gateway: <Gateway IP_Addres>
          nim_subnetmask: <Subnetmask IP_Address>
          vm_mac: <mac address of lpar>
      action: install_os

- name: Create an AIX/Linux logical partition instance with allowed_vlanids,port_vlan_priority
  powervm_lpar_instance:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth: '{{ curr_hmc_auth }}'
      system_name: <system_name/mtms>
      vm_name: lpar_no
      proc: 0
      os_type: aix_linux
      vnic_config:
          - vnic_adapter_id: 5
            port_vlan_id: 5
            port_vlan_priority: 6
            allowed_vlanids: ALL
            backing_devices:
               - location_code: <location_code>
                 capacity: 20
                 hosting_partition: <vios_name>
      state: present
```

## Return Values
- partition_info (dict, on success for state=present)
  - The configuration of the partition after creation
  - Example:
    ```
    {
      "AllocatedVirtualProcessors": null,
      "AssociatedManagedSystem": "<system-name>",
      "CurrentMemory": 1024,
      "CurrentProcessingUnits": null,
      "CurrentProcessors": 1,
      "Description": null,
      "HasDedicatedProcessors": "true",
      "HasPhysicalIO": "true",
      "IsVirtualServiceAttentionLEDOn": "false",
      "LastActivatedProfile": "default_profile",
      "MemoryMode": "Dedicated",
      "MigrationState": "Not_Migrating",
      "OperatingSystemVersion": "Unknown",
      "PartitionID": 11,
      "PartitionName": "<partition-name>",
      "PartitionState": "not activated",
      "PartitionType": "AIX/Linux",
      "PowerManagementMode": null,
      "ProgressState": null,
      "RMCState": "inactive",
      "ReferenceCode": "",
      "RemoteRestartState": "Invalid",
      "ResourceMonitoringIPAddress": null,
      "SharingMode": "sre idle proces"
    }
    ```

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- Anil Vijayan (@AnilVijayan)
- Navinakumar Kandakur (@nkandak1)
- Sreenidhi (@SreenidhiS1)