# platform_update – Applies consolidated system firmware (update/upgrade), VIOS, SR-IOV, and I/O adapter updates, including optional partition migration.

- Synopsis
- Requirements
- Parameters
- Notes
- Examples
- Return Values
- Status
- Authors

## Synopsis

This module performs update and upgrade for various system components as part of system maintenance or automation workflows. It supports:
- System Firmware update and upgrade
- VIOS and I/O Adapters update only
- SR-IOV Adapters update based on supported system firmware levels
- Logical Partition migration

All update and upgrade can be performed independently or combined in a single consolidated update operation. Supports `state=facts` to retrieve information about available adapters without making any changes.

## Requirements

The below requirements are needed on the host that executes this module.

- Python >= 3.9

## Parameters

- `hmc_host` (required, str)
  - IP address or hostname of the target Hardware Management Console (HMC).

- `hmc_auth` (required, dict)
  - Authentication credentials to connect to the HMC.
  - `username` (required, str)
    - Username for logging into the HMC.
  - `password` (optional, str)
    - Password for the HMC user.

- `system_name` (required, str)
  - The name or mtms (machine type model serial) of the managed system on which the operations are to be performed.

- `platform_config` (optional, dict)
  - Defines the configuration for the operation to be performed, such as system firmware update/upgrade (including SR-IOV adapter updates) or VIOS updates (including I/O adapter updates). Also supports performing partition migrations.

  - `system_firmware_update` (optional, dict)
    - System firmware update/upgrade configuration.
    - `update_type` (optional, str)
      - Type of firmware update/upgrade operation.
      - `NoUpdate`: System firmware update/upgrade is skipped, but SR-IOV adapter updates are still allowed.
      - `Update`: Applies an update.
      - `Upgrade`: Applies an upgrade.
      - When set to `Update` or `Upgrade`, the `sriov_adapter_update` will be implicit.
      - When set to `NoUpdate`, the fields `repository` and `level` are not required.
    - `update_order` (optional, int)
      - Priority order in which the update/upgrade should be applied.
    - `repository` (optional, str, default: IBMWebsite)
      - Specifies the source repository for the update image.
      - Currently only supports `IBMWebsite`.
    - `level` (optional, str, default: latest)
      - Specifies the firmware version level to apply. If not provided, the latest available version will be used.
    - `sriov_adapter_update` (optional, list)
      - List of SR-IOV adapter update configurations.
      - This option must not be provided if `update_type` is set to `Update` or `Upgrade` in `system_firmware_update`.
      - Items:
        - `all` (optional, bool)
          - Indicates whether the update should be applied to all adapters. If `true`, `adapter_id` is not required.
        - `adapter_id` (optional, int)
          - ID of the specific adapter to be updated. Required only when `all` is not specified.
        - `subtype` (optional, str)
          - Specifies the level of update to apply.
          - `DriverOnly`: perform only the driver update.
          - `Adapter`: perform both the adapter firmware and driver updates.

  - `partition_migration` (optional, dict)
    - Configuration for migrating logical partitions.
    - This option cannot be used alone. Must be specified along with either `vios_update` or `system_firmware_update`.
    - `is_quick_evac` (optional, bool)
      - Indicates whether to perform a quick evacuation during partition migration. Must always be set to `true` when performing partition migration.
    - `destination_managed_system` (optional, str)
      - Target managed system name.
    - `leave_partition_in_target` (optional, bool, default: False)
      - Whether to keep the partition in the target after platform update.

  - `vios_update` (optional, list)
    - Configuration for updating Virtual I/O Servers.
    - Items:
      - `update_type` (optional, str)
        - Specifies the type of VIOS update to be performed.
        - `NoUpdate`: No update will be applied to VIOS, but I/O adapter updates are still allowed.
        - `Update`: Applies a VIOS update using the provided configuration. The I/O adapter update is performed implicitly.
        - When set to `NoUpdate`, the fields `resource_type` and `vios_image_name` are not required.
      - `vios_name` (optional, str)
        - Name of the VIOS partition.
      - `update_order` (optional, int)
        - Priority order in which the update should be applied.
      - `resource_type` (optional, str, default: IBMWebsite)
        - Specifies the source repository for the update image. Currently only supports `IBMWebsite`.
      - `vios_image_name` (optional, str)
        - Specifies the VIOS image name to apply. Required if `update_type` is `Update`.
      - `io_adapter_update` (optional, list)
        - List of I/O adapters to update during VIOS update.
        - Items:
          - `all` (optional, bool)
            - Indicates whether all I/O adapters should be updated. If `true`, `device` is not required.
          - `device` (optional, list of str)
            - List of I/O adapter device names to be updated (e.g., `['ent0', 'ent1']`). Required only when `all` is not specified.
          - `repository` (optional, str, default: IBMWebsite)
            - Specifies the source repository for the update image.

- `state` (optional, str)
  - `facts` gathers and returns information about available SR-IOV adapters, Virtual I/O Servers (VIOS), and I/O adapters without making any changes.

## Notes

