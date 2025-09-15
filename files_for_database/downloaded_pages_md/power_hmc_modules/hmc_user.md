# hmc_user – Manage the hmc users

## Synopsis
- Create a Hardware Management Console user
- List Hardware Management Console user information
- Modify a Hardware Management Console user
- Remove Hardware Management Console users
- List LDAP Configurations
- Configure LDAP Settings
- Remove LDAP Configurations

## Parameters
- hmc_host (required, str)
  - The IP address or hostname of the HMC.

- hmc_auth (required, dict)
  - Username and Password credential of the HMC.
  - username (required, str): Username of the HMC to login.
  - password (optional, str): Password of the HMC.

- name (optional, str)
  - The user name of the HMC user. Valid for state=present, state=absent, state=updated, state=facts and state=ldap_facts.

- enable_user (optional, bool)
  - Enable an HMC user that was disabled due to inactivity. Valid only if state=updated.

- type (optional, str)
  - The type of user. During state=updated to change the default settings of HMC user, specify `default`.
  - During state=absent, supported values are `all|local|kerberos|ldap|automanage`.
  - During state=facts, valid values are `default|user`.

- resource (optional, str)
  - The LDAP resources to be listed. Valid only for state=ldap_facts. To filter the LDAP configuration of a particular user, use `name` with resource=`user`.

- ldap_resource (optional, str)
  - LDAP configuration to be removed. Valid only for action=remove_ldap_config.

- attributes (optional, dict)
  - Configuration attributes used during create and modify of HMC user.
  - new_name (optional, str): The new name to be updated.
  - taskrole (optional, str): One of `hmcsuperadmin|hmcoperator|hmcviewer|hmcpe|hmcservicerep|hmcclientliveupdate|<custom user role>`.
  - resourcerole (optional, str): The name of the resource role.
  - description (optional, str): The description of the user.
  - passwd (optional, str): Local and Kerberos users only.
  - current_passwd (optional, str): For changing the password of a Kerberos user; specify the user’s current password.
  - pwage (optional, str): Number of days. Valid only for local user. Default: 99999.
  - min_pwage (optional, str): Number of days. Valid only for local user. Default: 0.
  - authentication_type (optional, str): One of `local|kerberos|ldap`.
  - session_timeout (optional, int): Minutes. Default: 0.
  - verify_timeout (optional, int): Minutes. Default: 15.
  - idle_timeout (optional, int): Minutes. Default: 120.
  - inactivity_expiration (optional, int): Days. Default: 0.
  - remote_webui_access (optional, bool): Allow remote HMC Web UI login. Default: false.
  - remote_ssh_access (optional, bool): Allow remote SSH login. Default: true.
  - passwd_authentication (optional, bool): Allow password login.
  - remote_user_name (optional, str): Kerberos users only.
  - max_webui_login_attempts (optional, int): Maximum HMC UI login attempts.
  - webui_login_suspend_time (optional, int): Minutes.

- ldap_settings (optional, dict)
  - Configuration attributes used for configuring LDAP on HMC.
  - primary (optional, str): The primary LDAP server.
  - backup (optional, str): The backup LDAP server.
  - basedn (optional, str): The base DN for LDAP search.
  - binddn (optional, str): DN for binding to the LDAP server for non-anonymous binding.
  - bindpw (optional, str): Password for binding to the LDAP server for non-anonymous binding.
  - timelimit (optional, str): LDAP search time limit in seconds.
  - bindtimelimit (optional, str): LDAP server bind time limit in seconds.
  - automanage (optional, str): Whether HMC should automatically manage remotely authenticated LDAP users. `0` to disable, `1` to enable.
  - auth (optional, str): Authentication type for automatically managed LDAP users.
  - loginattribute (optional, str): Login attribute for authenticating LDAP users on the HMC.
  - hmcuserpropsattribute (optional, str): Attribute for retrieving user roles and properties from LDAP.
  - hmcauthnameattribute (optional, str): Attribute for retrieving the remote user ID used in Kerberos authentication.
  - searchfilter (optional, str): Filter to limit LDAP search for user information.
  - scope (optional, str): Search scope starting from base DN.
  - referrals (optional, str): Enable or disable automatic referral chasing.
  - starttls (optional, str): Enable or disable StartTLS.
  - hmcgroups (optional, str): Name of one or more user groups allowed to log in to this HMC.
  - authsearch (optional, str): Whether the HMC attempts an LDAP search with the user’s credentials as additional confirmation of successful bind.
  - tlsreqcert (optional, str): What checks to perform on a server-supplied certificate.
  - groupattribute (optional, str): Name of the Group attribute on the LDAP server. Requires memberattribute.
  - memberattribute (optional, str): Name of the group Member attribute on the LDAP server. Requires groupattribute.

- state (optional, str)
  - Desired state of the HMC user and LDAP.
  - `facts`: Return HMC user information or default settings; no changes.
  - `ldap_facts`: Return LDAP configuration or LDAP user details; no changes.
  - `updated`: Ensure the HMC user is updated with provided configuration.
  - `present`: Ensure the HMC user is created with provided configuration.
  - `absent`: Ensure the HMC user is removed.

- action (optional, str)
  - `configure_ldap`: Configure HMC LDAP client settings.
  - `remove_ldap_config`: Remove HMC LDAP client configuration.

## Notes
- All operations support passwordless authentication.

## Examples
```yaml
- name: List the properties of hmc user.
  hmc_user:
    state: facts
    hmc_host: "{{ inventory_hostname }}"
    name: <user_name>
    hmc_auth:
      username: <username>
      password: <password>

- name: Create hmc user.
  hmc_user:
    state: present
    hmc_host: "{{ inventory_hostname }}"
    name: <user_name>
    hmc_auth:
      username: <username>
      password: <password>
    attributes:
      authentication_type: local
      taskrole: hmcsuperadmin
      passwd: <new_user_password>

- name: Modify hmc user.
  hmc_user:
    state: updated
    hmc_host: "{{ inventory_hostname }}"
    name: <user_name>
    hmc_auth:
      username: <username>
      password: <password>
    attributes:
      new_name: <new_user_name>
      max_webui_login_attempts: 20

- name: Remove hmc user.
  hmc_user:
    state: absent
    hmc_host: "{{ inventory_hostname }}"
    name: <user_name>
    hmc_auth:
      username: <username>
      password: <password>

- name: List the ldap configuration.
  hmc_user:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: <username>
      password: <password>
    resource: user
    name: <hmc_user_name>
    state: ldap_facts

- name: Configure ldap settings.
  hmc_user:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: <username>
      password: <password>
    ldap_settings:
      primary: <primary_url>
      bindpw: <bind_pwd>
      basedn: ou=People,dc=<url>
      hmcauthnameattribute: <attribute>
      hmcuserpropsattribute: <attribute>
      binddn: cn=Manager,dc=<url>
      starttls: 0
    action: configure_ldap

- name: Remove ldap configuration.
  hmc_user:
    hmc_host: "{{ inventory_hostname }}"
    hmc_auth:
      username: <username>
      password: <password>
    ldap_resource: <resource_name>
    action: remove_ldap_config
```

## Return Values
- Command_output (dict)
  - Returned on success for all states except absent. Contains the respective user configuration.

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- Anil Vijayan (@AnilVijayan)
- Navinakumar Kandaur (@nkandak1)