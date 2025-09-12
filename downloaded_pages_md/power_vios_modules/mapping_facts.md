# mapping_facts – Returns the mapping between physical, logical, and virtual devices as facts

Contents
- Synopsis
- Requirements
- Parameters
- Examples
- Return Values
- Status
- Authors

## Synopsis

Returns information about the mapping between the virtual host adapters and the physical devices they are backed to.

## Requirements

The below requirements are needed on the host that executes this module.

- VIOS >= 2.2.5.0
- Python >= 2.7

## Parameters

- component (optional, str, default: all)
  - Specifies the type of devices to retrieve information for.
  - `vscsi` to list virtual SCSI devices.
  - `npiv` to list NPIV devices.
  - `net` to list shared Ethernet adapters.
  - `vnic` to list server virtual NIC adapters.
  - `ams` to list paging space devices that are used in active memory sharing.
  - `suspend` to list suspended virtual adapters.
  - `cluster` to list shared storage pool mappings.
  - `all` to list all devices.

- vadapter (optional, str, default: None)
  - Specifies the device name of a server virtual adapter.
  - Mutually exclusive with physloc.

- physloc (optional, str, default: None)
  - Specifies the device physical location code of a server virtual adapter.
  - Mutually exclusive with vadapter.

- vtd (optional, str, default: None)
  - Specifies the active memory sharing (AMS) paging device to be displayed.

- hostname (optional, str, default: None)
  - Specifies the host name or IP address of the VIOS partition.

- cpid (optional, str, default: None)
  - Specifies the client partition ID, in decimal, for which to return device mapping information.
  - This option is only supported on certain VIOS levels.

- types (optional, list, default: None)
  - Specifies the type of devices to display. The following types are supported:
  - `disk` to list physical backing devices.
  - `lv` to list logical volume backing devices.
  - `optical` to list optical backing devices.
  - `tape` to list tape backed devices.
  - `file` to list file backed devices.
  - `file_disk` to list file backed disk devices.
  - `file_opt` to list file backed optical devices.
  - `cl_disk` to list clustered backing devices.
  - `usb_disk` to list USB disks.

## Examples

```yaml
- name: Gather the mapping facts
  mapping_facts:

- name: Print the mapping facts
  debug:
    var: ansible_facts.mappings

- name: Populate the mapping facts with the mapping information for
        NPIV device vfchost0
  mapping_facts:
    component: npiv
    vadapter: vfchost0

- name: Populate the mapping facts with the mapping information for
        optical backing devices
  mapping_facts:
    types: optical
```

## Return Values

- ansible_facts (always, complex)
  - Facts to add to ansible_facts about the mapping between physical, logical, and virtual devices.

  - mappings (success, dict)
    - Contains mappings for NPIV, VSCSI, SEA, VNIC, AMS, SSP and suspend.

    - npiv (always, dict)
      - Maps virtual fibre channel adapter name to backing information.
      - Fields:
        - clntid (always, int): Client logical partition ID.
        - clntname (when available, str): Client logical partition name.
        - clntos (when available, str): The operating system on the client logical partition.
        - fc (when available, str): Physical fibre channel adapter name.
        - fcphysloc (when available, str): The physical location of the fibre channel adapter.
        - flags (always, int): Virtual fibre channel adapter flags.
        - physloc (always, str): The physical location code of the server virtual fibre channel adapter.
        - ports (always, int): Physical fibre channel port number.
        - status (always, str): Virtual fibre channel adapter status.
        - vfcclient (when available, str): Client virtual fibre channel adapter name.
        - vfcclientdrc (when available, str): Client virtual fibre channel adapter used for DRC.

    - net (always, dict)
      - Maps virtual ethernet adapter name to backing information.
      - Fields:
        - backing (always, str): Backing device.
        - bdphysloc (when available, str): The physical location code of the backing device.
        - physloc (always, str): The physical location code of the server virtual adapter.
        - sea (when available, str): Shared Ethernet adapter.
        - status (when available, str): Shared Ethernet adapter status.

    - vscsi (always, dict)
      - Maps server virtual SCSI adapter name to backing information.
      - Fields:
        - clientid (always, int): Client partition ID, in decimal.
        - physloc (always, str): The physical location code of the server’s virtual adapter.
        - vtds (always, dict): Maps virtual target device name to backing information.
          - backing (always, str): Backing device.
          - bdphysloc (always, str): The physical location code of the backing device.
          - lun (always, str): Logical unit number.
          - mirrored (when available, bool): The backing device is part of a PPRC pair.
          - status (always, str): Virtual target device status.

    - vnic (always, dict)
      - Maps server virtual NIC adapter name to backing information.
      - Fields:
        - physloc (always, str): The physical location code of the server’s virtual adapter.
        - clntid (always, int): Client logical partition ID.
        - clntname (when available, str): Client logical partition name.
        - clntos (when available, str): The operating system on the client logical partition.
        - backing (always, str): Backing device.
        - status (always, str): Server Virtual NIC Adapter status.
        - bdphysloc (always, str): The physical location code of the backing device.
        - clntdev (when available, str): The device name on the client logical partition.
        - clntphysloc (always, str): The physical location code of the client’s virtual adapter.

    - ams (always, dict)
      - Maps paging virtual target device name to backing information.
      - Fields:
        - streamid (always, str): Stream ID.
        - clientid (always, int): Client logical partition ID (in decimal).
        - status (always, str): Paging virtual target device status.
        - redundancy (always, bool): Redundancy usage for the paging VIOS logical partitions.
        - backing (always, str): Backing device.
        - poolid (always, str): Memory pool ID.
        - vasi (when available, str): Virtual Asynchronous Services Interface (VASI) device name.
        - pager (when available, str): Pager device name.
        - vbsd (when available, str): Virtual Block Storage Device (VBSD) name.

    - suspend (always, dict)
      - Maps suspended virtual adapter name to backing information.
      - Fields:
        - state (always, str): Suspended virtual adapter state.
        - clientname (when available, str): Client name.
        - streamid (always, str): Stream ID.
        - clientid (always, int): Client partition ID (in decimal).
        - vtds (always, dict): Maps virtual target device name to backing information.
          - status (always, str): Virtual target device status.
          - lun (when available, str): Logical unit number.
          - backing (when available, str): Backing device.
          - bdphysloc (when available, str): The physical location code of the backing device.
          - mirrored (when available, bool): The backing device is part of a PPRC pair.

    - cluster (always, dict)
      - Maps physical location code of the server virtual adapter to backing information.
      - Fields:
        - clientid (when available, int): Client partition ID (in decimal).
        - vtds (always, dict): Maps virtual target device name to backing information.
          - backing (always, str): Backing device.
          - lun (always, str): Logical unit number.

## Status

- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors

- AIX Development Team (@pbfinley1911)