- The current version supports only IBM Fix Central website as the update/upgrade source.
- Support for additional update/upgrade sources will be added in future releases.
- Supports defining the order in which update/upgrade are applied across components.
- To perform configuration operations, you do not need to specify a separate state or action. Supplying values under `platform_config` is sufficient to apply the changes directly to the HMC.
- When performing an update or upgrade operation via `IBMWebsite` with `level='latest'`, if the Ansible response status is `ok` and `changed` is `false`, and the result is `COMPLETED_WITH_ERROR` with the reason "update not available", it indicates that no newer update images are available or the target is already up-to-date.
- Module will not satisfy the idempotency requirement of Ansible, even though it partially confirms it. For instance, if the module is tasked to update/upgrade the HMC to the same level, it will still go ahead with the operation and finally the changed state will be reported as false.
- Upgrade the Power server after successfully evacuating the partition to the destination system, and ensure the partition is not returned to the original server.

## Examples

```yaml
- name: Update a SR-IOV adapters (DriverOnly) using IBM Fix Central
  platform_update:
    hmc_host: <host>
    hmc_auth:
      username: <hscroot>
      password: <hmcpass>
    system_name: <system_name>
    platform_config:
      system_firmware_update:
        update_type: NoUpdate
        update_order: 1
        sriov_adapter_update:
          - adapter_id: 1
            subtype: DriverOnly

- name: Update all SR-IOV adapters (Adapter) using IBM Fix Central (No Firware Update)
  platform_update:
    hmc_host: <host>
    hmc_auth:
      username: <hscroot>
      password: <hmcpass>
    system_name: <system_name>
    platform_config:
      system_firmware_update:
        update_type: NoUpdate
        update_order: 1
        sriov_adapter_update:
          - all: true
            subtype: Adapter

- name: Perform a System Firmware update using default level
  platform_update:
    hmc_host: <host>
    hmc_auth:
      username: <hscroot>
      password: <hmcpass>
    system_name: <system_name>
    platform_config:
      system_firmware_update:
        update_type: Update
        update_order: 1

- name: Perform a System Firmware update using specified level (level 12)
  platform_update:
    hmc_host: <host>
    hmc_auth:
      username: <hscroot>
      password: <hmcpass>
    system_name: <system_name>
    platform_config:
      system_firmware_update:
        update_type: Update
        update_order: 1
        level: 12

- name: Migrate a partition to a different managed system and perform a System Firmware update
  platform_update:
    hmc_host: <host>
    hmc_auth:
      username: <hscroot>
      password: <hmcpass>
    system_name: <system_name>
    platform_config:
      system_firmware_update:
        update_type: Update
        update_order: 1
        repository: IBMWebsite
      partition_migration:
        is_quick_evac: true
        destination_managed_system: "p920_system"
        leave_partition_in_target: true

- name: Update VIOS to latest available level from IBM Fix Central
  platform_update:
    hmc_host: <host>
    hmc_auth:
      username: <hscroot>
      password: <hmcpass>
    system_name: <system_name>
    platform_config:
      vios_update:
        - update_type: Update
          vios_name: "vios1"
          vios_image_name: "name"
          update_order: 1
          resource_type: IBMWebsite

- name: Update selected I/O adapters only (no VIOS update)
  platform_update:
    hmc_host: <host>
    hmc_auth:
      username: <hscroot>
      password: <hmcpass>
    system_name: <system_name>
    platform_config:
      vios_update:
        - update_type: NoUpdate
          vios_name: <vios1>
          update_order: 1
          repository: IBMWebsite
          io_adapter_update:
            - device:
                - "ent0"
                - "ent1"
              repository: IBMWebsite

- name: Update VIOS to specific image and all I/O adapters from IBM Fix Central
  platform_update:
    hmc_host: <host>
    hmc_auth:
      username: <hscroot>
      password: <hmcpass>
    system_name: <system_name>
    platform_config:
      vios_update:
        - update_type: NoUpdate
          vios_name: <vios1>
          update_order: 1
          resource_type: IBMWebsite
          io_adapter_update:
            - all: true
              repository: IBMWebsite

- name: Update multiple VIOS instances to the latest available level from IBM Fix Central with vios1 update first and then vios2
  platform_update:
    hmc_host: <host>
    hmc_auth:
      username: <hscroot>
      password: <hmcpass>
    system_name: <system_name>
    platform_config:
      vios_update:
        - update_type: Update
          vios_name: <vios1>
          update_order: 1
          vios_image_name: "name"
          resource_type: IBMWebsite
        - update_type: Update
          vios_name: <vios2>
          update_order: 2
          vios_image_name: <name>
          resource_type: IBMWebsite

- name: Updates System Firmware To latest and Vios to latest available level along with all I/O adapters from IBM Fix Central
  platform_update:
    hmc_host: <host>
    hmc_auth:
      username: <hscroot>
      password: <hmcpass>
    system_name: <system_name>
    platform_config:
      system_firmware_update:
        update_type: Update
        update_order: 1
        repository: IBMWebsite
      vios_update:
        - update_type: Update
          vios_name: <vios1>
          update_order: 1
          vios_image_name: "name"
          resource_type: IBMWebsite
          io_adapter_update:
            - all: true
              repository: IBMWebsite

- name: Facts
  platform_update:
    hmc_host: <host>
    hmc_auth:
      username: <hscroot>
      password: <hmcpass>
    system_name: <system_name>
    state: facts
```

## Return Values

- `result` (always, dict, e.g., {"changed": true, "command_output": {"Key1": "Value1", "Key2": "Value2", "...": "..."}})
  - Dictionary containing the outcome of the operation. Always includes `changed` indicating if the operation made any changes. The `command_output` key contains a dictionary with operation-specific details. The keys and values in `command_output` depend on the type of operation performed.

## Status

- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors

- Chiranthan M V (@chiranthanmv)