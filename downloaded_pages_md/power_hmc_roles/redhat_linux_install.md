# Ansible Role: redhat_linux_install

This Ansible role “Red Hat Linux Installation for IBM PowerVM” automates the process of installing Red Hat Enterprise Linux (RHEL) on IBM PowerVM logical partitions (LPARs) using a network-based installation via TFTP boot.

## Overview

This Ansible role automates the installation of Red Hat Enterprise Linux (RHEL) on IBM PowerVM logical partitions (LPARs) using a network-based TFTP boot method. It orchestrates the entire setup process including infrastructure configuration, VM provisioning, and OS deployment.

The role is designed to handle both existing and non-existing LPAR scenarios:
- If the LPAR already exists, the user can specify the ‘network_name’ to attach the appropriate virtual network.
- If the LPAR does not exist, the role will automatically create one. In this case, the user must provide values for ‘network_name’. Additionally user can provide ‘mem’, ‘proc’ and ‘volume_size’ parameter values. If these parameters are omitted, default values defined in the role’s ‘vars’ will be used.

## Note

This role does not support idempotency. Re-running the playbook may result in duplicate or conflicting configurations.

## Requirements

To perform the installation, the following components must be configured:
- HTTP (Repo) Server
  - Hosts the RHEL distribution files and serves them via HTTP.
  - This can be a dedicated server with multiple distro builds or a simple HTTP server with the required build.
- PXE Server
  - Runs both `tftpd` and `dhcpd` services. This role will configure these services if they are not already running.
- LPAR (Logical Partition)
  - The target system where RHEL will be installed. If LPAR is not available, it will be created by using the given details

## Role Workflow

- LPAR Existence Check and Creation
  - Checks if the LPAR already exists on the HMC.
  - If not found, creates a new LPAR with the specified network configuration and volume size.
- MAC Address Retrieval and Formatting
  - Retrieves the MAC address of the LPAR.
  - Converts the MAC address into colon and hyphen formats for use in DHCP and GRUB configurations.
- DHCP and TFTP Service Setup
  - Checks if DHCP and TFTP services are running on the PXE server.
  - Installs and configures these services if not already running.
  - Calculates DHCP range and generates configuration using templates.
- Kickstart File Generation
  - Creates a kickstart file on the repository server using a Jinja2 template.
- Boot File Preparation and GRUB Configuration
  - Downloads required boot files from the repository server to the PXE server.
  - Creates GRUB netboot directory and configuration files.
  - Copies GRUB configuration to appropriate boot paths.
- DHCP Configuration Updates and Reversion
  - Adds LPAR-specific DHCP entries to the PXE server configuration.
  - Restarts DHCP service to apply changes.
  - Reverts DHCP configuration after installation.
- Network Boot Initiation
  - Executes `lpar_netboot` from the HMC to initiate network boot on the LPAR.
- Post-Installation Validation
  - Waits for SSH availability on the LPAR.
  - Gathers system facts and prints OS distribution and version.

## Role Variables

- distro
  - type: str
  - required: true
  - description: Redhat distribution version in format Redhat9.3
- repo_dir
  - type: str
  - required: optional
  - description: The path in which http server is hosting the redhat repository, can be in default path /var/www/html/ a directory “crtl”. Specify in format “crtl”, this is used in roles as http://abc.com/crtl/
- curr_hmc_auth
  - type: str
  - required: true
  - description: Username and Password to login to HMC system, For security purpose it is highly recommended to store this sensitive information in an encrypted secret vault file.
- host_ip/host_gw/host_subnet/host_netmask
  - type: str
  - required: true
  - description: lpar Network details in format 9.9.9.9
- dns_ip
  - type: str
  - required: true
  - description: Nameserver IP details in format 9.1.1.1
- hostname
  - type: str
  - required: true
  - description: hostname of the lpar in format aaa.abc.com
- lpar_name
  - type: str
  - required: true
  - desription: name of lpar as in the HMC
- network_name
  - type: str
  - required: true
  - description: Name of the Virtual Network to be attached to the lpar.
- managed_system
  - type: str
  - required: true
  - description: system name in HMC in which lpar is available
- disk_size
  - type: int
  - required: true
  - description: Physical volume size in MB. Required while creating LPAR
- mem
  - type: int
  - required: true
  - description: The value of dedicated memory value in megabytes to create a partition, Default value is ‘2048 MB’. Required while creating LPAR
- proc
  - type: int
  - required: true
  - description: The number of dedicated processors to create a partition. Default value is ‘2’. This will not work during shared processor setting.

## Example Playbook

```yaml
- name: Redhat Install linux
  hosts: vm
  collections:
        - ibm.power_hmc
  gather_facts: false
  roles:
        - role: redhat_linux_install
          vars:
                host_ip: < host_ip >
                host_gw: < host_gateway >
                host_subnet: < host_subnet >
                host_netmask: < host_netmask >
                dns_ip: < dns_ip >
                hostname: < hostname >
                lpar_name: < partition_name >
                netowrk_name: < network_name >
                mem: 6144
                proc: 4
                disk_size: 28590
                managed_system: < system_name >
```

## Inventory

> - file with detials of pxe server, repository server and HMC server is required while running the playbook
> - For security purposes, it is highly recommended to store this sensitive information in an encrypted secret vault file.

## Sample Inventory File

```yaml
[repo]
repo_server  ansible_host=<ip> ansible_become_pass=<password> ansible_user=<username> ansible_password=<password>
[pxe]
pxe_server  ansible_host=<ip> ansible_become_pass=<password> ansible_user=<username> ansible_password=<password>
[hmcs]
hmc_server ansible_host=<ip> ansible_become_pass=<password> ansible_user=<username> ansible_password=<password>
[vm]
host_vm ansible_host=<ip> ansible_user=<username> ansible_password=<password>
```

## License

GPL-3.0-only

## Author Information

Spoorthy S