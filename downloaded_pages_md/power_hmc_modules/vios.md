# vios – Creation and management of Virtual I/O Server partition

## Synopsis
- Creates VIOS partition
- Installs VIOS
- Displays VIOS information
- Accepts VIOS License
- List all VIOS Images available in HMC
- Copy VIOS Images from SFTP/NFS server
- Delete VIOS Images from HMC

## Parameters
- hmc_host (required, str): The IP Address or hostname of the HMC.
- hmc_auth (required, dict): Username and Password credential of the HMC.
  - username (required, str): Username of the HMC to login.
  - password (optional, str): Password of the HMC.
- system_name (optional, str): The name or mtms (machine type model serial) of the managed system.
- name (optional, str): The name of the VirtualIOServer for installation through NIM server or image available on HMC local disk.
- settings (optional, dict): Configure attributes of the VIOS partition. Supports all attributes for mksyscfg (except lpar_env). Valid only for state=present.
- nim_IP (optional, str): Use Network Installation Manager (NIM) for VIOS installation; IP address of the NIM Server. Valid only for action=install.
- location_code (optional, str): Network adapter location code to use for NIM install. If not provided, the first pingable adapter attached to the partition is used. Valid only for action=install.
- nim_vlan_id (optional, str): VLAN ID (0–4094) for tagging during network install. Default: 0. Valid only for action=install.
- nim_vlan_priority (optional, str): VLAN priority (0–7) for tagging during network install. Default: 0. Valid only for action=install.
- nim_gateway (optional, str) [deprecated]: VIOS gateway IP Address. Valid only for action=install via NIM. Deprecated; use vios_gateway.
- nim_subnetmask (optional, str) [deprecated]: VIOS subnet mask. Valid only for action=install via NIM. Deprecated; use vios_subnetmask.
- vios_gateway (optional, str): VIOS gateway IP Address. Valid only for action=install (NIM or HMC image).
- vios_subnetmask (optional, str): VIOS subnet mask. Valid only for action=install (NIM or HMC image).
- vios_IP (optional, str): IP Address to be configured to VIOS. Valid only for action=install.
- prof_name (optional, str): Profile Name to be used for VIOS install. Default: default_profile. Valid only for action=install.
- timeout (optional, int): Max waiting time (minutes) for VIOS to fully boot. Minimum > 10. Default: 60. Valid only for action=install.
- image_dir (optional, str): Use the HMC-based image for installation. Name of the directory on HMC containing the VIOS image (same as directory_name used during copy). Valid only for action=install.
- label (optional, str): Label name for the installed VIOS instead of the default. Supported only for installation from HMC local disk image. Valid only for action=install.
- network_macaddr (optional, str): Client MAC address used for network installation. If not provided, the first pingable adapter attached to the partition is used. Valid only for action=install.
- vios_iso (optional, str): The VIOS ISO file to be installed. Supported only for installation from HMC local disk image. Valid only for action=install.
- virtual_optical_media (optional, bool): Include virtual optical media details. Default: false. Valid only for state=facts.
- free_pvs (optional, bool): Include unassigned Physical Volume details. Default: false. Valid only for state=facts.
- directory_name (optional, str): The name to give the VIOS installation image on the HMC.
- files (optional, list): One or two VIOS ISO files. Required for remote imports (sftp, nfs); not valid for USB.
- directory_list (optional, list): One or more VIOS installation image directories to remove.
- media (optional, str): Media type for the VIOS installation images (e.g., nfs, sftp).
- remote_server (optional, str): Hostname or IP address of the remote server (sftp, nfs).
- ssh_key_file (optional, str): SSH private key file name. If not fully qualified, must be in the user’s home directory on the HMC. Only valid for sftp and mutually exclusive with password.
- mount_location (optional, str): Required for VIOS image imports from NFS; NFS server mount location.
- remote_directory (optional, str): Directory on the remote server for the VIOS installation image. If not provided for SFTP, the user’s home directory is used; for NFS, the mount location is used.
- options (optional, str): Options for the NFS mount command (in double quotes). Default is version 3; use vers=4 for version 4. Valid only for VIOS image imports from NFS.
- sftp_auth (optional, dict): Username and Password for the SFTP server.
  - sftp_username (optional, str): Username of the SFTP server.
  - sftp_password (optional, str): Password of the SFTP server.
- state (optional, str):
  - facts: fetch details of specified VIOS
  - present: create VIOS with specified settings
  - listimages: list VIOS images present in HMC
- action (optional, str):
  - install: install VIOS through NIM Server or HMC disk image
  - accept_license: accept license after fresh installation of VIOS
  - copy: copy VIOS images from NFS/SFTP server to the HMC
  - delete: delete VIOS images present on the HMC

## Notes
- Only state=present, action=install, and action=accept_license support passwordless authentication.
- install action parameters nim_gateway and nim_subnetmask are deprecated. Use vios_gateway and vios_subnetmask instead.

## Examples
```yaml
- name: Create VIOS with default configuration.
  vios:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_system_name/mtms>
    name: <vios_partition_name>
    state: present

- name: Create VIOS with user defined settings.
  vios:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_system_name/mtms>
    name: <vios_partition_name>
    settings:
      profile_name: <profileName>
      io_slots: <ioslot1>,<ioslot2>
    state: present

- name: Install VIOS using NIM Server.
  vios:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_system_name/mtms>
    name: <vios name>
    nim_IP: <NIM Server IP>
    nim_gateway: <vios gateway ip>
    vios_IP: <vios ip>
    nim_subnetmask: <subnetmask>
    action: install

- name: Install VIOS using the image available on the HMC local disk
  vios:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_system_name/mtms>
    image_dir: <image directory name>
    vios_iso: <vios iso>
    vios_IP: <vios ip>
    vios_gateway: <vios gateway ip>
    vios_subnetmask: <subnetmask>
    network_macaddr: <mac address>
    name: <vios name>
    prof_name: <profile name>
    timeout: <timeout>
    label: <label>
    action: install

- name: Accept License after VIOS Installation.
  vios:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_system_name/mtms>
    name: <vios_partition_name>
    action: accept_license

- name: Show VIOS details with Free PVs and Virtual Optical Media.
  vios:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    system_name: <managed_system_name/mtms>
    name: <vios_partition_name>
    free_pvs: true
    virtual_optical_media: true
    state: facts

- name: List all VIOS Images
  vios:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    state: listimages
    register: images_info

- name: Stdout the VIOS Images Info
  debug:
    msg: '{{ images_info }}'

- name: Copy Vios Image via SFTP Server
  vios:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    media: sftp
    directory_name: dir_name
    remote_server: remote_server_IP
    sftp_auth:
      sftp_username: username
      sftp_password: password
    remote_directory: <directory_path>
    files:
      - file1
      - file2
    action: copy
    register: testout

- name: Copy Vios Image via NFS
  vios:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    media: nfs
    directory_name: dir_name
    remote_server: remote_server_IP
    remote_directory: <directory_path>
    mount_location: <mount_location>
    files:
      - file1
      - file2
    options: <NFS_version>
    action: copy
    register: testout

- name: Delete Vios Image
  vios:
    hmc_host: '{{ inventory_hostname }}'
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    directory_list:
      - dir_name1
      - dir_name2
    action: delete
```

## Return Values
- vios_info (on success for action=install, dict): Respective VIOS information

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- Anil Vijayan (@AnilVijayan)
- Navinakumar Kandakur (@nkandak1)