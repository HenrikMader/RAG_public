# hmc_command – Execute HMC command

## Synopsis
Generic module that can execute any HMC CLI command.

The given command will be executed on all selected HMC.

Information about the HMC CLI commands can be found in the https://www.ibm.com/docs/en/power10/7063-CR1?topic=hmc-commands

## Parameters
- hmc_host (required, str, default: None)
  - The IP address or hostname of the HMC.

- hmc_auth (required, dict, default: None)
  - Username and Password credential of the HMC.
  - username (required, str, default: None)
    - Username of the HMC to login.
  - password (optional, str, default: None)
    - Password of the HMC.

- cmd (required, str, default: None)
  - The command to be executed on HMC.

## Notes
- This module supports passwordless authentication.

## Examples
```yaml
- name: Execute a command on HMC
  hmc_command:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: '{{ ansible_user }}'
      password: '{{ hmc_password }}'
    cmd: <cmd>
```

## Return Values
- Command_output (always, str)
  - Respective command output

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- Navinakumar Kandakur (@nkandak1)