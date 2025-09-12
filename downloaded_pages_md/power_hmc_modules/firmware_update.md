# firmware_update – Change firmware level on Managed Systems

## Synopsis
Update/Upgrade a managed system.

## Parameters
- hmc_host (required, string)
  - IP address or hostname of the HMC.
- hmc_auth (required, dict)
  - Username and Password credential of the HMC.
  - username (required, string): HMC username.
  - password (optional, string): HMC password.
- system_name (required, string)
  - The name or mtms (machine type model serial) of the managed system.
- repository (optional, string, default: ibmwebsite)
  - The repository from which to retrieve the firmware updates. Valid values are ibmwebsite for the IBM service website, ftp for a remote FTP site, sftp for a remote secure FTP (SFTP) site
- remote_repo (optional, dict)
  - When the image repository needs credentials to be accessed remotely.
  - hostname (required, string): The hostname or IP address of the remote server where the firmware image is located.
  - userid (required, string): The user ID to use to log in to the remote FTP or SFTP server. This option is required when the firmware image is located on a remote FTP or SFTP server Otherwise, this option is not valid.
  - passwd (optional, string): The password to use to log in to the remote FTP or SFTP server. The passwd and sshkey options are mutually exclusive in case if location_type=sftp. This option is only valid when the firmware image is located on a remote FTP or SFTP server.
  - sshkey_file (optional, string): The name of the file that contains the SSH private key. This option is only valid if location_type=sftp.
  - directory (required, string): Location where the images are stored.
- level (optional, string, default: latest)
  - Specify sss to retrieve a specific level of Managed System or Power LIC updates, even if disruptive. sss is the three character identifier of the specific level to retrieve. This is only valid when the LIC type is either Managed System only or Power only.
  - Specify ccc,ppp to retrieve a specific level of Managed System and Power LIC updates, even if disruptive. ccc is the three character identifier of the specific level of Managed System LIC updates to retrieve. ppp is the three character identifier of the specific level of Power LIC updates to retrieve. This is only valid when the LIC type is both Managed System and Power.
  - Specify release1_level1,release2_level2,… to retrieve specific levels of LIC updates, even if disruptive. The level specified in each entry indicates the desired level for all components which are running the release specified in the entry.
- state (optional, string)
  - updated: executes an update on target system.
  - upgraded: executes an upgrade on target system.
- action (optional, string)
  - accept: accepts firmware level for target system.

## Notes
- All operations support passwordless authentication.

## Examples
```yaml
- name: Update to latest level with default values (latest at ibmwebsite).
  ibm.power_hmc.firmware_update:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth:
          username: '{{ ansible_user }}'
          password: '{{ hmc_password }}'
      system_name: <System name/mtms>
      state: updated

- name: Upgrade system to specific level at an sftp repo.
  firmware_update:
      hmc_host: '{{ inventory_hostname }}'
      hmc_auth: '{{ curr_hmc_auth }}'
      system_name: <System name/mtms>
      repository: sftp
      remote_repo:
      hostname: <hostname/ip>
      userid: <user>
      passwd: <password>
      directory: /repo/images/
      level: 01VL941_047
      state: upgraded
```

## Return Values
- service_pack (always, string, example: FW940.20)
  - The service pack representation of the system
- level (always, string, example: 55)
  - The specific level active on the system
- ecnumber (always, string, example: 01VL940)
  - The engineering change (EC) number associated with the firmware update

## Status

### Authors
- Mario Maldonado (@Mariomds)