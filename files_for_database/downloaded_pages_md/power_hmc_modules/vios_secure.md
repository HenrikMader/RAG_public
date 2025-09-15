# vios_secure – Configures firewall settings and applies security hardening rules.

## Synopsis
- Applies security hardening rules.
- Configures and removes the firewall settings of the network.

## Requirements
The below requirements are needed on the host that executes this module.
- Python >= 3.9

## Parameters
- hmc_host (required, str, default: None)
  - The IP Address or hostname of the HMC.

- hmc_auth (required, dict, default: None)
  - Username and Password credential of the HMC.
  - username (required, str, default: None)
    - Username of the HMC to login.
  - password (optional, str, default: None)
    - Password of the HMC.

- system_name (required, str, default: None)
  - The name or mtms (machine type model serial) of the managed system.

- vios_name (required, str, default: None)
  - The name of the VirtualIOServer.

- file (optional, str, default: None)
  - Specifies the security rules file to be applied.
  - Mutually exclusive with level.
  - This option is only valid for `setting_security` state.

- rule (optional, str, default: None)
  - Specifies the name of the rule to be applied.
  - This option is only valid for `setting_security` state.

- level (optional, str, default: None)
  - Specifies the security level settings to choose.
  - Specifying `high` security level might cause stability or serviceability issues especially in a cluster environment.
  - Mutually exclusive with file.
  - This option is only valid for `setting_security` state.

- ip_version (optional, str, default: None)
  - Specifies the version for firewall state and rules.
  - This option is only valid for `setting_firewall` and `firewall_facts` state.

- active (optional, bool, default: None)
  - Specifies the state of the firewall.
  - This option is only valid for `setting_firewall` state.

- reload (optional, bool, default: None)
  - Specifies this option for deleting ODM rules and the default values are loaded from the /home/ios/security/viosecure.ctl file.
  - For enabling the firewall rules for first time this option is required along with `active` option.
  - This option is only valid for `setting_firewall` state.

- firewall_config (optional, list, default: None)
  - Specifies the firewall state and rules.
  - This option is only valid for `setting_firewall` state.
  - Each item:
    - port (required, int, default: None)
      - Specifies the port number or a service name from the `/etc/services` file.
      - All the IP activity to and from that local port is allowed.
    - interface (optional, str, default: None)
      - Specifies the network interface name.
    - remote (optional, bool, default: None)
      - Specifies whether the port is a remote port.
      - All the IP activity to and from that remote port is allowed.
    - address (optional, str, default: None)
      - Specifies the IP address.
    - timeout (optional, str, default: None)
      - Specifies the timeout period.
      - The timeout period can be specified as a number (in seconds), or with a number followed by `m` (minutes), `h` (hours), or `d` (days).
      - The maximum timeout period is 30 days.
    - present (required, str, default: None)
      - Specify whether to activate or deactivate a port.

- state (optional, str, default: None)
  - `setting_security` ensures the new security hardening rules are applied.
  - `firewall_facts` does not change anything on the HMC and returns the firewall settings information.
  - `setting_firewall` ensures the firewall settings are configured.

## Notes
- This module requires the HMC login user to have specific permissions. To achieve this, the user should create a task role based on hmcsuperadmin with additional permissions, including ViosAdminOp, VirtualIOServerCommand and other permissions for managing lpar and cec resources. The following example demonstrates the same.
- Create a task role with above mentioned additional permissions using the following command:
  ```
  mkaccfg -t taskrole -i name=new_task_role,parent=hmcsuperadmin, resources=lpar:ActivateLPAR+CapturePartitionTemplate+ChangeLPARProperty+ ChangeNPortLogin+ChangeProfileProperty+CloseVTerm+Connect5250VTerm+ CreateProfile+Delete5250VTerm+DeleteLPAR+DeleteProfile+DisableEnableVirtualEthernet+ DlparOperation+HibernateLPAR+ListLPARProperty+ListProfileProperty+ManageLPARDebugData+ ManageLPARServEvents+ManageLicenseKeys+ManageProfile+MigrateLPAR+ Open5250VTerm+OpenVTerm+PartProfileCopy+RRStartLPAR+RebootLPAR+RemoteRestartLPAR+ ShutdownLPAR+VirtualIOServerCommand+ViosAdminOp, cec:ActivateSystemProfile+BackupProfileData+CECPowerOff+CECPowerOn+ CaptureSystemTemplate+ChangeCECPassword+ChangeCECProperty+ChangeCoD+ChangePowerManagement+ ChangeSnmpAlerts+ChangeSystemConnectionProperty+ChangeSystemProfileProperty+ ChangeTrustedSystemKey+ChangeVETCode+CoDPoolManagement+CollectCECVPDInfo+ ConfigProcessorRecovery+CreateLPAR+CreatePassThruCommand+CreateSystemProfile+ DLPARRestoreHWResources+DeleteSystemProfile+DeployPartitionTemplate+DeploySystemPlan+ DeploySystemTemplate+DeviceMaintenance+DisconnectOtherHmc+EditCECMTMS+ InitializeProfileData+InitializeSPFailover+LSProfileSpace+LaunchAsm+ ListCECProperty+ListCoDInformation+ListCoDNotifications+ListNPortLogin+ ListPCIeTopology+ListRioTopology+ListSSP+ListSnmpAlerts+ListSystemProfileProperty+ ListTrustedSystemKey+ListUtilizationData+ListVETInfo+MakeSystemPlan+ ManageCECServEvents+ManageCoDNotifications+ManageDumps+ ManageSPP+ManageSSP+ManageSriovAdapter+ManageSysProfile+ManageUtilizationData+ ManageVirtualNetwork+ManageVirtualStorage+MoveSriovAdapter+PartitionConfigurationImage+ RebuildCEC+RecoverPartitionData+RemoveCECConnection+RemoveCEConnection+RemoveProfileData+ RestoreProfileData+SetCECKeylockPosition+SysProfileCopy+UpdateLIC+ValidateSystemProfile+ ViewDumps+ViewPowerManagement+ViewSPP
  ```
- Create a user with the above created task role.

## Examples
```yaml
- name: Apply the security rule lls_maxage to VIOS
  vios_secure:
    hmc_host: '{{ hmc_ip }}'
    hmc_auth: '{{ hmc_auth }}'
    system_name: <sys>
    vios_name: <vios>
    rule: lls_maxage
    level: low
    state: setting_security

- name: Get firewall information for ipv6 of VIOS
  vios_secure:
    hmc_host: '{{ hmc_ip }}'
    hmc_auth: '{{ curr_hmc_auth }}'
    system_name: <sys>
    vios_name: <vios>
    ip_version: IPV6
  state: firewall_facts

- name: Configure firewall rule for port 2000 with interface en0 on VIOS
  vios_secure:
    hmc_host: '{{ hmc_ip }}'
    hmc_auth: '{{ curr_hmc_auth }}'
    system_name: <sys>
    vios_name: <vios>
    ip_version: IPV6
    firewall_config:
        - port: 2000
          present: allow
          interface: en0
    state: setting_firewall
```

## Return Values
- security_facts (on success for setting vios security, dict)
  - Respective security information

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- Sreenidhi S (@SreenidhiS1)