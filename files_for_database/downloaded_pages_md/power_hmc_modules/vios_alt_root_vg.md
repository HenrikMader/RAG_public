# vios_alt_root_vg – Create/Cleanup an alternate rootvg disk on a VIOS

## Synopsis
Copy the rootvg to an alternate disk.

Cleanup an existing alternate disk copy.

## Requirements
The below requirements are needed on the host that executes this module.

- Python >= 3

## Parameters
- hmc_host (required, str): The IP Address or hostname of the HMC.
- hmc_auth (required, dict): Username and Password credential of the HMC.
  - username (required, str): Username of the HMC to login.
  - password (optional, str): Password of the HMC.
- system_name (optional, str): The name or mtms (machine type model serial) of the managed system.
- vios_name (optional, str): The name of the VirtualIOServer.
- targets (optional, list):
  - Provided with `copy`, an alternate rootvg will be created on these targets.
  - Provided with `clean`, it removes the owning volume manager from the target disk(s).
- disk_size_policy (optional, str): When state=copy, specifies how to choose the alternate disk if targets is not specified.
  - `minimize` smallest disk that can be selected.
  - `upper` first disk found bigger than the rootvg disk.
  - `lower` disk size less than rootvg disk size but big enough to contain the used physical partitions.
  - `nearest` disk size closest to the rootvg disk.
- force (optional, bool, default: False): Forces removal of any existing alternate disk copy on target disks. Valid only for state = `copy`.
- state (optional, str):
  - `copy` to create alternate rootvg disk.
  - `clean` to cleanup an existing alternate disk copy.

## Notes
- This module requires the HMC login user to have specific permissions. To achieve this, the user should create a task role based on hmcsuperadmin with additional permissions, including ViosAdminOp, VirtualIOServerCommand and other permissions for managing lpar and cec resources. The following example demonstrates the same.
- Create a task role with above mentioned additional permissions using the following command:
```bash
mkaccfg -t taskrole -i name=new_task_role,parent=hmcsuperadmin, resources=lpar:ActivateLPAR+CapturePartitionTemplate+ChangeLPARProperty+ ChangeNPortLogin+ChangeProfileProperty+CloseVTerm+Connect5250VTerm+ CreateProfile+Delete5250VTerm+DeleteLPAR+DeleteProfile+DisableEnableVirtualEthernet+ DlparOperation+HibernateLPAR+ListLPARProperty+ListProfileProperty+ManageLPARDebugData+ ManageLPARServEvents+ManageLicenseKeys+ManageProfile+MigrateLPAR+ Open5250VTerm+OpenVTerm+PartProfileCopy+RRStartLPAR+RebootLPAR+RemoteRestartLPAR+ ShutdownLPAR+VirtualIOServerCommand+ViosAdminOp, cec:ActivateSystemProfile+BackupProfileData+CECPowerOff+CECPowerOn+ CaptureSystemTemplate+ChangeCECPassword+ChangeCECProperty+ChangeCoD+ChangePowerManagement+ ChangeSnmpAlerts+ChangeSystemConnectionProperty+ChangeSystemProfileProperty+ ChangeTrustedSystemKey+ChangeVETCode+CoDPoolManagement+CollectCECVPDInfo+ ConfigProcessorRecovery+CreateLPAR+CreatePassThruCommand+CreateSystemProfile+ DLPARRestoreHWResources+DeleteSystemProfile+DeployPartitionTemplate+DeploySystemPlan+ DeploySystemTemplate+DeviceMaintenance+DisconnectOtherHmc+EditCECMTMS+ InitializeProfileData+InitializeSPFailover+LSProfileSpace+LaunchAsm+ ListCECProperty+ListCoDInformation+ListCoDNotifications+ListNPortLogin+ ListPCIeTopology+ListRioTopology+ListSSP+ListSnmpAlerts+ListSystemProfileProperty+ ListTrustedSystemKey+ListUtilizationData+ListVETInfo+MakeSystemPlan+ ManageCECServEvents+ManageCoDNotifications+ManageDumps+ ManageSPP+ManageSSP+ManageSriovAdapter+ManageSysProfile+ManageUtilizationData+ ManageVirtualNetwork+ManageVirtualStorage+MoveSriovAdapter+PartitionConfigurationImage+ RebuildCEC+RecoverPartitionData+RemoveCECConnection+RemoveCEConnection+RemoveProfileData+ RestoreProfileData+SetCECKeylockPosition+SysProfileCopy+UpdateLIC+ValidateSystemProfile+ ViewDumps+ViewPowerManagement+ViewSPP
```
- Create a user with the above created task role.

## Examples
```yaml
- name: Copy the rootvg to an alternate disk hdsik1
  vios_alt_root_vg:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth: "{{ curr_hmc_auth }}"
    system_name: <system-name>
    vios_name: <vios-name>
    targets:
         - hdisk1
    state: copy

- name: Copy the rootvg to multiple disks hdisk1 and hdisk2
  vios_alt_root_vg:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth: "{{ curr_hmc_auth }}"
    system_name: <system-name>
    vios_name: <vios-name>
    targets:
         - hdisk1
         - hdisk2
    state: copy

- name: Copy the rootvg using minimize disk_size_policy
  vios_alt_root_vg:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth: "{{ curr_hmc_auth }}"
    system_name: <system-name>
    vios_name: <vios-name>
    disk_size_policy: minimize
    state: copy

- name: Cleanup an existing alternate disk
  vios_alt_root_vg:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth: "{{ curr_hmc_auth }}"
    system_name: <system-name>
    vios_name: <vios-name>
    state: clean
```

## Return Values
- alt_rootvg_info (dict, on success for copy rootvg): Respective alt_rootvg_info information.

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- Sreenidhi S (@SreenidhiS1)