# hmc_update_upgrade – Manages the update and upgrade of the HMC

## Synopsis
- Updates the HMC by installing a corrective service package located on an FTP/SFTP/NFS server/Ansible Controller Node/HMC hard disk.
- Upgrades the HMC by obtaining the required files from a remote server or from the HMC hard disk. The files are transferred onto a special partition on the HMC hard disk. After the files have been transferred, HMC will boot from this partition and perform the upgrade.
- Update/Upgrade the HMC from IBM Fix Central website.

## Requirements
The below requirements are needed on the host that executes this module.
- Python >= 3

## Parameters
- hmc_host (required, str, default: None)
  - The IPaddress or hostname of the HMC.

- hmc_auth (required, dict, default: None)
  - Username and Password credential of the HMC.
  - username (required, str, default: None)
    - Username of the HMC to login.
  - password (optional, str, default: None)
    - Password of the HMC.

- build_config (optional, dict, default: None)
  - Configuration parameters required for the HMC update/upgrade.
  - location_type (required, str, default: None)
    - The type of location which contains the corrective service ISO image. Valid values are:
      - `disk` for the HMC hard disk
      - `ftp` for an FTP site
      - `sftp` for a secure FTP (SFTP) site
      - `nfs` for an NFS file system
      - `ibmwebsite` for an IBM fixcentral website
    - When the location type is set to `disk`, first it looks for the `build_file` in HMC hard disk; if it doesn’t exist then it looks for `build_file` in the Ansible Controller node.
    - `ibmwebsite` location type supports update operation from V10 R2 M1030 release onwards and upgrade operation from V10 R3 M1060 release onwards.
  - hostname (optional, str, default: None)
    - The hostname or IPaddress of the remote server where the corrective service ISO image is located.
  - userid (optional, str, default: None)
    - The user ID to use to log in to the remote FTP or SFTP server. This option is required when the ISO image is located on a remote FTP or SFTP server. Otherwise, this option is not valid.
  - passwd (optional, str, default: None)
    - The password to use to log in to the remote FTP or SFTP server.
    - The *passwd* and *sshkey* options are mutually exclusive in case of `location_type=sftp`.
    - This option is only valid when the ISO image is located on a remote FTP or SFTP server.
  - sshkey_file (optional, str, default: None)
    - The name of the file that contains the SSH private key.
    - This option is only valid if `location_type=sftp`.
  - mount_location (optional, str, default: None)
    - The mount location defined on the NFS server where the corrective service ISO image is located. This option is valid only if `location_type=nfs`.
  - build_file (optional, str, default: None)
    - The name of the corrective service ISO image file.
    - This option is required when the ISO image is located on any of the following locations: HMC hard disk, Ansible controller node filesystem, remote FTP, SFTP, or NFS server.
    - During upgrade of the HMC, this option represents the host path where the network install image is kept.
    - During update of the HMC if `location_type=disk` and ISO image is kept in Ansible controller node or HMC hard disk, this option should be provided with the Ansible control node path in which ISO file or network install image is kept.
    - If the path specified contains the ISO file name then that specified ISO file will be considered for updation.
    - If the path specified does not contain the ISO file name then the specified folder will be searched for ISO files, sorted in alphabetical order and the 1st ISO will be considered for updation.
  - ptf (optional, str, default: None)
    - The name of the PTF to install.
    - This option is required when the ISO image is located on the IBM Fix Central website. Otherwise, this option is not valid.
    - This option is required only when the `location_type` is `ibmwebsite`.
    - This option is available for HMC versions from V10 R2 M1030 onwards for update and V10 R3 M1060 onwards for upgrade.

- state (optional, str, default: None)
  - The desired build state of the target HMC.
  - `facts` does not change anything on the HMC and returns current driver/build level of HMC.
  - `updated` ensures the target HMC is updated with given corrective service ISO image.
  - `upgraded` ensures the target HMC is upgraded with given upgrade files.

- action (optional, str, default: None)
  - `listptf` lists available Hardware Management Console (HMC) updates from the IBM Fix Central website.
    - This option is available for HMC versions from V10 R2 M1030 onwards.
  - `listupg` lists available Hardware Management Console (HMC) upgrades from the IBM Fix Central website.
    - This option is available for HMC versions from V10 R3 M1060 onwards.

## Notes
- Upgrade with `location_type=disk` will not support for V8 R870 and V9 R1 M910 release of the HMC.
- Update with `location_type=disk` and `build_file` in the HMC local path won’t remove the file after update.
- Module will not satisfy the idempotency requirement of Ansible, even though it partially confirms it. For instance, if the module is tasked to update/upgrade the HMC to the same level, it will still go ahead with the operation and finally the changed state will be reported as false.
- All Operations support passwordless authentication.
- By default, the HMC update/upgrade completion status is verified using Ping. To check the status via SSH, playbook must be executed in passwordless authentication mode.

## Examples
```yaml
- name: List the Power HMC current build level
  hmc_update_upgrade:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      state: facts

- name: Update the Power HMC to the V10R2M1040 build level from nfs location
  hmc_update_upgrade:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      build_config:
          location_type: nfs
          hostname: <NFS_Server_IP/Hostname>
          build_file: /Images/MF70893-10.2.1040.0-2304262325-x86_64.iso
          mount_location: /HMCImages
      state: updated

- name: Update the Power HMC to the V10R2M1041 build level from sftp location
  hmc_update_upgrade:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      build_config:
          location_type: sftp
          hostname: <SFTP_Server_IP/Hostname>
          userid: <SFTP_Server_Username>
          passwd: <SFTP_Server_Password>
          build_file: /Images/MF71190-10.2.1041.0-2308160028-x86_64.iso
      state: updated

- name: List all the available ptfs for update
  hmc_update_upgrade:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      action: listptf

- name: Update the Power HMC to the V10R2M1041(ifix) build level from ibmwebsite
  hmc_update_upgrade:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      build_config:
          location_type: ibmwebsite
          ptf: vMF71409
      state: updated

- name: Upgrade Power HMC to the mentioned PTF level using the image obtained from ibmwebsite
  hmc_update_upgrade:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth: '{{ curr_hmc_auth }}'
      build_config:
          location_type: ibmwebsite
          ptf: <ptf>
      state: upgraded

- name: Upgrade the Power HMC using NFS server
  hmc_update_upgrade:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth: '{{ curr_hmc_auth }}'
      build_config:
          location_type: nfs
          hostname: <hostname>
          mount_location: /HMCImages
          build_file: <build_file_path>
      state: upgraded

- name: Upgrade the Power HMC using SFTP server
  hmc_update_upgrade:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth: '{{ curr_hmc_auth }}'
      build_config:
          location_type: sftp
          hostname: <SFTP_Server_IP/Hostname>
          userid: <SFTP_Server_Username>
          passwd: <SFTP_Server_Password>
          build_file: <build_file>
      state: upgraded

- name: Provide a list of all available image files in ibmwebsite for upgrading Power HMC
  hmc_update_upgrade:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      action: listupg
```

## Return Values
- build_info (always, dict)
  - Respective build information.

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- Anil Vijayan (@AnilVijayan)
- Navinakumar Kandakur (@nkandak1)