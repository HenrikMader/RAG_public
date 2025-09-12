# vios_update_upgrade – Manages the update and upgrade of the VIOS from the HMC

## Synopsis
- When the Virtual I/O Server (VIOS) partition is running and has an active Resource Monitoring and Control (RMC) connection, this module enables the updating or upgrading of VIOS.
- Updates the VIOS by installing the VIOS installation image located on an NFS/SFTP/HMC hard disk/IBM Fix Central website.
- Upgrades the VIOS by obtaining the required files from NFS/SFTP/HMC hard disk.

## Parameters
- hmc_host (required, str): The IP address or hostname of the HMC.
- hmc_auth (required, dict): Username and Password credential of the HMC.
  - username (required, str): Username of the HMC to login.
  - password (optional, str): Password of the HMC.
- attributes (required, dict): Configuration parameters required for VIOS update and upgrade.
  - repository (optional, str): The repository that contains the VIOS installation image. Valid values: `sftp` (secure FTP server), `ibmwebsite` (IBM Fix Central website), `nfs` (NFS file system), `disk` (HMC). Note: `ibmwebsite` is only valid for updating VIOS.
  - system_name (optional, str): The name or MTMS (machine type model serial) of the managed system.
  - vios_id (optional, str): The ID of the VIOS to update/upgrade. `vios_id` and `vios_name` are mutually exclusive.
  - vios_name (optional, str): The name of the VIOS to update/upgrade. `vios_id` and `vios_name` are mutually exclusive.
  - image_name (optional, str): The name of the VIOS update image. Required when the VIOS update image is on the HMC hard disk or IBM Fix Central. Also used with `save` to specify the image that will be saved to the HMC’s hard disk.
  - files (optional, list): The list of files required for update/upgrade. Required and only valid when the VIOS update/upgrade image is on an SFTP/NFS remote server.
  - host_name (optional, str): The host name or IP address of the SFTP/NFS remote server.
  - user_id (optional, str): The user ID to use to log in to the remote SFTP server. Only valid if the remote image repository is SFTP.
  - password (optional, str): The password to use to log in to the remote SFTP server. `password` and `ssh_key_file` are mutually exclusive. Only valid if the remote image repository is SFTP.
  - ssh_key_file (optional, str): The file that contains the SSH private key. `password` and `ssh_key_file` are mutually exclusive. Only valid if the remote image repository is SFTP.
  - mount_loc (optional, str): The mount location defined on the NFS server that contains the VIOS update image. Only valid if the remote image repository is NFS.
  - option (optional, str): Options to be passed to the mount command used to mount the NFS file system that contains the VIOS update image. The HMC supports NFS versions 3 and 4 (default is 3). Only valid if the remote image repository is NFS.
  - directory (optional, str): The directory on the remote server that contains the VIOS update image. If not specified for SFTP, the remote server’s user home directory is used. If not specified for NFS, the mount directory is used.
  - disks (optional, list): One or more free VIOS disks to be used for the upgrade. You may need to free or add new disks to perform the upgrade. Depending on the existing VIOS rootvg size, required disk space may be greater than 30GB. Only valid for `upgraded`.
  - restart (optional, bool): Restart the VIOS after installing the update if the update requires a restart. Only valid for `updated`. Default: false.
  - save (optional, bool): Save the update image on the HMC hard disk.
- state (optional, str): The desired build state of the target VIOS.
  - `facts`: Does not change anything on the VIOS and returns current version of VIOS.
  - `updated`: Ensures the target VIOS is updated with the given installation ISO image.
  - `upgraded`: Ensures the target VIOS is upgraded with the given upgrade files.

## Notes
- All Operations support passwordless authentication.
- This module is not fully idempotent. For example, updating/upgrading to the same level will still perform the operation, but will ultimately report changed=false.

## Examples
```yaml
- name: Get the current version of VIOS.
  vios_update_upgrade:
    hmc_host: '{{ hmc_ip }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    attributes:
      vios_name: <vios_name>
      system_name: <sys/MTMS>
    state: facts

- name: Update the VIOS from the HMC using the image available on remote SFTP server.
  vios_update_upgrade:
    hmc_host: '{{ hmc_ip }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    attributes:
      repository: sftp
      vios_id: <vios_id>
      system_name: <sys/MTMS>
      password: <password>
      user_id: <username>
      host_name: <hostip>
      files:
        - <iso file1>
    state: updated

- name: Update the VIOS from the HMC using the image available on remote NFS server.
  vios_update_upgrade:
    hmc_host: '{{ hmc_ip }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    attributes:
      repository: nfs
      vios_id: <vios_id>
      system_name: <sys/MTMS>
      password: <password>
      user_id: <username>
      host_name: <hostip>
      files:
        - <iso file>
        - <bff file>
    state: updated

- name: Upgrade the VIOS from the HMC using the image available on HMC hard disk.
  vios_update_upgrade:
    hmc_host: '{{ hmc_ip }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    attributes:
      repository: disk
      vios_id: <vios_id>
      system_name: <sys/MTMS>
      password: <password>
      user_id: <username>
      host_name: <hostip>
      disks:
        - Disk1
        - Disk2
    state: upgraded
```

## Return Values
- Command_output (always, dict): Respective build information.

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- Sreenidhi S (@SreenidhiS1)