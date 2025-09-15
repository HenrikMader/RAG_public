# alt_root_vg – Create/Cleanup an alternate rootvg disk on a VIOS

## Synopsis
Copy the rootvg to an alternate disk or cleanup an existing one.

## Requirements
- VIOS >= 2.2.5.0
- Python >= 2.7

## Parameters
- action (optional, str, default: copy)
  - Specifies the operation to perform on the VIOS.
  - "copy" to perform an alternate disk copy.
  - "clean" to cleanup an existing alternate disk copy.
- targets (optional, list, default: None)
  - Specifies the target disks.
- disk_size_policy (optional, str, default: None)
  - When action=copy, specifies how to choose the alternate disk if targets is not specified.
  - "minimize": smallest disk that can be selected.
  - "upper": first disk found bigger than the rootvg disk.
  - "lower": disk size less than rootvg disk size but big enough to contain the used PPs.
  - "nearest": disk size closest to the rootvg disk.
- force (optional, bool, default: False)
  - Forces removal of any existing alternate disk copy on target disks.

## Notes
- alt_root_vg only backs up mounted file systems. Mount all file systems that you want to back up.
- When no target is specified, copy is performed to only one alternate disk even if the rootvg contains multiple disks.

## Examples
```yaml
- name: Perform an alternate disk copy of the rootvg to hdisk1
  alt_root_vg:
    targets: hdisk1

- name: Perform an alternate disk copy of the rootvg to the smallest disk that can be selected
  alt_root_vg:
    disk_size_policy: minimize

- name: Perform a cleanup of any existing alternate disk copy
  alt_root_vg:
    action: clean
```

## Return Values
- msg (always, str, e.g., "alt_root_vg copy operation completed successfully")
  - The execution message.
- stdout (always, str, e.g., "Bootlist is set to the boot disk: hdisk0 blv=hd5")
  - The standard output.
- stderr (always, str)
  - The standard error.

## Status
- This module is not guaranteed to have a backwards compatible interface. [preview]
- This module is maintained by community.

### Authors
- AIX Development Team (@pbfinley1911)