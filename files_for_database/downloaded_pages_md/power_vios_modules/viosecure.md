# viosecure – Configures security hardening rules and firewall

## Synopsis
- Activates and deactivates security hardening rules.
- Configures and unconfigures firewall settings.

## Requirements
The following are needed on the host that executes this module:
- VIOS >= 2.2.5.0
- Python >= 2.7

## Parameters
- level (optional, str)
  - Specifies the security level to apply.
  - Using `high` might cause stability or serviceability issues, especially in a cluster environment.
  - Mutually exclusive with `file`.

- rule (optional, str)
  - Name of the single rule to be applied.

- file (optional, str)
  - Path to a security rules file to apply.
  - Mutually exclusive with `level`.

- firewall (optional, dict)
  - Firewall state and rules.

  - ipv4 (optional, dict)
    - active (optional, bool)
      - Whether the firewall is enabled.
    - default (optional, bool)
      - Load default firewall rules.
      - Mutually exclusive with `rules`.
    - rules (optional, list)
      - List of firewall rule items:
        - present (optional, bool, default: true)
          - Whether the rule should exist.
        - port (required, str)
          - Port number or a service name from `/etc/services`.
          - Allows IP activity to/from that local port.
        - interface (optional, str)
          - Network interface (e.g., `en0`).
        - remote (optional, bool, default: false)
          - If true, the port refers to a remote port; allows IP activity to/from that remote port.
        - address (optional, str)
          - IP address.
        - timeout (optional, str)
          - Timeout period. Specify seconds as a number, or use `m` (minutes), `h` (hours), `d` (days). Max: 30 days.

  - ipv6 (optional, dict)
    - active (optional, bool)
      - Whether the firewall is enabled.
    - default (optional, bool)
      - Load default firewall rules.
      - Mutually exclusive with `rules`.
    - rules (optional, list)
      - List of firewall rule items:
        - present (optional, bool, default: true)
          - Whether the rule should exist.
        - port (required, str)
          - Port number or a service name from `/etc/services`.
          - Allows IP activity to/from that local port.
        - interface (optional, str)
          - Network interface (e.g., `en0`).
        - remote (optional, bool, default: false)
          - If true, the port refers to a remote port; allows IP activity to/from that remote port.
        - address (optional, str)
          - IP address.
        - timeout (optional, str)
          - Timeout period. Specify seconds as a number, or use `m` (minutes), `h` (hours), `d` (days). Max: 30 days.

## Notes
- Applying a `high` security profile might cause stability or serviceability issues, especially if the VIOS is part of a cluster environment.

## Examples
```yaml
- name: Apply all of the low system security settings to the system
  viosecure:
    level: low

- name: Apply security rules from file myfile
  viosecure:
    file: myfile

- name: Apply the single rule lls_maxage
  viosecure:
    level: low
    rule: lls_maxage

- name: Allow the users from IP address 10.10.10.10 to rlogin
  viosecure:
    firewall:
      ipv4:
        active: yes
        rules:
        - present: yes
          port: "login"
          address: "10.10.10.10"

- name: Allow users to rlogin for seven days
  viosecure:
    firewall:
      ipv4:
        active: yes
        rules:
        - present: yes
          port: "login"
          timeout: "7d"

- name: Allow rsh client activity through interface en0
  viosecure:
    firewall:
      ipv4:
        active: yes
        rules:
        - present: yes
          port: 514
          remote: yes
          interface: "en0"

- name: Load default firewall rules
  viosecure:
    firewall:
      ipv4:
        active: yes
        default: yes
```

## Return Values
- msg (always, str)
  - Execution message.
- stdout (always, str)
  - Standard output.
- stderr (always, str)
  - Standard error.
- firewall (always, dict)
  - Current firewall settings.

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- AIX Development Team (@pbfinley1911)