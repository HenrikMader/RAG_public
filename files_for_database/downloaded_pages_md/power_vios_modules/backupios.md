# backupios – Creates an installable image of the root volume group

## Synopsis
Creates a backup of the Virtual I/O Server and places it onto a file system.

## Requirements
- VIOS >= 2.2.5.0
- Python >= 2.7

## Parameters
- file (required, str; default: None)
  - Specifies the directory on which the image is to be stored.
  - When mksysb=yes, specifies the file name.

- mksysb (optional, bool; default: False)
  - Creates an mksysb image.

- nopack (optional, list; default: None)
  - When mksysb=yes, specifies the list of files to exclude from being packed.

- savevgstruct (optional, bool; default: True)
  - Specifies whether to save the volume groups structure of user-defined volume groups as part of the backupios process.

- savemedialib (optional, bool; default: True)
  - Specifies whether to save the contents of the media repository as part of the backupios process.

## Notes
- The backupios module backs up only the volume group structures that are activated. The structures of volume groups that are deactivated are not backed up.

## Examples
```yaml
- name: Generate a backup to /home/padmin/backup directory
  backupios:
    file: /home/padmin/backup

- name: Generate an mksysb backup to /home/padmin/backup.mksysb
  backupios:
    file: /home/padmin/backup.mksysb
    mksysb: yes
    savemedialib: no
    savevgstruct: no
```

## Return Values
- msg (always, str)
  - The execution message.

- stdout (always, str)
  - The standard output.

- stderr (always, str)
  - The standard error.

- ioslevel (always, str; example: 3.1.0.00)
  - The latest installed maintenance level of the system.

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- AIX Development Team (@pbfinley1911)