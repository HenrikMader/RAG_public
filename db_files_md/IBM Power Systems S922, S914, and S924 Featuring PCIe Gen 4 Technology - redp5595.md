Front cover

<!-- image -->

## IBM Power Systems S922, S914, and S924 Technical Overview and Introduction Featuring PCIe Gen 4 Technology

Bartlomiej Grabowski

Mauro Minomizaki

Armin Ro ¨ ll

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

IBM Redbooks

## IBM Power Systems S922, S914, and S924 Featuring PCIe Gen 4 Technology

July 2020

Note: Before using this information and the product it supports, read the information in 'Notices' on page vii.

## First Edition (July 2020)

This edition applies to the IBM Power System S914 (9009-41G), IBM Power System S922 (9009-22G), and IBM Power System S924 (9009-42G) servers that use the latest IBM POWER9™ processor-based technology.

© Copyright International Business Machines Corporation 2020. All rights reserved.

Note  to  U.S.  Government Users  Restricted  Rights  --  Use,  duplication  or  disclosure  restricted  by  GSA  ADP  Schedule Contract with IBM Corp.

## Contents

| Notices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                           | . vii   |
|-------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Trademarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                              | viii    |
| Preface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                           | . ix    |
| Authors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                          | . ix    |
| Now you can become a published author, too! . . . . . . . . . . . . . . . . . . . . . .                                                   | . .x    |
| Comments welcome. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                     | . .x    |
| Stay connected to IBM Redbooks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                            | . xi    |
| Chapter 1. IBM Power Systems S922, S914, and S924 overview . . . . .                                                                      | . 1     |
| 1.1 Systems overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                    | . 2     |
| 1.1.1 Power S922 server . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                           | . 2     |
| 1.1.2 Power S914 server . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                           | . 3     |
| 1.1.3 Power S924 server . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                           | . 4     |
| 1.1.4 Common features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                           | . 5     |
| 1.2 Operating environment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                       | . 6     |
| 1.3 Physical package . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                    | . 7     |
| 1.3.1 Tower model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                       | . 8     |
| 1.3.2 Rack-mount model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                            | . 8     |
| 1.4 System features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                   | . 9     |
| 1.4.1 Power S922 server features . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                | . 9     |
| 1.4.2 Power S914 server features . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                | 11      |
| 1.4.3 Power S924 server features . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                | 12      |
| 1.5 Minimum features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                    | 13      |
| 1.5.1 Power supply features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                             | 14      |
| 1.5.2 Processor module features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                               | 14      |
| 1.5.3 Memory features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                         | 17      |
| 1.5.4 Peripheral Component Interconnect Express slots. . . . . . . . . . . .                                                              | 18      |
| 1.6 Disk and media features . .                                                                                                           | 19      |
| . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.7 I/O drawers for Power S922, Power S914, and Power S924 servers. . | 33      |
| 1.7.1 PCIe Gen3 I/O expansion drawer. . . . . . . . . . . . . . . . . . . . . . . . .                                                     | 34      |
| 1.7.2 I/O drawers and usable PCI slots . . . . . . . . . . . . . . . . . . . . . . . . .                                                  | 35      |
| 1.7.3 EXP12SX SAS Storage Enclosure and EXP24SX SAS Storage Enclosure.                                                                    | 36      |
| 1.8 IBM i Solution Editions for Power S914 . . . . . . . . . . . . . . . . . . . . . . . .                                                | 38      |
| 1.9 IBM Capacity BackUp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                       | 38      |
| 1.9.1 Power S922 (9009-22G) IBM Capacity BackUp offering . . . . . . .                                                                    | 38      |
| 1.9.2 Power S914 (9009-41G) IBM Capacity BackUp offering . . . . . . .                                                                    | 40      |
| 1.9.3 Power S924 (9009-42G) IBM Capacity BackUp offering . . . . . . .                                                                    | 41      |
| 1.10 IBM Power Systems Enterprise Cloud Edition . . . . . . . . . . . . . . . . . .                                                       | 43      |
| 1.10.1 IBM PowerSC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                          | 43      |
| 1.10.2 IBM PowerSC Multi-Factor Authentication . . . . . . . . . . . . . . . . .                                                          | 44      |
| 1.10.3 IBM Cloud PowerVC Manager . . . . . . . . . . . . . . . . . . . . . . . . . .                                                      | 44      |
| 1.10.4 IBM VM Recovery Manager DR . . . . . . . . . . . . . . . . . . . . . . . . .                                                       | 44      |
| 1.10.5 IBM Aspera High-Speed Transfer Endpoint 100 Mbps. . . . . . . .                                                                    | 44      |
| 1.10.6 IBM Cloud Management Console . . . . . . . . . . . . . . . . . . . . . . . .                                                       | 45      |
| 1.11 IBM Power platform modernization . . . . . . . . . . . . . . . . . . . . . . . . . . .                                               | 45      |
| 1.11.1 IBM Power Systems Virtual Servers . . . . . . . . . . . . . . . . . . . . . .                                                      | 45      |
| 1.12 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                | 46      |
| System racks.                                                                                                                             |         |

| 1.12.1                                                                 | IBM 7014 Model T00 rack. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                    | . 46      |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| 1.12.2                                                                 | IBM 7014 Model T42 rack. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                    | . 47      |
| 1.12.3                                                                 | IBM 42U Slim Rack 7965-94Y . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                        | . 49      |
| 1.12.4                                                                 | 1.8 Meter Rack (0551) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                 | . 49      |
| 1.12.5                                                                 | 2.0 Meter Rack (#0553) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                  | . 49      |
| 1.12.6                                                                 | Rack (#ER05) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                            | . 49      |
| 1.12.7                                                                 | The AC power distribution unit and rack content . . . . . . . . . . . .                                                                                                               | . 50      |
| 1.12.8                                                                 | Rack-mounting rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | . 53      |
| 1.12.9                                                                 | Useful rack additions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                              | . 53      |
| 1.12.10 Original equipment manufacturer racks                          | . . . . . . . . . . . . . . . . . .                                                                                                                                                   | . 55      |
| 1.13 Hardware Management Console . .                                   | . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                                   | . 56      |
| 1.13.1                                                                 | New features. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                           | . 56      |
| 1.13.2                                                                 | Hardware Management Console overview . . . . . . . . . . . . . . . .                                                                                                                  | . 57      |
| 1.13.3                                                                 | . Hardware Management Console code level . . . . . . . . . . . . . . . .                                                                                                              | . 58      |
| 1.13.4                                                                 | Two architectures of Hardware Management Console. . . . . . . .                                                                                                                       | . 59      |
| 1.13.5                                                                 | Virtual Hardware Management Console . . . . . . . . . . . . . . . . . . .                                                                                                             | . 60      |
| 1.13.6                                                                 | Connectivity to POWER9 processor-based systems . . . . . . . . .                                                                                                                      | . 61      |
| 1.13.7                                                                 | High availability Hardware Management Console configuration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                              | . 62      |
| 1.13.8                                                                 | Flat panel display options                                                                                                                                                            | . 63      |
| Chapter 2. Architecture and technical overview . . . . . . . . . . . . | Chapter 2. Architecture and technical overview . . . . . . . . . . . .                                                                                                                | . 65      |
| 2.1 The                                                                | IBM POWER9 processor . . . . . . . . . . . . . . . . . . . .                                                                                                                          | . 69      |
| 2.1.1                                                                  | POWER9 processor overview. . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                      | . 69      |
| 2.1.2                                                                  | POWER9 processor features . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                     | . 71      |
| 2.1.3                                                                  | POWER9 processor core . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                   | . 71      |
| 2.1.4                                                                  | Simultaneous multithreading. . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                  | . 72      |
| 2.1.5                                                                  | Processor feature codes. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                | . 72      |
| 2.1.6                                                                  | Memory access. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                            | . 74      |
| 2.1.7                                                                  | On-chip L3 cache innovation and intelligent caching . . . . . . . . . .                                                                                                               | . 75      |
| 2.1.8                                                                  | Hardware transactional memory. . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                      | . 76      |
| 2.1.9                                                                  | Coherent Accelerator Processor Interface 2.0 . . . . . . . . . . . . . . .                                                                                                            | . 76      |
| 2.1.10 Comparing                                                       | Power management and system performance . . . . . . . . . . . . . . the POWER9, POWER8, and POWER7+ processors.                                                                       | . 78 . 80 |
| 2.1.11 2.2                                                             | subsystem. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                              | . 81      |
| Memory                                                                 | Memory                                                                                                                                                                                |           |
| 2.2.1                                                                  | Memory placement rules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                         | . 83      |
| 2.2.2 2.3                                                              | Memory bandwidth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . System buses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 88 . 93 |
| 2.3.1                                                                  | Memory buses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                        | . 93      |
| 2.3.2                                                                  | . . . . . . Inter-node SMP X-buses. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                     | . 93      |
| 2.3.3                                                                  | PCIe Gen 4 buses. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                             | . 93      |
| 2.3.4                                                                  | Service processor interface bus . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                   | . 95      |
| 2.4 Internal I/O subsystem . . . .                                     | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                     | . 96      |
| 2.4.1 Slot configuration                                               | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                             | . 96      |
| 2.4.2 System ports . . . .                                             | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                             | 100       |
| 2.5 Peripheral Component Interconnect adapters . . . .                 | . . . . . . . . . . . . . . .                                                                                                                                                         | 100       |
| 2.5.1                                                                  | Peripheral Component Interconnect Express . . . . . . . . . . . . . . . .                                                                                                             | 100       |
| 2.5.2                                                                  | LAN adapters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                          | 101       |
| 2.5.3 2.5.4                                                            | Graphics accelerator adapters . . . . . . . . . . . . . . . . . . . . . . . . . . . SAS adapters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | 103 104   |
| 2.5.5                                                                  | Fibre Channel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                         | 105       |
|                                                                        | adapters                                                                                                                                                                              |           |
| 2.5.6                                                                  | InfiniBand host channel adapter . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                   | 107 108   |
| 2.5.7 2.5.8                                                            | Cryptographic coprocessor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Coherent Accelerator Processor Interface adapters. . . . . . . . . . .                          | 109       |

| 2.5.9 USB adapters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . 109   |
|---------------------------------------------------------------------------------------------------------------------------|---------|
| 2.5.10 Async adapter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . 110   |
| 2.6 Internal storage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . 111   |
| 2.6.1 9009-41G and 9009-42G Backplane (#EJ1C) . . . . . . . . . . . . . . . . . . . . . .                                 | . 111   |
| 2.6.2 9009-41G and 9009-42G Split Backplane option for #EJ1C. . . . . . . . . . . .                                       | . 112   |
| 2.6.3 9009-41G and 9009-42G Backplane (#EJ1D) . . . . . . . . . . . . . . . . . . . . . .                                 | . 113   |
| 2.6.4 9009-41G and 9009-42G Expanded Function Backplane (#EJ1M) . . . . . .                                               | . 114   |
| 2.6.5 9009-41G and 9009-42G Gen 4 Backplane (#EJ1S) . . . . . . . . . . . . . . . . .                                     | . 115   |
| 2.6.6 9009-22G Backplane (#EJ1F) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                      | . 116   |
| 2.6.7 9009-22G Expanded Function Storage Backplane (#EJ1G) . . . . . . . . . . .                                          | . 118   |
| 2.6.8 NVMe support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . 118   |
| 2.6.9 RAID support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . 119   |
| 2.6.10 Easy Tier. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       | . 122   |
| 2.6.11 External SAS ports . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             | . 124   |
| 2.6.12 Media drawers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            | . 124   |
| 2.6.13 External DVD drives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . 124   |
| 2.6.14 RDX removable disk drives. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                   | . 125   |
| 2.7 External IO subsystems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . 126   |
| 2.7.1 Peripheral Component Interconnect Express Gen3 I/O expansion drawer                                                 | . 126   |
| 2.7.2 PCIe Gen3 I/O expansion drawer optical cabling . . . . . . . . . . . . . . . . . . . .                              | . 127   |
| 2.7.3 PCIe Gen3 I/O expansion drawer system power control network cabling .                                               | . 129   |
| 2.8 External disk subsystems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . 129   |
| 2.8.1 EXP12SX SAS Storage Enclosure and EXP24SX SAS Storage Enclosure.                                                    | . 130   |
| 2.8.2 IBM Storage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         | . 132   |
| 2.9 Operating system support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . 132   |
| 2.9.1 AIX operating system . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . 133   |
| 2.9.2 IBM i . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . 133   |
| 2.9.3 Linux operating system. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .               | . 134   |
| 2.9.4 Virtual I/O Server . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          | . 134   |
| 2.10 Power Systems reliability, availability, and serviceability capabilities . . . . . . . .                             | . 135   |
| 2.11 Manageability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    | . 136   |
| 2.11.1 Service user interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . 136   |
| 2.11.2 Power Systems Firmware maintenance . . . . . . . . . . . . . . . . . . . . . . . . . .                             | . 143   |
| 2.11.3 Concurrent Firmware Maintenance improvements . . . . . . . . . . . . . . . . . .                                   | . 146   |
| 2.11.4 IBM Electronic Services and IBM Electronic Service Agent . . . . . . . . . . .                                     | . 146   |
| Related publications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . 151   |
| IBM Redbooks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . 151   |
| Online resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . 151   |
| Help from IBM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 152   |

## Notices

This information was developed for products and services offered in the US. This material might be available from IBM in other languages. However, you may be required to own a copy of the product or product version in that language in order to access it.

IBM may not offer the products, services, or features discussed in this document in other countries. Consult your local IBM representative for information on the products and services currently available in your area. Any reference to an IBM product, program, or service is not intended to state or imply that only that IBM product, program, or service may be used. Any functionally equivalent product, program, or service that does not infringe any IBM intellectual property right may be used instead. However, it is the user's responsibility to evaluate and verify the operation of any non-IBM product, program, or service.

IBM may have patents or pending patent applications covering subject matter described in this document. The furnishing of this document does not grant you any license to these patents. You can send license inquiries, in writing, to:

IBM Director of Licensing, IBM Corporation, North Castle Drive, MD-NC119, Armonk, NY 10504-1785, US

INTERNATIONAL BUSINESS MACHINES CORPORATION PROVIDES THIS PUBLICATION 'AS IS' WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. Some jurisdictions do not allow disclaimer of express or implied warranties in certain transactions, therefore, this statement may not apply to you.

This information could include technical inaccuracies or typographical errors. Changes are periodically made to the information herein; these changes will be incorporated in new editions of the publication. IBM may make improvements and/or changes in the product(s) and/or the program(s) described in this publication at any time without notice.

Any references in this information to non-IBM websites are provided for convenience only and do not in any manner serve as an endorsement of those websites. The materials at those websites are not part of the materials for this IBM product and use of those websites is at your own risk.

IBM may use or distribute any of the information you provide in any way it believes appropriate without incurring any obligation to you.

The performance data and client examples cited are presented for illustrative purposes only. Actual performance results may vary depending on specific configurations and operating conditions.

Information concerning non-IBM products was obtained from the suppliers of those products, their published announcements or other publicly available sources. IBM has not tested those products and cannot confirm the accuracy of performance, compatibility or any other claims related to non-IBM products. Questions on the capabilities of non-IBM products should be addressed to the suppliers of those products.

Statements regarding IBM's future direction or intent are subject to change or withdrawal without notice, and represent goals and objectives only.

This information contains examples of data and reports used in daily business operations. To illustrate them as completely as possible, the examples include the names of individuals, companies, brands, and products. All of these names are fictitious and any similarity to actual people or business enterprises is entirely coincidental.

## COPYRIGHT LICENSE:

This information contains sample application programs in source language, which illustrate programming techniques on various operating platforms. You may copy, modify, and distribute these sample programs in any form without payment to IBM, for the purposes of developing, using, marketing or distributing application programs conforming to the application programming interface for the operating platform for which the sample programs are written. These examples have not been thoroughly tested under all conditions. IBM, therefore, cannot guarantee or imply reliability, serviceability, or function of these programs. The sample programs are provided 'AS IS', without warranty of any kind. IBM shall not be liable for any damages arising out of your use of the sample programs.

## Trademarks

IBM, the IBM logo, and ibm.com are trademarks or registered trademarks of International Business Machines Corporation, registered in many jurisdictions worldwide. Other product and service names might be trademarks of IBM or other companies. A current list of IBM trademarks is available on the web at 'Copyright and trademark information' at http://www.ibm.com/legal/copytrade.shtml

The following terms are trademarks or registered trademarks of International Business Machines Corporation, and might also be trademarks or registered trademarks in other countries.

AIX®

Aspera®

C3®

DS8000®

Easy Tier®

IBM®

IBM Cloud™

IBM FlashSystem®

IBM Spectrum®

Interconnect®

POWER®

Power Architecture®

POWER6™

POWER7®

POWER8®

POWER9™

PowerHA®

PowerPC®

PowerVM®

Redbooks®

Redbooks (logo)

®

Storwize®

System Storage™

<!-- image -->

The following terms are trademarks of other companies:

Intel, Intel logo, Intel Inside logo, and Intel Centrino logo are trademarks or registered trademarks of Intel Corporation or its subsidiaries in the United States and other countries.

The registered trademark Linux® is used pursuant to a sublicense from the Linux Foundation, the exclusive licensee of Linus Torvalds, owner of the mark on a worldwide basis.

LTO, Ultrium, the LTO Logo and the Ultrium logo are trademarks of HP, IBM Corp. and Quantum in the U.S. and other countries.

Microsoft, and the Windows logo are trademarks of Microsoft Corporation in the United States, other countries, or both.

Fedora, OpenShift, Red Hat, are trademarks or registered trademarks of Red Hat, Inc. or its subsidiaries in the United States and other countries.

UNIX is a registered trademark of The Open Group in the United States and other countries.

Other company, product, or service names may be trademarks or service marks of others.

## Preface

This IBM® Redpaper publication is a comprehensive guide that covers the IBM Power System S914 (9009-41G), IBM Power System S922 (9009-22G), and IBM Power System S924 (9009-42G) servers that use the latest IBM POWER9™ processor-based technology and support the IBM AIX®, IBM i, and Linux operating systems (OSs). The goal of this paper is to provide a hardware architecture analysis and highlight the changes, new technologies, and major features that are being introduced in these systems, such as:

- The latest IBM POWER9 processor, which is available in various configurations for the number of cores per socket
- More performance by using industry-leading Peripheral Component Interconnect® Express (PCIe) Gen 4 slots
- Enhanced internal disk scalability and performance with up to 11 NVMe adapters
- Introduction of a competitive Power S922 server with a 1-socket configuration that is targeted at IBM i customers

This publication is for professionals who want to acquire a better understanding of Power Systems products. The intended audience includes:

- Clients
- Sales and marketing professionals
- Technical support professionals
- IBM Business Partners
- Independent software vendors (ISVs)

This paper expands the set of Power Systems documentation by providing a desktop reference that offers a detailed technical description of the Power S922, Power S914, and Power S924 servers.

This paper was produced by a team of specialists from around the world working at IBM Redbooks, Austin Center.

Bartlomiej Grabowski is an IBM Champion and a Principal Systems Specialist in DHL IT Services. He has over 16 years of experience in enterprise solutions. He holds a bachelor's degree in computer science from the Academy of Computer Science and Management in Bielsko-Biala. His areas of expertise include Power Systems, IBM i, IBM PowerHA®, IBM PowerVM®, and storage solutions. Bartlomiej is also a developer of IBM certification exams. He is a Platinum IBM Redbooks® author.

Mauro Minomizaki is a Consulting Technical Sales Specialist working for IBM in Brazil. He has 25 years of experience in Power Systems. He holds a degree in Information Technology from Sao Paulo State University of Technology. His areas of expertise include Power Systems, Competitive and Winback situations, Sizing and Solution Architecture, and AIX Administration and Performance Tuning. He has written extensively on AIX, Power Systems Hardware, Server Consolidation, and Power Virtualization.

## Authors

Armin Ro ¨ll works as a Power Systems IT specialist in Germany. He has 24 years of experience in Power Systems and AIX pre-sales technical support. He holds a degree in experimental physics from the University of Hamburg, Germany. He co-authored the IBM AIX Version 4.3.3, the IBM AIX 5L Version 5.0, the IBM AIX 5L Version 5.3, the IBM AIX Version 6.1, and the IBM AIX 7.1 Differences Guide IBM Redbooks publications, and the IBM Power System E950 and the IBM Power System E980 IBM Redpapers.

The project that produced this publication was managed by: Scott Vetter , PMP

Thanks to the following people for their contributions to this project:

Ryan Achilles, Ron Arroyo, John Banchy, Joanna Bartz, Douglas Gibbs, Daniel Goldener, Walter Lipp, Stephen Lutz, Hari G Muralidharan, William Starke, N. L. Silva, Jeff Stuecheli, Wade Wallace, Ruby Zgabay

## Now you can become a published author, too!

Here's an opportunity to spotlight your skills, grow your career, and become a published author-all at the same time! Join an IBM Redbooks residency project and help write a book in your area of expertise, while honing your experience using leading-edge technologies. Your efforts will help to increase product acceptance and customer satisfaction, as you expand your network of technical contacts and relationships. Residencies run from two to six weeks in length, and you can participate either in person or as a remote resident working from your home base.

Find out more about the residency program, browse the residency index, and apply online at:

ibm.com /redbooks/residencies.html

## Comments welcome

Your comments are important to us!

We want our papers to be as helpful as possible. Send us your comments about this paper or other IBM Redbooks publications in one of the following ways:

- Use the online Contact us review Redbooks form found at:
- ibm.com /redbooks
- Send your comments in an email to:
- redbooks@us.ibm.com
- Mail your comments to:

IBM Corporation, IBM Redbooks Dept. HYTD Mail Station P099 2455 South Road Poughkeepsie, NY 12601-5400

## Stay connected to IBM Redbooks

- Find us on Facebook:
- http://www.facebook.com/IBMRedbooks
- Follow us on Twitter:
- http://twitter.com/ibmredbooks
- Look for us on LinkedIn:
- http://www.linkedin.com/groups?home=&amp;gid=2130806
- Explore new Redbooks publications, residencies, and workshops with the IBM Redbooks weekly newsletter:
- https://www.redbooks.ibm.com/Redbooks.nsf/subscribe?OpenForm
- Stay current on recent Redbooks publications with RSS Feeds:
- http://www.redbooks.ibm.com/rss.html

<!-- image -->

1

Chapter 1.

## IBM Power Systems S922, S914, and S924 overview

In this chapter, we introduce the newest generation of IBM Power System S922 (9009-22G), IBM Power System S914 (9009-41G), and IBM Power System S924 (9009-42G) servers that were announced in 2018. They are now updated with new Peripheral Component Interconnect Express (PCIe) Gen 4 I/O switches in the back end and more NVMe adapters support to meet your need for the high-performance and low latency demands that are present in various complex workloads, such as in-memory databases, cognitive, and cloud-enabled applications.

The Power S922 (9009-22G), Power S914 (9009-41G), and Power S924 (9009-42G) servers use the latest POWER9 processor technology to deliver unprecedented security, reliability, and manageability for your cloud and cognitive strategy and delivers industry-leading price and performance for your mission-critical workloads. The high data transfer rates that are offered by the PCIe Gen 4 internal switches provide higher I/O performance or consolidation of the I/O demands on to fewer adapters running at higher rates. This situation can result in better system performance at a lower cost when I/O demands are high.

The Power S922 (9009-22G) server delivers the outstanding performance of the POWER9 processor in a dense 2U (EIA units), rack-optimized form factor that is ideal for running multiple application workloads with security and reliability, and is cloud-enabled with integrated virtualization capabilities. There is a special configuration for IBM i with one active core that replaces the similar 1-core IBM POWER8® processor that is based on the IBM Power System S812.

The Power S914 (9009-41G) server is a powerful, single-socket server with the high performance and flexibility to meet today's growth and tomorrow's processing needs. You can use this cloud-enabled server to build an agile, containerized cloud on a server platform that is optimized for data and cognitive services.

The Power S924 (9009-42G) server is a powerful 2-socket server that includes up to 24 cores and powerful PCIe Gen 4 I/O slots to meet high-performance and high-bandwidth I/O demands. It also offers a wide range of storage backplanes options to meet your capacity needs. This server is offered in a 4U, rack-optimized form factor.

## 1.1  Systems overview

The following sections provide detailed information about the Power S922 (9009-22G), Power S914 (9009-41G), and Power S924 (9009-42G) servers.

## 1.1.1  Power S922 server

The Power S922 (9009-22G) server is a powerful one or two-socket server that includes up to 22 activated cores. If only one socket is populated at the time of the order, the second socket can be populated later. It has the I/O configuration flexibility to meet today's growth and tomorrow's processing needs. This server supports two processor sockets, offering a special one 4-core system configuration running 2.8 - 3.8 GHz, and up to two processor sockets of 8-core, 10-core, or 11-core processors running 2.8 - 3.9 GHz in a 19-inch rack-mount, 2U drawer configuration. All the cores are active.

There is a special configuration with one activated core that supports the IBM i operating system software tier P05 and replace the previous POWER8 one core offering that is based on the Power S812 server. Feature code #EP5Y must be selected, and it includes a 4-core POWER9 processor that is limited to one core activation (#EP6Y). The server in such configuration runs IBM i natively and Virtual I/O Server is not supported.

For the 8-, 10-, or 11-core processor configuration #EP58, #EP59, and #EP5B (software tier P10) VIOS is required to run IBM i. There are also limitations to the maximum size of the partition. Up to four cores per IBM i partition are supported. Multiple IBM i partitions can be created and run concurrently.

The Power S922 server supports a maximum of 32 DDR4 registered DIMM (RDIMM) slots. If only one processor socket is populated, then only 16 RDIMMs can be used. The memory features that are supported are 16 GB, 32 GB, 64 GB, and 128 GB, and run at speeds of , 2133, 2400 and 2666 Mbps, offering a maximum system memory of 2 TB if one socket is single-chip populated and 4 TB with both sockets populated.

The IBM Active Memory Expansion feature enables memory expansion by using compression and decompression of memory content, which can effectively expand the maximum memory capacity if extra server workload capacity and performance are available.

Note: Active Memory Expansion is not available for IBM i and Linux.

The following features are available for the storage backplane:

- #EJ1F: Eight SFF-3 bays with an optional split card (#EJ1H)
- #EJ1G: Eight SFF-3 bays with up to 7.2 GB write cache
- #EJ1H: Split #EJ1F to 4+4 SFF-3 Bays. Requires second SAS controller
- #EJ1V: Two NVMe U.2 drive slots
- #EJ1W: Four NVMe U.2 drive slots

The NVMe options offer fast boot times and are ideally suited for the rootvg of Virtual I/O Server (VIOS) partitions.

The Power S922 server is shown in Figure 1-1.

Figure 1-1   Front view of the Power S922 server

<!-- image -->

## 1.1.2  Power S914 server

The Power S914 (9009-41G) server is a powerful, one-socket server that includes up to eight activated cores. It has the I/O configuration flexibility to meet today's growth and tomorrow's processing needs. A one-socket system with a 4-core or 6-core POWER9 processor is available in either rack (19-inch rack-mount 4U) or tower configurations. The 8-core higher performance system is available only in a rack configuration.

The Power S914 server supports a maximum of 16 DDR4 error-correcting code (ECC) RDIMM slots. The memory features that are supported are 16 GB, 32 GB, and 64 GB, and run at speeds of 2133, 2400 and 2666 Mbps, offering a maximum system memory of 1 TB.

If you use the 4-core processor #EP50, the system is limited to a maximum of 64 GB of RAM per system. You must select one of the following memory options:

- Two or 4 of #EM62 (16 GB)
- Two of #EM63 (32 GB)

The Active Memory Expansion feature enables memory expansion by using compression and decompression of memory content, which can effectively expand the maximum memory capacity if extra server workload capacity and performance are available.

Note: Active Memory Expansion is not available for IBM i and Linux.

Several different features are available for the storage backplane:

- #EJ1C: Twelve SFF-3 bays with an optional split card (#EJ1E)
- #EJ1D: Eighteen SFF-3 bays/Dual IOA with Write Cache
- #EJ1E: Twelve SFF-3 bays/RDX bays Split feature to 6+6 small form factor (SFF) bays: Adds a second SAS Controller.
- #EJ1M: Twelve SFF-3 bays/RDX bay/2 EXT PT.
- #EJ1S: Gen 4 Backplane with six SFF-3 bays and two NVMe U.2 drives
- #EJ1T: Two NVMe U.2 drive slots
- #EJ1U: Four NVMe U.2 drive slots

The NVMe option offers fast boot times and is ideally suited for the rootvg of VIOS partitions.

For more information about the NVMe technology, see 2.6.8, 'NVMe support' on page 118.

The Power S914 tower server is shown in Figure 1-2.

Figure 1-2   The Power S914 tower

<!-- image -->

## 1.1.3  Power S924 server

The Power S924 (9009-42G) server is a powerful one- or two-socket server that includes up to 24 activated cores. It has the I/O configuration flexibility to meet today's growth and tomorrow's processing needs. This server supports two processor sockets, offering 8 or 16 cores at 3.8 - 4.0 GHz, 10 or 20 cores at 3.5 - 3.9 GHz, 11 or 22 cores at 3.45 - 3.9 GHz, or the maximum core configuration with 12 or 24 cores at 3.4 - 3.9 GHz. The systems are in a 19-inch rack-mount, 4U drawer configuration. All the cores are active.

The Power S924 server supports a maximum of 32 DDR4 RDIMM slots per processor socket that is populated. The memory features that are supported are 16 GB, 32 GB, 64 GB, and 128 GB, offering a maximum system memory of 4 TB.

The Active Memory Expansion feature enables memory expansion by using compression and decompression of memory content, which can effectively expand the maximum memory capacity if more server workload capacity and performance are available.

Note: Active Memory Expansion is not available for IBM i and Linux.

Several different features are available for the storage backplane:

- #EJ1C: Twelve SFF-3 bays with an optional split card (#EJ1E)
- #EJ1D: Eighteen SFF-3 bays/Dual IOA with Write Cache

- #EJ1E: Split feature to 6+6 SFF bays
- Twelve SFF-3 bays/RDX bay/2 EXT PT: Adds a second SAS Controller.
- #EJ1M: Twelve SFF-3 bays/RDX bays
- #EJ1S: Gen 4 Backplane with six SFF-3 bays and two NVMe U.2 drives
- #EJ1T: Two NVMe U.2 drive slots
- #EJ1U: Four NVMe U.2 drive slots

The Power S924 server is shown in Figure 1-3.

Figure 1-3   Front view of the Power S924 server

<!-- image -->

## 1.1.4  Common features

Many features are common to all the servers in this book, and some of them are described in this section.

## No internal DVD option

There is no internal DVD option, although an external USB DVD drive is available as feature code #EUA5. Customers are encouraged to use USB flash drives to install OSs and VIOS whenever possible because they are much faster than a DVD.

## The operator panel

The operator panel is now composed of two parts. All the servers have the first part, which provides the power switch and LEDs, as shown in Figure 1-4.

Figure 1-4   Operator panel: Power switch and LEDs

<!-- image -->

The second part is an LCD panel with three buttons, as shown in Figure 1-5.

Figure 1-5   Operator panel: LCD and switches

<!-- image -->

The LCD panel is mandatory in the Power S914 tower. It is also required if the server runs IBM i. In the Power S922, Power S914, and Power S924 rack-mounted servers, it is optional, but if a rack contains any of these servers, one of them must have an LCD panel.

The LCD panel can be moved (by using the correct procedure) from one server to another server, which enables appropriate service to be carried out.

## 1.2  Operating environment

Table 1-1 list the electrical characteristics of the Power S922, Power S914, and Power S924 servers.

Table 1-1   Electrical characteristics for Power S922, Power S914, and Power S924 servers

| Electrical characteristics   | Properties                         | Properties                                                                             | Properties                         |
|------------------------------|------------------------------------|----------------------------------------------------------------------------------------|------------------------------------|
| Electrical characteristics   | Power S922 server                  | Power S914 server                                                                      | Power S924 server                  |
| Operating voltage            | 1400 Wpower supply: 200 - 240 V AC | 900 Wpower supply: 100 - 127 V AC or 200 - 240 V AC 1400 Wpower supply: 200 - 240 V AC | 1400 Wpower supply: 200 - 240 V AC |
| Operating frequency          | 47/63 Hz                           | 47/63 Hz                                                                               | 47/63 Hz                           |
| Thermal output               | 6,416 Btu/hour (maximum)           | 5,461 Btu/hour (maximum)                                                               | 9,386 Btu/hour (maximum)           |
| Power consumption            | 1880 watts (maximum)               | 1600 watts (maximum)                                                                   | 2750 watts (maximum)               |
| Power-source loading         | 1.94 kVa (maximum configuration)   | 1.65 kVa (maximum configuration)                                                       | 2.835 kVa (maximum configuration)  |
| Phase                        | Single                             | Single                                                                                 | Single                             |

Note: The maximum measured value is the worst-case power consumption that is expected from a fully populated server under an intensive workload. The maximum measured value also accounts for component tolerance and non-ideal operating conditions. Power consumption and heat load vary greatly by server configuration and utilization. The IBM Systems Energy Estimator should be used to obtain a heat output estimate that is based on a specific configuration.

Table 1-2 lists the environment requirements for the servers.

Table 1-2   Environment requirements for Power S922, Power S914, and Power S924 servers

Table 1-3 lists the noise emissions for the systems.

| Environment                | Recommended operating                                                      | Allowable operating   | Non-operating         |
|----------------------------|----------------------------------------------------------------------------|-----------------------|-----------------------|
| Temperature                | 18 - 27°C (64.4 - 80.6°F)                                                  | 5 - 40°C (41 - 104°F) | 5 - 45°C (41 - 113°F) |
| Humidity range             | 5.5°C (42°F) dewpoint (DP) to 60% relative humidity (RH) or 15°C (59°F) DP | 8% - 85% RH           | 8% - 80% RH           |
| Maximum DP                 | N/A                                                                        | 24°C (75°F)           | 27°C (80°F)           |
| Maximum operating altitude | N/A                                                                        | 3050 m (10000 ft)     | N/A                   |

Table 1-3   Noise emissions for Power S922, Power S914, and Power S924 servers

| Product            | Declared A-weighted sound power level, L WAd a (B) b   | Declared A-weighted sound power level, L WAd a (B) b   | Declared A-weighted sound pressure level, L pAm (dB) c   | Declared A-weighted sound pressure level, L pAm (dB) c   |
|--------------------|--------------------------------------------------------|--------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
|                    | Operating                                              | Idle                                                   | Operating                                                | Idle                                                     |
| Power S922         | 7.8                                                    | 6.9                                                    | 61                                                       | 53                                                       |
| Power S914 (tower) | 5.8                                                    | 5.3                                                    | 39                                                       | 34                                                       |
| Power S914 (rack)  | 5.9                                                    | 5.3                                                    | 41                                                       | 34                                                       |
| Power S924         | 6.4                                                    | 5.2                                                    | 46                                                       | 34                                                       |

- a. Declared level L WAd  is the upper-limit A-weighted sound power level. Declared level L pAm is the mean A-weighted emission sound pressure level that is measured at the 1-meter bystander positions.
- b. All measurements are made in conformance with ISO 7779 and declared in conformance with ISO 9296.
- c. 10 dB (decibel) equals 1 B (bel).

Important: NVMePCIeadapters (EC5G, EC5B, EC5C, EC5D, EC5E, EC5F, EC6U, EC6V, EC6W, EC6X, EC6Y, EC6Z) require higher fan floors to compensate for their higher thermal output. This may affect the accoustic output of the server depending on the configuration. The e-config tool should be used to ensure a suitable configuration.

NVMe U.2 drives (ES1G, EC5V, ES1H, EC5W) also require additional cooling to compensate for their higher thermal output.

## 1.3  Physical package

The Power S914 server is available in both rack-mount and tower form factors. The Power S922 and Power S924 servers are available in rack-mount form factor only.

## 1.3.1 Tower model

Table 1-4 shows the physical dimensions of the Power S914 tower chassis.

Table 1-4   Physical dimensions of the Power S914 tower chassis

| Dimension                       | Power S914 server (9009-41G)   |
|---------------------------------|--------------------------------|
| Width                           | 182.4mm (7.18 in.)             |
| Width with stand                | 328.5 mm (12.93 in.)           |
| Depth                           | 751.7 mm (29.59 in.)           |
| Depth with front-rotatable door | 814.7 mm (32.07 in.)           |
| Height                          | 486.1 mm (19.14 in.)           |
| Height with handle              | 522 mm (20.55 in.)             |
| Weight                          | 46.94 kg (103.5 lb)            |

## 1.3.2  Rack-mount model

Table 1-5 shows the physical dimensions of the Power S922 rack-mounted chassis. The server is available only in a rack-mounted form factor and takes 2U of rack space.

Table 1-5   Physical dimensions of the Power S922 rack-mounted chassis

| Dimension   | Power S922 server (9009-22G)   |
|-------------|--------------------------------|
| Width       | 482 mm (18.97 in.)             |
| Depth       | 766.5 mm (30.2 in.)            |
| Height      | 86.7 mm (3.4 in.)              |
| Weight      | 30.4 kg (67 lb)                |

Figure 1-6 show the front view of the Power S922 server.

Figure 1-6   Front view of the Power S922 server

<!-- image -->

Table 1-6 shows the physical dimensions of the rack-mounted Power S914 and Power S924 chassis. The server is available only in a rack-mounted form factor and takes 4U of rack space.

Table 1-6   Physical dimensions of the rack-mounted Power S914 and Power S924 chassis

| Dimension   | Power S914 server (9009-41G)   | Power S924 server (9009-42G)   |
|-------------|--------------------------------|--------------------------------|
| Width       | 482 mm(18.97 in.)              | 482 mm (18.97 in.)             |
| Depth       | 769.6 mm (30.3 in.)            | 769.6 mm (30.3 in.)            |

| Dimension   | Power S914 server (9009-41G)   | Power S924 server (9009-42G)   |
|-------------|--------------------------------|--------------------------------|
| Height      | 173.3 mm (6.8 in.)             | 173.3 mm (6.8 in.)             |
| Weight      | 36.3 kg (80 lb)                | 39.9 kg (88 lb)                |

Figure 1-7 shows the front view of the Power S924 server.

Figure 1-7   Front view of the Power S924 server

<!-- image -->

## 1.4 System features

The system chassis contains one processor module (Power S914 server) or up to two processor modules (Power S922 and Power S924 servers). Each of the POWER9 processor chips in the server has a 64-bit architecture, up to 512 KB of L2 cache per core, and up to 10 MB of L3 cache per core. All the cores are active.

## 1.4.1 Power S922 server features

This summary describes the standard features of the Power S922 server:

- POWER9 processor-based modules:
- -4-core typical 2.8 - 3.8 GHz (maximum) POWER9 processor.
- -8-core typical 3.4 - 3.9 GHz (maximum) POWER9 processor.
- -10-core typical 2.9 - 3.8 GHz (maximum) POWER9 processor.
- -11-core typical 2.8 - 3.8 GHz (maximum) POWER9 processor.
- -1-core typical 2.8 to 3.8 GHz (maximum) POWER9 processor (IBM i initial order).
- High-performance Mbps DDR4 ECC memory:
- -16 GB, 32 GB, 64 GB, or 128 GB memory. Different sizes and configurations run at different frequencies of 2133, 2400, and 2666 Mbps.
- -Up to 4 TB of DDR4 memory with two IBM POWER® processors.
- -Up to 2 TB of DDR4 memory with one POWER processor.
- Storage feature:
- -Storage Backplane Gen 4 with two or four NVMe U.2 drive slots.
- -Eight SFF bays, one integrated SAS controller without cache, and JBOD, RAID 0, RAID 5, RAID 6, or RAID 10. Optionally, split the SFF-3 bays and add a second integrated SAS controller without cache.

- -Expanded Function Storage Backplane 8 SFF-3 bays/Single IOA with Write Cache. Optionally, attach an EXP12SX or EXP24SX SAS hard disk drive (HDD) or solid-state drive (SSD) Expansion Drawer to the single IOA.

- One PCIe3 NVMe carrier card can be ordered only with a storage backplane. If a PCIe3 NVMe carrier card is ordered with a storage backplane, then the optional split feature is not supported.
- PCIe slots with a single processor:
- -Three x16 Gen 4 low-profile (LP), half-length slots. (One of these slots is Coherent Accelerator Processor Interface (CAPI) capable.)
- -One x8 Gen 4 LP, half-length slot with x16 connector (CAPI-capable).
- -Four x8 Gen 4 LP, half-length slots. (One of these slots is used for the required base local area network (LAN) adapter.)
- PCIe slots with two processors:
- -Five x16 Gen 4 LP, half-length slots. (Three of these slots are CAPI-capable.)
- -Two x8 Gen 4 LP, half-length slots with x16 connectors. (One of these slots is CAPI-capable.)
- -Four x8 Gen 4 LP, half-length slots. (One of these slots is used for the required base LAN adapter.)
- Integrated:
- -Service processor.
- -EnergyScale technology.
- -Hot-plug and redundant cooling.
- -Two front USB 3.0 ports.
- -Two optional rear USB 3.0 ports.
- -Two Hardware Management Console (HMC) 1 GbE RJ45 ports.
- -One system port with a RJ45 connector.
- -Two hot-plug, redundant power supplies.
- -19-inch rack-mounting hardware (2U).

## 1.4.2 Power S914 server features

This summary describes the standard features of the Power S914 server:

- POWER9 processor-based modules:
- -4-core typical 2.3 - 3.8 GHz (maximum) POWER9 processor.
- -6-core typical 2.3 - 3.8 GHz (maximum) POWER9 processor.
- -8-core typical 2.8 - 3.8 GHz (maximum) POWER9 processor (rack-mounted configuration only).
- High-performance Mbps DDR4 ECC memory:
- -16 GB, 32 GB, or 64 GB memory.
- -Up to 1024 GB of DDR4 memory with one POWER processor.
- Storage feature:
- -Twelve SFF-3 bays/RDX bays. Optionally, split the SFF-3 bays and add a second integrated SAS controller without cache.
- -Eighteen SFF-3 bays/Dual IOA with Write Cache and External SAS port.

- -Twelve SFF-3 bays/RDX Bay/Dual IOA with Write Cache and External SAS port. Optionally, attach an EXP12SX or EXP24SX SAS HDD / SSD Expansion Drawer to the dual IOA.
- -#EJ1S: Gen 4 Backplane with six SFF-3 bays and two NVMe U.2 drives.
- -#EJ1T: Two NVMe U.2 drive slots.
- -#EJ1U: Four NVMe U.2 drive slots.
- PCIe slots with single processor:
- -Three x16 Gen 4 full-height, half-length (FHHL) slots. (One of these slots is CAPI-capable.)
- -One x8 Gen 4 FHHL slot with x16 connector (CAPI-capable).
- -Four x8 Gen 4 FHHL slots. (One of these slots is used for the required base LAN adapter.)
- Integrated:
- -Service processor.
- -EnergyScale technology.
- -Hot-swap and redundant cooling.
- -One front USB 3.0 port.
- -Two rear USB 3.0 ports.
- -Two HMC 1 GbE RJ45 ports.
- -One system port with a RJ45 connector.
- -Four hot-plug, redundant power supplies.
- -19-inch rack-mounting hardware (4U).

## 1.4.3  Power S924 server features

This summary describes the standard features of the Power S924 servers:

- POWER9 processor-based modules:
- -8-core typical 3.8 - 4.0 GHz (maximum) POWER9 processor.
- -10-core typical 3.5 - 3.9 GHz (maximum) POWER9 processor.
- -11-core typical 3.45 - 3.9 GHz (maximum) POWER9 processor.
- -12-core typical 3.4 - 3.9 GHz (maximum) POWER9 processor.
- High-performance Mbps DDR4 ECC memory:
- -16 GB, 32 GB, 64 GB, or 128 GB memory. Different sizes and configurations run at different frequencies of 2133, 2400, and 2666 Mbps.
- -Up to 4 TB of DDR4 memory with two POWER processors.
- -Up to 2 TB of DDR4 memory with one POWER processor.
- Storage feature:
- -Base 12 SFF-3 bays/RDX bay. Optionally, split the SFF-3 bays and add a second integrated SAS controller without cache.
- -Expanded function 18 SFF-3 bays/Dual IOA with Write Cache and Optional External SAS port.

- -Expanded function 12 SFF-3 bays/RDX Bay/Dual IOA with Write Cache and Optional External SAS port. Optionally, attach an EXP12SX or EXP24SX SAS HDD / SSD Expansion Drawer to the dual IOA.
- -#EJ1S: Gen 4 Backplane with six SFF-3 bays and two NVMe U.2 drives.
- -#EJ1T: Two NVMe U.2 drive slots.
- -#EJ1U: Four NVMe U.2 drive slots.
- PCIe slots with a single processor:
- -Three x16 Gen 4 FHHL slots. (One of these slots is CAPI-capable.)
- -One x8 Gen 4 FHHL slot with x16 connector (CAPI-capable).
- -Four x8 Gen 4 FHHL slots. (One of these slots is used for the required base LAN adapter.)
- PCIe slots with two processors:
- -Five x16 Gen 4 FHHL slots. (Three of these slots are CAPI-capable.)
- -Two x8 Gen 4 FHHL slots with x16 connectors. (One of these slots is CAPI-capable.)
- -Four x8 Gen 4 FHHL slots. (One of these slots is used for the required base LAN adapter.)
- Integrated:
- -Service processor.
- -EnergyScale technology.
- -Hot-swap and redundant cooling.
- -One front USB 3.0 port.
- -Two rear USB 3.0 ports.
- -Two HMC 1 GbE RJ45 ports.
- -One system port with a RJ45 connector.
- -Four hot-plug, redundant power supplies.
- -19-inch rack-mounting hardware (4U).

## 1.5  Minimum features

The minimum Power S922 or Power S914 initial order must include a processor module (four cores is the minimum), two 16 GB DIMMs, two power supplies and power cords, an OS indicator, a cover set indicator, and a Language Group Specify. Also, it must include one of the following storage options and one of the following network options:

- Storage options:
- -For boot from NVMe: One NVMe carrier and one NVMe U.2 Module.
- -For boot from a local SFF-3 HDD/SDD: One storage backplane and one SFF-3 HDD or SDD.
- -For boot from SAN: An internal HDD or SSD and RAID card are not required if Boot from SAN (#0837) is selected. A Fibre Channel (FC) adapter must be ordered if #0837 is selected.

- Network options:
- -One PCIe2 4-port 1 Gb Ethernet adapter.
- -One of the supported 10 Gb Ethernet adapters.

The minimum Power S924 initial order must include a processor module, two 16 GB DIMMs, four power supplies and power cords, an OS indicator, a cover set indicator, and a Language Group Specify. Also, it must include one of the following storage options and one of the following network options:

- Storage options:
- -For boot from NVMe: One NVMe carrier and one NVMe U.2 Module.
- -For boot from a local SFF-3 HDD/SDD: One storage backplane and one SFF-3 HDD or SDD.
- -For boot from SAN: An internal HDD or SSD and RAID card are not required if Boot from SAN (#0837) is selected. An FC adapter must be ordered if #0837 is selected.
- Network options:
- -One PCIe2 4-port 1 Gb Ethernet adapter.
- -One of the supported 10 Gb Ethernet adapters.

## 1.5.1  Power supply features

The Power S922 server supports two 1400 W 200 - 240 V AC (#EB2M) power supplies. Two power supplies are always installed. One power supply is required during the boot phase and for normal system operation, and the second is for redundancy.

The Power S914 server supports the following power supplies:

- Four 900 W 100 - 127 V AC or 200 - 240 V AC options (#EB2L) power supplies supporting a tower chassis. Two power supplies are required during the boot phase and for normal system operation, and the third and fourth ones are for redundancy.
- Two 1400 W 200 - 240 V AC options (#EB2M) power supplies supporting a rack chassis. One power supply is required during the boot phase and for normal system operation, and the second one is for redundancy.

The Power S924 server supports four 1400 W 200 - 240 V AC (#EB2M) power supplies. Four power supplies are always installed. Two power supplies are required during the boot phase and for normal system operation, and the third and fourth ones are for redundancy.

Note: If one of the redundant power supplies might fail, an Early Power Off Warning (EPOW) is sent to the service processor and the server runs a shutdown.

## 1.5.2  Processor module features

The following section describes the processor modules that are available for the Power S922, Power S914, and Power S924 servers.

## Power S922 processor modules

A maximum of one processor with four processor cores (#EP56), or a maximum of two processors of either eight processor cores (#EP58),10 processor cores (#EP59), or 11 processor cores (#EP5B) is allowed. All processor cores must be activated.

The following list defines the allowed quantities of processor activation entitlements:

- One 4-core typical 2.8 - 3.8 GHz (maximum) processor (#EP56) requires that four processor activation codes be ordered. A maximum of four processor activations (#EP66) is allowed.
- One 8-core typical 3.4 - 3.9 GHz (maximum) processor (#EP58) requires that eight processor activation codes be ordered. A maximum of eight processor activations (#EP68) is allowed.
- Two 8-core typical 3.4 - 3.9 GHz (maximum) processors (#EP58) require that 16 processor activation codes be ordered. A maximum of 16 processor activations (#EP68) is allowed.
- One 10-core typical 2.9 - 3.8 GHz (maximum) processor (#EP59) requires that 10 processor activation codes be ordered. A maximum of 10 processor activation feature codes (#EP69) is allowed.
- Two 10-core typical 2.9 - 3.8 GHz (maximum) processors (#EP59) require that 20 processor activation codes be ordered. A maximum of 20 processor activation feature codes (#EP69) is allowed.
- Two 11-core typical 2.8 - 3.8 GHz (maximum) processors (#E5PB) require that 22 processor activation codes be ordered. A maximum of 22 processor activation feature codes (#EP6B) is allowed.

Table 1-7 summarizes the processor features that are available for the Power S922 server.

Table 1-7   Processor features for the Power S922 server

| Feature code   | Processor module description                             |
|----------------|----------------------------------------------------------|
| #EP56          | 4-core typical 2.8 - 3.8 GHz (maximum) POWER9 processor  |
| #EP58          | 8-core typical 3.4 - 3.9 GHz (maximum) POWER9 processor  |
| #EP59          | 10-core typical 2.9 - 3.8 GHz (maximum) POWER9 processor |
| #EP5B          | 11-core typical 2.8 - 3.8 GHz (maximum) POWER9 processor |
| #EPSY          | 1-core typical 2.8 - 3.8 GHz (maximum) POWER9 processor  |
| #EP66          | One processor entitlement for #EP56                      |
| #EP68          | One processor entitlement for #EP58                      |
| #EP69          | One processor entitlement for #EP59                      |
| #EP6B          | One processor entitlement for #EP5B                      |

## Power S914 processor modules

A maximum of one processor with four processor cores (#EP50), one processor with six processor cores (#EP51), or one processor with eight processor cores (#EP52) is allowed. All processor cores must be activated.

The following list defines the allowed quantities of processor activation entitlements:

- One 4-core typical 2.3 - 3.8 GHz (maximum) processor (#EP50) requires that four processor activation codes be ordered. A maximum of four processor activations (#EP60) is allowed.
- One 6-core typical 2.3 - 3.8 GHz (maximum) processor (#EP51) requires that six processor activation codes be ordered. A maximum of six processor activation feature codes (#EP61) is allowed.
- One 8-core typical 2.8 - 3.8 GHz (maximum) processor (#EP52) requires that eight processor activation codes be ordered. A maximum of eight processor activation feature codes (#EP62) is allowed.

Table 1-8 summarizes the processor features that are available for the Power S914 server.

Table 1-8   Processor features for the Power S914 server

| Feature code   | Processor module description                            |
|----------------|---------------------------------------------------------|
| #EP50          | 4-core typical 2.3 - 3.8 GHz (maximum) POWER9 processor |
| #EP51          | 6-core typical 2.3 - 3.8 GHz (maximum) POWER9 processor |
| #EP52          | 8-core typical 2.8 - 3.8 GHz (maximum) POWER9 processor |
| #EP60          | One processor entitlement for #EP50                     |
| #EP61          | One processor entitlement for #EP51                     |
| #EP62          | One processor entitlement for #EP52                     |

## Power S924 processor modules

A maximum of two processors with eight processor cores (#EP1E), two processors with 10 processor cores (#EP1F), or two processors with 12 processor cores (#EP1G) is allowed. All processor cores must be activated.

The following list defines the allowed quantities of processor activation entitlements:

- One 8-core typical 3.8 - 4.0 GHz (maximum) processor (#EP5E) requires that eight processor activation codes be ordered. A maximum of eight processor activations (#EP6E) is allowed.
- Two 8-core typical 3.8 - 4.0 GHz (maximum) processors (#EP5E) require that 16 processor activation codes be ordered. A maximum of 16 processor activations (#EP6E) is allowed.
- One 10-core typical 3.5 - 3.9 GHz (maximum) processor (#EP5F) requires that 10 processor activation codes be ordered. A maximum of 10 processor activation feature codes (#EP6F) is allowed.
- Two 10-core typical 3.5 - 3.9 GHz (maximum) processors (#EP5F) require that 20 processor activation codes be ordered. A maximum of 20 processor activation feature codes (#EP6F) is allowed.
- One11-core typical 3.45 - 3.9 GHz (maximum) processors (#EP5H) require that 22 processor activation codes be ordered. A maximum of 22 processor activation feature codes (#EP6H) is allowed.
- One12-core typical 3.4 - 3.9 GHz (maximum) processors (#EP1G) require that 24 processor activation codes be ordered. A maximum of 24 processor activation feature codes (#EP4G) is allowed.

Table 1-9 summarizes the processor features that are available for the Power S924 server.

Table 1-9   Processor features for the Power S924 server

| Feature code   | Processor module description                              |
|----------------|-----------------------------------------------------------|
| #EP1E          | 8-core typical 3.8 - 4.0 GHz (maximum) POWER9 processor   |
| #EP1F          | 10-core typical 3.5 - 3.9 GHz (maximum) POWER9 processor  |
| #EP1H          | 11-core typical 3.45 - 3.9 GHz (maximum) POWER9 processor |
| #EP1G          | 12-core typical 3.4 - 3.9 GHz (maximum) POWER9 processor  |
| #EP4E          | One processor entitlement for #EP1E                       |
| #EP4F          | One processor entitlement for #EP1F                       |
| #EP4H          | One processor entitlement for #EP1H                       |
| #EP4G          | One processor entitlement for #EP1G                       |

## 1.5.3  Memory features

A minimum of 32 GB of memory is required on the Power S922, Power S914, and Power S924 servers. Memory upgrades require memory pairs. The base memory is two 16 GB DDR4 memory modules (#EM62).

Table 1-10 lists the memory features that are available for the Power S922, Power S914, and Power S924 servers.

Table 1-10   Summary of memory features for Power S922, Power S914, and Power S924 servers

| Feature code   | DIMM capacity   |   Minimum quantity | Maximum quantity Power S922, and Power S924 and Power S914 servers   |
|----------------|-----------------|--------------------|----------------------------------------------------------------------|
| #EM62          | 16 GB           |                  0 | 32/16 a                                                              |
| #EM63          | 32 GB           |                  0 | 32/16                                                                |
| #EM64          | 64 GB           |                  0 | 32/16                                                                |
| #EM65 b        | 128 GB          |                  0 | 32/0                                                                 |

- a. The maximum number of DIMMs for the S914 is 16.
- b. The memory #EM65 is not available for the Power S914 server.

Note: Different sizes and configurations run at different frequencies of 2133, 2400, and 2666 Mbps.

## 1.5.4 Peripheral Component Interconnect Express slots

The following section describes the available PCIe slots:

- The Power S922 server has up to 11 PCIe hot-plug slots. The 2U height of the server allows only for the installation of PCIe adapters in the half-height half-length (HHHL) LP form factor.
- -With two POWER9 processor single-chip modules (SCMs), 11 PCIe slots are available:
- Three x16 Gen 4 CAPI-capable slots with each directly connected to an SCM.
- One x8 Gen 4 with x16 connector CAPI-capable slot that is directly connected to an SCM.
- One x8 Gen 4 with x16 connector slot that is directly connected to an SCM.
- Two x16 Gen 4 slots that are connected to an internal Gen 4 switch.
- Four x8 Gen 4 slots that are connected to an internal Gen 4 switch.
- -With one POWER9 processor SCM, eight PCIe slots are available:
- One x16 Gen 4 CAPI-capable slot that is directly connected to an SCM.
- One x8 Gen 4 with x16 connector CAPI-capable slot that is directly connected to an SCM.
- Two x16 Gen 4 slots that are connected to an internal Gen 4 switch.
- Four x8 Gen 4 slots that are connected to an internal Gen 4 switch.
- The tower or the rack configuration of the Power S914 supports the installation of PCIe adapters with FHHL form factor:
- -The single POWER9 processor SCM of a Power S914 server provides PCIe connectivity to eight PCIe hot-plug slots:
- One x16 Gen 4 CAPI-capable slot that is directly connected to an SCM.
- One x8 Gen 4 with x16 connector CAPI-capable slot that is directly connected to an SCM.
- Two x16 Gen 4 slots that are connected to an internal Gen 4 switch.
- Four x8 Gen 4 slots that are connected to an internal Gen 4 switch.
- The Power S924 server has up to 11 PCIe hot-plug slots that support the installation of PCIe adapters with FHHL form factor only:
- -With two POWER9 processor SCMs, 11 PCIe slots are available:
- Three x16 Gen 4 CAPI-capable slots with each directly connected to an SCM.
- One x8 Gen 4 with x16 connector CAPI-capable slot that is directly connected to an SCM.
- One x8 Gen 4 with x16 connector slot that is directly connected to an SCM.
- Two x16 Gen 4 slots that are connected to an internal Gen 4 switch.
- Four x8 Gen 4 slots that are connected to an internal Gen 4 switch.
- -With one POWER9 processor SCM, eight PCIe slots are available:
- One x16 Gen 4 CAPI-capable slot that is directly connected to an SCM.
- One x8 Gen 4 with x16 connector CAPI-capable slot that is directly connected to an SCM.

- Two x16 Gen 4 slots that are connected to an internal Gen 4 switch.
- Four x8 Gen 4 slots that are connected to an internal Gen 4 switch.

The x16 slots can provide up to twice the bandwidth of x8 slots because they offer twice as many PCIe lanes. PCIe Gen 4 slots can support up to twice the bandwidth of a PCIe Gen3 slot, and PCIe Gen3 slots can support up to twice the bandwidth of a PCIe Gen2 slot, assuming an equivalent number of PCIe lanes.

At least one PCIe Ethernet adapter is required on the server by IBM to ensure correct manufacturing, testing, and support of the server. One of the x8 PCIe slots is used for this required adapter.

These servers are smarter about energy efficiency when cooling the PCIe adapter environment. They sense which IBM PCIe adapters are installed in their PCIe slots and, if an adapter requires higher levels of cooling, they automatically speed up fans to increase airflow across the PCIe adapters. Faster fans increase the sound level of the server.

## 1.6  Disk and media features

Five backplane options are available for the Power S922 servers:

- Base Storage Backplane 8 SFF-3 bays (#EJ1F)
- 4 + 4 SFF-3 bays split backplane (#EJ1H)
- Expanded function Storage Backplane 8 SFF-3 bays/Single IOA with Write Cache (#EJ1G)
- Storage Backplane Gen 4 with two NVMe U.2 drive slots (#EJ1V)
- Storage Backplane Gen 4 with four NVMe U.2 drive slots (#EJ1W)

The Storage Backplane option (#EJ1F) provides eight SFF-3 bays and one SAS controller with zero write cache.

By optionally adding the Split Backplane (#EJ1H), a second integrated SAS controller with no write cache is provided, and the eight SSF-3 bays are logically divided into two sets of four bays. Each SAS controller independently runs one of the four-bay sets of drives.

Seven backplane options are available for the Power S914 and Power S924 servers:

- Base Storage Backplane 12 SFF-3 bays/RDX bay (#EJ1C)
- 6 +6 SFF-3 bays split backplane for #EJ1C (#EJ1E)
- Expanded function Storage Backplane 18 SFF-3 bays/Dual IOA with Write Cache and optional external SAS port (#EJ1D)
- Expanded function Storage Backplane 12 SFF-3 bays/RDX bay/Dual IOA with Write Cache and optional external SAS port (#EJ1M)
- Storage Backplane Gen 4 with six SFF-3 Bays and two NVMe U.2 drive slots (#EJ1S)
- Storage Backplane Gen 4 with two NVMe U.2 drive slots (#EJ1T)
- Storage Backplane Gen 4 with four NVMe U.2 drive slots (#EJ1U)

The Base Storage Backplane option (#EJ1C) provides 12 SFF-3 bays and one SAS controller with zero write cache.

By optionally adding the Split Backplane (#EJ1E), a second integrated SAS controller with no write cache is provided, and the 12 SSF-3 bays are logically divided into two sets of six bays. Each SAS controller independently runs one of the six-bay sets of drives.

The backplane options provide SFF-3 SAS bays in the system unit. These 2.5-inch or SFF SAS bays can contain SAS drives (HDD or SSD) mounted on a Gen3 tray or carrier. Thus, the drives are designated SFF-3. SFF-1 or SFF-2 drives do not fit in an SFF-3 bay. All SFF-3 bays support concurrent maintenance or hot-plug capability.

These backplane options use leading-edge, integrated SAS RAID controller technology that is designed and patented by IBM. A custom-designed IBM PowerPC® based ASIC chip is the basis of these SAS RAID controllers, and provides RAID 5 and RAID 6 performance levels, especially for SSDs. Internally, SAS ports are implemented and provide plenty of bandwidth. The integrated SAS controllers are placed in dedicated slots and do not reduce the number of available PCIe slots.

This backplane option supports HDDs or SSDs or a mixture of HDDs and SSDs in the SFF-3 bays. Mixing HDDs and SSDs applies even within a single set of six bays of the split backplane option.

Note: If you mix HDDs and SSDs, they must be in separate arrays (unless you use the IBM Easy Tier® function).

This backplane option can offer different drive protection options: RAID 0, RAID 5, RAID 6, or RAID 10. RAID 5 requires a minimum of three drives of the same capacity. RAID 6 requires a minimum of four drives of the same capacity. RAID 10 requires a minimum of two drives. Hot-spare capability is supported by RAID 5, RAID 6, and RAID 10.

This backplane option is supported by AIX and Linux, VIOS, and IBM i. It is highly recommended but not required that the drives be protected. With IBM i, all drives are required to be protected by either RAID or mirroring.

Unlike the hot-plug PCIe slots and SAS bays, concurrent maintenance is not available for the integrated SAS controllers. Scheduled downtime is required if a service action is required for these integrated resources.

In addition to supporting HDDs and SSDs in the SFF-3 SAS bays, the Expanded Function Storage Backplane (#EJ1G) supports the optional attachment of an EXP12SX or EXP24SX Expansion Drawer. All bays are accessed by both of the integrated SAS controllers. The bays support concurrent maintenance (hot-plug).

Note: FC EC5X will be an important new entry level point for NVMe to boot AIX, Linux, and VIOS.

Table 1-11 shows the available disk drive feature codes that can be installed in the Power S922 (9009-22G) server.

Table 1-11   Disk drive feature code description for the Power S922 (9009-22G) server

| Feature code   | CCIN   | Description                                                 |   Maximum | OS support    |
|----------------|--------|-------------------------------------------------------------|-----------|---------------|
| ESNJ           | 5B41   | 283 GB 15K RPM SAS SFF-3 4K Block Cached Disk Drive (IBM i) |         8 | IBM i         |
| 1953           | 19B1   | 300 GB 15k RPM SAS SFF-2 Disk Drive (AIX/Linux)             |       672 | AIX and Linux |

| Feature code   | CCIN   | Description                                                      |   Maximum | OS support            |
|----------------|--------|------------------------------------------------------------------|-----------|-----------------------|
| ESDB           | 59E0   | 300 GB 15 K RPM SAS SFF-3 Disk Drive (AIX/Linux)                 |         8 | AIX and Linux         |
| ESEZ           | 59C9   | 300 GB 15 K RPM SAS SFF-2 4 K Block - 4096 Disk Drive            |       672 | AIX and Linux         |
| ESNK           | 5B41   | 300 GB 15 K RPM SAS SFF-3 4k Block Cached Disk Drive (AIX/Linux) |         8 | AIX and Linux         |
| ESNM           | 5B43   | 300 GB 15 K RPM SAS SFF-2 4k Block Cached Disk Drive (AIX/Linux) |       672 | AIX and Linux         |
| ESFB           | 59E1   | 300 GB 15 K RPM SAS SFF-3 4 K Block - 4096 Disk Drive            |         8 | AIX and Linux         |
| ES90           | 5B13   | 387 GB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                 |         8 | AIX, IBM i, and Linux |
| ES94           | 5B10   | 387 GB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ESB0           | 5B19   | 387 GB Enterprise SAS 5xx SFF-3 SSD for AIX/Linux                |         8 | AIX, IBM i, and Linux |
| ESB2           | 5B16   | 387 GB Enterprise SAS 5xx SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESB8           | 5B13   | 387 GB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                 |         8 | AIX, IBM i, and Linux |
| ESBA           | 5B10   | 387 GB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ESGT           | 5B19   | 387 GB Enterprise SAS 5xx SFF-3 SSD for AIX/Linux                |         8 | AIX, IBM i, and Linux |
| ESGV           | 5B16   | 387 GB Enterprise SAS 5xx SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| 1964           | 19B3   | 600 GB 10k RPM SAS SFF-2 Disk Drive (AIX/Linux)                  |       672 | AIX and Linux         |
| ESD5           | 59D0   | 600 GB 10K RPM SAS SFF-3 Disk Drive (AIX/Linux)                  |         8 | AIX and Linux         |
| ESEV           | 59D2   | 600 GB 10K RPM SAS SFF-2 Disk Drive 4 K Block - 4096             |       672 | AIX and Linux         |
| ESF5           | 59D3   | 600 GB 10K RPM SAS SFF-3 Disk Drive 4 K Block - 4096             |         8 | AIX and Linux         |
| ESFF           | 59E5   | 600 GB 15 K RPM SAS SFF-3 4 K Block - 4096 Disk Drive            |         8 | AIX and Linux         |
| ESFP           | 59CC   | 600 GB 15 K RPM SAS SFF-2 4 K Block - 4096 Disk Drive            |       672 | AIX and Linux         |
| ESNP           | 5B45   | 600 GB 15 K RPM SAS SFF-3 4k Block Cached Disk Drive (AIX/Linux) |         8 | AIX and Linux         |
| ESNR           | 5B47   | 600 GB 15 K RPM SAS SFF-2 4k Block Cached Disk Drive (AIX/Linux) |       672 | AIX and Linux         |

| Feature code   | CCIN   | Description                                                      |   Maximum | OS support            |
|----------------|--------|------------------------------------------------------------------|-----------|-----------------------|
| ESB4           | 5B1A   | 775 GB Enterprise SAS 5xx SFF-3 SSD for AIX/Linux                |         8 | AIX, IBM i, and Linux |
| ESB6           | 5B17   | 775 GB Enterprise SAS 5xx SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESBE           | 5B14   | 775 GB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                 |         8 | AIX, IBM i, and Linux |
| ESBG           | 5B11   | 775 GB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ESGX           | 5B1A   | 775 GB Enterprise SAS 5xx SFF-3 SSD for AIX/Linux                |         8 | AIX, IBM i, and Linux |
| ESGZ           | 5B17   | 775 GB Enterprise SAS 5xx SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESNA           | 5B11   | 775 GB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ESNC           | 5B14   | 775 GB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                 |         8 | AIX, IBM i, and Linux |
| ESJ0           | 5B29   | 931 GB Mainstream SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ESJ8           | 5B2B   | 931 GB Mainstream SAS 4k SFF-3 SSD for AIX/Linux                 |         8 | AIX, IBM i, and Linux |
| ESF3           | 59DA   | 1.2TB10KRPMSASSFF-2DiskDrive4KBlock - 4096                       |       672 | AIX and Linux         |
| ESF9           | 59DB   | 1.2TB10KRPMSASSFF-3DiskDrive4KBlock - 4096                       |         8 | AIX and Linux         |
| ESBJ           | 5B15   | 1.55 TB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                |         8 | AIX, IBM i, and Linux |
| ESBL           | 5B12   | 1.55 TB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESNE           | 5B12   | 1.55 TB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESNG           | 5B15   | 1.55 TB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                |         8 | AIX, IBM i, and Linux |
| EC5G           | 58FC   | PCIe3 x8 LP 1.6 TB NVMe Flash adapter for AIX/Linux              |         5 | AIX, IBM i, and Linux |
| EC5X           | 5987   | Mainstream 800 GB SSD NVMe U.2 module for AIX/Linux              |         4 | AIX, IBM i, and Linux |
| ES1E           | 59B8   | 1.6 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for AIX/Linux |         4 | AIX, IBM i, and Linux |
| ESFT           | 59DD   | 1.8TB10KRPMSASSFF-2DiskDrive4KBlock - 4096                       |       672 | AIX and Linux         |
| ESFV           | 59DE   | 1.8TB10KRPMSASSFF-3DiskDrive4KBlock - 4096                       |         8 | AIX and Linux         |

| Feature code   | CCIN   | Description                                                      |   Maximum | OS support            |
|----------------|--------|------------------------------------------------------------------|-----------|-----------------------|
| ESJ2           | 5B21   | 1.86 TB Mainstream SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESJA           | 5B20   | 1.86 TB Mainstream SAS 4k SFF-3 SSD for AIX/Linux                |         8 | AIX, IBM i, and Linux |
| EC5C           | 58FD   | PCIe3 x8 LP 3.2 TB NVMe Flash adapter for AIX/Linux              |         5 | AIX, IBM i, and Linux |
| ES1G           | 59B9   | 3.2 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for AIX/Linux |         4 | AIX, IBM i, and Linux |
| ESJ4           | 5B2D   | 3.72 TB Mainstream SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESJC           | 5B2C   | 3.72 TB Mainstream SAS 4k SFF-3 SSD for AIX/Linux                |         8 | AIX, IBM i, and Linux |
| ES62           | 5B1D   | 3.86 - 4.0 TB 7200 RPM4KSASLFF-1Nearline Disk Drive (AIX/Linux)  |       336 | AIX and Linux         |
| EC5E           | 58FE   | PCIe3 x8 LP 6.4 TB NVMe Flash adapter for AIX/Linux              |         5 | AIX, IBM i, and Linux |
| EC5V           |        | 6.4 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for AIX/Linux |         4 | AIX, IBM i, and Linux |
| ESJE           | 5B2E   | 7.45 TB Mainstream SAS 4k SFF-3 SSD for AIX/Linux                |         8 | AIX, IBM i, and Linux |
| ESJ6           | 5B2F   | 7.45 TB Mainstream SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ES64           | 5B1F   | 7.72 - 8.0 TB 7200 RPM4KSASLFF-1Nearline Disk Drive (AIX/Linux)  |       336 | AIX and Linux         |
| 1818           | 19B3   | Quantity 150 of #1964                                            |         4 |                       |
| 1929           | 19B1   | Quantity 150 of #1953                                            |         4 |                       |
| ESPM           | 5B43   | Quantity 150 of #ESNM (300 GB 15k SFF-2)                         |         4 |                       |
| ESPR           | 5B47   | Quantity 150 of #ESNR (600 GB 15k SFF-2)                         |         4 |                       |
| EQ62           | 5B1D   | Quantity 150 of #ES62 3.86 - 4.0 TB 7200 rpm 4k LFF-1 Disk       |         2 |                       |
| EQ64           | 5B1F   | Quantity 150 of #ES64 7.72 - 8.0 TB 7200 rpm 4k LFF-1 Disk       |         2 |                       |
| EQEV           | 59D2   | Quantity 150 of #ESEV (600 GB 10k SFF-2)                         |         4 |                       |
| EQEZ           | 59C9   | Quantity 150 of #ESEZ (300 GB SFF-2)                             |         4 |                       |
| EQF3           | 59DA   | Quantity 150 of #ESF3 (1.2 TB 10k SFF-2)                         |         4 |                       |
| EQFP           | 59CC   | Quantity 150 of #ESFP (600 GB SFF-2)                             |         4 |                       |
| EQFT           | 59DD   | Quantity 150 of #ESFT (1.8 TB 10k SFF-2)                         |         4 |                       |

Table 1-12 shows the available disk drive feature codes that can be installed in the Power S914 (9009-41G) server.

Table 1-12   Disk drive feature code description for the Power S914 (9009-41G) server

| Feature code   | CCIN   | Description                                                      |   Maximum | OS support            |
|----------------|--------|------------------------------------------------------------------|-----------|-----------------------|
| 1953           | 19B1   | 300 GB 15k RPM SAS SFF-2 Disk Drive (AIX/Linux)                  |       672 | AIX and Linux         |
| ESNJ           | 5B41   | 283 GB 15 K RPM SAS SFF-3 4k Block Cached Disk Drive (IBM i)     |        18 | AIX, IBM i, and Linux |
| ESNL           | 5B43   | 283 GB 15 K RPM SAS SFF-2 4k Block Cached Disk Drive (IBM i)     |       672 | AIX, IBM i, and Linux |
| 1953           | 19B1   | 300 GB 15k RPM SAS SFF-2 Disk Drive (AIX/Linux)                  |       672 | AIX and Linux         |
| ESDB           | 59E0   | 300 GB 15 K RPM SAS SFF-3 Disk Drive (AIX/Linux)                 |        18 | AIX, IBM i, and Linux |
| ESNM           | 5B43   | 300 GB 15 K RPM SAS SFF-2 4k Block Cached Disk Drive (AIX/Linux) |       672 | AIX, IBM i, and Linux |
| ESNK           | 5B41   | 300 GB 15 K RPM SAS SFF-3 4k Block Cached Disk Drive (AIX/Linux) |        18 | AIX, IBM i, and Linux |
| ES90           | 5B13   | 387 GB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                 |        18 | AIX, IBM i, and Linux |
| ES91           | 5B13   | 387 GB Enterprise SAS 4k SFF-3 SSD for IBM i                     |        18 | AIX, IBM i, and Linux |
| ES94           | 5B10   | 387 GB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ES95           | 5B10   | 387 GB Enterprise SAS 4k SFF-2 SSD for IBM i                     |       336 | IBM i                 |
| ESB0           | 5B19   | 387 GB Enterprise SAS 5xx SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESB2           | 5B16   | 387 GB Enterprise SAS 5xx SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESB8           | 5B13   | 387 GB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                 |        18 | AIX, IBM i, and Linux |
| ESB9           | 5B13   | 387 GB Enterprise SAS 4k SFF-3 SSD for IBM i                     |        18 | AIX, IBM i, and Linux |
| ESBA           | 5B10   | 387 GB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ESBB           | 5B10   | 387 GB Enterprise SAS 4k SFF-2 SSD for IBM i                     |       336 | AIX, IBM i, and Linux |
| ESGT           | 5B19   | 387 GB Enterprise SAS 5xx SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESGV           | 5B16   | 387 GB Enterprise SAS 5xx SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESEU           | 59D2   | 571 GB 10K RPM SAS SFF-2 Disk Drive 4 K Block - 4224             |       672 | AIX, IBM i, and Linux |
| ESF4           | 59D3   | 571 GB 10K RPM SAS SFF-3 Disk Drive 4 K Block - 4224             |        18 | AIX, IBM i, and Linux |

| Feature code   | CCIN   | Description                                                      |   Maximum | OS support            |
|----------------|--------|------------------------------------------------------------------|-----------|-----------------------|
| ESNN           | 5B45   | 571 GB 15 K RPM SAS SFF-3 4k Block Cached Disk Drive (IBM i)     |        18 | AIX, IBM i, and Linux |
| ESNQ           | 5B47   | 571 GB 15 K RPM SAS SFF-2 4k Block Cached Disk Drive (IBM i)     |       672 | AIX, IBM i, and Linux |
| 1964           | 19B3   | 600 GB 10k RPM SAS SFF-2 Disk Drive (AIX/Linux)                  |       672 | AIX and Linux         |
| ESD5           | 59D0   | 600 GB 10K RPM SAS SFF-3 Disk Drive (AIX/Linux)                  |        18 | AIX, IBM i, and Linux |
| ESEV           | 59D2   | 600 GB 10K RPM SAS SFF-2 Disk Drive 4 K Block - 4096             |       672 | AIX, IBM i, and Linux |
| ESF5           | 59D3   | 600 GB 10K RPM SAS SFF-3 Disk Drive 4 K Block - 4096             |        18 | AIX, IBM i, and Linux |
| ESNP           | 5B45   | 600 GB 15 K RPM SAS SFF-3 4k Block Cached Disk Drive (AIX/Linux) |        18 | AIX, IBM i, and Linux |
| ESNR           | 5B47   | 600 GB 15 K RPM SAS SFF-2 4k Block Cached Disk Drive (AIX/Linux) |       672 | AIX, IBM i, and Linux |
| ESB4           | 5B1A   | 775 GB Enterprise SAS 5xx SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESB6           | 5B17   | 775 GB Enterprise SAS 5xx SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESBE           | 5B14   | 775 GB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                 |        18 | AIX, IBM i, and Linux |
| ESBF           | 5B14   | 775 GB Enterprise SAS 4k SFF-3 SSD for IBM i                     |        18 | AIX, IBM i, and Linux |
| ESBG           | 5B11   | 775 GB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ESBH           | 5B11   | 775 GB Enterprise SAS 4k SFF-2 SSD for IBM i                     |       336 | AIX, IBM i, and Linux |
| ESGX           | 5B1A   | 775 GB Enterprise SAS 5xx SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESGZ           | 5B17   | 775 GB Enterprise SAS 5xx SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESNA           | 5B11   | 775 GB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ESNB           | 5B11   | 775 GB Enterprise SAS 4k SFF-2 SSD for IBM i                     |       336 | AIX, IBM i, and Linux |
| ESNC           | 5B14   | 775 GB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                 |        18 | AIX, IBM i, and Linux |
| ESND           | 5B14   | 775 GB Enterprise SAS 4k SFF-3 SSD for IBM i                     |        18 | AIX, IBM i, and Linux |
| ESJ0           | 5B29   | 931 GB Mainstream SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ESJ1           | 5B29   | 931 GBMainstream SAS 4k SFF-2 SSD for IBM i                      |       336 | IBM i                 |
| ESJ8           | 5B2B   | 931 GB Mainstream SAS 4k SFF-3 SSD for AIX/Linux                 |        18 | AIX, IBM i, and Linux |

| Feature code   | CCIN   | Description                                                      |   Maximum | OS support            |
|----------------|--------|------------------------------------------------------------------|-----------|-----------------------|
| ESJ9           | 5B2B   | 931 GBMainstream SAS 4k SFF-3 SSD for IBM i                      |        18 | IBM i                 |
| ESF2           | 59DA   | 1.1TB10KRPMSASSFF-2DiskDrive4KBlock - 4224                       |       672 | AIX, IBM i, and Linux |
| ESF8           | 59DB   | 1.1TB10KRPMSASSFF-3DiskDrive4KBlock - 4224                       |        18 | AIX, IBM i, and Linux |
| ESF3           | 59DA   | 1.2TB10KRPMSASSFF-2DiskDrive4KBlock - 4096                       |       672 | AIX, IBM i, and Linux |
| ESF9           | 59DB   | 1.2TB10KRPMSASSFF-3DiskDrive4KBlock - 4096                       |        18 | AIX, IBM i, and Linux |
| ESBJ           | 5B15   | 1.55 TB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESBK           | 5B15   | 1.55 TB Enterprise SAS 4k SFF-3 SSD for IBM i                    |        18 | AIX, IBM i, and Linux |
| ESBL           | 5B12   | 1.55 TB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESBM           | 5B12   | 1.55 TB Enterprise SAS 4k SFF-2 SSD for IBM i                    |       336 | AIX, IBM i, and Linux |
| ESNE           | 5B12   | 1.55 TB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESNF           | 5B12   | 1.55 TB Enterprise SAS 4k SFF-2 SSD for IBM i                    |       336 | AIX, IBM i, and Linux |
| ESNG           | 5B15   | 1.55 TB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESNH           | 5B15   | 1.55 TB Enterprise SAS 4k SFF-3 SSD for IBM i                    |        18 | AIX, IBM i, and Linux |
| EC5X           | 5987   | Mainstream 800 GB SSD NVMe U.2 module for AIX/Linux              |         4 | AIX, IBM i, and Linux |
| ES1E           | 59B8   | 1.6 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for AIX/Linux |         4 | AIX, IBM i, and Linux |
| ES1F           | 59B8   | 1.6 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for IBM i     |         4 | IBM i                 |
| ESFS           | 59DD   | 1.7TB10KRPMSASSFF-2DiskDrive4KBlock - 4224                       |       672 | AIX, IBM i, and Linux |
| ESFU           | 59DE   | 1.7TB10KRPMSASSFF-3DiskDrive4KBlock - 4224                       |        18 | AIX, IBM i, and Linux |
| ESFT           | 59DD   | 1.8TB10KRPMSASSFF-2DiskDrive4KBlock - 4096                       |       672 | AIX, IBM i, and Linux |
| ESFV           | 59DE   | 1.8TB10KRPMSASSFF-3DiskDrive4KBlock - 4096                       |        18 | AIX, IBM i, and Linux |
| ESJ2           | 5B21   | 1.86 TB Mainstream SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESJ3           | 5B21   | 1.86 TB Mainstream SAS 4k SFF-2 SSDfor IBM i                     |       336 | IBM i                 |
| ESJA           | 5B20   | 1.86 TB Mainstream SAS 4k SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESJB           | 5B20   | 1.86 TB Mainstream SAS 4k SFF-3 SSDfor IBM i                     |        18 | IBM i                 |

| Feature code   | CCIN   | Description                                                      |   Maximum | OS support            |
|----------------|--------|------------------------------------------------------------------|-----------|-----------------------|
| ES1G           | 59B9   | 3.2 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for AIX/Linux |         4 | AIX, IBM i, and Linux |
| ES1H           | 59B9   | 3.2 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for IBM i     |         4 | IBM i                 |
| ESJ4           | 5B2D   | 3.72 TB Mainstream SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESJ5           | 5B2D   | 3.72 TB Mainstream SAS 4k SFF-2 SSDfor IBM i                     |       336 | IBM i                 |
| ESJC           | 5B2C   | 3.72 TB Mainstream SAS 4k SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESJD           | 5B2C   | 3.72 TB Mainstream SAS 4k SFF-3 SSDfor IBM i                     |        18 | IBM i                 |
| ES62           | 5B1D   | 3.86 - 4.0 TB 7200 RPM4KSASLFF-1Nearline Disk Drive (AIX/Linux)  |       336 | AIX, IBM i, and Linux |
| EC5V           |        | 6.4 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for AIX/Linux |         4 | AIX, IBM i, and Linux |
| EC5W           | 59BA   | 6.4 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for IBM i     |         4 | IBM i                 |
| ESJ6           | 5B2F   | 7.45 TB Mainstream SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESJ7           | 5B2F   | 7.45 TB Mainstream SAS 4k SFF-2 SSDfor IBM i                     |       336 | IBM i                 |
| ESJE           | 5B2E   | 7.45 TB Mainstream SAS 4k SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESJF           | 5B2E   | 7.45 TB Mainstream SAS 4k SFF-3 SSDfor IBM i                     |        18 | IBM i                 |
| ES64           | 5B1F   | 7.72 - 8.0 TB 7200 RPM4KSASLFF-1Nearline Disk Drive (AIX/Linux)  |       336 | AIX, IBM i, and Linux |
| 1818           | 19B3   | Quantity 150 of #1964                                            |         4 |                       |
| 1929           | 19B1   | Quantity 150 of #1953                                            |         4 |                       |
| EQ62           | 5B1D   | Quantity 150 of #ES62 3.86 - 4.0 TB7200 rpm 4k LFF-1 Disk        |         2 |                       |
| EQ64           | 5B1F   | Quantity 150 of #ES64 7.72 - 8.0 TB7200 rpm 4k LFF-1 Disk        |         2 |                       |
| EQEU           | 59D2   | Quantity 150 of #ESEU (571 GB 10k SFF-2)                         |         4 |                       |
| EQEV           | 59D2   | Quantity 150 of #ESEV (600 GB 10k SFF-2)                         |         4 |                       |
| EQF2           | 59DA   | Quantity 150 of #ESF2 (1.1 TB 10k SFF-2)                         |         4 |                       |
| EQF3           | 59DA   | Quantity 150 of #ESF3 (1.2 TB 10k SFF-2)                         |         4 |                       |
| EQFS           | 59DD   | Quantity 150 of #ESFS (1.7 TB 10k SFF-2)                         |         4 |                       |
| EQFT           | 59DD   | Quantity 150 of #ESFT (1.8 TB 10k SFF-2)                         |         4 |                       |
| ESPL           | 5B43   | Quantity 150 of #ESNL (283 GB 15k SFF-2)                         |         4 |                       |
| ESPM           | 5B43   | Quantity 150 of #ESNM (300 GB 15k SFF-2)                         |         4 |                       |
| ESPQ           | 5B47   | Quantity 150 of #ESNQ (571 GB 15k SFF-2)                         |         4 |                       |

| Feature code   | CCIN   | Description                              |   Maximum | OS support   |
|----------------|--------|------------------------------------------|-----------|--------------|
| ESPR           | 5B47   | Quantity 150 of #ESNR (600 GB 15k SFF-2) |         4 |              |
| ER94           | 5B10   | Quantity 150 of ES94 387 GB SAS 4k       |         2 |              |
| ER95           | 5B10   | Quantity 150 of ES95 387 GB SAS 4k       |         2 |              |
| ERGV           | 5B16   | Quantity 150 of ESGV 387 GB SSD 4k       |         2 |              |
| ERGZ           | 5B17   | Quantity 150 of ESGZ 775 GB SSD 4k       |         2 |              |
| ERJ0           | 5B29   | Quantity 150 of ESJ0 931 GB SAS 4k       |         2 |              |
| ERJ1           | 5B29   | Quantity 150 of ESJ1 931 GB SAS 4k       |         2 |              |
| ERJ2           | 5B21   | Quantity 150 of ESJ2 1.86 TB SAS 4k      |         2 |              |
| ERJ3           | 5B21   | Quantity 150 of ESJ3 1.86 TB SAS 4k      |         2 |              |
| ERJ4           | 5B2D   | Quantity 150 of ESJ4 3.72 TB SAS 4k      |         2 |              |
| ERJ5           | 5B2D   | Quantity 150 of ESJ5 3.72 TB SAS 4k      |         2 |              |
| ERJ6           | 5B2F   | Quantity 150 of ESJ6 7.45 TB SAS 4k      |         2 |              |
| ERJ7           | 5B2F   | Quantity 150 of ESJ7 7.45 TB SAS 4k      |         2 |              |
| ERNA           | 5B11   | Quantity 150 of ESNA 775 GB SSD 4k       |         2 |              |
| ERNB           | 5B11   | Quantity 150 of ESNB 775 GB SSD 4k       |         2 |              |
| ERNE           | 5B12   | Quantity 150 of ESNE 1.55 TB SSD 4k      |         2 |              |
| ERNF           | 5B12   | Quantity 150 of ESNF 1.55 TB SSD 4k      |         2 |              |
| ESQ2           | 5B16   | Quantity 150 of ESB2 387 GB SAS 4k       |         2 |              |
| ESQ6           | 5B17   | Quantity 150 of ESB6 775 GB SAS 4k       |         2 |              |
| ESQA           | 5B10   | Quantity 150 of ESBA 387 GB SAS 4k       |         2 |              |
| ESQB           | 5B10   | Quantity 150 of ESBB 387 GB SAS 4k       |         2 |              |
| ESQG           | 5B11   | Quantity 150 of ESBG 775 GB SAS 4k       |         2 |              |
| ESQH           | 5B11   | Quantity 150 of ESBH 775 GB SAS 4k       |         2 |              |
| ESQL           | 5B12   | Quantity 150 of ESBL 1.55 TB SAS 4k      |         2 |              |
| ESQM           | 5B12   | Quantity 150 of ESBM 1.55 TB SAS 4k      |         2 |              |

Table 1-13 shows the available disk drive feature codes that can be installed in the Power S924 (9009-24G) server.

Table 1-13   Disk drive feature code description for the Power S924 (9009-24G) server

| Feature code   | CCIN   | Description                                                  |   Maximum | OS support            |
|----------------|--------|--------------------------------------------------------------|-----------|-----------------------|
| 1953           | 19B1   | 300 GB 15k RPM SAS SFF-2 Disk Drive (AIX/Linux)              |       672 | AIX and Linux         |
| 1963           | 19B3   | 600 GB 15k RPM SAS SFF-2 Disk Drive (AIX/Linux)              |       672 | AIX and Linux         |
| ESNJ           | 5B41   | 283 GB 15 K RPM SAS SFF-3 4k Block Cached Disk Drive (IBM i) |        18 | AIX, IBM i, and Linux |

| Feature code   | CCIN   | Description                                                      |   Maximum | OS support            |
|----------------|--------|------------------------------------------------------------------|-----------|-----------------------|
| ESNL           | 5B43   | 283 GB 15 K RPM SAS SFF-2 4k Block Cached Disk Drive (IBM i)     |       672 | AIX, IBM i, and Linux |
| 1953           | 19B1   | 300 GB 15k RPM SAS SFF-2 Disk Drive (AIX/Linux)                  |       672 | AIX and Linux         |
| ESDB           | 59E0   | 300 GB 15 K RPM SAS SFF-3 Disk Drive (AIX/Linux)                 |        18 | AIX, IBM i, and Linux |
| ESNM           | 5B43   | 300 GB 15 K RPM SAS SFF-2 4k Block Cached Disk Drive (AIX/Linux) |       672 | AIX, IBM i, and Linux |
| ESNK           | 5B41   | 300 GB 15 K RPM SAS SFF-3 4k Block Cached Disk Drive (AIX/Linux) |        18 | AIX, IBM i, and Linux |
| ES90           | 5B13   | 387 GB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                 |        18 | AIX, IBM i, and Linux |
| ES91           | 5B13   | 387 GB Enterprise SAS 4k SFF-3 SSD for IBM i                     |        18 | IBM i                 |
| ES94           | 5B10   | 387 GB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ES95           | 5B10   | 387 GB Enterprise SAS 4k SFF-2 SSD for IBM i                     |       336 | IBM i                 |
| ESB0           | 5B19   | 387 GB Enterprise SAS 5xx SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESB2           | 5B16   | 387 GB Enterprise SAS 5xx SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESB8           | 5B13   | 387 GB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                 |        18 | AIX, IBM i, and Linux |
| ESB9           | 5B13   | 387 GB Enterprise SAS 4k SFF-3 SSD for IBM i                     |        18 | AIX, IBM i, and Linux |
| ESBA           | 5B10   | 387 GB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ESBB           | 5B10   | 387 GB Enterprise SAS 4k SFF-2 SSD for IBM i                     |       336 | AIX, IBM i, and Linux |
| ESGT           | 5B19   | 387 GB Enterprise SAS 5xx SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESGV           | 5B16   | 387 GB Enterprise SAS 5xx SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESEU           | 59D2   | 571 GB 10K RPM SAS SFF-2 Disk Drive 4 K Block - 4224             |       672 | AIX, IBM i, and Linux |
| ESF4           | 59D3   | 571 GB 10K RPM SAS SFF-3 Disk Drive 4 K Block - 4224             |        18 | AIX, IBM i, and Linux |
| ESNN           | 5B45   | 571 GB 15 K RPM SAS SFF-3 4k Block Cached Disk Drive (IBM i)     |        18 | AIX, IBM i, and Linux |
| ESNQ           | 5B47   | 571 GB 15 K RPM SAS SFF-2 4k Block Cached Disk Drive (IBM i)     |       672 | AIX, IBM i, and Linux |
| 1964           | 19B3   | 600 GB 10k RPM SAS SFF-2 Disk Drive (AIX/Linux)                  |       672 | AIX and Linux         |
| ESD5           | 59D0   | 600 GB 10K RPM SAS SFF-3 Disk Drive (AIX/Linux)                  |        18 | AIX, IBM i, and Linux |

| Feature code   | CCIN   | Description                                                      |   Maximum | OS support            |
|----------------|--------|------------------------------------------------------------------|-----------|-----------------------|
| ESEV           | 59D2   | 600 GB 10K RPM SAS SFF-2 Disk Drive 4 K Block - 4096             |       672 | AIX, IBM i, and Linux |
| ESF5           | 59D3   | 600 GB 10K RPM SAS SFF-3 Disk Drive 4 K Block - 4096             |        18 | AIX, IBM i, and Linux |
| ESNP           | 5B45   | 600 GB 15 K RPM SAS SFF-3 4k Block Cached Disk Drive (AIX/Linux) |        18 | AIX, IBM i, and Linux |
| ESNR           | 5B47   | 600 GB 15 K RPM SAS SFF-2 4k Block Cached Disk Drive (AIX/Linux) |       672 | AIX, IBM i, and Linux |
| ESB4           | 5B1A   | 775 GB Enterprise SAS 5xx SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESB6           | 5B17   | 775 GB Enterprise SAS 5xx SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESBE           | 5B14   | 775 GB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                 |        18 | AIX, IBM i, and Linux |
| ESBF           | 5B14   | 775 GB Enterprise SAS 4k SFF-3 SSD for IBM i                     |        18 | AIX, IBM i, and Linux |
| ESBG           | 5B11   | 775 GB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ESBH           | 5B11   | 775 GB Enterprise SAS 4k SFF-2 SSD for IBM i                     |       336 | AIX, IBM i, and Linux |
| ESGX           | 5B1A   | 775 GB Enterprise SAS 5xx SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESGZ           | 5B17   | 775 GB Enterprise SAS 5xx SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESNA           | 5B11   | 775 GB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ESNB           | 5B11   | 775 GB Enterprise SAS 4k SFF-2 SSD for IBM i                     |       336 | IBM i                 |
| ESNC           | 5B14   | 775 GB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                 |        18 | AIX, IBM i, and Linux |
| ESND           | 5B14   | 775 GB Enterprise SAS 4k SFF-3 SSD for IBM i                     |        18 | IBM i                 |
| ESJ0           | 5B29   | 931 GB Mainstream SAS 4k SFF-2 SSD for AIX/Linux                 |       336 | AIX, IBM i, and Linux |
| ESJ1           | 5B29   | 931 GBMainstream SAS 4k SFF-2 SSD for IBM i                      |       336 | IBM i                 |
| ESJ8           | 5B2B   | 931 GB Mainstream SAS 4k SFF-3 SSD for AIX/Linux                 |        18 | AIX, IBM i, and Linux |
| ESJ9           | 5B2B   | 931 GBMainstream SAS 4k SFF-3 SSD for IBM i                      |        18 | IBM i                 |
| ESF2           | 59DA   | 1.1TB10KRPMSASSFF-2DiskDrive4KBlock - 4224                       |       672 | AIX, IBM i, and Linux |
| ESF8           | 59DB   | 1.1TB10KRPMSASSFF-3DiskDrive4KBlock - 4224                       |        18 | AIX, IBM i, and Linux |
| ESF3           | 59DA   | 1.2TB10KRPMSASSFF-2DiskDrive4KBlock - 4096                       |       672 | AIX, IBM i, and Linux |

| Feature code   | CCIN   | Description                                                      |   Maximum | OS support            |
|----------------|--------|------------------------------------------------------------------|-----------|-----------------------|
| ESF9           | 59DB   | 1.2TB10KRPMSASSFF-3DiskDrive4KBlock - 4096                       |        18 | AIX, IBM i, and Linux |
| ESBJ           | 5B15   | 1.55 TB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESBK           | 5B15   | 1.55 TB Enterprise SAS 4k SFF-3 SSD for IBM i                    |        18 | AIX, IBM i, and Linux |
| ESBL           | 5B12   | 1.55 TB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESBM           | 5B12   | 1.55 TB Enterprise SAS 4k SFF-2 SSD for IBM i                    |       336 | AIX, IBM i, and Linux |
| ESNE           | 5B12   | 1.55 TB Enterprise SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESNF           | 5B12   | 1.55 TB Enterprise SAS 4k SFF-2 SSD for IBM i                    |       336 | IBM i                 |
| ESNG           | 5B15   | 1.55 TB Enterprise SAS 4k SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESNH           | 5B15   | 1.55 TB Enterprise SAS 4k SFF-3 SSD for IBM i                    |        18 | IBM i                 |
| EC5X           | 5987   | Mainstream 800 GB SSD NVMe U.2 module for AIX/Linux              |         4 | AIX, IBM i, and Linux |
| ES1E           | 59B8   | 1.6 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for AIX/Linux |         4 | AIX, IBM i, and Linux |
| ES1F           | 59B8   | 1.6 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for IBM i     |         4 | IBM i                 |
| ESFS           | 59DD   | 1.7TB10KRPMSASSFF-2DiskDrive4KBlock - 4224                       |       672 | AIX, IBM i, and Linux |
| ESFU           | 59DE   | 1.7TB10KRPMSASSFF-3DiskDrive4KBlock - 4224                       |        18 | AIX, IBM i, and Linux |
| ESFT           | 59DD   | 1.8TB10KRPMSASSFF-2DiskDrive4KBlock - 4096                       |       672 | AIX, IBM i, and Linux |
| ESFV           | 59DE   | 1.8TB10KRPMSASSFF-3DiskDrive4KBlock - 4096                       |        18 | AIX, IBM i, and Linux |
| ESJ2           | 5B21   | 1.86 TB Mainstream SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESJ3           | 5B21   | 1.86 TB Mainstream SAS 4k SFF-2 SSDfor IBM i                     |       336 | IBM i                 |
| ESJA           | 5B20   | 1.86 TB Mainstream SAS 4k SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESJB           | 5B20   | 1.86 TB Mainstream SAS 4k SFF-3 SSDfor IBM i                     |        18 | IBM i                 |
| ES1G           | 59B9   | 3.2 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for AIX/Linux |         4 | AIX, IBM i, and Linux |
| ES1H           | 59B9   | 3.2 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for IBM i     |         4 | IBM i                 |
| ESJ4           | 5B2D   | 3.72 TB Mainstream SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESJ5           | 5B2D   | 3.72 TB Mainstream SAS 4k SFF-2 SSDfor IBM i                     |       336 | IBM i                 |

| Feature code   | CCIN   | Description                                                      |   Maximum | OS support            |
|----------------|--------|------------------------------------------------------------------|-----------|-----------------------|
| ESJC           | 5B2C   | 3.72 TB Mainstream SAS 4k SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESJD           | 5B2C   | 3.72 TB Mainstream SAS 4k SFF-3 SSDfor IBM i                     |        18 | IBM i                 |
| ES62           | 5B1D   | 3.86 - 4.0 TB 7200 RPM4KSASLFF-1Nearline Disk Drive (AIX/Linux)  |       336 | AIX, IBM i, and Linux |
| EC5V           | 59BA   | 6.4 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for AIX/Linux |         4 | AIX, IBM i, and Linux |
| EC5W           | 59BA   | 6.4 TB Enterprise 4 K NVMe SFF U.2 15 mm SSD PCIe4 for IBM i     |         4 | IBM i                 |
| ESJ6           | 5B2F   | 7.45 TB Mainstream SAS 4k SFF-2 SSD for AIX/Linux                |       336 | AIX, IBM i, and Linux |
| ESJ7           | 5B2F   | 7.45 TB Mainstream SAS 4k SFF-2 SSDfor IBM i                     |       336 | IBM i                 |
| ESJE           | 5B2E   | 7.45 TB Mainstream SAS 4k SFF-3 SSD for AIX/Linux                |        18 | AIX, IBM i, and Linux |
| ESJF           | 5B2E   | 7.45 TB Mainstream SAS 4k SFF-3 SSDfor IBM i                     |        18 | IBM i                 |
| ES64           | 5B1F   | 7.72 - 8.0 TB 7200 RPM4KSASLFF-1Nearline Disk Drive (AIX/Linux)  |       336 | AIX, IBM i, and Linux |
| 1818           | 19B3   | Quantity 150 of #1964                                            |         4 |                       |
| 1929           | 19B1   | Quantity 150 of #1953                                            |         4 |                       |
| EQ62           | 5B1D   | Quantity 150 of #ES62 3.86 - 4.0 TB 7200 rpm 4k LFF-1 Disk       |         2 |                       |
| EQ64           | 5B1F   | Quantity 150 of #ES64 7.72 - 8.0 TB 7200 rpm 4k LFF-1 Disk       |         2 |                       |
| EQEU           | 59D2   | Quantity 150 of #ESEU (571 GB 10k SFF-2)                         |         4 |                       |
| EQEV           | 59D2   | Quantity 150 of #ESEV (600 GB 10k SFF-2)                         |         4 |                       |
| EQF2           | 59DA   | Quantity 150 of #ESF2 (1.1 TB 10k SFF-2)                         |         4 |                       |
| EQF3           | 59DA   | Quantity 150 of #ESF3 (1.2 TB 10k SFF-2)                         |         4 |                       |
| EQFS           | 59DD   | Quantity 150 of #ESFS (1.7 TB 10k SFF-2)                         |         4 |                       |
| EQFT           | 59DD   | Quantity 150 of #ESFT (1.8 TB 10k SFF-2)                         |         4 |                       |
| ESPL           | 5B43   | Quantity 150 of #ESNL (283 GB 15k SFF-2)                         |         4 |                       |
| ESPM           | 5B43   | Quantity 150 of #ESNM (300 GB 15k SFF-2)                         |         4 |                       |
| ESPQ           | 5B47   | Quantity 150 of #ESNQ (571 GB 15k SFF-2)                         |         4 |                       |
| ESPR           | 5B47   | Quantity 150 of #ESNR (600 GB 15k SFF-2)                         |         4 |                       |
| ER94           | 5B10   | Quantity 150 of ES94 387 GB SAS 4k                               |         2 |                       |
| ER95           | 5B10   | Quantity 150 of ES95 387 GB SAS 4k                               |         2 |                       |
| ERGV           | 5B16   | Quantity 150 of ESGV 387 GB SSD 4k                               |         2 |                       |
| ERGZ           | 5B17   | Quantity 150 of ESGZ 775 GB SSD 4k                               |         2 |                       |

| Feature code   | CCIN   | Description                         |   Maximum | OS support   |
|----------------|--------|-------------------------------------|-----------|--------------|
| ERJ0           | 5B29   | Quantity 150 of ESJ0 931 GB SAS 4k  |         2 |              |
| ERJ1           | 5B29   | Quantity 150 of ESJ1 931 GB SAS 4k  |         2 |              |
| ERJ2           | 5B21   | Quantity 150 of ESJ2 1.86 TB SAS 4k |         2 |              |
| ERJ3           | 5B21   | Quantity 150 of ESJ3 1.86 TB SAS 4k |         2 |              |
| ERJ4           | 5B2D   | Quantity 150 of ESJ4 3.72 TB SAS 4k |         2 |              |
| ERJ5           | 5B2D   | Quantity 150 of ESJ5 3.72 TB SAS 4k |         2 |              |
| ERJ6           | 5B2F   | Quantity 150 of ESJ6 7.45 TB SAS 4k |         2 |              |
| ERJ7           | 5B2F   | Quantity 150 of ESJ7 7.45 TB SAS 4k |         2 |              |
| ERNA           | 5B11   | Quantity 150 of ESNA 775 GB SSD 4k  |         2 |              |
| ERNB           | 5B11   | Quantity 150 of ESNB 775 GB SSD 4k  |         2 |              |
| ERNE           | 5B12   | Quantity 150 of ESNE 1.55 TB SSD 4k |         2 |              |
| ERNF           | 5B12   | Quantity 150 of ESNF 1.55 TB SSD 4k |         2 |              |
| ESQ2           | 5B16   | Quantity 150 of ESB2 387 GB SAS 4k  |         2 |              |
| ESQ6           | 5B17   | Quantity 150 of ESB6 775 GB SAS 4k  |         2 |              |
| ESQA           | 5B10   | Quantity 150 of ESBA 387 GB SAS 4k  |         2 |              |
| ESQB           | 5B10   | Quantity 150 of ESBB 387 GB SAS 4k  |         2 |              |
| ESQG           | 5B11   | Quantity 150 of ESBG 775 GB SAS 4k  |         2 |              |
| ESQH           | 5B11   | Quantity 150 of ESBH 775 GB SAS 4k  |         2 |              |
| ESQL           | 5B12   | Quantity 150 of ESBL 1.55 TB SAS 4k |         2 |              |
| ESQM           | 5B12   | Quantity 150 of ESBM 1.55 TB SAS 4k |         2 |              |

The RDX docking station #EUA4 accommodates RDX removable disk cartridges of any capacity. The disk is in a protective rugged cartridge enclosure that plugs into the docking station. The docking station holds one removable rugged disk drive / cartridge at a time. The rugged removable disk cartridge and docking station perform saves, restores, and backups similar to a tape drive. This docking station can be an excellent entry capacity / performance option.

The Standalone USB DVD drive (#EUA5) is an optional, stand-alone external USB-DVD device. It requires high current at 5 V and must use the front USB 3.0 port.

## 1.7 I/O drawers for Power S922, Power S914, and Power S924 servers

If more PCIe slots beyond the system node are required, a PCIe Gen3 I/O drawer (#EMX0) can be attached to the Power S922, Power S914, and Power S924 servers.

The EXP12SX SAS Storage Enclosure and EXP24SX SAS Storage Enclosure (#ESLS/ELLS or #ESLL/ELLL) provide extra storage capacity.

Note: Limitations of specific versions of the Power S914 server:

- SAS Storage Enclosures (#ESLS/ELLS or #ESLL/ELLL) cannot be attached to the 4-core configuration of a Power S914 server (#EP50).
- The tower configuration of the Power S914 server does not allow I/O expansion drawers (#EMX0).

## 1.7.1  PCIe Gen3 I/O expansion drawer

This 19-inch, 4U (4 EIA) enclosure provides PCIe Gen3 slots outside of the system unit. It has two module bays. One 6-slot fan-out Module (#EMXH or #EMXG) can be placed in each module bay. Two 6-slot modules provide a total of 12 PCIe Gen3 slots. Each fan-out module is connected to a PCIe3 Optical Cable adapter that is in the system unit over an active optical CXP cable (AOC) pair or CXP copper cable pair.

The PCIe Gen3 I/O Expansion Drawer has two redundant, hot-plug power supplies. Each power supply has its own separately ordered power cord. The two power cords plug into a power supply conduit that connects to the power supply. The single-phase AC power supply is rated at 1030 W and can use 100 - 120 V or 200 - 240 V. If using 100 - 120 V, then the maximum is 950 W. It is a best practice that the power supply connects to a power distribution unit (PDU) in the rack. Power Systems PDUs are designed for a 200 - 240 V electrical source.

A blind swap cassette (BSC) is used to house the full-height adapters that go into these slots. The BSC is the same BSC that is used with the previous generation server's 12X attached I/O drawers (#5802, #5803, #5877, and #5873). The drawer includes a full set of BSCs, even if the BSCs are empty.

Concurrent repair, and adding or removing PCIe adapters is done by HMC-guided menus or by OS support utilities.

Figure 1-8 shows a PCIe Gen3 I/O expansion drawer.

Figure 1-8   PCIe Gen3 I/O expansion drawer

<!-- image -->

## 1.7.2 I/O drawers and usable PCI slots

Figure 1-9 shows the rear view of the PCIe Gen3 I/O expansion drawer that is equipped with two PCIe3 6-slot fan-out modules with the location codes for the PCIe adapter slots.

Figure 1-9 Rear view of a PCIe Gen3 I/O expansion drawer with PCIe slots location codes

<!-- image -->

Table 1-14 provides details about the PCI slots in the PCIe Gen3 I/O expansion drawer that is equipped with two PCIe3 6-slot fan-out modules.

Table 1-14 PCIe slot locations for the PCIe Gen3 I/O expansion drawer with two fan-out modules

| Slot    | Location code   | Description   |
|---------|-----------------|---------------|
| Slot 1  | P1-C1           | PCIe3, x16    |
| Slot 2  | P1-C2           | PCIe3, x8     |
| Slot 3  | P1-C3           | PCIe3, x8     |
| Slot 4  | P1-C4           | PCIe3, x16    |
| Slot 5  | P1-C5           | PCIe3, x8     |
| Slot 6  | P1-C6           | PCIe3, x8     |
| Slot 7  | P2-C1           | PCIe3, x16    |
| Slot 8  | P2-C2           | PCIe3, x8     |
| Slot 9  | P2-C3           | PCIe3, x8     |
| Slot 10 | P2-C4           | PCIe3, x16    |
| Slot 11 | P2-C5           | PCIe3, x8     |
| Slot 12 | P2-C6           | PCIe3, x8     |

In the table:

- All slots support full-length, full-height adapters or short (LP) adapters with a full-height tailstock in single-wide, Gen3, BSC.
- Slots C1 and C4 in each PCIe3 6-slot fan-out module are x16 PCIe3 buses, and slots C2, C3®, C5, and C6 are x8 PCIe buses.
- All slots support enhanced error handling (EEH).
- All PCIe slots are hot-swappable and support concurrent maintenance.

Table 1-15 summarizes the maximum number of I/O drawers that are supported and the total number of PCI slots that are available.

Table 1-15   Maximum number of I/O drawers that are supported and total number of PCI slots

| Server                 |   Maximumnumberof I/O exp drawers |   Maximumnumberof I/O fan-out modules |   Maximum PCIe slots |
|------------------------|-----------------------------------|---------------------------------------|----------------------|
| Power S922 (1-socket)  |                                 1 |                                     1 |                   11 |
| Power S922 (2-socket)  |                                 2 |                                     3 |                   26 |
| Power S914(1-socket) a |                                 1 |                                     1 |                   13 |
| Power S924 (1-socket)  |                                 1 |                                     1 |                   13 |
| Power S924 (2-socket)  |                                 2 |                                     3 |                   26 |

- a. The PCIe expansion drawer (#EMX0) does not apply to the 4-core configuration.

## 1.7.3  EXP12SX SAS Storage Enclosure and EXP24SX SAS Storage Enclosure

If you need more disks than are available with the internal disk bays, you can attach more external disk subsystems, such as an EXP12SX SAS Storage Enclosure (#ESLL) or EXP24SX SAS Storage Enclosure (#ESLS).

The EXP24SX SAS Storage Enclosure is a storage expansion enclosure with twelve 3.5-inch large form factor (LFF) SAS bays. It supports up to 12 hot-plug HDDs in only 2 EIA of space in a 19-inch rack. The EXP24SX SAS Storage Enclosure SFF bays use LFF Gen1 (LFF-1) trays. The 4 KB sector drives (#4096 or #4224) are supported. SSDs are not supported.

The EXP24SX SAS Storage Enclosure is a storage expansion enclosure with twenty-four 2.5-inch SFF SAS bays. It supports up to 24 hot-plug HDDs or SSDs in only 2 EIA of space in a 19-inch rack. The EXP24SX SAS Storage Enclosure SFF bays use SFF Gen2 (SFF-2) carriers or trays.

With AIX, Linux, and VIOS, the EXP24SX SAS Storage Enclosure or EXP24SX SAS Storage Enclosure can be ordered with four sets of six bays (mode 4), two sets of 12 bays (mode 2), or one set of 24-four bays (mode 1). With IBM i, only one set of 24 bays (mode 1) is supported. It is possible to change the mode setting in the field by using commands along with a documented procedure.

Important: When changing modes, a skilled, technically qualified person should follow the special documented procedures. Improperly changing modes can potentially delete existing RAID sets, prevent access to existing data, or allow other partitions to access another partition's existing data.

Four mini-SAS HD ports on the EXP24SX SAS Storage Enclosure or EXP24SX SAS Storage Enclosure are attached to PCIe Gen3 SAS adapters or attached to an integrated SAS controller in the Power S922, Power S914, or Power S924 servers.

The attachment between the EXP24SX SAS Storage Enclosure or EXP24SX SAS Storage Enclosure or and the PCIe3 SAS adapters or integrated SAS controllers is through SAS YO12 or X12 cables. All ends of the YO12 and X12 cables have mini-SAS HD narrow connectors.

The EXP24SX SAS Storage Enclosure or EXP24SX SAS Storage Enclosure includes redundant AC power supplies and two power cords.

Figure 1-10 shows the EXP24SX Expansion Drawer.

Figure 1-10   The EXP24SX Expansion Drawer

<!-- image -->

Figure 1-11 shows the EXP12SX Expansion Drawer.

Figure 1-11   The EXP12SX Expansion drawer

<!-- image -->

## 1.8  IBM i Solution Editions for Power S914

IBM i Solution Editions are designed to help you take advantage of the combined experience and expertise of IBM and independent software vendors (ISVs) in building business value with your IT investments. A qualifying purchase of software, maintenance, services, or training for a participating ISV solution is required when purchasing an IBM i Solution Edition.

The IBM Solution Edition for Power S914 supports 4-core (#EP50) and 6-core (#EP51) configurations. For a list of participating ISVs, a registration form, and more details, see IIBM i Solution Editions.

Here are the requirements to be eligible to purchase an IBM Solution Edition for Power S914:

- The server must be ordered with a Solution Edition feature code.
- The server must be a new purchase, not a miscellaneous equipment specification (MES) upgrade.
- The offering must include new or upgraded software licenses, or software maintenance from the ISV for the qualifying IBM server. Services and training for the qualifying server can also be provided. For more information, contact your individual ISV.
- Proof of purchase (for example, a copy of the invoice) of the solution with a participating ISV must be provided to IBM on request. The proof must be dated within 90 days before or after the date of order of the qualifying server.
- The combined value (software, maintenance, services, and training) of the ISV purchase must be USD 6,500 or greater. For more information, contact your individual ISV.
- Not eligible as an IBM Capacity BackUp (CBU).

## 1.9  IBM Capacity BackUp

The CBU designation enables you to temporarily transfer IBM i processor license entitlements and IBM i user license entitlements that are purchased for a primary machine to a secondary CBU-designated system for high availability (HA) and disaster recovery (DR) (HADR) operations. Temporarily transferring these resources instead of purchasing them for your secondary system can result in significant savings. Processor activations cannot be transferred.

If your primary or CBU machine is sold or discontinued from use, any temporary entitlement transfers must be returned to the machine on which they were originally acquired. For CBU registration, terms, and conditions, see IBM Power Systems Capacity BackUp.

## 1.9.1  Power S922 (9009-22G) IBM Capacity BackUp offering

The CBU specify (#0444) is available only as part of a new server purchase. Certain system prerequisites must be met, and system registration and approval are required before the CBU specify feature can be applied on a new server. Standard IBM i terms and conditions do not allow either IBM i processor license entitlements or IBM i user license entitlements to be transferred permanently or temporarily. These entitlements remain with the machine for which they were ordered. When you register the association between your primary and on-order CBU system, you must agree to certain terms and conditions regarding the temporary transfer.

After a new CBU system is registered as a pair with the proposed primary system and the configuration is approved, you can temporarily move your optional IBM i processor license entitlement and IBM i user license entitlements from the primary system to the CBU system when the primary system is down or while the primary system processors are inactive. The CBU system can then support failover and role-swapping for a full range of test and HADR scenarios. Temporary entitlement transfer means that the entitlement is a property that is transferred from the primary system to the CBU system, which may remain in use on the CBU system while the registered primary and CBU systems are deployed for the HADR operation. The intent of the CBU offering is to enable regular role-swap operations.

The primary systems for a Power S922 (9009-22G) CBU server with its IBM i P10 software tier can be a POWER9 or POWER8 server with a P10 or P20 software tie, as shown in the following list:

- Power S824 (8286-42A) server
- Power S814 6-core or 8-core (8286-41A) server
- Power S822 (8284-22A) server
- Power S924 (9009-42A) server
- Power S914 6-core or 8-core (9009-41A) server
- Power S922 (9009-22A) server
- Power S922 (9009-22G) server

The primary machine must be in the same enterprise as the CBU system. The IBM i Solution Editions are not eligible for CBU status.

Before you can temporarily transfer IBM i processor license entitlements from the registered primary system, you must have more than one IBM i processor license on the primary machine and at least one IBM i processor license on the CBU system. An activated processor must be available on the CBU system to use the transferred entitlement. You can then transfer any IBM i processor entitlements above the minimum one, assuming the total IBM i workload on the primary system does not require the IBM i entitlement that you want to transfer during the time of the transfer. During this temporary transfer, the CBU system's internal records of its total number of IBM i processor license entitlements are not updated, and you might see IBM i license noncompliance warning messages from the CBU system. These warning messages in this situation do not mean that you are not in compliance.

Before you can temporarily transfer IBM i user entitlements, you must have more than the minimum number of IBM i user entitlements on a primary system. You can then transfer any IBM i user entitlements above the minimum, assuming the total IBM i users on the primary system do not require the IBM i entitlement that you want to transfer during the time of the transfer. The Power S824 and Power S924 servers do not have user entitlements that can be transferred, and only processor license entitlements can be transferred. The minimum number of IBM i users on the POWER9 and the POWER8 with IBM i user entitlements are:

- Power S814 6-core or 8-core (8286-41A) server: 10 users
- Power S822 (8284-22A) server: 10 users
- Power S914 6-core or 8-core (9009-41A) server: 10 users
- Power S922 (9009-22A) server: 10 users
- Power S922 (9009-22G) server: 10 users

For example, if you have a Power S914 6-core server as your primary system with two IBM i processor license entitlements (one above the minimum) and 40 IBM i user entitlements (30 above the minimum), you can temporarily transfer up to one IBM i entitlement and up to 30 user entitlements. During this temporary transfer, the CBU system's internal records of its total number of IBM i processor and user license entitlements is not updated, and you might see IBM i license noncompliance warning messages from the CBU system.

## 1.9.2 Power S914 (9009-41G) IBM Capacity BackUp offering

The CBU specify (#0444) is available only as part of a new server purchase. Certain system prerequisites must be met, and system registration and approval are required before the CBU specify feature can be applied on a new server. Standard IBM i terms and conditions do not allow either IBM i processor license entitlements or IBM i user license entitlements to be transferred permanently or temporarily. These entitlements remain with the machine for which they were ordered. When you register the association between your primary and on-order CBU systems, you must agree to certain terms and conditions regarding the temporary transfer.

After a new CBU system is registered along with the proposed primary system and the configuration is approved, you can temporarily move your optional IBM i processor license entitlement and IBM i user license entitlements from the primary system to the CBU system when the primary system is down or while the primary system processors are inactive. The CBU system can then support failover and role-swapping for a full range of test and HADR scenarios. Temporary entitlement transfer means that the entitlement is a property that is transferred from the primary system to the CBU system, which may remain in use on the CBU system while the registered primary and CBU systems are in deployment for the HADR operation. The intent of the CBU offering is to enable regular role-swap operations. The primary machine must be in the same enterprise as the CBU system. The IBM i Solution Editions are not eligible for CBU status.

The Power S914 server is available with six or eight cores in the P10 software tier and four cores in the P05 software tier.

## Power S914 software tiers for IBM i on model 9009-41G

Here are the software tiers:

- The 4-core processor (#EP50, QPRCFEAT EP10) is IBM i software tier P05.
- The 6-core processor (#EP51, QPRCFEAT EP11) is IBM i software tier P10.
- The 8-core processor (#EP52, QPRCFEAT EP12) is IBM i software tier P10.

## Power S914 CBU server in the P10 software tier

The primary systems for a Power S914 (9009-41G) CBU server with a IBM i P10 software tier can be a POWER8 or POWER9 server with a P10 or P20 software tier:

- Power S824 (8286-42A) server
- Power S814 6-core or 8-core (8286-41A) server
- Power S822 (8284-22A) server
- Power S924 (9009 42A) server
- Power S914 6-core or 8-core (9009-41A) server
- Power S922 (9009-22A) server
- Power S922 (9009-22G) server

Before you can temporarily transfer IBM i user entitlements, you must have more than the minimum number of IBM i user entitlements on a primary server. You can then transfer any IBM i user entitlements above the minimum, assuming that the total IBM i users on the primary system do not require the IBM i entitlement that you want to transfer during the time of the transfer. The Power S924 and S824 servers do not have IBM i user entitlements to transfer, only processor entitlements. For a P10 primary, the minimum number of IBM i user entitlements on the eligible P10 POWER9 and POWER8 servers are:

- Power S814 6-core or 8-core (8286-41A) server: 10 users
- Power S822 (8284-22A) server: 10 users
- Power S914 6-core or 8-core (9009-41A) server: 10 users

- Power S922 (9009-22A) server: 10 users
- Power S922 (9009-22G) server: 10 users

## Power S914 CBU server in the P05 software tier

The primary systems for a Power S914 (9009-41G) CBU server with a IBM i P05 software tier can be a POWER8 or POWER9 server with a P05 or P10 software tier:

- Power S814 (8286-41A) 4, 6, or 8 core server
- Power S822 (8284-22A) server
- Power S914 (9009-41A) 4, 6, or 8 core server
- Power S922 (9009-22A) server
- Power S922 (9009-22G) server

Before you can temporarily transfer IBM i user entitlements, you must have more than the minimum number of IBM i user entitlements on a primary server. You can then transfer any IBM i user entitlements above the minimum, assuming that the total IBM i users on the primary system do not require the IBM i entitlement that you want to transfer during the time of the transfer. The minimum number of IBM i user entitlements on the P05 or P10 POWER9 and POWER8 with IBM i user entitlements are:

- Power S814 4-core (8286-41A) server: Five users
- Power S814 6-core or 8-core (8286-41A) server: 10 users
- Power S822 (8284-22A) server: 10 users
- Power S914 4-core (9009-41A) server: 10 users
- Power S914 6-core or 8-core (9009-41A) server: 10 users
- Power S922 (9009-22A) server: 10 users
- Power S914 4-core (9009-41G) server: 5users
- Power S914 6-core or 8-core (9009-41G) server: 10 users
- Power S922 (9009-22G) server: 10 users

For example, if you have a 2-core server as your primary system with two IBM i processor license entitlements (one above the minimum) and 50 IBM i user entitlements (20 above the minimum), you can temporarily transfer up to one IBM i entitlement and up to 20 user entitlements. During this temporary transfer, the CBU system's internal records of its total number of IBM i processor and user license entitlements is not updated, and you might see IBM i license noncompliance warning messages from the CBU system.

## 1.9.3  Power S924 (9009-42G) IBM Capacity BackUp offering

The CBU specify (#0444) is available only as part of a new server purchase. Certain system prerequisites must be met, and system registration and approval are required before the CBU specify feature can be applied on a new server. Standard IBM i terms and conditions do not allow either IBM i processor license entitlements or IBM i user license entitlements to be transferred permanently or temporarily. These entitlements remain with the machine for which they were ordered. When you register the association between your primary and on-order CBU systems, you must agree to certain terms and conditions regarding the temporary transfer.

After a new CBU system is registered along with the proposed primary system and the configuration is approved, you can temporarily move your optional IBM i processor license entitlement and IBM i Enterprise Enablement (#5250) entitlements from the primary system to the CBU system while the primary system is down or the primary system processors are inactive.

The CBU system can then support failover and role-swapping for a full range of test and HADR scenarios. Temporary entitlement transfer means that the entitlement is a property that is transferred from the primary system to the CBU system, which may remain in use on the CBU system while the registered primary and CBU systems are in deployment for the HADR operation. The intent of the CBU offering is to enable regular role-swap operations.

Before you can temporarily transfer Enterprise Enablement entitlements (#5250), you must have more than one Enterprise Enablement entitlement (#5250) on the primary server and at least one Enterprise Enablement entitlement (#5250) on the CBU system. You can then transfer the entitlements that are not required on the primary server during the time of transfer and that are above the minimum of one entitlement. The minimum number of permanent entitlements on the CBU is one; however, you are required to license all permanent workloads, such as replication workloads. If, for example, the replication workload uses four processor cores at peak workload, then you are required to permanently license four cores on the CBU.

For example, if you have a 12-core Power S824 server as your primary system with six IBM i processor license entitlements (five above the minimum) and two Enterprise Enablement entitlements (#5250) (one above the minimum), you can temporarily transfer up to five IBM i entitlements and one Enterprise Enablement entitlement (#5250). During the temporary transfer, the CBU system's internal records of its total number of IBM i processor entitlements are not updated, and you might see IBM i license noncompliance warning messages from the CBU system.

The CBU specify (#0444) is available only as part of a new server purchase. Certain system prerequisites must be met, and system registration and approval are required before the CBU specify feature can be applied on a new server. Standard IBM i terms and conditions do not allow either IBM i processor license entitlements or Enterprise Enablement entitlements (#5250) to be transferred permanently or temporarily. These entitlements remain with the machine for which they were ordered. When you register the association between your primary and on-order CBU systems, you must agree to certain terms and conditions regarding the temporary transfer.

The servers with P20 or higher software tiers do not have user entitlements that can be transferred, and only processor license entitlements can be transferred.

Here are the eligible primary servers for a Power S924 CBU:

- Power S824 (8286-42A) server
- Power S924 (9009-42A) server
- Power S924 (9009-42G) server
- Power E870 (9119-MME) server
- Power E880 (9119-MHE) server
- Power E870C (9080-MME) server
- Power E880C (9080-MHE) server

## Power S924 software tiers for IBM i on model 9009-42A

Here are the Power S924 software tiers for IBM on model 9009-42A:

- The 8-core processor (#EP5E, QPRCRFEAT EP5E) is IBM i software tier P20.
- The 10-core processor (#EP5F, QPRCRFEAT EP5F) is IBM i software tier P20.
- The 11-core processor (#EP5H, QPRCRFEAT EP5H) is IBM i software tier P20.
- The 12-core processor (#EP5G, QPRCRFEAT EP5G) is IBM i software tier P20.

## 1.10  IBM Power Systems Enterprise Cloud Edition

The Power S922 (9009-22G), Power S914 (9009-41G), and Power S924 (9009-42G) servers are the first set of entry servers that come cloud-enabled with integrated PowerVM Enterprise capabilities.

The Power Systems Enterprise Cloud Edition V1.2 is a complete package that adds flexible licensing models in the cloud era. It helps you to rapidly deploy multi-cloud infrastructures with a compelling set of cloud-enabled capabilities. The new Power Systems Enterprise Cloud Edition primarily provides value for clients that use both AIX and Linux on Power, with simplified licensing models and advanced features.

The Power Systems Enterprise Cloud Edition (5765-ECB) includes:

- IBM PowerSC Standard Edition
- IBM PowerSC Multi-Factor Authentication
- IBM Cloud™ PowerVC Manager
- IBM VM Recovery Manager DR
- IBM Aspera® High-Speed Transfer Endpoint 100 Mbps (one endpoint per server)
- IBM Cloud Management Console (36-month term)

If you use IBM AIX as a primary OS, there is a specific offering: Power Systems Enterprise Cloud Edition with AIX (5765-ECA) that includes AIX 7.2 licenses with the offering:

- IBM AIX 7.2 Standard Edition
- IBM PowerSC Standard Edition
- IBM PowerSC Multi-Factor Authentication
- IBM Cloud PowerVC Manager
- IBM VM Recovery Manager DR
- IBM Aspera High-Speed Transfer Endpoint 100 Mbps (one endpoint per server)
- IBM Cloud Management Console (36-month term)

## 1.10.1  IBM PowerSC

IBM PowerSC provides a security and compliance solution that is optimized for virtualized environments on Power Systems servers running IBM PowerVM and IBM AIX or Linux on Power. Security control and compliance are some of the key components that are needed to defend virtualized data centers and a cloud infrastructure against evolving threats.

The PowerSC product contains six subcomponents:

- Compliance Automation (CA)
- Real Time Compliance (RTC)
- Patch Management and Trusted Network Computing (TNC)
- Trusted Logging (TL)
- Trusted Boot (TB)
- Trusted Firewall (TF)

For more information, see IBM PowerSC Standard Edition V1.2 enhances security and compliance solution for virtualized environments.

## 1.10.2 IBM PowerSC Multi-Factor Authentication

IBM PowerSC Multi-Factor Authentication raises the level of assurance of your mission-critical systems with a flexible and tightly integrated multi-factor authentication (MFA) solution for IBM AIX and Linux on Power virtual workloads running on Power Systems servers.

For more information, see the Announcement Letter.

## 1.10.3  IBM Cloud PowerVC Manager

IBM Cloud PowerVC Manager includes all the functions of the PowerVC Standard Edition plus the following features:

- A self-service portal that allows the provisioning of new VMs without direct system administrator intervention. An option is for policy approvals for the requests that are received from the self-service portal.
- Deploy templates that simplify cloud deployments.
- Cloud management policies that simplify management of cloud deployments.
- Metering data that can be used for chargeback.

For more information, see the Announcement Letter.

## 1.10.4  IBM VM Recovery Manager DR

IBM VM Recovery Manager DR V1.3 is an automated DR solution that enables Power Systems users to achieve low recovery times for both planned and unplanned outages. It introduces support for more storage replication solutions and support for an extra guest OS, broadening the offering's applicability to a wider range of client requirements.

IBM VM Recovery Manager DR offers support for:

- IBM i as a guest OS, adding to the current support for IBM AIX and Linux
- IBM DS8000® Global Mirror
- IBM SAN Volume Controller/IBM Storwize® Metro and Global Mirror
- Extended Memory Controller (EMC) Symmetrix Remote Data Facility (SRDF) synchronous replication
- Boot device selection for IBM POWER8 processor-based systems

For more information, see the Announcement Letter.

## 1.10.5  IBM Aspera High-Speed Transfer Endpoint 100 Mbps

IBM Aspera High-Speed Transfer Endpoint 100 Mbps help moves large amounts of data by using innovative data transfer tools at optimal speed regardless of distance or network conditions. Transfers are stable, robust, and predictable, even for the largest files, most challenging networks, and greatest distances. Supporting deployments on premises or on public, private, and hybrid cloud platforms, and covering a wide range of server, desktop, and mobile OSs, Aspera solutions are designed to deliver end-to-end security-rich features, reliability, and exceptional bandwidth control. Aspera solutions are industry-standard applications for moving large files, directories, and data sets over wide area network (WANs) with optimized performance, scaling significantly with on-demand cloud storage and computing capacity.

For more information, see the Announcement Letter.

## 1.10.6  IBM Cloud Management Console

IBM Cloud Management Console for Power Systems provides a consolidated view of the capacity, inventory, patch level, and logging information of the Power Systems servers in your enterprise so that you can simplify and improve their management. The offering inside the Power Systems Enterprise Cloud Edition is delivered with a 36-month term license, which provides greater flexibility for deployment and cost control. After signing up for IBM Cloud Management Console, clients can securely access the offering in IBM Cloud.

For more information, see the Announcement Letter.

## 1.11  IBM Power platform modernization

Cloud capabilities are a prerequisite for using enterprise-level IT resources. Besides the Power Systems Enterprise Cloud Edition offering that is described in 1.10, 'IBM Power Systems Enterprise Cloud Edition' on page 43, there is a rich infrastructure around Power Systems to help modernize services with the strategic initiatives of your business.

The most important products are:

- IBM Power Systems Virtual Servers
- Red Hat OpenShift Container Platform for Power

## 1.11.1  IBM Power Systems Virtual Servers

IBM Power Systems Virtual Servers on IBM Cloud is an infrastructure as a service (IaaS) offering that you can use to deploy a virtual server, also known as a logical partition (LPAR), in a matter of minutes. Power Systems clients who have typically relied upon an on-premises only infrastructure can now quickly and economically extend their Power IT resources into the cloud. Using IBM Power Virtual Servers on IBM Cloud is an alternative to avoid the large capital expense or added risk when moving your essential workloads to a public cloud.

An IBM Cloud integrates your IBM AIX and IBM i capabilities into the IBM Cloud experience, which means you get fast, self-service provisioning, flexible management both on-premises and off, and access to a stack of enterprise IBM Cloud services all with pay-as-you-use billing that lets you easily scale up and out.

You can quickly deploy an IBM Power Systems Virtual Servers on IBM Cloud instance to meet your specific business needs. With IBM Power Systems Virtual Servers on IBM Cloud, you can create a hybrid cloud environment that allows you to easily control workload demands.

For more information, see IBM Power Systems Virtual Servers - Getting started tutorial.

## 1.11.2  Red Hat OpenShift Container Platform for Power

Red Hat OpenShift Container Platform for Power (5639-OCP) provides a secure, enterprise-grade platform for on-premises, private platform-as-a-service clouds on Power Systems servers. It brings together industry-leading container orchestration from Kubernetes, advanced application build and delivery automation, and Red Hat Enterprise Linux certified containers for Power Systems.

It brings developers and IT operations together with a common platform. It provides applications, platforms, and services for creating and delivering cloud-native applications and management so IT can ensure that the environment is secure and available.

Red Hat OpenShift Container Platform for Power provides enterprises the same functions as the Red Hat OpenShift Container Platform offering on other platforms. Key features include:

- A self-service environment for application and development teams.
- Pluggable architecture that supports a choice of container run times, networking, storage, Continuous Integration / Continuous Deployment (CI-CD), and more.
- Ability to automate routine tasks for application teams.

Red Hat OpenShift Container Platform subscriptions are offered in two core increments that are designed to run in a virtual guest. The purchase of a separate Red Hat Enterprise Linux subscription (5639-RLE) is required as the base OS.

For more information, see 5639-RLE Red Hat Enterprise Linux for Power, little endian V7.0.

## 1.12  System racks

The Power S922, Power S914, and Power S924 servers are mounted in the 36U 7014-T00 (#0551), the 42U 7014-T42 (#0553), or the IBM 42U Slim Rack (7965-94Y) racks. These racks are built to the 19-inch EIA 310D standard.

Order information: The racking approach for the initial order must be either a 7014-T00, 7014-T42, or 7965-94Y. If an extra rack is required for I/O expansion drawers as an MES to an existing system, either an #0551, #0553, or #ER05 rack must be ordered.

You must leave 2U of space at either the bottom or top of the rack, depending on the client's cabling preferences, to allow for cabling to exit the rack.

If a system is installed in a rack or cabinet that is not from IBM, ensure that the rack meets the requirements that are described in 1.12.10, 'Original equipment manufacturer racks' on page 55.

Responsibility: The client is responsible for ensuring that the installation of the drawer in the preferred rack or cabinet results in a configuration that is stable, serviceable, safe, and compatible with the drawer requirements for power, cooling, cable management, weight, and rail security.

## 1.12.1  IBM 7014 Model T00 rack

The 1.8-meter (71-inch) Model T00 is compatible with past and present Power Systems servers. The features of the T00 rack are as follows:

- Has 36U of usable space.
- Has optional removable side panels.
- Has optional side-to-side mounting hardware for joining multiple racks.
- Has increased power distribution and weight capacity.
- Supports both AC and DC configurations.

- Up to four PDUs can be mounted in the PDU bays (see Figure 1-13 on page 51), but others can fit inside the rack. For more information, see 1.12.7, 'The AC power distribution unit and rack content' on page 50.
- For the T00 rack, three door options are available:
- -Front Door for 1.8 m Rack (#6068).
- This feature provides an attractive black full-height rack door. The door is steel, with a perforated flat front surface. The perforation pattern extends from the bottom to the top of the door to enhance ventilation and provide some visibility into the rack.
- -A 1.8 m Rack Acoustic Door (#6248).
- This feature provides a front and rear rack door that is designed to reduce acoustic sound levels in a general business environment.
- -A 1.8 m Rack Trim Kit (#6263).

If no front door is used in the rack, this feature provides a decorative trim kit for the front.

- Ruggedized Rack Feature

For enhanced rigidity and stability of the rack, the optional Ruggedized Rack Feature (#6080) provides more hardware that reinforces the rack and anchors it to the floor. This hardware is designed primarily for use in locations where earthquakes are a concern. The feature includes a large steel brace or truss that bolts into the rear of the rack.

It is hinged on the left side so it can swing out of the way for easy access to the rack drawers when necessary. The Ruggedized Rack Feature also includes hardware for bolting the rack to a concrete floor or a similar surface, and bolt-in steel filler panels for any unoccupied spaces in the rack.

- Weights are as follows:
- -T00 base empty rack: 244 kg (535 lb.).
- -T00 full rack: 816 kg (1795 lb.).
- -Maximum weight of drawers is 572 kg (1260 lb.).
- -Maximum weight of drawers in a zone 4 earthquake environment is 490 kg (1080 lb.). This number equates to 13.6 kg (30 lb.) per EIA.

Important: If more weight is added to the top of the rack, for example, adding feature code #6117, the 490 kg (1080 lb) must be reduced by the weight of the addition. As an example, feature code #6117 weighs approximately 45 kg (100 lb), so the new maximum weight of drawers that the rack can support in a zone 4 earthquake environment is 445 kg (980 lb). In the zone 4 earthquake environment, the rack must be configured starting with the heavier drawers at the bottom of the rack.

## 1.12.2  IBM 7014 Model T42 rack

The 2.0-meter (79.3-inch) Model T42 addresses the client requirement for a tall enclosure to house the maximum amount of equipment in the smallest possible floor space. The following features are for the model T42 rack (which differ from the model T00):

- The T42 rack has 42U of usable space (6U of extra space).
- The model T42 supports AC power only.
- Weights are as follows:
- -T42 base empty rack: 261 kg (575 lb.)
- -T42 full rack: 930 kg (2045 lb.)

The available door options for the Model T42 rack are shown in Figure 1-12.

Figure 1-12   Door options for the T42 rack

<!-- image -->

The door options are explained in the following list:

- The 2.0 m Rack Trim Kit (#6272) is used if no front door is used in the rack.
- The Front Door for a 2.0 m Rack (#6069) is made of steel, with a perforated flat front surface. The perforation pattern extends from the bottom to the top of the door to enhance ventilation and provide some visibility into the rack. This door is non-acoustic and has a depth of about 25 mm (1 in.).
- The 2.0 m Rack Acoustic Door (#6249) consists of a front and rear door to reduce noise by approximately 6 dB(A). It has a depth of approximately 191 mm (7.5 in.).
- The High-End Appearance Front Door (#6250) provides a front rack door with a field-installed IBM Power System 780 logo indicating that the rack contains a Power 780 system. The door is not acoustic and has a depth of about 90 mm (3.5 in.).

High end: For the High-End Appearance Front Door (#6250), use the High-End Appearance Side Covers (#6238) to make the rack appear as though it is a high-end server (but in a 19-inch rack format instead of a 24-inch rack).

- Feature code #ERG7 provides an attractive black full-height rack door. The door is steel, with a perforated flat front surface. The perforation pattern extends from the bottom to the top of the door to enhance ventilation and provide some visibility into the rack. The non-acoustic door has a depth of about 134 mm (5.3 in.).

## Rear Door Heat Exchanger

To lead away more heat, a special door that is named the Rear Door Heat Exchanger (RDHX) (#6858) is available. This door replaces the standard rear door on the rack. Copper tubes that are attached to the rear door circulate chilled water, which is provided by the customer. The chilled water removes heat from the exhaust air being blown through the servers and attachments that are mounted in the rack. With industry-standard quick couplings, the water lines in the door attach to the customer-supplied secondary water loop.

For more information about planning for the installation of the IBM Rear Door Heat Exchanger, see IBM Knowledge Center.

## 1.12.3  IBM 42U Slim Rack 7965-94Y

The 2.0-meter (79-inch) Model 7965-94Y is compatible with past and present Power Systems servers and provides an excellent 19-inch rack enclosure for your data center. Its 600 mm (23.6 in.) width combined with its 1100 mm (43.3 in.) depth plus its 42 EIA enclosure capacity provides great footprint efficiency for your systems and allows it to be easily placed on standard 24-inch floor tiles.

The IBM 42U Slim Rack has a lockable perforated front steel door that provides ventilation, physical security, and visibility of indicator lights in the installed equipment within. In the rear, either a lockable perforated rear steel door (#EC02) or a lockable RDHX (1164-95X) is used. Lockable optional side panels (#EC03) increase the rack's aesthetics, help control airflow through the rack, and provide physical security. Multiple 42U Slim Racks can be bolted together to create a rack suite (#EC04).

Up to six optional 1U PDUs can be placed vertically in the sides of the rack. More PDUs can be placed horizontally, but they each use 1U of space in this position.

## 1.12.4  1.8 Meter Rack (0551)

The 1.8 Meter Rack (#0551) is a 36 EIA unit rack. The rack that is delivered as #0551 is the same rack that is delivered when you order the 7014-T00 rack. The included features might vary. Certain features that are delivered as part of the 7014-T00 must be ordered separately with #0551.

## 1.12.5  2.0 Meter Rack (#0553)

The 2.0 Meter Rack (#0553) is a 42 EIA unit rack. The rack that is delivered as #0553 is the same rack that is delivered when you order the 7014-T42 rack. The included features might vary. Certain features that are delivered as part of the 7014-T42 must be ordered separately with #0553.

## 1.12.6  Rack (#ER05)

This feature provides a 19-inch, 2.0-meter high rack with 42 EIA units of total space for installing a rack-mounted central electronics complex (CEC) or expansion units. The 600 mm wide rack fits within a data center's 24-inch floor tiles and provides better thermal and cable management capabilities. The following features are required on #ER05:

- #EC01 front door
- #EC02 rear door or #EC05 RDHX indicator

PDUs on the rack are optional. Each #7196 and #7189 PDU uses one of six vertical mounting bays. Each PDU beyond four uses 1U of rack space.

If you order Power Systems equipment in an MES order, use the equivalent rack #ER05 instead of 7965-94Y so IBM Manufacturing can include the hardware in the rack.

## 1.12.7 The AC power distribution unit and rack content

For rack models T00 and T42, 12-outlet PDUs are available, which include the AC PDUs #9188 and #7188 and the AC Intelligent PDU+ (iPDU) #5889 and #7109. The iPDUs+ (#5889 and #7109) are identical to #9188 and #7188 PDUs, but are equipped with one Ethernet port, one console serial port, and one RS232 serial port for power monitoring.

The PDUs have 12 client-usable IEC 320-C13 outlets. There are six groups of two outlets that are fed by six circuit breakers. Each outlet is rated up to 10 A, but each group of two outlets is fed from one 15 A circuit breaker.

High-function PDUs provide more electrical power per PDU and offer better 'PDU footprint' efficiency. In addition, they are iPDUs that provide insight to actual power usage by receptacle and also provide remote power on/off capability for easier support by individual receptacle. The PDUs can be ordered as #EPTJ, #EPTL, #EPTN, #EPTQ, #ECJJ, #ECJL, #ECJN, and #ECJQ.

High-function PDU feature codes are shown in Table 1-16.

Table 1-16   Available high-function PDUs

| PDUs                   | 1-phase or 3-phase depending on country wiring standards   | 1-phase or 3-phase depending on country wiring standards   | 3-phase 208 V depending on country wiring standards   | 3-phase 208 V depending on country wiring standards   |
|------------------------|------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
|                        | Old generation                                             | New generation                                             | Old generation                                        | New generation                                        |
| Nine C19 receptacles   | #EPTJ                                                      | #ECJJ                                                      | #EPTL                                                 | #ECJL                                                 |
| Twelve C13 receptacles | #EPTN                                                      | #ECJN                                                      | #EPTQ                                                 | #ECJQ                                                 |

Here are brief descriptions of new generation high-function PDUs:

- High Function 9xC19 PDU plus (#ECJJ)
- This is an intelligent, switched 200 - 240 volt AC PDU plus with nine C19 receptacles on the front of the PDU. The PDU is mounted at the rear of the rack, making the nine C19 receptacles easily accessible. For comparison, this feature code is most similar to the earlier generation #EPTJ PDU.
- High Function 9xC19 PDU plus 3-Phase (#ECJL)
- This is an intelligent, switched 208 volt 3-phase AC PDU plus with nine C19 receptacles on the front of the PDU. The PDU is mounted at the rear of the rack making the nine C19 receptacles easily accessible. For comparison, this feature code is most similar to the earlier generation #EPTL PDU.
- High Function 12xC13 PDU plus (#ECJN)
- This is an intelligent, switched 200 - 240 volt AC PDU plus with 12 C13 receptacles on the front of the PDU. The PDU is mounted at the rear of the rack making the 12 C13 receptacles easily accessible. For comparison, this feature code is most similar to the earlier generation #EPTN PDU.
- High Function 12xC13 PDU plus 3-Phase (#ECJQ)
- This is an intelligent, switched 208 volt 3-phase AC PDU plus with 12 C13 receptacles on the front of the PDU. The PDU is mounted at the rear of the rack making the 12 C13 receptacles easily accessible. For comparison, this feature code is most similar to the earlier generation #EPTQ PDU.

Four PDUs can be mounted vertically in the back of the T00 and T42 racks. Figure 1-13 shows the placement of the four vertically mounted PDUs. At the rear of the rack, two more PDUs can be installed horizontally in the T00 rack and three in the T42 rack. The four vertical mounting locations are filled first in the T00 and T42 racks. Mounting PDUs horizontally uses 1U per PDU and reduces the space that is available for other racked components. When mounting PDUs horizontally, the preferred approach is to use fillers in the EIA units that are occupied by these PDUs to facilitate proper air-flow and ventilation in the rack.

Figure 1-13   Power distribution unit placement and view

<!-- image -->

The PDU receives power through a UTG0247 power-line connector. Each PDU requires one PDU-to-wall power cord. Various power cord features are available for various countries and applications by varying the PDU-to-wall power cord, which must be ordered separately. Each power cord provides the unique design characteristics for the specific power requirements. To match new power requirements and save previous investments, these power cords can be requested with an initial order of the rack or with a later upgrade of the rack features.

Table 1-17 shows the available wall power cord options for the PDU and iPDU features, which must be ordered separately.

Table 1-17   Wall power cord options for the PDU and iPDU features

| Feature code   | Wall plug              | Rated voltage (V AC)   |   Phase | Rated amperage   | Geography                 |
|----------------|------------------------|------------------------|---------|------------------|---------------------------|
| #6653          | IEC 309, 3P+N+G, 16 A  | 230                    |       3 | 16 A/phase       | Internationally available |
| #6489          | IEC309 3P+N+G, 32 A    | 230                    |       3 | 32 A/phase       | EMEA                      |
| #6654          | NEMA L6-30             | 200 - 208, 240         |       1 | 24 A             | US, Canada, LA, and Japan |
| #6655          | RS 3750DP (watertight) | 200 - 208, 240         |       1 | 24 A             | US, Canada, LA, and Japan |
| #6656          | IEC 309, P+N+G, 32 A   | 230                    |       1 | 24 A             | EMEA                      |
| #6657          | PDL                    | 230 - 240              |       1 | 32 A             | Australia and New Zealand |
| #6658          | Korean plug            | 220                    |       1 | 30 A             | North and South Korea     |
| #6492          | IEC 309, 2P+G, 60 A    | 200 - 208, 240         |       1 | 48 A             | US, Canada, LA, and Japan |
| #6491          | IEC309,P+N+G, 63 A     | 230                    |       1 | 63 A             | EMEA                      |
| #6667          | PDL 56P532             | 230 - 240              |       3 | 32 A             | Australia and New Zealand |
| #7196          | IEC 320                | 200 - 208, 240         |       3 | 60 A             | US, Canada, LA, and Japan |

Notes: Ensure that the appropriate power cord feature is configured to support the power that is being supplied. Based on the power cord that is used, the PDU can supply 4.8 - 19.2 kVA. The power of all the drawers plugged into the PDU must not exceed the power cord limitation.

The Universal PDUs are compatible with previous models.

To better enable electrical redundancy, each server has two power supplies that must be connected to separate PDUs, which are not included in the base order.

For maximum availability, a preferred approach is to connect power cords from the same system to two separate PDUs in the rack, and to connect each PDU to independent power sources.

For detailed power requirements and power cord details about the 7014 and 7965-94Y racks, see IBM Knowledge Center.

## 1.12.8 Rack-mounting rules

Consider the following primary rules when you mount the system into a rack:

- The system is placed at any location in the rack. For rack stability, start filling a rack from the bottom.
- Any remaining space in the rack can be used to install other systems or peripheral devices if the maximum permissible weight of the rack is not exceeded and the installation rules for these devices are followed.
- Before placing the system into the service position, be sure to follow the rack manufacturer's safety instructions regarding rack stability.

Order information: The racking approach for the initial order must be either a 7014-T00, 7014-T42, or 7965-94Y. If an extra rack is required for I/O expansion drawers as an MES to an existing system, either an #0551, #0553, or #ER05 rack must be ordered.

You must leave 2U of space at either the bottom or top of the rack, depending on the client's cabling preferences, to allow for cabling to exit the rack.

## 1.12.9 Useful rack additions

This section highlights several rack addition solutions for Power Systems rack-based systems.

## IBM System Storage 7226 Model 1U3 Multi-Media Enclosure

The IBM System Storage™ 7226 Model 1U3 Multi-Media Enclosure can accommodate up to two tape drives, two RDX removable disk drive docking stations, or up to four DVD-RAM drives.

The IBM System Storage 7226 Multi-Media Enclosure supports LTO Ultrium, DVD-RAM, and RDX removable storage requirements on the following IBM systems:

- IBM POWER6™ processor-based systems
- IBM POWER7® processor-based systems
- IBM POWER8 processor-based systems
- IBM POWER9 processor-based systems

The IBM System Storage 7226 Multi-Media Enclosure offers an expansive list of drive feature options, as shown in Table 1-18.

Table 1-18   Supported drive features for the 7226-1U3

| Feature code   | Description                                    | Status    |
|----------------|------------------------------------------------|-----------|
| #1420          | DVD-RAM SAS Optical Drive                      | Available |
| #1422          | DVD-RAM Slim SAS Optical Drive                 | Available |
| #5762          | DVD-RAM USB Optical Drive                      | Available |
| #5763          | DVD Front USB Port Sled with DVD-RAM USB Drive | Available |
| #5757          | DVD RAM Slim USB Optical Drive                 | Available |
| #8348          | LTO Ultrium 6 Half High Fibre Tape Drive       | Available |
| #8341          | LTO Ultrium 6 Half High SAS Tape Drive         | Available |
| #8441          | LTO Ultrium 7 Half High SAS Tape Drive         | Available |

| Feature code   | Description                              | Status    |
|----------------|------------------------------------------|-----------|
| #8546          | LTO Ultrium 8 Half High Fibre Tape Drive | Available |
| #EU03          | RDX 3.0 Removable Disk Docking Station   | Available |

Here are the option descriptions:

- LTO Ultrium 6 Half-High 2.5 TB SAS and Tape Drive: With a data transfer rate up to 320 MBps (assuming a 2.5:1 compression), the LTO Ultrium 6 drive is read/write compatible with LTO Ultrium 6 and 5 media, and read-only compatible with LTO Ultrium 4. By using data compression, an LTO-6 cartridge can store up to 6.25 TB of data.
- The LTO Ultrium 7 drive offers a data rate of up to 300 MBps with compression. It also provides read/write compatibility with Ultrium 7 and Ultrium 6 media formats, and read-only compatibility with Ultrium 5 media formats. By using data compression, an LTO-7 cartridge can store up to 15 TB of data.
- The LTO Ultrium 8 drive offers a data rate of up to 300 MBps with compression. It also provides read/write compatibility with Ultrium 8 and Ultrium 7 media formats. It is not read or write compatible with other Ultrium media formats. By using data compression, an LTO-8 cartridge can store up to 30 TB of data.
- DVD-RAM: The 9.4 GB SAS Slim Optical Drive with an SAS and USB interface option is compatible with most standard DVD disks.
- RDX removable disk drives: The RDX USB docking station is compatible with most RDX removable disk drive cartridges when it is used in the same OS. The 7226 offers the following RDX removable drive capacity options:
- -500 GB (#1107)
- -1.0 TB (#EU01)
- -2.0 TB (#EU2T)

Removable RDX drives are in a rugged cartridge that inserts in to an RDX removable (USB) disk docking station (#1103 or #EU03). RDX drives are compatible with docking stations, which are installed internally in POWER6, IBM POWER6+, POWER7, IBM POWER7+, POWER8, and POWER9 processor-based servers, where applicable.

Figure 1-14 shows the IBM System Storage 7226 Multi-Media Enclosure.

Figure 1-14   IBM System Storage 7226 Multi-Media Enclosure

<!-- image -->

The IBM System Storage 7226 Multi-Media Enclosure offers customer-replaceable unit (CRU) maintenance service to help make the installation or replacement of new drives efficient. Other 7226 components are also designed for CRU maintenance.

The IBM System Storage 7226 Multi-Media Enclosure is compatible with most POWER6, POWER6+, POWER7, POWER7+, POWER8, and POWER9 processor-based systems that offer current level AIX, IBM i, and Linux OSs.

For a complete list of host software versions and release levels that support the IBM System Storage 7226 Multi-Media Enclosure, see System Storage Interoperation Center (SSIC).

Note: Any of the existing 7216-1U3, and 7214-1U2 multimedia drawers are also supported.

## 1.12.10  Original equipment manufacturer racks

The system can be installed in a suitable original equipment manufacturer (OEM) rack if that the rack conforms to the EIA-310-D standard for 19-inch racks. This standard is published by the Electrical Industries Alliance (EIA). For more information, see IBM Knowledge Center.

The website mentions the following key points:

- The front rack opening must be 451 mm wide ± 0.75 mm (17.75 in. ± 0.03 in.), and the rail-mounting holes must be 465 mm ± 0.8 mm (18.3 in. ± 0.03 in.) apart on-center (that is, the horizontal width between the vertical columns of holes on the two front-mounting flanges and on the two rear-mounting flanges). Figure 1-15 is a top view showing the specification dimensions.

Figure 1-15   Top view of the rack specification dimensions (not specific to IBM)

<!-- image -->

- The vertical distance between the mounting holes must consist of sets of three holes spaced (from bottom to top) 15.9 mm (0.625 in.), 15.9 mm (0.625 in.), and 12.67 mm (0.5 in.) on-center, making each three-hole set of vertical hole spacing 44.45 mm (1.75 in.) apart on center. Rail-mounting holes must be 7.1 mm ± 0.1 mm (0.28 in. ± 0.004 in.) in diameter. Figure 1-16 shows the top front specification dimensions.

Figure 1-16   Rack specification dimensions: Top front view

<!-- image -->

## 1.13 Hardware Management Console

This section describes the HMCs that are available for Power Systems servers.

## 1.13.1 New features

Here are some of the new features of the HMCs:

- New HMCs are now based on a platform with POWER processors.
- Intel x86-based HMCs are supported but are no longer available.
- Virtual HMCs (vHMCs) are available for x86 and Power Systems virtual environments.

## 1.13.2 Hardware Management Console overview

Administrators can use the HMC, which is a dedicated appliance, to configure and manage system resources on Power Systems servers. You can use the HMC to manage the servers through a GUI, command-line interface (CLI), or a REST API interface. The HMC provides basic virtualization management support for configuring LPARs and dynamic resource allocation, including processor and memory settings for selected Power Systems servers.

The HMC also supports advanced service functions, including guided repair and verification, concurrent firmware updates for managed systems, and around-the-clock error reporting through IBM Electronic Service Agent (IBM ESA) for faster support.

The HMC management features help improve a server usage, simplify systems management, and accelerate provisioning of server resources by using PowerVM virtualization technology.

The HMC is available as a hardware appliance or as a virtual machine (vHMC) hosted on a x86 or the Power platform. The Power S922, Power S914, and Power S924 servers support several service environments.

- Attachment to one or more HMCs or vHMCs is a supported option by the system with PowerVM. This is the default configuration for servers supporting multiple logical partitions with dedicated resource or virtual I/O. In this case all servers have at least on logical parition.
- For non-HMC systems a full system partition is used with PowerVM and only a single operating system can be installed. The primary service interface is through the operating system and the service processor.

The following architectures are available for hosting the HMC:

- x86-based HMCs: 7042-CR7, CR8, or CR9
- POWER based HMC: 7063-CR1
- vHMC on x86 or Power Systems LPARs

Important: To support firmware level FW950 and later, a virtual HMC, or POWER architecture-based HMC (machine type 703-CR1 or later) is required. For a list of supported HMCs, see https://www14.software.ibm.com/webapp/set2/flrt/sas?page=mtm-supported-hmc

Hardware support for CRUs comes standard with the HMC. In addition, users can upgrade this support level to IBM onsite support to be consistent with other Power Systems servers.

## Note:

- The Integrated Virtual Management (IVM) is no longer supported.

For more information about vHMC, see Virtual HMC Appliance (vHMC) Overview.

Figure 1-17 shows the HMC model selections and tier updates.

Figure 1-17   HMC model selections

<!-- image -->

## 1.13.3  Hardware Management Console code level

The HMC code must be running at Version 9 Release 1 modification 940 service pack 1 (V9R1M941) or later when you manage the Power S922, Power S914, and Power S924 servers.

Important: When running FW950 and later, ensure that your HMC hardware is supported. See https://www14.software.ibm.com/webapp/set2/flrt/sas?page=mtm-supported-hmc

If you are attaching an HMC to a new server or adding a function to an existing server that requires a firmware update, the HMC machine code might need to be updated to support the server firmware level. In a dual-HMC configuration, both HMCs must be at the same version and release of the HMC code.

To determine the HMC machine code level that is required for the firmware level on any server, go to Fix Level Recommendation Tool (FLRT) on or after the planned availability date for this product.

FLRT identifies the correct HMC machine code for the selected system firmware level.

## Note:

- Access to firmware and machine code updates is conditional on entitlement and license validation in accordance with IBM policy and practice. IBM might verify entitlement through customer number, serial number electronic restrictions, or any other means or methods that are employed by IBM at its discretion.
- HMC V9 supports only the Enhanced+ version of the GUI. The Classic version is no longer available.
- HMC V9R1.911.0 added support for managing IBM OpenPOWER systems. The same HMC that is used to manage Flexible Service Processor (FSP)-based enterprise systems can manage the baseboard management controller (BMC) based Power Systems AC and Power Systems LC servers. This support provides a consistent and consolidated hardware management solution.
- HMC V9 supports connections to servers that are based on IBM servers that are based on POWER9, POWER8, and POWER7 processors. POWER6 servers or earlier are not supported.

## 1.13.4  Two architectures of Hardware Management Console

There are now two options for the HMC hardware: The earlier Intel-based HMCs, and the newer model based on an IBM POWER8 processor. The x86-based HMCs are withdrawn from marketing but still supported as an option for managing the Power S922, Power S914, and Power servers.

A mix of Intel and POWER processor-based HMCs can be used for managing POWER9 servers if the firmware level is the same.

As a best practice, use 7063-CR1 or a vHMC for the server management.

## Intel based HMCs

Intel based HMCs that still support V9R1 firmware are:

- 7042-CR9
- 7042-CR8
- 7042-CR7

## POWER8 processor-based HMC

The POWER8 processor-based HMC is machine type and model 7063-CR1. It has the following specifications:

- 1U base configuration
- IBM POWER8 120 W 6-core CPU
- 32 GB (4 x 8 GB) of DDR4 system memory
- Two 2-TB SATA LFF 3.5-inch HDD RAID 1 disks
- Rail bracket option for round hole rack mounts
- Two USB 3.0 hub ports in the front of the server
- Two USB 3.0 hub ports in the rear of the server
- Redundant 1 kW power supplies
- Four 10-Gb Ethernet Ports (RJ-45) (10 Gb/1 Gb/100 Mb)
- One 1-Gb Ethernet port for management (BMC)

Note: System administrators can remotely start or stop a 7063-CR1 HMC by using ipmitool or the WebUI.

## 1.13.5 Virtual Hardware Management Console

The virtual appliance can be installed in x86 or POWER virtualized infrastructures.

## vHMC for x86 hypervisors

The supported hypervisors for x86 are:

- VMware ESXi 6.0 or higher
- Kernel-based Virtual Machine (KVM) on Red Hat Enterprise Linux 7 or higher
- Xen 4.2 or higher on SUSE Linux Enterprise Server 12

The minimum requirements for running the HMC virtual appliance are:

- 16 GB of memory.
- Four virtual processors.
- Two network interfaces (a maximum of four are allowed).
- One disk drive that contains 500 GB of available disk space.

## vHMC for POWER hypervisor

PowerVM is the only supported hypervisor for POWER machines.

The minimum requirements for running the HMC virtual appliance are:

- 16 GB of memory is recommended.
- One processing unit and four shared virtual processors in capped sharing mode.
- 160 GB of disk space. (500 GB is recommended.)

Note: You cannot manage the server that hosts the HMC virtual appliance.

## 1.13.6 Connectivity to POWER9 processor-based systems

POWER9 processor-based servers and their predecessor systems that are managed by an HMC require Ethernet connectivity between the HMC and the server's service processor. Additionally, to perform an operation on an LPAR, initiate Live Partition Mobility (LPM), or perform PowerVM Active Memory Sharing operations, you must have an Ethernet link to the managed partitions. A minimum of two Ethernet ports are needed on the HMC to provide such connectivity.

For the HMC to communicate properly with the managed server, eth0 of the HMC must be connected to either the HMC1 or HMC2 ports of the managed server, although other network configurations are possible. You may attach a second HMC to the remaining HMC port of the server for redundancy. The two HMC ports must be addressed by two separate subnets.

Figure 1-18 shows a simple network configuration to enable the connection from the HMC to the server and to allow for dynamic LPAR operations. For more information about the HMC and the possible network connections, see IBM Power Systems HMC Implementation and Usage Guide , SG24-7491.

Figure 1-18   Network connections from the HMC to service processor and LPARs

<!-- image -->

By default, the service processor HMC ports are configured for dynamic IP address allocation. The HMC can be configured as a DHCP server, providing an IP address at the time that the managed server is powered on. In this case, the FSP is allocated an IP address from a set of address ranges that is predefined in the HMC software.

If the service processor of the managed server does not receive a DHCP reply before timeout, predefined IP addresses are set up on both ports. Static IP address allocation is also an option and can be configured by using the Advanced System Management Interface (ASMI) menus.

Notes: The two service processor HMC ports have the following features:

- 1 Gbps connection speed.
- Visible only to the service processor. They can be used to attach the server to an HMC or to access the ASMI options from a client directly from a client web browser.
- Use the following network configuration if no IP addresses are set:
- -Service processor eth0 (HMC1 port): 169.254.2.147 with netmask 255.255.255.0
- -Service processor eth1 (HMC2 port): 169.254.3.147 with netmask 255.255.255.0

## 1.13.7  High availability Hardware Management Console configuration

The HMC is an important hardware component. Although Power Systems servers and their hosted partitions can continue to operate when the managing HMC becomes unavailable, certain operations, such as dynamic LPAR, partition migration that uses PowerVM LPM, or the creation of a partition, cannot be performed without the HMC. Power Systems servers may have two HMCs attached to a system, which provides redundancy if one of the HMCs is unavailable.

To achieve HMC redundancy for a POWER9 processor-based server, the server must be connected to two HMCs:

- The HMCs must be running the same level of HMC code.
- The HMCs must use different subnets to connect to the service processor.
- The HMCs must be able to communicate with the server's partitions over a public network to allow for full synchronization and functionality.

Figure 1-19 shows one possible HA HMC configuration that manages two servers.

Figure 1-19   Highly available HMC networking example

<!-- image -->

Each HMC is connected to one FSP port of each managed server.

For simplicity, only the hardware management networks (LAN1 and LAN2) are HA. However, the open network (LAN3) can be made HA by using a similar concept and adding a second network between the partitions and HMCs.

For more information about redundant HMCs, see IBM Power Systems HMC Implementation and Usage Guide , SG24-7491.

## 1.13.8  Flat panel display options

The IBM 7316 Model TF4 is a rack-mountable flat panel console kit that can also be configured with the tray pulled forward and the monitor folded up, providing full viewing and keying capability for the HMC operator.

The Model TF4 is a follow-on product to the Model TF3 and offers the following features:

- A slim, sleek, and lightweight monitor design that occupies only 1U (1.75 in.) in a 19-inch standard rack.
- A 18.5-inch (409.8 mm x 230.4 mm) flat panel TFT monitor with truly accurate images and virtually no distortion.
- The ability to mount the IBM Travel Keyboard in the 7316-TF4 rack keyboard tray.
- Support for the IBM 1x8 Rack Console Switch (#4283) IBM Keyboard/Video/Mouse switches. #4283 is a 1x8 Console Switch that fits in the 1U space behind the TF4. It is a CAT5-based switch containing eight rack interface (ARI) ports for connecting either PS/2 or USB console switch cables. It supports chaining of servers that use IBM Conversion Options switch cable (#4269). This feature provides four cables that connect a keyboard/video/mouse switch to a system, or can be used in a daisy-chain scenario to connect up to 128 systems to a single keyboard/video/mouse switch. It also supports server-side USB attachments.

<!-- image -->

Chapter 2.

2

## Architecture and technical overview

This chapter describes the overall system architecture for the IBM Power System S922 (9009-22G), the IBM Power System S914 (9009-41G), and the IBM Power System S924 (9009-42G) servers. The bandwidths that are provided throughout the chapter are theoretical maximums that are used for reference.

The speeds that are shown are at an individual component level. Multiple components and application implementation are key to achieving the best performance.

Always do the performance sizing at the application workload environment level and evaluate performance by using real-world performance measurements and production workloads.

Figure 2-2 on page 67, Figure 2-3 on page 68, and Figure 2-1 show the general architecture of the Power S922 (9009-22G), Power S914 (9009-41G), and Power S924 (9009-42G) servers.

Figure 2-1   Power S922 (9009-22G) logical system diagram

<!-- image -->

Note: For slots C6 and C12 check adapter placement rules when using x16 cards in these slots to obtain the best throughput.

Figure 2-2   Power S914 (9009-41G) logical system diagram

<!-- image -->

Figure 2-3   Power S924 (9009-42G) logical system diagram

<!-- image -->

## 2.1  The IBM POWER9 processor

This section introduces the POWER9 processor as it is used in the Power S922, Power S914, and Power S924 servers and describes its main characteristics and features in general.

## 2.1.1  POWER9 processor overview

Power S922, Power S914, and Power S924 servers are based on the POWER9 single-chip module (SCM) in a package that is optimized for commercial entry servers.

POWER9 introduced a modular execution slice microarchitecture where each execution slice has its own instruction queue, register files, execution engine, and cache port, and is implemented as a 64-bit, 8-byte doubleword data flow. The POWER9 architecture supports two core variants: An SMT4 core supporting up to four threads with four execution slices and an SMT8 core supporting up to eight threads with eight execution slices. The SMT8 core is optimized for larger partitions and especially suited for transactional workloads and data-centric business analytics applications that exhibit multiple threads with strong thread interaction. The Power S922, Power S914, and Power S924 servers all use the SMT8 core variant with 4, 6, 8, 10, 11, or 12 active cores per installed processor module depending on the particular processor feature codes selected. A single-core processor option is also available on the S922.

The POWER9 SCM is based on 14-nm FinFET Silicon-On-Insulator (SOI) fabrication technology. Each module is 68.5 mm x 68.5 mm in size and contains 8 billion transistors.

As shown in Figure 2-4, the chip contains 12 cores, two memory controllers, Peripheral Component Interconnect Express (PCIe) Gen 4 I/O controllers, and an interconnection system that connects all components within the chip at 7 TBps. Each core has 512 KB of L2 cache, and 10 MB of L3 embedded dynamic random access memory (eDRAM). The interconnect also extends through module and system board technology to other POWER9 processors in addition to DDR4 memory and various I/O devices.

Figure 2-4   The 12-core POWER9 processor chip

<!-- image -->

The POWER9 processor has eight memory channels, and each channel supports up to two DDR4 DIMM slots. The Power S914 server can support up to 1 TB of memory, and the Power S922 and Power S924 servers can support up to 4 TB of memory in two-socket configurations.

Limitation: The Power S914 server in a 4-core configuration is limited to 64 GB of memory.

## 2.1.2 POWER9 processor features

POWER9 chips that are used in Power S922, Power S914, and Power S924 systems provide embedded logic for the following features:

- Two memory controllers that support direct-attached DDR4 memory.
- Three integrated PCIe Gen 4 controllers with a total of 42 lanes running at 16 Gbps.
- Two 842 compression/decompression engines for 4 K and 64 K memory pages.
- Native Gzip compression and decompression accelerator.
- Two cryptographic accelerator engines supporting Advanced Encryption Standard (AES) and Secure Hash Algorithm (SHA) operations.
- Random number generator (RNG).

Table 2-1 summarizes the POWER9 processor features.

Table 2-1   Summary of the POWER9 processor technology

| Technology                                   | POWER9 processor                                |
|----------------------------------------------|-------------------------------------------------|
| Die size                                     | 68.5 mm × 68.5 mm                               |
| Fabrication technology                       | 14-nm lithography Copper interconnect SOI eDRAM |
| Maximum processor cores per processor module | 12                                              |
| Maximum execution threads core/module        | 8/96                                            |
| Maximum L2 cache core/module                 | 512 KB / 6 MB                                   |
| Maximum On-chip L3 cache core/module         | 10 MB / 120 MB                                  |
| Number of transistors                        | 8 billion                                       |
| Compatibility                                | With prior generation of POWER processor        |

## 2.1.3  POWER9 processor core

The POWER9 processor core is a 64-bit implementation of the IBM Power Instruction Set Architecture (ISA) Version 3.0, and has the following features:

- Multithreaded design, which is capable of up to eight-way simultaneous multithreading (SMT8).
- 64 KB, eight-way set-associative L1 instruction cache.
- 64 KB, eight-way set-associative L1 data cache.
- Enhanced prefetch, with instruction speculation awareness and data prefetch depth awareness.
- Enhanced branch prediction that uses both local and global prediction tables with a selector table to choose the best predictor.
- Improved out-of-order execution.
- Two symmetric fixed-point execution units.

- Two symmetric load/store units and two load units, all four of which can also run simple fixed-point instructions.
- An integrated, multi-pipeline vector-scalar floating point unit for running both scalar and SIMD-type instructions, including the Vector Multimedia eXtension (VMX) instruction set and the improved Vector Scalar eXtension (VSX) instruction set, which is capable of up to 16 floating point operations per cycle (eight double precision or 16 single precision).
- In-core AES encryption capability.
- Hardware data prefetching with 16 independent data streams and software control.
- Hardware decimal floating point (DFP) capability.

For more information about Power ISA Version 3.0, see OpenPOWER: IBM Power ISA Version 3.0B.

## 2.1.4 Simultaneous multithreading

POWER9 processor advancements in multi-core and multithread scaling are remarkable. A significant performance opportunity comes from parallelizing workloads to enable the full potential of the microprocessor, and the large memory bandwidth. Application scaling is influenced by both multi-core and multithread technology.

SMT enables a single physical processor core to simultaneously dispatch instructions from more than one hardware thread context. With SMT, each POWER9 core can present eight hardware threads. Because there are multiple hardware threads per physical processor core, more instructions can run at the same time. SMT is primarily beneficial in commercial environments where the speed of an individual transaction is not as critical as the total number of transactions that are performed. SMT typically increases the throughput of workloads with large or frequently changing working sets, such as database servers and web servers.

The Power S922, Power S914, and Power S924 servers support the full range of SMT modes that are available with POWER9 processors: single thread mode (SMT0), dual thread mode (SMT2), four-way SMT mode (SMT4), and eight-way SMT mode (SMT8).

## 2.1.5  Processor feature codes

This section provides detailed information about the available processor card feature codes for Power S922, Power S914, and Power S924 servers. For each of the named servers, the number of functional cores, their typical frequency range, and the processor core activation feature codes that are related to the supported processor card features are listed.

## Power S922 processor feature codes

The Power S922 (9009-22G) server is a 2-socket server with up to 22 active cores. Four different POWER9 processor card features with 1, 4, 8, 10, or 11 functional cores are available to choose from. You cannot use different processor card features within a Power S922 server. The smallest POWER9 4-core processor card allows only for one-socket configurations. All other processor card features can be used in one-socket or two-socket configurations. It is possible to add a second socket as a miscellaneous equipment specification (MES) upgrade order to a system that was initially ordered with only one 8-core, 10-core, or 11-core processor card.

By default, all functional cores on a processor card must be activated through related processor core activation features. However, to assist with the optimization of software licensing, the factory deconfiguration feature #2319 is available at initial order to permanently reduce the number of active cores.

Table 2-2 shows the number of functional cores, their typical frequency range, and the processor core activation feature codes for each of the available processor card feature codes of a Power S922 server.

Table 2-2   Processor feature code specification for the Power S922 server

| Processorcard feature code   | Configuration options   | Number of cores         | Typical frequency range [GHz]   | Processor core activation feature code   |
|------------------------------|-------------------------|-------------------------|---------------------------------|------------------------------------------|
| #EP5Y                        | 1-socket only           | 1 (IBM i initial order) | 2.8 - 3.8                       | 2319                                     |
| #EP56                        | 1-socket only           | 4                       | 2.8 - 3.8                       | EP66                                     |
| #EP58                        | 1- or 2-socket          | 8                       | 3.4 - 3.9                       | EP68                                     |
| #EP59                        | 1- or 2-socket          | 10                      | 2.9 - 3.8                       | EP69                                     |
| #EP5B                        | 1- or 2-socket          | 11                      | 2.9 - 3.8                       | EP6B                                     |

## Power S914 processor feature codes

The Power S914 (9009-41G) server supports only one processor socket with a maximum of up to eight active cores. Three different POWER9 processor card features with 4, 6, or 8 functional cores are available to choose from. By default, all functional cores on a processor card must be activated through related processor core activation features. However, to assist with the optimization of software licensing, the factory deconfiguration feature #2319 is available at initial order to permanently reduce the number of active cores.

Table 2-3 shows the number of functional cores, their typical frequency range, and the processor core activation feature codes for each of the available processor card feature codes of a Power S914 server.

Table 2-3   Processor feature codes specification for the Power S914 server

| Processor card feature code   |   Number of cores | Typical frequency range [GHz]   | Processor core activation feature code   |
|-------------------------------|-------------------|---------------------------------|------------------------------------------|
| #EP50                         |                 4 | 2.3 - 3.8                       | EP60                                     |
| #EP51                         |                 6 | 2.3 - 3.8                       | EP61                                     |
| #EP52                         |                 8 | 2.8 - 3.8                       | EP62                                     |

## Power S924 processor feature codes

The Power S924 (9009-42G) server is a powerful 2-socket server with up to 24 cores. Four different POWER9 processor card features with 8, 10, 11, or 12 functional cores are available to choose from. You cannot use different processor card features within a Power S924 server. All processor card features can be used in one-socket or two-socket configurations. It is possible to add a second socket as a MES upgrade order to a system that was initially ordered with only one 8-core, 10-core, 11-core, or 12-core processor card.

By default, all functional cores on a processor card must be activated through related processor core activation features. However, to assist with the optimization of software licensing, the factory deconfiguration feature #2319 is available at initial order to permanently reduce the number of active cores.

Table 2-4 shows the number of functional cores, their typical frequency range, and the processor core activation feature codes for each of the available processor card feature codes of a Power S924 server.

Table 2-4   Processor feature code specification for the Power S924 server

| Processor card feature code   | Configuration options   |   Number of cores | Typical frequency range [GHz]   | Processor core activation feature code   |
|-------------------------------|-------------------------|-------------------|---------------------------------|------------------------------------------|
| #EP5E                         | 1- or 2-socket          |                 8 | 3.8 - 4.0                       | #EP6E                                    |
| #EP5F                         | 1- or 2-socket          |                10 | 3.5 - 3.9                       | #EP6F                                    |
| #EP5H                         | 1- or 2-socket          |                11 | 3.45 - 3.9                      | #EP6H                                    |
| #EP5G                         | 1- or 2-socket          |                12 | 3.4 - 3.9                       | #EP6G                                    |

## 2.1.6  Memory access

The Power S922, Power S914, and Power S924 scale-out servers use direct-attached DDR4 industry-standard RDIMMs (IS RDIMMs). Each POWER9 processor-based module has two memory controllers, which operate four memory channels each. One memory channel can support up to two DIMMs, which implies a maximum of 16 DDR4 IS RDIMMs slots per POWER9 processor-based module. If only one DIMM slot of a memory channel is populated, the configuration is referred to as single drop , and if both DIMM slots of a memory channel are populated, the configuration is referred to as double-drop constellation. The nominal data rate of a memory RDIMM is different for single-drop and double-drop constellations. RDIMMs in single-drop mode run at 2666 Mbps, and in double-drop mode the data rate is slightly lower at 2133 Mbps.

Table 2-5 shows the RDIMM data rates for the available RDIMM sizes in single- (one DIMM per channel) and double- (two DIMMs per channel) drop mode.

Table 2-5   RDIMM data rate for certain RDIMM sizes

| RDIMM size   | Data rate in single-drop mode (One DIMM per channel)   | Data rate in double-drop mode (Two DIMMs per channel)   |
|--------------|--------------------------------------------------------|---------------------------------------------------------|
| 16 GB        | 2666 Mbps                                              | 2133 Mbps                                               |
| 32 GB        | 2666 Mbps                                              | 2133 Mbps                                               |
| 64 GB        | 2666 Mbps                                              | 2133 Mbps                                               |
| 128 GB       | 2666 Mbps                                              | 2133 Mbps                                               |

The Power S914 server can support up to 1 TB of memory. The Power S922 and Power S924 servers in a two-socket configuration can use up to 4 TB of memory.

Figure 2-5 illustrates the POWER9 direct-attached memory architecture by using two memory control units (MCUs) with four DDR4 channels each.

Figure 2-5   Overview of POWER9 direct-attach memory architecture

<!-- image -->

## 2.1.7  On-chip L3 cache innovation and intelligent caching

Like POWER8, the POWER9 processor uses a breakthrough in material engineering and microprocessor fabrication to implement the L3 cache in eDRAM technology and place it on the processor die. The L3 cache is critical to a balanced design, as is the ability to provide good signaling between the L3 cache and other elements of the hierarchy, such as the L2 cache or symmetric multiprocessor (SMP) interconnect.

The on-chip L3 cache is organized into separate areas with differing latency characteristics. Each processor core is associated with a 10 MB fast local region of L3 cache (FLR-L3), but also has access to other L3 cache regions as a shared L3 cache. Additionally, each core can negotiate to use the FLR-L3 cache that is associated with another core, depending on the reference patterns. Data can also be cloned and stored in more than one core's FLR-L3 cache, again depending on the reference patterns. This intelligent cache management enables the POWER9 processor to optimize the access to L3 cache lines and minimize overall cache latencies.

Here are the L3 cache features on the POWER9 processor:

- Private 10-MB L3 cache/shared L3.
- Twenty-way set associative.
- One hundred twenty-eight-byte cache lines with 64-byte sector support.
- Ten eDRAM banks (interleaved for access overlapping).
- Sixty-four-byte-wide data bus to L2 for reads.
- Sixty-four-byte-wide data bus from L2 for L2 castouts.
- Eighty 1 Mb eDRAM macros that are configured in 10 banks, with each bank having a 64-byte wide data bus.
- All cache accesses have the same latency.

A 20-way directory is organized as four banks, with up to four reads or two reads and two writes every two processor clock cycles to differing banks.

## 2.1.8 Hardware transactional memory

Transactional memory is an alternative to lock-based synchronization. It attempts to simplify parallel programming by grouping read and write operations and running them like a single operation. Transactional memory is like database transactions where all shared memory accesses and their effects are either committed together or discarded as a group. All threads can enter the critical region simultaneously. If there are conflicts in accessing the shared memory data, threads try accessing the shared memory data again or are stopped without updating the shared memory data. Therefore, transactional memory is also called lock-free synchronization . Transactional memory can be a competitive alternative to lock-based synchronization.

Transactional memory provides a programming model that makes parallel programming easier. A programmer delimits regions of code that access shared data, and the hardware runs these regions atomically and in isolation, buffering the results of individual instructions and retrying execution if isolation is violated. Generally, transactional memory enables programs to use a programming style that is close to coarse-grained locking to achieve performance that is close to fine-grained locking.

Most implementations of transactional memory are based on software. The POWER9 processor-based servers provide a hardware-based implementation of transactional memory that is more efficient than the software implementations and requires no interaction with the processor core, therefore enabling the system to operate in maximum performance.

## 2.1.9  Coherent Accelerator Processor Interface 2.0

IBM Coherent Accelerator Processor Interface (CAPI) 2.0 is the evolution of CAPI and defines a coherent accelerator interface structure for attaching special processing devices to the POWER9 processor bus. As with the original CAPI, CAPI 2.0 can attach accelerators that have coherent shared memory access with the processors in the server and share full virtual address translation with these processors by using standard PCIe Gen 4 buses with twice the bandwidth compared to the previous generation.

Applications can have customized functions in Field Programmable Gate Arrays (FPGAs) and queue work requests directly into shared memory queues to the FPGA. Applications can also have customized functions by using the same effective addresses (pointers) they use for any threads running on a host processor. From a practical perspective, CAPI enables a specialized hardware accelerator to be seen as an extra processor in the system with access to the main system memory and coherent communication with other processors in the system.

Figure 2-6 shows a comparison of the traditional model, where the accelerator must go through the processor to access memory with CAPI.

Figure 2-6   CAPI accelerator that is attached to the POWER9 processor

<!-- image -->

The benefits of using CAPI include the ability to access shared memory blocks directly from the accelerator, perform memory transfers directly between the accelerator and processor cache, and reduce the code path length between the adapter and the processors. This reduction in the code path length might occur because the adapter is not operating as a traditional I/O device, and there is no device driver layer to perform processing. CAPI also presents a simpler programming model.

The accelerator adapter implements the POWER Service Layer, which provides address translation and system memory cache for the accelerator functions. The custom processors on the system board, consisting of an FPGA or an ASIC, use this layer to access shared memory regions, and cache areas as though they were a processor in the system. This ability enhances the performance of the data access for the device and simplifies the programming effort to use the device. Instead of treating the hardware accelerator as an I/O device, it is treated as a processor, which eliminates the requirement of a device driver to perform communication. It also eliminates the need for direct memory access that requires system calls to the operating system (OS) kernel. By removing these layers, the data transfer operation requires fewer clock cycles in the processor, improving the I/O performance.

The implementation of CAPI on the POWER9 processor enables hardware companies to develop solutions for specific application demands. Companies use the performance of the POWER9 processor for general applications and the custom acceleration of specific functions by using a hardware accelerator with a simplified programming model and efficient communication with the processor and memory resources.

## 2.1.10 Power management and system performance

The POWER9 processor-based Power S922, Power S914, and Power S924 servers implement Workload Optimized Frequency (WOF) technology as a new feature of the IBM EnergyScale power management technology. With IBM EnergyScale in a POWER9 processor-based server, the POWER8 processor-based dynamic power saver (DPS) modes that favor either lower power consumption or favor performance are replaced by two new power saver modes:

- Dynamic performance mode (DPM)
- Maximum performance mode (MPM)

Every POWER9 processor-based scale-out or scale-up server has either DPM or MPM enabled by default. For the Power S914 server (9009-41G), DPM is enabled by default, and the Power S922 (9009-22G) and Power S924 (9009-42G) servers have MPM enabled by default. Power S914 servers, especially the tower models, may be used in an office workspace where the extra fan noise that might be potentially caused by the MPM is unacceptable. If the acoustics are not an issue, you can change the Power S914 system setting from DPM to MPM.

Both DPM and MPM dynamically adjust the processor frequency to maximize performance and enable a much higher processor frequency range compared to POWER8 processor-based servers. Each of the new power saver modes delivers consistent system performance without any variation if the nominal operating environment limits are met.

For POWER9 processor-based servers that are under control of the PowerVM hypervisor, the DPM and MPM are system-wide configuration settings, but each processor module frequency is optimized separately.

Several factors determine the maximum frequency that a processor module can run at:

- Processor utilization: Lighter workloads run at higher frequencies.
- Number of active cores: Fewer active cores run at higher frequencies.
- Environmental conditions: At lower ambient temperatures, cores are enabled to run at higher frequencies.

The new power saver modes are defined as follows:

DPM

In DPM, the workload is run at the highest frequency possible if the nominal power consumption limit of the processor modules is accepted. The frequency of the processor modules is always at the nominal frequency of the POWER9 processor-based server or above the nominal frequency up to the upper limit of the DPM frequency range.

This DPM typical frequency range (DTFR) is published as part of the system specifications of a particular POWER9 processor-based server if it is running by default in the DPM. The system performance is deterministic within the allowed operating environmental limits, so it does not depend on the ambient temperature if the temperature stays within the supported range.

The idle power saver (IPS) function can be enabled or disabled. If IPS is enabled and all cores in a processor module are idle for hundreds of milliseconds, the frequency of the cores in the respective module drop to the predefined power save frequency.

MPM

In MPM, the workload is run at the highest frequency possible, but unlike in the DPM, the processor module may operate at a higher power consumption level. The higher power draw enables the processor modules to run in an MPM typical frequency range (MTFR) where the lower limit is above the nominal frequency and the upper limit is determined by the system's maximum frequency.

The MTFR is published as part of the system specifications of a particular POWER9 processor-based if it is running by default in MPM. The higher power draw potentially increases the fan speed of the respective system node to meet the higher cooling requirements, which cause a higher noise emission level of up to 15 decibels. The processor frequency typically stays within the limits that are given by the MTFR, but may be lowered to frequencies between the MTFR lower limit and the nominal frequency at high ambient temperatures above 25 °C (77 °F). If the data center ambient environment is less than 25 °C, the frequency in MPM is consistently in the upper range of the MTFR (roughly 10% to 20% better than nominal). At lower ambient temperatures (below 25 °C), MPM mode also provides deterministic performance. As the ambient temperature increases above 25 °C, determinism can no longer be guaranteed.

The IPS function can be enabled or disabled. If IPS is enabled, the frequency is dropped to the static power saver level if the entire system meets the configured idle conditions.

Figure 2-7 shows the frequency ranges for the POWER9 static nominal mode (all modes disabled), the DPM, and the MPM. The frequency adjustments for different workload characteristics, ambient conditions, and idle states are also indicated.

Figure 2-7   POWER9 power management modes and related frequency ranges

<!-- image -->

Table 2-6, Table 2-7, and Table 2-8 show the static nominal frequencies and the frequency ranges of the DPM and the MPM of all processor module types that are available for Power S922, Power S914, and Power S924 servers.

Table 2-6   Characteristic frequencies and frequency ranges for Power S922 server

| Feature code   |   Cores per SCM | Static nominal frequency [GHz]   | DPM frequency range [GHz]   | MPM frequency range [GHz]   |
|----------------|-----------------|----------------------------------|-----------------------------|-----------------------------|
| #EP56          |               4 | 2.3 2.3 -                        | 3.8                         | 2.8 - 3.8                   |
| #EP58          |               8 | 3.0                              | 3.0 - 3.9                   | 3.4 - 3.9                   |
| #EP59          |              10 | 2.5                              | 2.5 - 3.8                   | 2.9 - 3.8                   |
| #EP5B          |              11 | 2.4                              | 2.4 - 3.8                   | 2.8 - 3.8                   |

Table 2-7 Characteristic frequencies and frequency ranges for Power S914 server

| Feature code   |   Cores per SCM |   Static nominal frequency [GHz] | DPM frequency range [GHz]   | MPM frequency range [GHz]   |
|----------------|-----------------|----------------------------------|-----------------------------|-----------------------------|
| #EP50          |               4 |                              2.3 | 2.3 - 3.8                   | 2.8 - 3.8                   |
| #EP51          |               6 |                              2.3 | 2.3 - 3.8                   | 2.8 - 3.8                   |
| #EP52          |               8 |                              2.8 | 2.8 - 3.8                   | 3.15 - 3.8                  |

Table 2-8   Characteristic frequencies and frequency ranges for Power S924 server

| Feature code   |   Cores per SCM | Static nominal frequency [GHz]   | DPM frequency range [GHz]   | MPM frequency range [GHz]   |
|----------------|-----------------|----------------------------------|-----------------------------|-----------------------------|
| #EP5E 8        |           3.3   | 3.3 - 4.0                        | 3.8 -                       | 4.0                         |
| #EP5F 10       |           2.9   | 2.9 -                            | 3.9                         | 3.5 - 3.9                   |
| #EP5G 11       |           2.817 |                                  | 2.817 - 3.9                 | 3.45 - 3.9                  |
| #EP5H 12       |           2.75  |                                  | 2.75 - 3.9                  | 3.4 - 3.9                   |

For more information about IBM EnergyScale, see IBM EnergyScale for POWER9 Processor-Based Systems .

## 2.1.11  Comparing the POWER9, POWER8, and POWER7+ processors

The Power S922, Power S914, and Power S924 servers use POWER9 processor-based modules with 12 architected cores that can support eight SMT execution contexts.

Table 2-9 shows a comparison between the POWER9 processor implementation for Power S922, Power S914, and Power S924 servers, and the POWER8 and POWER7 processors implementation for previous Power Systems server generations.

Table 2-9   Comparing the POWER9, POWER8, and POWER7+ processor implementations

| Characteristics   | POWER9 a          | POWER8   | POWER7+   |
|-------------------|-------------------|----------|-----------|
| Technology        | 14 nm             | 22 nm    | 32 nm     |
| Die size          | 68.5 mm x 68.5 mm | 649 mm 2 | 567 mm 2  |

| Characteristics              | POWER9 a                                                                                                  | POWER8                                                                                                 | POWER7+                                                                                                  |
|------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Number of transistors        | 8 billion                                                                                                 | 4.2 billion                                                                                            | 2.1 billion                                                                                              |
| Maximum cores                | 12                                                                                                        | 12                                                                                                     | 8                                                                                                        |
| Maximum SMT threads per core | 8 threads                                                                                                 | 8 threads                                                                                              | 4 threads                                                                                                |
| Maximum frequency            | 3.8 - 4.0 GHz                                                                                             | 4.15 GHz                                                                                               | 4.4 GHz                                                                                                  |
| L2 Cache                     | 512 KB per cores                                                                                          | 512 KB per core                                                                                        | 256 KB per core                                                                                          |
| L3 Cache                     | 10 MB of FLR-L3 cache per core with each core having access to the full 120 MB of L3 cache, on-chip eDRAM | 8 MBof FLR-L3 cache per core with each core having access to the full 96 MB of L3 cache, on-chip eDRAM | 10 MB of FLR-L3 cache per core with each core having access to the full 80 MB of L3 cache, on-chip eDRAM |
| Memory support               | DDR4                                                                                                      | DDR3 and DDR4                                                                                          | DDR3                                                                                                     |
| I/O bus                      | PCIe Gen 4                                                                                                | PCIe Gen3                                                                                              | GX++                                                                                                     |

- a. POWER9 processor implementation for Power S922, Power S914, and Power S924 servers.

## 2.2  Memory subsystem

The POWER9 MCU provides the system memory interface between the on-chip SMP fabric and the memory interface physical unit (DDR PHY unit), which connects to DDR4 industry-standard RDIMMs (IS RDIMMs).

There are logically eight independent MCUs on the POWER9 processor that interface to eight DDR4/4E memory buses. Each MCU memory port supports up to two DDR4 DIMM slots. If only one DIMM slot is populated, the configuration is referred to as a single-drop constellation , and if both DIMM slots are populated, the configuration is referred to as a double-drop constellation .

Physically, the MCUs are grouped into two instances of the extended memory controller (EMC) chiplet: MCU Group 0 and MCU Group 1. So, each EMC chiplet contains four MCUs plus pervasive logic.

On new systems orders, IS RDIMMs with 16 GB, 32 GB, 64 GB, and 128 GB are used in various combinations throughout the new 9009-22G, 9009-41G, and 9009-42G server family. Independent of the size, all RDIMMs on single-drop constellation run at 2666 Mbps and on a double-drop constellation at 2133 Mbps data rates.

Note: The 8 GB (#EM60) memory features offered for earlier Power S922 (9009-22A), Power S914 (9009-41A), and Power S924 (9009-42A) servers are not available on new orders but are supported on new 9009-22G, 9009-41G, and 9009-42G servers.

The Power S914 (9009-41G) server is a one-socket system that supports one POWER9 processor-based module. The server offers a maximum of 16 DDR4 DIMM slots.

Memory features of 16 GB (#EM62), 32 GB (#EM63), and 64 GB (#EM64) are available for 6-core #EP51 or 8-core #EP52 processor module configurations at initial order. By using the 64 GB RDIMM size on all 16 DDR4 DIMM slots, the Power S914 server can have a maximum of 1 TB system memory. Memory features must be ordered in pairs and at least two memory slots must be populated, which implies a minimum memory capacity of 32 GB.

For 4-core #EP50 processor module servers, the maximum of total system memory is 64 GB, and the following memory configurations are supported:

- Quantity of 2 or 4 of #EM62 (16 GB DDR4 RDIMM)
- Quantity of 2 of #EM63 (32 GB DDR4 RDIMM)

The Power S922 (9009-22G) and Power S924 (9009-42G) servers are two-socket servers that support either one or two POWER9 processor-based modules. The servers offer a maximum of 32 DDR4 DIMM slots, with 16 DIMM slots per installed processor module.

Memory features for 16 GB (#EM62), 32 GB (#EM63), 64 GB (#EM64), and 128 GB (#EM65) are available for all processor module configurations of the Power S922 and Power S924 systems at initial order.

By using the 128 GB RDIMM size on all 32 DDR4 DIMM slots, the Power S922 and Power S924 servers can have a maximum of 4 TB system memory. Memory features must be ordered in pairs and at least two memory slots must be populated per processor module, which implies a minimum memory capacity of 32 GB for one-socket and 64 GB for two-socket configurations. Memory data rates vary depending on the RDIMM size and module placement, as shown in Table 2-10.

Table 2-10   RDIMM data rate for 9009-22G, 9009-41G, and 9009-42G servers

| RDIMM size   | Data rate (1 RDIMM per port)   | Data rate (2 RDIMMs per port)   |
|--------------|--------------------------------|---------------------------------|
| 8 GB a       | 2400 Mbps                      | 2133 Mbps                       |
| 16 GB        | 2666 Mbps                      | 2133 Mbps                       |
| 32 GB        | 2666 Mbps                      | 2133 Mbps                       |
| 64 GB        | 2666 Mbps                      | 2133 Mbps                       |
| 128 GB       | 2666 Mbps                      | 2133 Mbps                       |

- a. RDIMMs of 8 GB size are supported but not available on new system orders.

The maximum theoretical memory bandwidth for a POWER9 processor-based module is 170 GBps. The total maximum theoretical memory bandwidth for a two-socket system is 340 GBps.

All servers support an optional feature that is called Active Memory Expansion that enables the effective maximum memory capacity to be much larger than the true physical memory on AIX. This feature runs innovative compression and decompression of memory content by using a dedicated coprocessor to provide memory expansion up to 125%, depending on the workload type and its memory usage.

For example, a server with 256 GB RAM physically installed can effectively be expanded over 512 GB RAM. This approach can enhance virtualization and server consolidation by allowing a partition to do more work with the same physical amount of memory or a server to run more partitions and do more work with the same physical amount of memory.

## 2.2.1 Memory placement rules

The following memory options are available to order:

- 16 GB DDR4 DRAM (#EM62)
- 32 GB DDR4 DRAM (#EM63)
- 64 GB DDR4 DRAM (#EM64)
- 128 GB DDR4 DRAM (#EM65)

Note: If you use the 4-core processor module #EP50, only 16 GB (#EM62) and 32 GB (#EM63) memory sizes are offered.

All memory features must be ordered in pairs, with a minimum of 32 GB for the Power S922, Power S914, and Power S924 servers that have a single processor module installed. A 64 GB memory feature is the minimum for Power S922 or Power S924 servers with two processors modules installed.

The supported maximum memory is as follows for the Power S914 (9009-41G) server:

- One 4-core #EP50 processor module installed: 64 GB (four 16 GB RDIMMs or two 32 GB RDIMMs)
- One 6-core #EP51 or 8-core #EP52 processor module installed: 1 TB (sixteen 64 GB RDIMMs)

The supported maximum memory is as follows for the Power S922 (9009-22G) and the Power S924 (9009-42G) servers:

- One processor module installed: 2 TB (sixteen 128 GB RDIMMs)
- Two processors modules installed: 4 TB (thirty-two 128 GB RDIMMs)

The basic rules for memory placement follow:

- Each feature code equates to a single physical RDIMM.
- All memory features must be ordered in pairs.
- All memory features must be ordered in even quantities:
- -For single-processor module configurations, the supported quantities of RDIMMs are 2, 4, 6, 8, 12, and 16. Quantities of 10 or 14 RDIMMs are not supported.
- -For double-processor module configurations, the supported quantities of RDIMMs are 4, 6, 8, 10, 12, 14, 16, 20, 24, 28, and 32. Quantities of 18, 22, 26, or 30 RDIMMs are not supported.

If the configuration rules require you to order a quad of memory features, not all features must be the same size, but can be a combination of two memory feature pairs of different sizes.

- All memory RDIMMs must be installed in pairs.
- Each RDIMM within a pair must be of the same capacity.

In general, the preferred approach is to install memory evenly across all processors in the system. Balancing memory across the installed processors enables memory access in a consistent manner and typically results in the best possible performance for your configuration. You should account for any plans for future memory upgrades when you decide which memory feature size to use at the time of the initial system order.

Figure 2-8 shows the physical memory DIMM slot topology of the Power S914 server and for one-socket configurations of the Power S922 and Power S924 servers.

Figure 2-8   Memory DIMM slot topology for one-socket configurations

<!-- image -->

For servers with a single processor module that is installed, the plugging order for the memory RDIMMs is as follows (see Figure 2-9):

- Pair installation:
- -The first RDIMM pair is installed at Red 1 (C33 DDR0-A and C17 DDR1-A).
- -The second RDIMM pair is installed at Gold 2 (C36 DDR4-A and C22 DDR5-A).
- -The third RDIMM pair is installed at Cyan 3 (C31 DDR2-A and C15 DDR3-A).
- -The fourth RDIMM pair is installed at Gray 4 (C38 DDR6-A and C20 DDR7-A).
- Quad installation:
- -Two fifth RDIMM pairs (or quad) are installed at Red 5 (C34 DDR0-B and C18 DDR1-B) and at Cyan 5 (C32 DDR2-B and C16 DDR3-B).
- -Two sixth RDIMM pairs (or quad) are installed at Gold 6 (C35 DDR4-B and C21 DDR-B) and at Gray 6 (C37 DDR6-B and C19 DDR7-B).

Figure 2-9   RDIMM plug sequence for the Power S914 server

<!-- image -->

## More considerations:

- You cannot mix RDIMMs of different capacity and ranking in a single-drop constellation within an MCU group. A 1-socket 9009-41G system runs in single-drop constellation if it contains eight or fewer memory modules, so the size and rank type of all RDIMMs within each MCU group must be identical. This rule is also significant if 8 GB #EM60 RDIMMs from earlier Power S922 (9009-22A), Power S914 (9009-41A), or Power S924 (9009-42A) servers are migrated to a 9009-41G server. Table 2-11 lists the size and the rank count of all supported memory feature codes for Power S922, Power S914, and Power S924 systems.
- a. 1R designates RDIMMs with one rank and 2R designates RDIMMs with two ranks.
- b. RDIMMs of 8 GB size are supported but not available on new system orders.
- The memory feature order and placement rules require that the transition from a single-drop to double-drop constellation occurs on MCU group boundaries. The installation of a quad transforms the respective MCU group from a single-drop to a double-drop constellation.
- RDIMMs in the same color cells must be identical (same size and rank).

Table 2-11   Size and rank type of supported memory feature codes

| Feature code   | Size   | Ranking a   |
|----------------|--------|-------------|
| #EM60 b        | 8 GB   | 1R          |
| #EM62          | 16 GB  | 1R          |
| #EM63          | 32 GB  | 2R          |
| #EM64          | 64 GB  | 2R          |
| #EM65          | 128 GB | 2R          |

Note: Each color in Figure 2-9 represents a unique RDIMM size and type.

Figure 2-10 shows the physical memory DIMM topology of the Power S922 and Power S924 servers.

Figure 2-10   Memory DIMM slot topology for the Power S922 and the Power S924 servers

<!-- image -->

For the Power S922 and Power S924 servers, the plugging order for the memory RDIMMs is as follows (see Figure 2-11):

- Pair installation:
- -The first DIMM pair is installed at Red 1 (C33 DDR0-A and C17 DDR1-A) of SCM-0.
- -The second DIMM pair is installed at Green 2 (C41 DDR0-A and C25 DDR1-A) of SCM-1.
- -The third DIMM pair is installed at Gold 3 (C36 DDR4-A and C22 DDR5-A) of SCM-0.
- -The fourth DIMM pair is installed at Purple 4 (C44 DDR4-A and C30 DDR5-A) of SCM-1.
- -The fifth DIMM pair is installed at Cyan 5 (C31 DDR2-A and C15 DDR3-A) of SCM-0.
- -The sixth DIMM pair is installed at Pink 6 (C39 DDR2-A and C23 DDR3-A) of SCM-1.
- -The seventh DIMM pair is installed at Gray 7 (C38 DDR6-A and C20 DDR7-A) of SCM-0.
- -The eighth DIMM pair is installed at Yellow 8 (C46 DDR6-A and C28 DDR7-A) of SCM-1.
- Quad installation:
- -Two ninth DIMM pairs (or quad) are installed at Red 9 (C34 DDR0-B and C18 DDR1-B) and at Cyan 9 (C32DDR2-B and C16 DDR3-B) of SCM-0.
- -Two 10th DIMM pairs (or quad) are installed at Green 10 (C42 DDR0-B and C26 DDR1-B) and at Pink 10 (C40 DDR2-B and C24 DDR3-B) of SCM-1.
- -Two 11th DIMM pairs (or quad) are installed at Gold 11 (C35 DDR4-B and C21 DDR5-B) and at Gray 11 (C37 DDR6-B and C19 DDR7-B) of SCM-0.
- -Two 12th DIMM pairs (or quad) are installed at Purple 12 (C43 DDR4-B and C29 DDR5-B) and at Yellow 12 (C45 DDR6-B and C27 DDR7-B) of SCM-1.

Figure 2-11   RDIMM plug sequence for Power S922 and Power S924 servers

<!-- image -->

## More considerations:

- You cannot mix RDIMMs of different capacity and ranking in a single-drop constellation within an MCU group. A two-socket Power S922 or Power S924 server runs in single-drop constellation if it contains 16 or fewer memory modules, so the size and rank type of all RDIMMs within each MCU group must be identical. This rule is also significant if 8 GB #EM60 RDIMMs from earlier Power S922 (9009-22A), Power S914 (9009-41A), or Power S924 (9009-42A) servers are migrated to a 9009-22G or 9009-42G server. Table 2-11 on page 85 lists the size and the rank count of all supported memory feature codes for Power S922, Power S914, and Power S924 servers.
- DIMMs at same color cells must be identical (same size and rank).

## 2.2.2 Memory bandwidth

The Power S914 server provides one POWER9 processor-based module and the Power S922 and Power S924 servers can be configured with either one or two processor modules. Each processor module drives eight memory channels that are organized in two MCU groups. Each memory channel or port supports single- or double-drop industry-standard RDIMMs, so each channel can accommodate one or two DIMMs. As data flows from main memory towards the execution units of the POWER9 processor cores, they pass through the 512 KB L2 and the 64 KB L1 cache. In many cases, the 10 MB L3 victim cache might also provide the data that is needed for the instruction execution.

The following sections show the cache and memory bandwidth capabilities of the Power S922, Power S914, and Power S924 servers.

## Power S922 (9009-22G) cache and memory bandwidth

Table 2-12 shows the maximum cache bandwidth for a single core as defined by the width of the relevant channels and the related transaction rates of a Power S922 server.

Table 2-12   The Power S922 (9009-22G) single core architectural maximum cache bandwidth

| Single core   | Power S922 server         | Power S922 server         |
|---------------|---------------------------|---------------------------|
|               | 1 core @3.8 GHz (maximum) | 1 core @3.9 GHz (maximum) |
| L1 data cache | 364.8 GBps                | 374.4 GBps                |
| L2 cache      | 364.8 GBps                | 374.4 GBps                |
| L3 cache      | 243.2 GBps                | 249.6 GBps                |

The bandwidth figures for the caches are calculated as follows:

- L1 data cache: In one clock cycle, four 16-byte load operations and two 16-byte store operations can be accomplished. The values vary depending on the core frequency and are computed as follows:
- -Core running at 3.8 GHz: (4 x 16 B + 2 x 16 B) x 3.8 GHz = 364.8 GBps
- -Core running at 3.9 GHz: (4 x 16 B + 2 x 16 B) x 3.9 GHz = 374.4 GBps
- L2 cache: In one clock cycle, one 64-byte read operation to the core and two 16-byte store operations from the core can be accomplished. The values vary depending on the core frequency and are computed as follows:
- -Core running at 3.8 GHz: (4 x 16 B + 2 x 16 B) x 3.8 GHz = 364.8 GBps
- -Core running at 3.9 GHz: (4 x 16 B + 2 x 16 B) x 3.9 GHz = 374.4 GBps
- L3 cache: With two clock cycles, one 64-byte read operation to the L2 cache and one 64-byte store operation from the L2 cache can be accomplished. The values vary depending on the core frequency and are computed as follows:
- -Core running at 3.8 GHz: (1 x 64 B + 1 x 64 B) x 3.8 GHz / 2 = 243.2 GBps
- -Core running at 3.9 GHz: (1 x 64 B + 1 x 64 B) x 3.9 GHz / 2 = 249.6 GBps

For the maximum configuration with two processor modules installed and all memory channels populated in single-drop constellation, the overall aggregated memory bandwidth figures of the Power S922 server as defined by the width of the relevant channels and the related transaction rates are shown in Table 2-13.

Table 2-13   The Power S922 (9009-22G) total architectural maximum cache and memory bandwidth

| Total bandwidths   | Power S922 server           | Power S922 server           |
|--------------------|-----------------------------|-----------------------------|
|                    | 16 cores @3.9 GHz (maximum) | 20 cores @3.8 GHz (maximum) |
| L1 data cache      | 5990.4 GBps                 | 7296 GBps                   |
| L2 cache           | 5990.4 GBps                 | 7296 GBps                   |
| L3 cache           | 3993.6 GBps                 | 4864 GBps                   |
| Total memory       | 340 GBps                    | 340 GBps                    |
| PCIe Interconnect  | 320 GBps                    | 320 GBps                    |
| X Bus SMP          | 16 GBps                     | 16 GBps                     |

## Power S914 (9009-41G) server cache and memory bandwidth

Table 2-14 shows the maximum cache bandwidth for a single core as defined by the width of the relevant channels and the related transaction rates of a Power S914 server.

Table 2-14   The Power S914 (9009-41G) single core architectural maximum cache bandwidth

| Single core   | Power S914 server 1 core @3.8 GHz (maximum)   |
|---------------|-----------------------------------------------|
| L1 data cache | 364.8 GBps                                    |
| L2 cache      | 364.8 GBps                                    |
| L3 cache      | 243.2 GBps                                    |

The bandwidth figures for the caches are calculated as follows:

- L1 data cache: In one clock cycle, four 16-byte load operations and two 16-byte store operations can be accomplished. The value depends on the core frequency and is computed as follows:

Core running at 3.8 GHz: (4 x 16 B + 2 x 16 B) x 3.8 GHz = 364.8 GBps

- L2 cache: In one clock cycle, one 64-byte read operation to the core and two 16-byte store operations from the core can be accomplished. The value depends on the core frequency and is computed as follows:

Core running at 3.8 GHz: (4 x 16 B + 2 x 16 B) x 3.8 GHz = 364.8 GBps

- L3 cache: With two clock cycles, one 64-byte read operation to the L2 cache and one 64-byte store operation from the L2 cache can be accomplished. The value depends on the core frequency and is computed as follows:

Core running at 3.8 GHz: (1 x 64 B + 1 x 64 B) x 3.8 GHz / 2 = 243.2 GBps

For the maximum configuration with one processor module installed and all memory channels populated in a one-drop constellation, the overall aggregated bandwidth figures of the Power S914 as defined by the width of the relevant channels and the related transaction rates are shown in Table 2-15.

Table 2-15   The Power S914 (9009-41G) total architectural maximum cache and memory bandwidth

| Total bandwidths   | Power S914 server          | Power S914 server          | Power S914 server          |
|--------------------|----------------------------|----------------------------|----------------------------|
|                    | 4 cores @3.8 GHz (maximum) | 6 cores @3.8 GHz (maximum) | 8 cores @3.8 GHz (maximum) |
| L1 data cache      | 1459.2 GBps                | 2188.8 GBps                | 2918.4 GBps                |
| L2 cache           | 1459.2 GBps                | 2188.8 GBps                | 2918.4 GBps                |
| L3 cache           | 972.8 GBps                 | 1459.2 GBps                | 1945.6 GBps                |
| Total memory       | 170 GBps                   | 170 GBps                   | 170 GBps                   |
| PCIe Interconnect  | 160 GBps                   | 160 GBps                   | 160 GBps                   |

## Power S924 (9009-42G) cache and memory bandwidth

Table 2-16 shows the maximum cache bandwidth for a single core as defined by the width of the relevant channels and the related transaction rates of a Power S924 server.

Table 2-16   The Power S924 (9009-42G) single core architectural maximum cache bandwidth

| Single core   | Power S924 server         | Power S924 server         |
|---------------|---------------------------|---------------------------|
|               | 1 core @3.9 GHz (maximum) | 1 core @4.0 GHz (maximum) |
| L1 data cache | 374.4 GBps                | 384 GBps                  |
| L2 cache      | 374.4 GBps                | 384 GBps                  |
| L3 cache      | 249.6 GBps                | 256 GBps                  |

The bandwidth figures for the caches are calculated as follows:

- L1 data cache: In one clock cycle, four 16-byte load operations and two 16-byte store operations can be accomplished. The values vary depending on the core frequency and are computed as follows:
- -3.9 GHz core: (4 x 16 B + 2 x 16 B) x 3.9 GHz = 374.4 GBps
- -4.0 GHz core: (4 x 16 B + 2 x 16 B) x 4.0 GHz = 384 GBps
- L2 cache: In one clock cycle, one 64-byte load operation and two 16-byte store operations can be accomplished. The values vary depending on the core frequency and are computed as follows:
- -3.9 GHz core: (4 x 16 B + 2 x 16 B) x 3.9 GHz = 374.4 GBps
- -4.0 GHz core: (4 x 16 B + 2 x 16 B) x 4.0 GHz = 384 GBps
- L3 cache: With two clock cycles, one 64-byte read operation to the L2 cache and one 64-byte store operation from the L2 cache can be accomplished. The value depends on the core frequency and is computed as follows:
- -Core running at 3.9 GHz: (1 x 64 B + 1 x 64 B) x 3.9 GHz / 2 = 249.6 GBps
- -Core running at 4.0 GHz: (1 x 64 B + 1 x 64 B) x 4.0 GHz / 2 = 256 GBps

For the maximum configuration with two processor modules installed and all memory channels populated in single-drop constellation, the overall aggregated memory bandwidth figures of the Power S924 server as defined by the width of the relevant channels and the related transaction rates are shown in Table 2-17.

Table 2-17   The Power S924 (9009-42G) total architectural maximum cache and memory bandwidth

| Total bandwidths   | Power S924 server           | Power S924 server           | Power S924 server           |
|--------------------|-----------------------------|-----------------------------|-----------------------------|
|                    | 16 cores @4.0 GHz (maximum) | 20 cores @3.9 GHz (maximum) | 24 cores @3.9 GHz (maximum) |
| L1 (data) cache    | 6144 GBps                   | 7488 GBps                   | 8985.6 GBps                 |
| L2 cache           | 6144 GBps                   | 7488 GBps                   | 8985.6 GBps                 |
| L3 cache           | 4096 GBps                   | 4992 GBps                   | 5990.4 GBps                 |
| Total memory       | 340 GBps                    | 340 GBps                    | 340 GBps                    |
| PCIe Interconnect  | 320 GBps                    | 320 GBps                    | 320 GBps                    |
| X Bus SMP          | 16 GBps                     | 16 GBps                     | 16 GBps                     |

Note: There are several POWER9 design points to consider when comparing hardware designs that use SMP communication bandwidths as a unique measurement. The POWER9 architecture provides:

- More cores per socket, which leads to lower inter-CPU communication.
- More RAM density (up to 2 TB per socket), which leads to less inter-CPU communication.
- Greater RAM bandwidth for less dependence on an L3 cache.
- Intelligent hypervisor scheduling that places RAM usage close to the CPU.
- New SMP routing so that multiple channels are available when congestion occurs.

## Memory bandwidth considerations

The Power S922, Power S914, and Power S924 servers are memory performance-optimized with eight DIMM slots that are populated per processor module because in this configuration all memory DIMMs work in single-drop mode with a data rate of 2666 Mbps. If both DIMMs are populated (double drop) in a memory channel, the data rate is reduced to 2133 Mbps.

The maximum bandwidth of the system depends on the number of channels that are used and whether the channel operates in single-drop or double-drop mode. A DDR4 DIMM that is clocked at 2666 MHz has a maximum transfer rate of 21.25 GBps. A DDR4 DIMM that is clocked t 2133 MHz has a maximum transfer rate of 17.06 GBps. To calculate the maximum bandwidth, use the following formula:

Maximum Bandwidth = Number of DIMMs in single-drop mode x 21.25 GBps) + ((Number of DIMMs in double-drop mode / 2) x 17.06 GBps)

Table 2-18 shows the maximum memory bandwidth for the Power S914 server, depending on the number of DIMMs that are populated.

Table 2-18   Maximum memory bandwidth for the Power S914 (9009-41G)

|   DIMM quantity | Maximum bandwidth in GBps a   |
|-----------------|-------------------------------|
|               2 | 43                            |
|               4 | 85                            |
|               6 | 128                           |
|               8 | 170                           |
|              12 | 153 b                         |
|              16 | 136 c                         |

- a. Numbers are rounded to the nearest integer.
- b. MCU Group 0 operates in double-drop mode and MCU Group 1 operates in single-drop mode.
- c. Both MCU groups run in double-drop mode.

Table 2-19 shows the maximum memory bandwidth of the Power S922 and Power S924 servers, depending on the number of DIMMs that are populated.

Table 2-19   Maximum memory bandwidth of Power S922 (9009-22G) and Power S924 (9009-42G)

|   DIMM quantity | Maximum bandwidth in GBps a   |
|-----------------|-------------------------------|
|               4 | 85                            |
|               6 | 128                           |
|               8 | 170                           |
|              10 | 213                           |
|              12 | 255                           |
|              14 | 298                           |
|              16 | 340                           |
|              20 | 323 b                         |
|              24 | 306 c                         |
|              28 | 290 d                         |
|              32 | 273 e                         |

- a. Numbers are rounded to the nearest integer.
- b. MCU Group 0 of POWER9 SCM 0 operates in double-drop mode.
- c. MCU Group 0 of POWER9 SCM 0 and SCM 1 operate in double-drop mode.
- d. MCU Group 0 and MCU Group 1 of POWER9 SCM 0 and MCU Group 0 of SCM 1 operate in double-drop mode.
- e. MCU Group 0 and MCU Group 1 of POWER9 SCM 0 and SCM 1 operate in double-drop mode.

## 2.3  System buses

The Power S922, Power S914, and Power S924 servers are based on the POWER9 SCM in a package that is optimized for commercial entry servers. For each of the named systems, one processor module supports the following buses:

- Eight DDR4 ports support a maximum 2666 Mbps data rate if a single DIMM per channel is used and a maximum 2133 Mbps data rate if two DIMMs per channel are used.
- Two 30-bit + two spare (4-byte) inter-node SMP X buses at 16 Gbps signaling rate.
- 42 lanes PCIe Gen 4 at 16 Gbps signaling rate.
- Processor service interface (PSI) bus.

The following sections cover these buses in more detail. For more information, see the logical system diagrams at the beginning of Chapter 2, 'Architecture and technical overview' on page 65.

## 2.3.1  Memory buses

There are logically eight independent MCUs that are implemented on a POWER9 SCM. Each MCU provides the interface to one DDR4 memory bus and each of the related MCU memory ports provide access to two DDR4 DIMM slots. IS RDIMMs with DRAM data rates of 2133, 2400, and 2666 Mbps are supported to populate the DIMM slots.

For more information about the memory subsystem architecture, the available memory features and related placement rules, and the relevant bandwidth figures, see 2.2, 'Memory subsystem' on page 81.

## 2.3.2  Inter-node SMP X-buses

Each POWER9 SCM provides two X-bus links that are used in 2-socket Power S922 and Power S924 servers to create a scalable cache-coherent SMP system. The differential X-bus contains two clock groups. Each clock group consists of one clock, 16 data lanes, and one spare data lane. Both clock groups are connected to the same processor. The X-bus runs at a rate of 16 GHz. The peak bandwidth is 60 GBps per link with a peak data bandwidth of 48 GBps due to cyclic redundancy check (CRC) logic.

The two X-bus inter-node SMP connections between the sockets in Power S922 or Power S924 servers deliver a peak data bandwidth of 96 GBps.

## 2.3.3  PCIe Gen 4 buses

In Power S922, Power S914, and Power S924 servers, each POWER9 SCM integrates three PCIe Gen 4 controllers: E0, E1, and E2. E0 and E2 have 16 lanes and E1 has 10 lanes for a total of 42 lanes with a full duplex bandwidth of 4 GBps per lane. The 42 lanes can be configured to support up to six independent PCIe host bridges (PHBs) or PCIe buses. The number of used PHBs of an SCM is variable and depends on the position of the socket on the system board: SCM0 or SCM1.

Table 2-20 shows the PCIe bus configuration for the first (and only) socket (SCM0) of a Power S914 server or for the first socket (SCM0) of a Power S922 or a Power S924 server.

Table 2-20   PCIe Gen 4 I/O configuration for POWER9 SCM0

| PCIeGen4 controller   | PCIehost bridge   | Number of lanes   | Slot connection type                          | Slot number and specification a                                                               |
|-----------------------|-------------------|-------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------|
| E0                    | PHB0              | x16               | Direct                                        | C9 PCIe4 x16 CAPI 2.0 capable LP/FHHL                                                         |
| E1                    | PHB1              | x8                | Multiplexed through 52-lane PCIe Gen 4 switch | C10 PCIe4 x8 LP/FHHL                                                                          |
| E1                    | PHB1              | x8                | Multiplexed through 52-lane PCIe Gen 4 switch | C11 PCIe4 x8 LP/FHHL                                                                          |
| E1                    | PHB1              | x8                | Multiplexed through 52-lane PCIe Gen 4 switch | C12 PCIe4 x16 LP/FHHL                                                                         |
| E1                    | PHB1              | x8                | Multiplexed through 52-lane PCIe Gen 4 switch | C49 PCIe4 x8 with x16 connector internal slot: internal SAS adapter or NVMe pass-through card |
| E1                    | PHB2              | x1 b              | Direct                                        | PCIe2 USB 3.0 4-port c                                                                        |
| E2                    | PHB3              | x8                | Multiplexed through 52-lane PCIe Gen 4 switch | C5 PCIe4 x8 LP/FHHL                                                                           |
| E2                    | PHB3              | x8                | Multiplexed through 52-lane PCIe Gen 4 switch | C6 PCIe4 x16 LP/FHHL                                                                          |
| E2                    | PHB3              | x8                | Multiplexed through 52-lane PCIe Gen 4 switch | C7 PCIe4 x8 LP/FHHL                                                                           |
| E2                    | PHB3              | x8                | Multiplexed through 52-lane PCIe Gen 4 switch | C50 PCIe4 x8 with x16 connector internal slot: internal SAS adapter or NVMe pass-through card |
| E2                    | PHB4              | x8                | Direct                                        | C8 x8 CAPI 2.0 capable with x16 connector LP/FHHL                                             |

- a. The Power S922 server supports only low-profile (LP) adapters, and the Power S914 and Power S924 servers support only full-height half-length (FHHL) adapters.
- b. The PCIe host bridge PHB2 supports x2 lanes, but only one lane is needed to back the USB interface.
- c. Two USB ports are accessible from the front and two USB ports at the rear of a Power S922 server. Power S914 and Power S924 servers provide 1 USB port at the front and 2 USB ports at the rear.

The internal slots C49 and C50 can each accommodate #EJ1Q NVMe U.2 pass-through cards. One #EJ1Q card is automatically added to the system if feature #EJ1V storage backplane Gen 4 with two NVMe U.2 drive slots is configured. Two #EJ1Q cards are automatically added to the system if feature #EJ1W storage backplane Gen 4 with four NVMe U.2 drive slots are chosen. The #EJ1Q NVMe U.2 pass-through card splits the eight incoming lanes from the internal PCIe Gen 4 switch into two bundles of four lanes that are used to support one independent NVMe U.2 form factor drive per 4-lane bus.

The total aggregated PCIe Gen 4 I/O full duplex bandwidth that is available for a one-socket system adds up to 160 GBps, of which 96 GBps is directly provided to two external PCIe slots (C8 and C9) and 64 GBps is available through the six external PCIe slots (C5, C6, C7, C10, C11, and C12) that are attached to the two internal PCIe Gen 4 switches.

Table 2-21 shows the PCIe bus configuration for the second socket (SCM1) of Power S922 or Power S924 2-socket configurations.

Table 2-21   PCIe Gen 4 I/O configuration for POWER9 SCM1 in two-socket configurations

| PCIeGen4 controller   | PCIehost bridge   | Number of lanes   | Slot connection type   | Slot number and specification a        |
|-----------------------|-------------------|-------------------|------------------------|----------------------------------------|
| E0                    | PHB0              | x16               | Direct                 | C4 PCIe4 x16 CAPI 2.0 capable LP/FHHL  |
| E1                    | PHB1              | x8                | Direct                 | C2 PCIe4 x8 with x16 connector LP/FHHL |
| E2                    | PHB3              | x16               | Direct                 | C3 PCIe4 x16 CAPI 2.0 capable LP/FHHL  |

- a. The Power S922 server supports only LP adapters, and the Power S924 server supports only FHHL adapters.

The total aggregated PCIe Gen 4 I/O full duplex bandwidth that is available for a two-socket server adds up to 320 GBps, of which 256 GBps is directly provided to five external PCIe slots (C2, C3, C4, C8, and C9), and 64 GBps is available through the six external PCIe slots (C5, C6, C7, C10, C11, and C12) that are attached to the internal PCIe Gen 4 switches.

Table 2-22 provides a summary of the aggregated full duplex PCIe Gen 4 bandwidth that is available through the integrated internal and external PCIe adapter slots.

Table 2-22   PCIe Gen 4 full duplex bandwidth for Power S922, Power S914, and Power S924 servers

| PCIe Gen 4 full duplex bandwidth                                   | Power S922   | Power S914     | Power S924   |
|--------------------------------------------------------------------|--------------|----------------|--------------|
| One-socket system total                                            | 160 GBps     | 160 GBps       | 160 GBps     |
| Two-socket system total                                            | 320 GBps     | Not applicable | 320 GBps     |
| Aggregated over direct-attached slots of a one-socket system       | 96 GBps      | 96 GBps        | 96 GBps      |
| Aggregated over direct-attached slots of a two-socket system       | 256 GBps     | Not applicable | 256 GBps     |
| Aggregated over slots that are attached to the PCIe Gen 4 switches | 64 GBps      | 64 GBps        | 64 GBps      |

## 2.3.4  Service processor interface bus

Power S922, Power S914, and Power S924 servers are always delivered with one Flexible Service Processor (FSP) card in slot P1-C1 at the rear of the system. The FSP is required to accomplish system maintenance and virtualization configuration tasks. The processor service interface (PSI) bus that is implemented on POWER9 processor-based modules is used to connect each installed SCM to the FSP card.

## 2.4  Internal I/O subsystem

As described in 2.3, 'System buses' on page 93, each POWER9 SCM in a Power S922, Power S914, or Power S924 server integrates three PCIe Gen 4 controllers for a total of 42 lanes. Depending on the particular system configuration, the PCIe controllers connect to either eight PCIe slots (a one-socket system) or 11 PCIe slots (a two-socket system).

All PCIe slots are implemented in PCIe Gen 4 technology and support hot-plug adapter installation and maintenance and enhanced error handling (EEH). PCIe EEH-enabled adapters respond to a special data packet that is generated from the affected PCIe slot hardware by calling system firmware, which examines the affected bus, allows the device driver to reset it, and continues without a system restart.

PCIe slots that are directly connected to a POWER9 SCM show the best performance characteristics and should be used to install high-performance adapters. This recommendation is reflected and further elaborated by the I/O adapter enlarged capacity enablement order that is shown in Table 2-24 on page 97, Table 2-26 on page 98, and Table 2-28 on page 99, and the PCIe adapter placement documents for the Power S922 (9009-22G), Power S914 (9009-41G), and Power S924 (9009-42G) servers in IBM Knowledge Center.

The POWER9 SCMs that are are connected directly to the high-performance slots also support CAPI 2.0 adapters for the most demanding I/O channels. Per installed socket, two high-performance slots are CAPI 2.0 capable and for example, can be populated with 100 Gb InfiniBand Enhanced Data Rate (EDR) CAPI adapters (#EC62 and #EC63).

All PCIe Gen 4 adapter slots of the Power S922, Power S914, and Power S924 servers support hardware-backed network virtualization through single root IO virtualization (SR-IOV) technology.

## 2.4.1  Slot configuration

The various slot configurations are described in this section. For each server model, the PCIe slot locations are listed by the slot type and the CAPI capability, and the I/O adapter enlarged capacity enablement order is provided for each individual PCIe adapter slot. Illustrations help you find the PCIe slots locations at the rear of the servers.

## Slot configuration for the Power S922 server

The number of PCIe slots that are available with a Power S922 server depends on the number of installed processor modules. Table 2-23 provides an overview of the available PCIe slot types and the related slot location codes in Power S922 servers. The 2U height of a Power S922 server allows only for the installation of PCIe adapters in the half-height half-length (HHHL) LP form factor.

Table 2-23   PCIe slot locations for a slot type in the Power S922 server

| Slot type                        |   Numberof slots | Location codes                               |
|----------------------------------|------------------|----------------------------------------------|
| PCIe Gen 4 x8                    |                4 | P1-C5, P1-C7, P1-C10, and P1-C11             |
| PCIe Gen 4 x8 with x16 connector |                2 | P1-C2 a and P1-C8                            |
| PCIe Gen 4 x16                   |                5 | P1-C3 a , P1-C4 a , P1-C6, P1-C9, and P1-C12 |

- a. This slot is available when the second processor module is populated.

Table 2-24 lists the PCIe adapter slot locations and related characteristics for the Power S922 server.

Table 2-24   PCIe slot locations and capabilities for the Power S922 server

| Location code   | Description                                           | Parent device     | CAPI 2.0 capability   |   I/O adapter enlarged capacity enablement order a |
|-----------------|-------------------------------------------------------|-------------------|-----------------------|----------------------------------------------------|
| P1-C2 b         | PCIe Gen 4 x8 with x16 connector                      | Processor SCM1    | No                    |                                                  5 |
| P1-C3 b         | PCIe Gen 4 x16                                        | Processor SCM1    | Yes                   |                                                  2 |
| P1-C4 b         | PCIe Gen 4 x16                                        | Processor SCM1    | Yes                   |                                                  3 |
| P1-C5           | PCIe Gen 4 x8                                         | PCIe Gen 4 switch | No                    |                                                  8 |
| P1-C6           | PCIe Gen 4 x16                                        | PCIe Gen 4 switch | No                    |                                                  6 |
| P1-C7           | PCIe Gen 4 x8                                         | PCIe Gen 4 switch | No                    |                                                 10 |
| P1-C8 b         | PCIe Gen 4 x8 with x16 connector                      | Processor SCM0    | Yes                   |                                                  4 |
| P1-C9 b         | PCIe Gen 4 x16                                        | Processor SCM0    | Yes                   |                                                  1 |
| P1-C10          | PCIe Gen 4 x8                                         | PCIe Gen 4 switch | No                    |                                                  9 |
| P1-C11          | PCIe Gen 4 x8 (default local area network (LAN) slot) | PCIe Gen 4 switch | No                    |                                                 11 |
| P1-C12          | PCIe Gen 4 x16                                        | PCIe Gen 4 switch | No                    |                                                  7 |

- a. Enabling the I/O adapter enlarged capacity option affects only Linux partitions.
- b. A high-performance slot that is directly connected to the processor module.

Figure 2-12 shows the rear view of the Power S922 server with the location codes for the PCIe adapter slots. The PCIe slot C5 is populated with an optional USB 3.0 adapter in this illustration.

Note: The rear USB ports are optional and require feature EBK8. Feature EBK8 is a cable and ports with an internal connector for the rear port. It can be optioned when there is no PCI card in slot C5.

Figure 2-12   Rear view of a rack-mounted Power S922 server with PCIe slots location codes

<!-- image -->

## Slot configurations for Power S914 and Power S924 servers

The number of PCIe slots that are available with a Power S914 or Power S924 server depends on the number of installed processor modules. By design, Power S914 servers can

be delivered only with one socket, and Power S924 servers are available in one-socket or two-socket configurations.

The Power S914 tower configuration and the 4U height of a Power S914 or Power S924 rack server allow only for the installation of PCIe adapters with the FHHL form factor.

Table 2-25 provides an overview of the available PCIe slot types and the related slot location codes for Power S914 servers.

Table 2-25 PCIe slot locations for a slot type in a Power S914 server

| Slot type                        |   Numberof slots | Location codes                   |
|----------------------------------|------------------|----------------------------------|
| PCIe Gen 4 x8                    |                4 | P1-C5, P1-C7, P1-C10, and P1-C11 |
| PCIe Gen 4 x8 with x16 connector |                1 | P1-C8                            |
| PCIe Gen 4 x16                   |                3 | P1-C6, P1-C9, and P1-C12         |

Table 2-26 lists the PCIe adapter slot locations and related characteristics for the same type of server.

Table 2-26   PCIe slot locations and capabilities for a Power S914 server

| Location code   | Description                      | Parent device     | CAPI 2.0 capability   |   I/O adapter enlarged capacity enablement order a |
|-----------------|----------------------------------|-------------------|-----------------------|----------------------------------------------------|
| P1-C5           | PCIe Gen 4 x8                    | PCIe Gen 4 switch | No                    |                                                  5 |
| P1-C6           | PCIe Gen 4 x16                   | PCIe Gen 4 switch | No                    |                                                  3 |
| P1-C7           | PCIe Gen 4 x8                    | PCIe Gen 4 switch | No                    |                                                  7 |
| P1-C8           | PCIe Gen 4 x8 with x16 connector | Processor SCM0    | Yes                   |                                                  2 |
| P1-C9           | PCIe Gen 4 x16                   | Processor SCM0    | Yes                   |                                                  1 |
| P1-C10          | PCIe Gen 4 x8                    | PCIe Gen 4 switch | No                    |                                                  6 |
| P1-C11          | PCIe Gen 4 x8 (default LAN slot) | PCIe Gen 4 switch | No                    |                                                  8 |
| P1-C12          | PCIe Gen 4 x16                   | PCIe Gen 4 switch | No                    |                                                  4 |

- a. Enabling the I/O adapter enlarged capacity option affect only Linux partitions.

Table 2-27 provides an overview of the available PCIe slot types and the related slot location codes for Power S924 servers.

Table 2-27   PCIe slot locations for a slot type in Power S924 servers

| Slot type                        |   Numberof slots | Location codes                               |
|----------------------------------|------------------|----------------------------------------------|
| PCIe Gen 4 x8                    |                4 | P1-C5, P1-C7, P1-C10, and P1-C11             |
| PCIe Gen 4 x8 with x16 connector |                2 | P1-C2 a and P1-C8                            |
| PCIe Gen 4 x16                   |                5 | P1-C3 a , P1-C4 a , P1-C6, P1-C9, and P1-C12 |

- a. This slot is available when the second processor module is populated.

Table 2-28 lists the PCIe adapter slot locations and related characteristics for the same type of servers.

Table 2-28   PCIe slot locations and capabilities for the Power S924 server

| Location code   | Description                      | Parent device     | CAPI 2.0 capability   |   I/O adapter enlarged capacity enablement order a |
|-----------------|----------------------------------|-------------------|-----------------------|----------------------------------------------------|
| P1-C2 b         | PCIe Gen 4 x8 with x16 connector | Processor SCM1    | No                    |                                                  5 |
| P1-C3 b         | PCIe Gen 4 x16                   | Processor SCM1    | Yes                   |                                                  2 |
| P1-C4 b         | PCIe Gen 4 x16                   | Processor SCM1    | Yes                   |                                                  3 |
| P1-C5           | PCIe Gen 4 x8                    | PCIe Gen 4 switch | No                    |                                                  8 |
| P1-C6           | PCIe Gen 4 x16                   | PCIe Gen 4 switch | No                    |                                                  6 |
| P1-C7           | PCIe Gen 4 x8                    | PCIe Gen 4 switch | No                    |                                                 10 |
| P1-C8 b         | PCIe Gen 4 x8 with x16 connector | Processor SCM0    | Yes                   |                                                  4 |
| P1-C9 b         | PCIe Gen 4 x16                   | Processor SCM0    | Yes                   |                                                  1 |
| P1-C10          | PCIe Gen 4 x8                    | PCIe Gen 4 switch | No                    |                                                  9 |
| P1-C11          | PCIe Gen 4 x8 (default LAN slot) | PCIe Gen 4 switch | No                    |                                                 11 |
| P1-C12          | PCIe Gen 4 x16                   | PCIe Gen 4 switch | No                    |                                                  7 |

- a. Enabling the I/O adapter enlarged capacity option affects only Linux partitions.
- b. A high-performance slot that is directly connected to the processor module.

Figure 2-13 shows the rear view of the Power S924 server with the location codes for the PCIe adapter slots.

Figure 2-13   Rear view of a rack-mounted Power S924 server with the PCIe slots location codes

<!-- image -->

## 2.4.2 System ports

The system board has one serial port that is called a system port . The one system port is RJ45 and supported by AIX and Linux for attaching serial devices, such as an asynchronous device, for example, a console. If the device does not have a RJ45 connection, a converter cable such as #3930 can provide a 9-pin D-shell connection.

## 2.5  Peripheral Component Interconnect adapters

This section covers the various types and functions of the PCI adapters that are supported by the Power S922 (9009-22G), Power S914 (9009-41G), and Power S924 (9009-42G) servers.

Important: There is no Fibre Channel over Ethernet (FCoE) support on POWER9 processor-based servers.

## 2.5.1  Peripheral Component Interconnect Express

PCIe uses a serial interface and enables point-to-point interconnections between devices (by using a directly wired interface between these connection points). A single PCIe serial link is a dual-simplex connection that uses two pairs of wires (one pair for transmit and one pair for receive) that can transmit only 1 bit per cycle. These two pairs of wires are called a lane . A PCIe link can consist of multiple lanes. In such configurations, the connection is labeled as x1, x2, x8, x12, x16, or x32, where the number is effectively the number of lanes.

The PCIe interfaces that are supported on this server are PCIe Gen 4, which are capable of 32 GBps simplex (64 GBps duplex) on a single x16 interface. PCIe Gen 4 slots also support previous generations (Gen3, Gen2, and Gen1) adapters, which operate at lower speeds, according to the following rules:

- Place x1, x4, x8, and x16 speed adapters in the same size connector slots before mixing the adapter speed with the connector slot size.
- Adapters with smaller speeds are allowed in larger-sized PCIe connectors, but higher-speed adapters are not compatible in smaller connector sizes (that is, a x16 adapter cannot go into an x8 PCIe slot connector).

All adapters support EEH. PCIe adapters use a different type of slot than PCI adapters. If you attempt to force an adapter into the wrong type of slot, you might damage the adapter or the slot.

POWER9 processor-based servers can support two different form factors of PCIe adapters:

- PCIe LP cards, which are used with the Power S922 PCIe slots. These cards are not compatible with Power S914 and Power S924 servers because of their low height, but there are similar cards in other form factors.
- PCIe full-height and full-high cards are not compatible with the Power S922 server and are designed for the following servers:
- -Power S914 server
- -Power S924 server

Before adding or rearranging adapters, use the IBM System Planning Tool (SPT) to validate the new adapter configuration.

If you are installing a new feature, ensure that you have the software that is required to support the new feature and determine whether there are any existing update prerequisites to install by going to the IBM Power Systems Prerequisite website.

The following sections describe the supported adapters and provide tables of orderable feature numbers. The tables indicate OS support (AIX, IBM i, and Linux) for each of the adapters.

Note: The maximum number of adapters in each case might require the server to have an external I/O drawer.

## 2.5.2  LAN adapters

To connect the Power S922, Power S914, and Power S924 servers to a LAN, you can use the LAN adapters that are supported in the PCIe slots of the system unit.

Table 2-29 lists the LAN adapters that are available for the Power S922 (9009-22G) server.

Table 2-29   LAN adapters that are available for the Power S922 (9009-22G) server

| Feature code   | CCIN   | Description                                          |   Minimum |   Maximum | OS support            |
|----------------|--------|------------------------------------------------------|-----------|-----------|-----------------------|
| 5260           | 576F   | PCIe2 LP 4-port 1 GbE Adapter                        |         0 |         9 | AIX, IBM i, and Linux |
| 5899           | 576F   | PCIe2 4-port 1 GbE Adapter                           |         0 |        12 | AIX, IBM i, and Linux |
| EC2R           | 58FA   | PCIe3 LP 2-Port 10 Gb NIC&ROCE SR/Cu Adapter         |         0 |         8 | AIX, IBM i, and Linux |
| EC2S           | 58FA   | PCIe3 2-Port 10 Gb NIC&ROCE SR/Cu Adapter            |         0 |         4 | AIX, IBM i, and Linux |
| EC2T           | 58FB   | PCIe3 LP 2-Port 25/10 Gb NIC&ROCE SR/Cu Adapter      |         0 |         8 | AIX, IBM i, and Linux |
| EC2U           | 58FB   | PCIe3 2-Port 25/10 Gb NIC&ROCE SR/Cu Adapter         |         0 |         4 | AIX, IBM i, and Linux |
| EC67           | 2CF3   | PCIe4 LP 2-port 100 Gb ROCE EN LP adapter            |         0 |         3 | AIX, IBM i, and Linux |
| EN0H           | 2B93   | PCIe3 4-port (10 Gb FCoE & 1 GbE) SR&RJ45            |         0 |        12 | AIX, IBM i, and Linux |
| EN0J           | 2B93   | PCIe3 LP 4-port (10 Gb FCoE & 1 GbE) SR&RJ45         |         0 |         9 | AIX, IBM i, and Linux |
| EN0K           | 2CC1   | PCIe3 4-port (10 Gb FCoE & 1 GbE) SFP+Copper&RJ45    |         0 |        12 | AIX, IBM i, and Linux |
| EN0L           | 2CC1   | PCIe3 LP 4-port (10 Gb FCoE & 1 GbE) SFP+Copper&RJ45 |         0 |         9 | AIX, IBM i, and Linux |
| EN0S           | 2CC3   | PCIe2 4-Port (10 Gb+1 GbE) SR+RJ45 Adapter           |         0 |        12 | AIX, IBM i, and Linux |
| EN0T           | 2CC3   | PCIe2 LP 4-Port (10 Gb+1 GbE) SR+RJ45 Adapter        |         0 |         9 | AIX, IBM i, and Linux |
| EN0U           | 2CC3   | PCIe2 4-port (10 Gb+1 GbE) Copper SFP+RJ45 Adapter   |         0 |        12 | AIX, IBM i, and Linux |

| Feature code   | CCIN   | Description                                           |   Minimum |   Maximum | OS support            |
|----------------|--------|-------------------------------------------------------|-----------|-----------|-----------------------|
| EN0V           | 2CC3   | PCIe2 LP 4-port (10 Gb+1 GbE) Copper SFP+RJ45 Adapter |         0 |         9 | AIX, IBM i, and Linux |
| EN0W           | 2CC4   | PCIe2 2-port 10/1 GbE BaseT RJ45 Adapter              |         0 |        12 | AIX, IBM i, and Linux |
| EN0X           | 2CC4   | PCIe2 LP 2-port 10/1 GbE BaseT RJ45 Adapter           |         0 |         9 | AIX, IBM i, and Linux |
| EN15           | 2CE3   | PCIe3 4-port 10 GbE SR Adapter                        |         0 |        18 | AIX, IBM i, and Linux |

Table 2-30 lists the LAN adapters that are available for the Power S914 (9009-41G) server.

Table 2-30 LAN adapters that are available for Power S914 (9009-41G) server

| Feature code   | CCIN   | Description                                        |   Minimum |   Maximum | OS support            |
|----------------|--------|----------------------------------------------------|-----------|-----------|-----------------------|
| 5899           | 576F   | PCIe2 4-port 1 GbE Adapter                         |         0 |        13 | AIX, IBM i, and Linux |
| EC2S           | 58FA   | PCIe3 2-Port 10 Gb NIC&ROCE SR/Cu Adapter          |         0 |         8 | AIX, IBM i, and Linux |
| EC2U           | 58FB   | PCIe3 2-Port 25/10 Gb NIC&ROCE SR/Cu Adapter       |         0 |         8 | AIX, IBM i, and Linux |
| EC66           | 2CF3   | PCIe4 2-port 100 Gb ROCE EN adapter                |         0 |         1 | AIX, IBM i, and Linux |
| EN0H           | 2B93   | PCIe3 4-port (10 Gb FCoE & 1 GbE) SR&RJ45          |         0 |        12 | AIX, IBM i, and Linux |
| EN0K           | 2CC1   | PCIe3 4-port (10 Gb FCoE & 1 GbE) SFP+Copper&RJ45  |         0 |        12 | AIX, IBM i, and Linux |
| EN0S           | 2CC3   | PCIe2 4-Port (10 Gb+1 GbE) SR+RJ45 Adapter         |         0 |        12 | AIX, IBM i, and Linux |
| EN0U           | 2CC3   | PCIe2 4-port (10 Gb+1 GbE) Copper SFP+RJ45 Adapter |         0 |        12 | AIX, IBM i, and Linux |
| EN0W           | 2CC4   | PCIe2 2-port 10/1 GbE BaseT RJ45 Adapter           |         0 |        12 | AIX, IBM i, and Linux |
| EN15           | 2CE3   | PCIe3 4-port 10 GbE SR Adapter                     |         0 |        12 | AIX, IBM i, and Linux |

Table 2-31 lists the LAN adapters that are available for the Power S924 (9009-42G) server.

Table 2-31   LAN adapters that are available for the Power S924 (9009-42G) server

| Feature code   | CCIN   | Description                               |   Minimum |   Maximum | OS support            |
|----------------|--------|-------------------------------------------|-----------|-----------|-----------------------|
| 5899           | 576F   | PCIe2 4-port 1 GbE Adapter                |         0 |        26 | AIX, IBM i, and Linux |
| EC2S           | 58FA   | PCIe3 2-Port 10 Gb NIC&ROCE SR/Cu Adapter |         0 |        13 | AIX, IBM i, and Linux |

| Feature code   | CCIN   | Description                                        |   Minimum |   Maximum | OS support            |
|----------------|--------|----------------------------------------------------|-----------|-----------|-----------------------|
| EC2U           | 58FB   | PCIe3 2-Port 25/10 Gb NIC&ROCE SR/Cu Adapter       |         0 |        13 | AIX, IBM i, and Linux |
| EC66           | 2CF3   | PCIe4 2-port 100 Gb ROCE EN adapter                |         0 |         3 | AIX, IBM i, and Linux |
| EN0H           | 2B93   | PCIe3 4-port (10 Gb FCoE & 1 GbE) SR&RJ45          |         0 |        25 | AIX, IBM i, and Linux |
| EN0K           | 2CC1   | PCIe3 4-port (10 Gb FCoE & 1 GbE) SFP+Copper&RJ45  |         0 |        25 | AIX, IBM i, and Linux |
| EN0S           | 2CC3   | PCIe2 4-Port (10 Gb+1 GbE) SR+RJ45 Adapter         |         0 |        25 | AIX, IBM i, and Linux |
| EN0U           | 2CC3   | PCIe2 4-port (10 Gb+1 GbE) Copper SFP+RJ45 Adapter |         0 |        25 | AIX, IBM i, and Linux |
| EN0W           | 2CC4   | PCIe2 2-port 10/1 GbE BaseT RJ45 Adapter           |         0 |        25 | AIX, IBM i, and Linux |
| EN15           | 2CE3   | PCIe3 4-port 10 GbE SR Adapter                     |         0 |        25 | AIX, IBM i, and Linux |

## 2.5.3 Graphics accelerator adapters

An adapter can be configured to operate in either 8-bit or 24-bit color modes. The adapter supports both analog and digital monitors.

Table 2-32 lists the graphics accelerator adapter that is available for the Power S922 (9009-22G) server.

Table 2-32   The graphics accelerator adapter that is available for the Power S922 (9009-22G) server

|   Feature code |   CCIN | Description                               |   Minimum |   Maximum | OS support    |
|----------------|--------|-------------------------------------------|-----------|-----------|---------------|
|           5269 |   5269 | PCIe LP POWER GXT145 Graphics Accelerator |         0 |         6 | AIX and Linux |

Table 2-33 lists the graphics accelerator adapter that is available for the Power S914 (9009-41G) server.

Table 2-33   The graphics accelerator adapter that is available for the Power S914 (9009-41G) server

|   Feature code |   CCIN | Description                                   |   Minimum |   Maximum | OS support    |
|----------------|--------|-----------------------------------------------|-----------|-----------|---------------|
|           5748 |   5269 | POWER GXT145 PCI Express Graphics Accelerator |         0 |         4 | AIX and Linux |

Table 2-34 lists the graphics accelerator adapter that is available for the Power S924 (9009-42G) server.

Table 2-34   The graphics accelerator card that is available for the Power S924 (9009-42G) server

|   Feature code |   CCIN | Description                                   |   Minimum |   Maximum | OS support    |
|----------------|--------|-----------------------------------------------|-----------|-----------|---------------|
|           5748 |   5269 | POWER GXT145 PCI Express Graphics Accelerator |         0 |         7 | AIX and Linux |

## 2.5.4  SAS adapters

Table 2-35 lists the SAS adapters that are available for the Power S922 (9009-22G) server.

Table 2-35   SAS adapters that are available for the Power S922 (9009-22G) server

| Feature code   | CCIN   | Description                                               |   Minimum |   Maximum | OS support            |
|----------------|--------|-----------------------------------------------------------|-----------|-----------|-----------------------|
| EJ0J           | 57B4   | PCIe3 RAID SAS Adapter Quad-port 6 Gb x8                  |         0 |         8 | AIX, IBM i, and Linux |
| EJ0M           | 57B4   | PCIe3 LP RAID SAS Adapter Quad-Port 6 Gb x8               |         0 |         7 | AIX, IBM i, and Linux |
| EJ10           | 57B4   | PCIe3 SAS Tape/DVD Adapter Quad-port 6 Gb x8              |         0 |        12 | AIX, IBM i, and Linux |
| EJ11           | 57B4   | PCIe3LPSASTape/DVDAdapterQuad-port 6 Gb x8                |         0 |         7 | AIX, IBM i, and Linux |
| EJ14           | 57B1   | PCIe3 12 GB Cache RAID PLUS SAS Adapter Quad-port 6 Gb x8 |         0 |         8 | AIX, IBM i, and Linux |

Table 2-36 lists the SAS adapters that are available for the Power S914 (9009-41G) server.

Table 2-36   SAS adapters that are available for the Power S914 (9009-41G) server

| Feature code   | CCIN   | Description                                               |   Minimum |   Maximum | OS support            |
|----------------|--------|-----------------------------------------------------------|-----------|-----------|-----------------------|
| EJ0J           | 57B4   | PCIe3 RAID SAS Adapter Quad-port 6 Gb x8                  |         0 |        10 | AIX, IBM i, and Linux |
| EJ10           | 57B4   | PCIe3 SAS Tape/DVD Adapter Quad-port 6 Gb x8              |         0 |        10 | AIX, IBM i, and Linux |
| EJ14           | 57B1   | PCIe3 12 GB Cache RAID PLUS SAS Adapter Quad-port 6 Gb x8 |         0 |        10 | AIX, IBM i, and Linux |

Table 2-37 lists the SAS adapters that are available for the Power S924 (9009-42G) server.

Table 2-37   SAS adapters that are available for the Power S924 (9009-42G) server

| Feature code   | CCIN   | Description                                               |   Minimum |   Maximum | OS support            |
|----------------|--------|-----------------------------------------------------------|-----------|-----------|-----------------------|
| EJ0J           | 57B4   | PCIe3 RAID SAS Adapter Quad-port 6 Gb x8                  |         0 |        19 | AIX, IBM i, and Linux |
| EJ10           | 57B4   | PCIe3 SAS Tape/DVD Adapter Quad-port 6 Gb x8              |         0 |        19 | AIX, IBM i, and Linux |
| EJ14           | 57B1   | PCIe3 12 GB Cache RAID PLUS SAS Adapter Quad-port 6 Gb x8 |         0 |        19 | AIX, IBM i, and Linux |

## 2.5.5  Fibre Channel adapters

The servers support direct or SAN connections to devices that use Fibre Channel (FC) adapters.

Note: If you are attaching a device or switch with an SC type fiber connector, then an LC-SC 50-Micron Fiber Converter Cable (#2456) or an LC-SC 62.5-Micron Fiber Converter Cable (#2459) is required.

Table 2-39 on page 106 summarizes the FC adapters that are available for the Power S922 (9009-22G) server. They all have LC connectors.

Table 2-38   Fibre Channel adapters that are available for the Power S922 (9009-22G) server

| Feature code   | CCIN   | Description                                 |   Minimum |   Maximum | OS support            |
|----------------|--------|---------------------------------------------|-----------|-----------|-----------------------|
| EN0A           | 577F   | PCIe3 16 Gb 2-port Fibre Channel Adapter    |         0 |        12 | AIX, IBM i, and Linux |
| EN0B           | 577F   | PCIe3 LP 16 Gb 2-port Fibre Channel Adapter |         0 |         8 | AIX, IBM i, and Linux |
| EN1A           | 578F   | PCIe3 32 Gb 2-port Fibre Channel Adapter    |         0 |        12 | AIX, IBM i, and Linux |
| EN1B           | 578F   | PCIe3 LP 32 Gb 2-port Fibre Channel Adapter |         0 |         8 | AIX, IBM i, and Linux |
| EN1C           | 578E   | PCIe3 16 Gb 4-port Fibre Channel Adapter    |         0 |        12 | AIX, IBM i, and Linux |
| EN1D           | 578E   | PCIe3 LP 16 Gb 4-port Fibre Channel Adapter |         0 |         8 | AIX, IBM i, and Linux |

| Feature code   | CCIN   | Description                                 |   Minimum |   Maximum | OS support   |
|----------------|--------|---------------------------------------------|-----------|-----------|--------------|
| EN1G           | 579B   | PCIe3 2-Port 16 GbFibreChannel Adapter      |         0 |        12 | AIX          |
| EN1H           | 579B   | PCIe3 LP 2-Port 16 Gb Fibre Channel Adapter |         0 |         8 | AIX          |

Table 2-39 summarizes the FC adapters that are available for the Power S914 (9009-41G) server. They all have LC connectors.

Table 2-39   Fibre Channel adapters that are available for the Power S914 (9009-41G) server

| Feature code   | CCIN   | Description                              |   Min |   Max | OS support            |
|----------------|--------|------------------------------------------|-------|-------|-----------------------|
| EN0A           | 577F   | PCIe3 16 Gb 2-port Fibre Channel Adapter |     0 |    12 | AIX, IBM i, and Linux |
| EN1A           | 578F   | PCIe3 32 Gb 2-port Fibre Channel Adapter |     0 |    12 | AIX, IBM i, and Linux |
| EN1C           | 578E   | PCIe3 16 Gb 4-port Fibre Channel Adapter |     0 |    12 | AIX, IBM i, and Linux |
| EN1G           | 579B   | PCIe3 2-Port 16 Gb Fibre Channel Adapter |     0 |    12 | AIX                   |

Table 2-40 summarizes the FC adapters that are available for the Power S924 (9009-42G) server. They all have LC connectors.

Table 2-40   Fibre Channel adapters that are available for the Power S924 (9009-42G) server

| Feature code   | CCIN   | Description                              |   Min |   Max | OS support            |
|----------------|--------|------------------------------------------|-------|-------|-----------------------|
| EN0A           | 577F   | PCIe3 16 Gb 2-port Fibre Channel Adapter |     0 |    25 | AIX, IBM i, and Linux |
| EN1A           | 578F   | PCIe3 32 Gb 2-port Fibre Channel Adapter |     0 |    25 | AIX, IBM i, and Linux |
| EN1C           | 578E   | PCIe3 16 Gb 4-port Fibre Channel Adapter |     0 |    25 | AIX, IBM i, and Linux |
| EN1G           | 579B   | PCIe3 2-Port 16 Gb Fibre Channel Adapter |     0 |    25 | AIX                   |

Note: Using N\_Port ID Virtualization (NPIV) through the Virtual I/O Server (VIOS) requires an NPIV-capable FC adapter, such as the #EN0A.

## 2.5.6 InfiniBand host channel adapter

The InfiniBand Architecture (IBA) is an industry-standard architecture for server I/O and inter-server communication. It was developed by the InfiniBand Trade Association (IBTA) to provide the levels of reliability, availability, performance, and scalability that are necessary for present and future server systems with levels better than can be achieved by using bus-oriented I/O structures.

InfiniBand is an open set of interconnect standards and specifications. The main InfiniBand specification is published by the IBTA and is available at the IBTA website.

InfiniBand is based on a switched fabric architecture of serial point-to-point links, where these InfiniBand links can be connected to either host channel adapters (HCAs), which are used primarily in servers, or target channel adapters (TCAs), which are used primarily in storage subsystems.

The InfiniBand physical connection consists of multiple byte lanes. Each individual byte lane is a four-wire, 2.5, 5.0, or 10.0 Gbps bidirectional connection. Combinations of link width and byte lane speed allow for overall link speeds of 2.5 - 120 Gbps. The architecture defines a layered hardware protocol and also a software layer to manage initialization and the communication between devices. Each link can support multiple transport services for reliability and multiple prioritized virtual communication channels.

For more information about InfiniBand, see HPC Clusters Using InfiniBand on IBM Power Systems Servers , SG24-7767.

A connection to supported InfiniBand switches is accomplished by using the QDR optical cables (#3290 and #3293).

Table 2-41 lists the InfiniBand adapters that are available for the Power S922 (9009-22G) server.

Table 2-41   InfiniBand adapters that are available for the Power S922 (9009-22G) server

| Feature code   | CCIN   | Description                                        |   Minimum |   Maximum | OS support            |
|----------------|--------|----------------------------------------------------|-----------|-----------|-----------------------|
| EC62           | 2CF1   | PCIe4 LP 1-port 100 Gb EDR InfiniBand CAPI adapter |         0 |         3 | AIX, IBM i, and Linux |
| EC64           | 2CF2   | PCIe4 LP 2-port 100 Gb EDR InfiniBand CAPI adapter |         0 |         3 | AIX, IBM i, and Linux |

Table 2-42 lists the InfiniBand adapter that is available for the Power S914 (9009-41G) server.

Table 2-42   InfiniBand adapter that is available for the Power S914 (9009-41G) server

| Feature code   | CCIN   | Description                                     |   Minimum |   Maximum | OS support            |
|----------------|--------|-------------------------------------------------|-----------|-----------|-----------------------|
| EC63           | 2CF1   | PCIe4 1-port 100 Gb EDR InfiniBand CAPI adapter |         0 |         1 | AIX, IBM i, and Linux |

Table 2-43 lists the InfiniBand adapter that is available for the Power S924 (9009-42G) server.

Table 2-43   IInfiniBand adapter that is available for the Power S924 (9009-42G) server

| Feature code   | CCIN   | Description                                     |   Minimum |   Maximum | OS support            |
|----------------|--------|-------------------------------------------------|-----------|-----------|-----------------------|
| EC63           | 2CF1   | PCIe4 1-port 100 Gb EDR InfiniBand CAPI adapter |         0 |         3 | AIX, IBM i, and Linux |

## 2.5.7  Cryptographic coprocessor

Table 2-44 lists the cryptographic coprocessor card that is available for the Power S922 (9009-22G) server.

Table 2-44   The cryptographic coprocessor that is available for the Power S922 (9009-22G) server

| Feature code   |   CCIN | Description                            |   Minimum |   Maximum | OS support            |
|----------------|--------|----------------------------------------|-----------|-----------|-----------------------|
| EJ33           |   4767 | PCIe3 Crypto Coprocessor BSC-Gen3 4767 |         0 |        12 | AIX, IBM i, and Linux |

Table 2-45 lists the cryptographic coprocessor cards that are available for the Power S914 (9009-41G) server.

Table 2-45   Cryptographic coprocessors that are available for the Power S914 (9009-41G) server

| Feature code   |   CCIN | Description                            |   Minimum |   Maximum | OS support            |
|----------------|--------|----------------------------------------|-----------|-----------|-----------------------|
| EJ32           |   4767 | PCIe3 Crypto Coprocessor no BSC 4767   |         0 |         7 | AIX, IBM i, and Linux |
| EJ33           |   4767 | PCIe3 Crypto Coprocessor BSC-Gen3 4767 |         0 |         6 | AIX, IBM i, and Linux |

Table 2-46 lists the cryptographic coprocessor cards that are available for the Power S924 (9009-42G) server.

Table 2-46   Cryptographic coprocessors that are available for the Power S924 (9009-42G) server

| Feature code   |   CCIN | Description                            |   Minimum |   Maximum | OS support            |
|----------------|--------|----------------------------------------|-----------|-----------|-----------------------|
| EJ32           |   4767 | PCIe3 Crypto Coprocessor no BSC 4767   |         0 |        10 | AIX, IBM i, and Linux |
| EJ33           |   4767 | PCIe3 Crypto Coprocessor BSC-Gen3 4767 |         0 |        18 | AIX, IBM i, and Linux |

## 2.5.8 Coherent Accelerator Processor Interface adapters

Table 2-47 lists the CAPI-capable adapters that are available for the Power S922 (9009-22G) server.

Table 2-47   CAPI-capable adapters that are available for the Power S922 (9009-22G) server

| Feature code   | CCIN   | Description                                        |   Minimum |   Maximum | OS support            |
|----------------|--------|----------------------------------------------------|-----------|-----------|-----------------------|
| EC62           | 2CF1   | PCIe4 LP 1-port 100 Gb EDR InfiniBand CAPI adapter |         0 |         3 | AIX, IBM i, and Linux |
| EC64           | 2CF2   | PCIe4 LP 2-port 100 Gb EDR InfiniBand CAPI adapter |         0 |         3 | AIX, IBM i, and Linux |

Table 2-48 lists the CAPI-capable adapter that is available for the Power S914 (9009-41G) server.

Table 2-48   CAPI-capable adapter that is available for the Power S914 (9009-41G) server

| Feature code   | CCIN   | Description                                     |   Minimum |   Maximum | OS support            |
|----------------|--------|-------------------------------------------------|-----------|-----------|-----------------------|
| EC63           | 2CF1   | PCIe4 1-port 100 Gb EDR InfiniBand CAPI adapter |         0 |         1 | AIX, IBM i, and Linux |

Table 2-49 lists the CAPI-capable adapter that is available for the Power S924 (9009-42G) server.

Table 2-49   CAPI-capable adapter that is available for the Power S924 (9009-42G) server

| Feature code   | CCIN   | Description                                     |   Minimum |   Maximum | OS support            |
|----------------|--------|-------------------------------------------------|-----------|-----------|-----------------------|
| EC63           | 2CF1   | PCIe4 1-port 100 Gb EDR InfiniBand CAPI adapter |         0 |         3 | AIX, IBM i, and Linux |

## 2.5.9  USB adapters

Table 2-50 lists the USB adapters that are available for the Power S922 (9009-22G) server.

Table 2-50   USB adapters that are available for the Power S922 (9009-22G) server

| Feature code   | CCIN   | Description                     |   Minimum |   Maximum | OS support            |
|----------------|--------|---------------------------------|-----------|-----------|-----------------------|
| EC45           | 58F9   | PCIe2 LP 4-Port USB 3.0 Adapter |         0 |         8 | AIX, IBM i, and Linux |
| EC46           | 58F9   | PCIe2 4-Port USB 3.0 Adapter    |         0 |        12 | AIX, IBM i, and Linux |

It is also possible to add a set of rear USB 3.0 ports using feature code EBK8.

Table 2-51 lists the USB adapter that is available for the Power S914 (9009-41G) server.

Table 2-51   USB adapter that is available for the Power S914 (9009-41G) server

| Feature code   | CCIN   | Description                  |   Minimum |   Maximum | OS support            |
|----------------|--------|------------------------------|-----------|-----------|-----------------------|
| EC46           | 58F9   | PCIe2 4-Port USB 3.0 Adapter |         0 |        12 | AIX, IBM i, and Linux |

Table 2-52 lists the USB adapter that is available for the Power S924 (9009-42G) server.

Table 2-52   USB adapter that is available for the Power S924 (9009-42G) server

| Feature code   | CCIN   | Description                  |   Minimum |   Maximum | OS support            |
|----------------|--------|------------------------------|-----------|-----------|-----------------------|
| EC46           | 58F9   | PCIe2 4-Port USB 3.0 Adapter |         0 |        25 | AIX, IBM i, and Linux |

## 2.5.10  Async adapter

Table 2-53 lists the Async adapter that is available for the Power S922, S914, and S924 server.

Table 2-53   ASYNC adapter that is available for the Power S922 (9009-22G) server

|   Feature code | CCIN   | Description                |   Minimum |   Maximum | OS support            |
|----------------|--------|----------------------------|-----------|-----------|-----------------------|
|           5785 |        | Async EIA-232 PCIe Adapter |         0 |         3 | AIX, IBM i, and Linux |

Table 2-53 lists the Async adapter that is available for the Power S924, S914, and S922 server.

Table 2-54   ASYNC adapter that is available for the Power S914 (9009-41G) server

|   Feature code | CCIN   | Description                |   Minimum |   Maximum | OS support            |
|----------------|--------|----------------------------|-----------|-----------|-----------------------|
|           5785 |        | Async EIA-232 PCIe Adapter |         0 |         4 | AIX, IBM i, and Linux |

Table 2-53 lists the Async adapter that is available for the Power S924, S914, and S922 server.

Table 2-55   ASYNC adapter that is available for the Power S924 (9009-42G) servef

|   Feature code | CCIN   | Description                |   Minimum |   Maximum | OS support            |
|----------------|--------|----------------------------|-----------|-----------|-----------------------|
|           5785 |        | Async EIA-232 PCIe Adapter |         0 |         7 | AIX, IBM i, and Linux |

## 2.6  Internal storage

The internal storage on the Power S922, Power S914, and Power S924 servers depends on the DASD/Media backplane that is used. The servers support various DASD/Media backplanes.

Power S922 (9009-22G) servers support the following backplanes:

#EJ1F

Eight SFF-3 Bays with optional split card (#EJ1H)

#EJ1G

Expanded function Storage Backplane 8 SFF-3 Bays/Single IOA with write cache

#EJ1V

Storage Backplane Gen 4 with two NVMe U.2 drive slots

#EJ1W

Storage Backplane Gen 4 with four NVMe U.2 drive slots

Note: If the new backplanes #EJ1V or #EJ1W are ordered, a minimum of one #ES1E, #ES1G, #EC5V, #EC5X (NVMe U.2 drive) must be ordered.

- Maximum of two #ES1E, #ES1G, #EC5V, #EC5X per one #EJ1V.
- Maximum of four #ES1E, #ES1G, #EC5V, #EC5X per one #EJ1W.
- Mixing of #ES1E, #ES1G, #EC5V, #EC5X is allowed on a backplane.

Power S914 (9009-41G) and Power S924 (9009-42G) servers support the following backplanes:

#EJ1C

Twelve SFF-3 Bays with an optional split card (#EJ1E)

#EJ1D

Eighteen SFF-3 Bays/Dual IOA with Write Cache

#EJ1M

Twelve SFF-3 Bays/RDX Bays with write cache and optional external SAS port

#EJ1S

Storage Backplane Gen 4 with six SFF-3 Bays and two NVMe U.2 drive slots

#EJ1T

Storage Backplane Gen 4 with two NVMe U.2 drive slots

#EJ1U

Storage Backplane Gen 4 with four NVMe U.2 drive slots

IBM i OS performance: Clients with write-sensitive disk / hard disk drive (HDD) workloads should upgrade from the base storage backplane (#EJ1C / #EJ1E) to the expanded function storage backplanes (#EJ1M / #EJ1D) to gain the performance advantage of write cache.

## 2.6.1 9009-41G and 9009-42G Backplane (#EJ1C)

This feature code is the base storage backplane with an integrated SAS controller for SAS bays in the system unit. SAS bays are 2.5-inch or small form factor (SFF) and use drives that are mounted on a carrier / tray that is specific to the system unit (SFF-3).

The high-performance SAS controller provides RAID 0, RAID 5, RAID 6, or RAID 10 support for either HDDs or solid-state drives (SSDs). JBOD support for HDD is also supported. The controller has no write cache.

For servers that support split backplane capability, add #EJ1E. For write cache performance, use #EJ1D or #EJ1M instead of this backplane.

Both 5xx and 4-KB sector HDDs / SSDs are supported. 5xx and 4-KB drives cannot be mixed in the same array.

This feature code provides a storage backplane with one integrated SAS adapter with no cache, running 12 SFF-3 SAS bays in the system unit and one RDX bay in the system unit.

## Supported OSs are:

- Red Hat Enterprise Linux
- SUSE Linux Enterprise Server
- Ubuntu Server
- AIX
- IBM i

The internal connections to the physical disks are shown in Figure 2-14.

Figure 2-14 #EJ1C connections

<!-- image -->

## 2.6.2 9009-41G and 9009-42G Split Backplane option for #EJ1C

The #EJ1E option modifies the base storage backplane cabling and adds a second, high-performance SAS controller. The existing 12 SFF-3 SAS bays are cabled to be split into two sets of six bays, each with one SAS controller. Both SAS controllers are in integrated slots and do not use a PCIe slot.

The high-performance SAS controllers each provides RAID 0, RAID 5, RAID 6, or RAID 10 support. JBOD support for HDDs is also supported. There is no write cache on either controller.

Both 5xx and 4-KB sector HDDs / SSDs are supported. 5xx and 4-KB drives cannot be mixed in the same array.

This feature code provides a second integrated SAS adapter with no cache and internal cables to provide two sets of six SFF-3 bays in the system unit.

You must have an #EJ1C backplane to use this feature code.

## Supported OSs:

- Red Hat Enterprise Linux
- SUSE Linux Enterprise Server
- Ubuntu Server
- AIX
- IBM i

The internal connections to the physical disks are shown in Figure 2-15.

Figure 2-15   #EJ1E connections

<!-- image -->

## 2.6.3  9009-41G and 9009-42G Backplane (#EJ1D)

This feature code is an expanded function storage backplane with dual integrated SAS controllers with write cache and an optional external SAS port. High-performance controllers run SFF-3 SAS bays in the system unit. Dual controllers (also called dual I/O adapters or paired controllers) and their write cache are placed in integrated slots and do not use PCIe slots. The write cache augments the controller's high performance for workloads with writes, especially for HDDs. A 1.8-GB physical write cache is used with compression to provide up to 7.2-GB cache capacity. The write cache contents are protected against power loss by using flash memory and super capacitors, which removes the need for battery maintenance.

The high-performance SAS controllers provide RAID 0, RAID 5, RAID 6, RAID 10, RAID 5T2, RAID 6T2, or RAID 10T2 support. Patented active/active configurations with at least two arrays are supported.

The Easy Tier function is supported so that the dual controllers can automatically move hot data to attached SSDs and cold data to attached HDDs for AIX and Linux, and VIOS environments.

SFF or 2.5-inch drives are mounted on a carrier / tray that is specific to the system unit (SFF-3). The backplane has 18 SFF-3 bays.

This backplane enables two SAS ports (#EJ0W) at the rear of the system unit to support the attachment of one EXP24S/EXP24SX I/O drawer in mode1 to hold HDDs or SSDs.

#EJ0W is an optional feature with #EJ1M. One x8 PCIe slot is used by #EJ0W.

This backplane does not support a split backplane. For a split backplane, use #EJ1C plus #EJ1E.

Both 5xx and 4-KB sector HDDs / SSDs are supported. 5xx and 4-KB drives cannot be mixed in the same array.

This feature code provides a storage backplane with a pair of integrated SAS adapters with write cache, with an optional external SAS port running up to:

- A set of 18 SFF-3 SAS bays in the system unit
- Two SAS ports at the rear of the system unit to connect to a single EXP24S/EXP24SX I/O drawer

## Supported OSs:

- Red Hat Enterprise Linux
- SUSE Linux Enterprise Server
- Ubuntu Server
- AIX
- IBM i

## 2.6.4  9009-41G and 9009-42G Expanded Function Backplane (#EJ1M)

This feature code is an expanded function storage backplane with dual integrated SAS controllers with write cache and an optional external SAS port. High-performance controllers run SFF-3 SAS bays and an RDX bay in the system unit. Dual controllers (also called dual I/O adapters or paired controllers) and their write cache are placed in integrated slots and do not use PCIe slots.

A write cache augments the controller's high performance for workloads with writes, especially for HDDs. A 1.8-GB physical write cache is used with compression to provide up to 7.2-GB cache capacity. The write cache contents are protected against power loss by using flash memory and super capacitors, which removes the need for battery maintenance.

The high-performance SAS controllers provide RAID 0, RAID 5, RAID 6, RAID 10, RAID 5T2, RAID 6T2, or RAID 10T2 support. Patented active/active configurations with at least two arrays are supported.

The Easy Tier function is supported so that the dual controllers can automatically move hot data to attached SSDs and cold data to attached HDDs for AIX and Linux, and VIOS environments.

SFF or 2.5-inch drives are mounted on a carrier / tray that is specific to the system unit (SFF-3). The backplane has 12 SFF-3 bays.

This backplane also enables two SAS ports (#EJ0W) at the rear of the system unit, which support the attachment of one EXP24S/EXP24SX I/O drawer in mode1, which holds HDDs or SSDs.

#EJ0W is an optional feature with #EJ1M, and one 8 PCIe slot is used by #EJ0W.

This backplane does not support a split backplane. For a split backplane, use the #EJ1C with #EJ1E backplane features.

Both 5xx and 4-KB sector HDDs / SSDs are supported. 5xx and 4-KB drives cannot be mixed in the same array.

This feature code provides an expanded function storage backplane with a pair of integrated SAS adapters with a write cache, and an optional external SAS port running up to:

- A set of 12 SFF-3 SAS bays in the system unit
- One RDX bay in the system unit
- Two SAS ports at the rear of the system unit to connect to a single EXP24S/EXP24SX I/O drawer

## Supported OSs:

- Red Hat Enterprise Linux
- SUSE Linux Enterprise Server
- Ubuntu Server
- AIX
- IBM i

## 2.6.5  9009-41G and 9009-42G Gen 4 Backplane (#EJ1S)

This Gen 4 backplane option provides six SFF-3 SAS bays and two NVMe slots in the system unit. These 2.5-inch or SFF SAS bays can contain SAS drives (HDDs or SSDs) that are mounted on a Gen3 tray or carrier. Thus, the drives are designated SFF-3. SFF-1 or SFF-2 drives do not fit in an SFF-3 bay. All SFF-3 bays support concurrent maintenance or hot-plug capability.

This backplane option can offer different drive protection options: RAID 0, RAID 5, RAID 6, or RAID 10. RAID 5 requires a minimum of three drives of the same capacity. RAID 6 requires a minimum of four drives of the same capacity. RAID 10 requires a minimum of two drives. Hot-spare capability is supported by RAID 5, RAID 6, or RAID 10.

RAID 5 and RAID 6 result in more drive write activity than mirroring or unprotected drives.

This backplane option is supported by AIX and Linux, and VIOS. As a best practice, the drives should be protected.

The NVMe option offers fast start times and is ideally suited to housing the rootvg of VIOS partitions. This backplane provides two U.2 module slots.

Table 2-56 shows the NVMe options when using the #EJ1S Backplane with AIX or Linux.

Table 2-56   Available NVMe Flash Adapters for the #EJ1S Backplane for AIX or Linux

| Feature code   | CCIN   | Description                                      |   Minimum |   Maximum |
|----------------|--------|--------------------------------------------------|-----------|-----------|
| EC5B           | 58FC   | PCIe3 x8 1.6 TB NVMe Flash Adapter for AIX/Linux |         0 |         2 |
| EC5D           | 58FD   | PCIe3 x8 3.2 TB NVMe Flash Adapter for AIX/Linux |         0 |         2 |

| Feature code   | CCIN   | Description                                      |   Minimum |   Maximum |
|----------------|--------|--------------------------------------------------|-----------|-----------|
| EC5F           | 58FE   | PCIe3 x8 6.4 TB NVMe Flash Adapter for AIX/Linux |         0 |         2 |

Table 2-57 shows the NVMe options when using #EJ1S Backplane with IBM i.

Table 2-57   Available NVMe Flash Adapters for the #EJ1S Backplane for IBM i

| Feature code   | CCIN   | Description                                  |   Minimum |   Maximum |
|----------------|--------|----------------------------------------------|-----------|-----------|
| EC6V           | 58FC   | PCIe3 x8 1.6 TB NVMe Flash Adapter for IBM i |         0 |         2 |
| EC6X           | 58FD   | PCIe3 x8 3.2 TB NVMe Flash Adapter for IBM i |         0 |         2 |
| EC6Z           | 58FE   | PCIe3 x8 6.4 TB NVMe Flash Adapter for IBM i |         0 |         2 |

## Supported OSs:

- SUSE Linux Enterprise Server 12 Service Pack 3 or later
- SUSE Linux Enterprise Server for SAP with SUSE Linux Enterprise Server 12 Service Pack 3 or later
- Red Hat Enterprise Linux
- Ubuntu Server
- AIX

Each NVMe device is a separate PCIe endpoint, which means that each NVMe device can be assigned to a different logical partition (LPAR) or VIOS. At the OS level, each device appears to the OS as an individual disk. For example, in AIX, the device might appear as hdisk0.

## 2.6.6  9009-22G Backplane (#EJ1F)

The backplane option provides SFF-3 SAS bays in the system unit. These 2.5-inch or SFF SAS bays can contain SAS drives (HDDs or SSDs) that are mounted on a Gen3 tray or carrier. Thus, the drives are designated SFF-3. SFF-1 or SFF-2 drives do not fit in an SFF-3 bay. All SFF-3 bays support concurrent maintenance or hot-plug capability.

This backplane option uses leading-edge, integrated SAS RAID controller technology that is designed and patented by IBM. A custom-designed PowerPC based ASIC chip is the basis of these SAS RAID controllers, and provides RAID 0, RAID 5, RAID 6, and RAID 10 functions with HDDs and SSDs. Internally, SAS ports are implemented and provide plentiful bandwidth. The integrated SAS controllers are placed in dedicated slots and do not reduce the number of available PCIe slots.

The Storage Backplane option (#EJ1F) provides eight SFF-3 bays and one SAS controller with zero write cache.

Optionally, by adding the Split Backplane (#EJ1H), a second integrated SAS controller with no write cache is provided, and the eight SSF-3 bays are logically divided into two sets of four bays. Each SAS controller independently runs one of the four-bay sets of drives.

This backplane option supports HDDs or SSDs or a mixture of HDDs and SSDs in the SFF-3 bays. Mixing HDDs and SSDs applies even within a single set of four bays of the split backplane option. If you are mixing HDDs and SSDs, they must be in separate arrays (unless you use the Easy Tier function).

This backplane option can offer different drive protection options: RAID 0, RAID 5, RAID 6, or RAID 10. RAID 5 requires a minimum of three drives of the same capacity. RAID 6 requires a minimum of four drives of the same capacity. RAID 10 requires a minimum of two drives. Hot-spare capability is supported by RAID 5, RAID 6, or RAID 10.

RAID 5 and RAID 6 result in more drive write activity than mirroring or unprotected drives.

his backplane option is supported by AIX, IBM i, Linux, and VIOS. As a preferred practice, the drives should be protected.

Note: IBM i requires VIOS for the 8-, 10-, 0r 11-core processors (#EP58, #EP59, #EP5B. IBM i is supported without the VIOS on the 1-core #EPSY S922.

## 2.6.7 9009-22G Expanded Function Storage Backplane (#EJ1G)

In addition to supporting HDDs and SSDs in the SFF-3 SAS bays, the Expanded Function Storage Backplane (#EJ1G) supports the optional attachment of an EXP12SX Expansion Drawer or EXP24SX Expansion Drawer. All bays are accessed by both of the integrated SAS controllers. The bays support concurrent maintenance (hot-plug).

## 2.6.8  NVMe support

This section provides information about the available NVMe adapters and backplanes.

## NVMe adapters

Table 2-58 provides a list of NVMe cards that are available for the Power S922 (9009-22G) server.

Table 2-58   NVMe adapters that are available for the Power S922 (9009-22G) server

| Feature code   | CCIN   | Description                      |   Minimum |   Maximum | OS support            |
|----------------|--------|----------------------------------|-----------|-----------|-----------------------|
| EC5G           | 58FC   | PCIe3 LP 1.6 TB SSD NVMe Adapter |         0 |        10 | AIX, IBM i, and Linux |
| EC5C           | 58FD   | PCIe3 LP 3.2 TB SSD NVMe adapter |         0 |        10 | AIX, IBM i, and Linux |
| EC5E           | 58FE   | PCIe3 LP 6.4 TB SSD NVMe adapter |         0 |        10 | AIX, IBM i, and Linux |

Table 2-59 provides a list of NVMe cards that are available for the Power S914 (9009-41G) server.

Table 2-59   NVMe adapters that are available for the Power S914 (9009-41G) server

| Feature code   | CCIN   | Description                                  |   Minimum |   Maximum | OS support            |
|----------------|--------|----------------------------------------------|-----------|-----------|-----------------------|
| EC5B           | 58FC   | PCIe3 LP 1.6 TB SSD NVMe Adapter             |         0 |         7 | AIX, IBM i, and Linux |
| EC5D           | 58FD   | PCIe3 LP 3.2 TB SSD NVMe adapter             |         0 |         7 | AIX, IBM i, and Linux |
| EC5F           | 58FE   | PCIe3 LP 6.4 TB SSD NVMe adapter             |         0 |         7 | AIX, IBM i, and Linux |
| EC6V           | 58FC   | PCIe3 x8 1.6 TB NVMe Flash Adapter for IBM i |         0 |         7 | IBM i                 |
| EC6X           | 58FD   | PCIe3 x8 3.2 TB NVMe Flash Adapter for IBM i |         0 |         7 | IBM i                 |
| EC6Z           | 58FE   | PCIe3 x8 6.4 TB NVMe Flash Adapter for IBM i |         0 |         7 | IBM i                 |

Table 2-60 provides a list of NVMe cards that are available for the Power S924 (9009-42G) server.

Table 2-60   NVMe adapters that are available for the Power S924 (9009-42G) server

| Feature code   | CCIN   | Description                                  |   Minimum |   Maximum | OS support            |
|----------------|--------|----------------------------------------------|-----------|-----------|-----------------------|
| EC5B           | 58FC   | PCIe3 LP 1.6 TB SSD NVMe Adapter             |         0 |        10 | AIX, IBM i, and Linux |
| EC5D           | 58FD   | PCIe3 LP 3.2 TB SSD NVMe Adapter             |         0 |        10 | AIX, IBM i, and Linux |
| EC5F           | 58FE   | PCIe3 LP 6.4 TB SSD NVMe Adapter             |         0 |        10 | AIX, IBM i, and Linux |
| EC6V           | 58FC   | PCIe3 x8 1.6 TB NVMe Flash Adapter for IBM i |         0 |        10 | IBM i                 |
| EC6X           | 58FD   | PCIe3 x8 3.2 TB NVMe Flash Adapter for IBM i |         0 |        10 | IBM i                 |
| EC6Z           | 58FE   | PCIe3 x8 6.4 TB NVMe Flash Adapter for IBM i |         0 |        10 | IBM i                 |

## NVMe Backplanes

There are new backplane options if you need only a few NVMe Flash adapters, for example, to boot a VIOS.

The following options are available for the 9009-22G:

- #EJ1V: Storage Backplane Gen 4 with 2 NVMe U.2 drive slots
- #EJ1W: Storage Backplane Gen 4 with 4 NVMe U.2 drive slots

The following options are available for the 9009-41G and 9009-42G:

- #EJ1T: Storage Backplane Gen 4 with 2 NVMe U.2 drive slots
- #EJ1U: Storage Backplane Gen 4 with 4 NVMe U.2 drive slots

## Minimum NVMe configurations

Table 2-61 provides the minimum configurations for NVMe adapters by operating system.

Table 2-61   NVMe minimum configuration

| Operating system   | Minimum configuration           |   Quantity |
|--------------------|---------------------------------|------------|
| AIX, VIOS, Linux   | #EC5X Mainstream 800 GB U2 NVMe |          1 |
| IBM i              | #ES1E 1.6 TB 4K NVMe            |          2 |

## 2.6.9  RAID support

There are multiple protection options for HDDs / SSDs in the Power S922, Power S914, and Power S924 servers, whether they are contained in the SAS SFF bays in the system unit or are drives in disk-only I/O drawers. Although protecting drives is always preferred, AIX and Linux users can choose to leave a few or all drives unprotected at their own risk, and IBM supports these configurations.

## Drive protection

HDD / SSD protection can be provided by AIX, IBM i, and Linux, or by the HDD / SSD hardware controllers.

Apart from NVMe backplane options, all of the storage backplanes with SAS bays offer RAID. The default storage backplanes contain one SAS HDD / SSD controller and support JBOD and RAID 0, 5, 6, and 10 for AIX or Linux. A secondary non-redundant controller is added when you use the split backplane option, so each of the six disk bays has a separated disk controller.

When you choose the optional #EJ1D or #EJ1M storage backplane, the controller is replaced by a pair of high-performance RAID controllers with dual integrated SAS controllers with 1.8 GB of physical write cache. High-performance controllers run 18 SFF-3 SAS bays with 1.8-inch SSD bays. Dual controllers (also called dual I/O adapters or paired controllers) and their write cache are placed in integrated slots and do not use PCIe slots. Patented active/active configurations with at least two arrays are supported.

The write cache, which is responsible for increasing write performance by caching data before it is written to the physical disks, can have its data compression capabilities activated, which provides up to 7.2 GB effective cache capacity. The write cache contents are protected against power loss by flash memory and super capacitors, which removes the need for battery maintenance.

The high-performance SAS controllers provide RAID 0, RAID 5, RAID 6, and RAID 10 support, and the Easy Tier variants (RAID 5T2, RAID 6T2, and RAID 10T2) if the server has both HDDs and SSDs installed.

The Easy Tier function is supported, so the dual controllers can automatically move hot data to an attached SSD and cold data to an attached HDD for AIX and Linux, and VIOS environments. To learn more about Easy Tier, see 2.6.10, 'Easy Tier' on page 122.

AIX and Linux can use disk drives that are formatted with 512-byte blocks when they are mirrored by the OS. These disk drives must be reformatted to 528-byte sectors when used in RAID arrays. Although a small percentage of the drive's capacity is lost, extra data protection, such as error-correcting code (ECC) and bad block detection, is gained in this reformatting. For example, a 300 GB disk drive, when reformatted, provides approximately 283 GB. IBM i always uses drives that are formatted to 528 bytes. SSDs are always formatted with 528-byte sectors.

## Supported RAID functions

The base hardware supports RAID 0, 5, 6, and 10. When more features are configured, the server supports hardware RAID 0, 5, 6, 10, 5T2, 6T2, and 10T2:

- RAID 0 provides striping for performance, but does not offer any fault tolerance.
- The failure of a single drive results in the loss of all data on the array. This version of RAID increases I/O bandwidth by simultaneously accessing multiple data paths.
- RAID 5 uses block-level data striping with distributed parity.
- RAID 5 stripes both data and parity information across three or more drives. Fault tolerance is maintained by ensuring that the parity information for any block of data is placed on a drive that is separate from the ones that are used to store the data itself. This version of RAID provides data resiliency if a single drive fails in a RAID 5 array.
- RAID 6 uses block-level data striping with dual distributed parity.
- RAID 6 is the same as RAID 5 except that it uses a second level of independently calculated and distributed parity information for more fault tolerance. A RAID 6 configuration requires N+2 drives to accommodate the additional parity data, making it less cost-effective than RAID 5 for equivalent storage capacity. This version of RAID provides data resiliency if one or two drives fail in a RAID 6 array. When you work with large capacity disks, RAID 6 enables you to sustain data parity during the rebuild process.
- RAID 10 is a striped set of mirrored arrays.
- It is a combination of RAID 0 and RAID 1. A RAID 0 stripe set of the data is created across a two-disk array for performance benefits. A duplicate of the first stripe set is then mirrored on another two-disk array for fault tolerance. This version of RAID provides data resiliency if a single drive fails, and it can provide resiliency for multiple drive failures.

RAID 5T2, RAID 6T2, and RAID 10T2 are RAID levels with Easy Tier enabled. They require that both types of disks exist on the system under the same controller (HDDs and SSDs), and that both types are configured under the same RAID type.

## 2.6.10  Easy Tier

With a standard backplane (#EJ1C or #EJ1F), the server can handle both HDDs and SSDs that are attached to its storage backplane if they are on separate arrays.

The high-function backplane (#EJ1D) can handle both types of storage in two different ways:

- Separate arrays: SSDs and HDDs coexist on separate arrays, just like the Standard SAS adapter can.
- Easy Tier: SSDs and HDDs coexist under the same array.

When the SDDs and HDDS are under the same array, the adapter can automatically move the most accessed data to faster storage (SSDs) and less accessed data to slower storage (HDDs). This situation is called Easy Tier .

There is no need for coding or software intervention after the RAID is configured correctly. Statistics on block accesses are gathered every minute, and after the adapter realizes that some portion of the data is being frequently requested, it moves this data to faster devices. The data is moved in chunks of 1 MB or 2 MB called bands .

From the OS point-of-view, there is just a regular array disk. From the SAS controller point-of-view, there are two arrays with parts of the data being serviced by one tier of disks and parts by another tier of disks.

Figure 2-16 shows an Easy Tier array.

Figure 2-16   Easy Tier array

<!-- image -->

The Easy Tier configuration is accomplished through a standard OS SAS adapter configuration utility. Figure 2-17 and Figure 2-18 show two examples of tiered array creation for AIX.

Figure 2-17   Array type selection panel on AIX RAID Manager

<!-- image -->

Figure 2-18   Tiered arrays (RAID 5T2, RAID 6T2, and RAID 10T2) example on AIX RAID Manager

<!-- image -->

To support Easy Tier, make sure that the server is running at least the following minimum levels:

- VIOS 2.2.3.3 with interim fix IV56366 or later
- AIX 7.1 TL3 SP3 or later
- Red Hat Enterprise Linux 6.5 or later
- SUSE Linux Enterprise Server 11 SP3 or later

IBM i supports Easy Tier only through VIOS.

## 2.6.11  External SAS ports

The Power S914 and Power S924 DASD backplanes (#EJ1D and #EJ1M) offer a connection to an external SAS port.

Power S914 and Power S924 servers that use the high-performance RAID feature support two external SAS ports. The external SAS ports are used for expansion to an external SAS drawer.

More drawers and the IBM System Storage 7226 Tape and DVD Enclosure Express (Model 1U3) can be attached by installing more SAS adapters.

Note: Only one SAS drawer is supported from the external SAS port. More SAS drawers can be supported through SAS adapters.

## 2.6.12  Media drawers

IBM multimedia drawers, such as the 7226-1U3 or 7214-1U2, or tape units, such as the TS2240, TS2340, TS3100, TS3200, and TS3310, can be connected by using external SAS ports.

## 2.6.13  External DVD drives

There is a trend to use good quality USB flash drives rather than DVD drives. Being mechanical, DVD drives are less reliable than solid-state technology.

If you feel that you do need a DVD drive, IBM offers a stand-alone external USB unit (#EUA5), which is shown in Figure 2-19.

Figure 2-19   Stand-alone USB DVD drive with cable (#EUA5)

<!-- image -->

Note: If you use an external or stand-alone USB drive, which does not have its own power supply, you should use a USB socket at the front of the system to ensure enough current is available.

## 2.6.14  RDX removable disk drives

These Power Systems servers support RDX removable disk drives, which are commonly used for quick backups.

If #EJ1C or #EJ1M is configured, an internal bay is available and can be populated by #EU00.

There is also an external / stand-alone RDX unit (#EUA4).

Various disk drives are available, as shown in Table 2-62.

Table 2-62   RDX disk drives

| Feature code   | Part number   | Description                 |
|----------------|---------------|-----------------------------|
| #1107          | 46C5379       | 500 GB Removable Disk Drive |
| #EU01          | 46C2335       | 1 TB Removable Disk Drive   |
| #EU2T          | 46C2975       | 2 TB Removable Disk Drive   |

## 2.7  External IO subsystems

This section describes the PCIe Gen3 I/O expansion drawer that can be attached to the Power S922, Power S914, and Power S924 servers.

## 2.7.1  Peripheral Component Interconnect Express Gen3 I/O expansion drawer

The PCIe Gen3 I/O expansion (EMX0) drawer is a 4U high, PCI Gen3-based, and rack-mountable I/O drawer. It offers two PCIe fan-out modules (#EMXF or #EMXG). The PCIe fan-out module provides six PCIe Gen3 full-high full-length slots (two x16 and four x8). The PCIe slots are hot-pluggable.

The PCIe fan-out module has two CXP ports, which are connected to two CXP ports on a PCIe Optical Cable Adapter (#EJ05, #EJ07, or #EJ08, depending on the server that is selected). A pair of active optical CXP cables (AOCs) or a pair of CXP copper cables are used for this connection.

Concurrent repair and add/removal of PCIe adapters is done by Hardware Management Console (HMC) guided menus or by OS support utilities.

A blind swap cassette (BSC) is used to house the full-high adapters that go into these slots. The BSC is the same BSC that is used with the previous generation server's #5802/5803/5877/5873 12X attached I/O drawers.

Figure 2-20 shows the back view of the PCIe Gen3 I/O expansion drawer.

Figure 2-20   Rear view of the PCIe Gen3 I/O expansion drawer

<!-- image -->

## 2.7.2 PCIe Gen3 I/O expansion drawer optical cabling

I/O drawers are connected to the adapters in the system node through data transfer cables:

- 3M Optical Cable Pair for PCIe3 Expansion Drawer (#ECC7)
- 10M Optical Cable Pair for PCIe3 Expansion Drawer (#ECC8)
- 3M Copper CXP Cable Pair for PCIe3 Expansion Drawer (#ECCS)

Cable lengths: Use the 3.0 m cables for intra-rack installations. Use the 10.0 m cables for inter-rack installations.

Limitation: You cannot mix copper and optical cables on the same PCIe Gen3 I/O drawer. Both fan-out modules use copper cables or both use optical cables.

A minimum of one PCIe3 Optical Cable Adapter for PCIe3 Expansion Drawer is required to connect to the PCIe3 6-slot fan-out module in the I/O expansion drawer. The fan-out module has two CXP ports. The top CXP port of the fan-out module is cabled to the top CXP port of the PCIe3 Optical Cable Adapter. The bottom CXP port of the fan-out module is cabled to the bottom CXP port of the same PCIe3 Optical Cable Adapter.

To set up the cabling correctly, complete the following steps:

1. Connect an optical cable or copper CXP cable to connector T1 on the PCIe3 optical cable adapter in your server.
2. Connect the other end of the optical cable or copper CXP cable to connector T1 on one of the PCIe3 6-slot fan-out modules in your expansion drawer.
3. Connect another cable to connector T2 on the PCIe3 optical cable adapter in your server.
4. Connect the other end of the cable to connector T2 on the PCIe3 6-slot fan-out module in your expansion drawer.
5. Repeat steps 1 - 4 for the other PCIe3 6-slot fan-out module in the expansion drawer, if required.

Drawer connections: Each fan-out module in a PCIe3 Expansion Drawer can be connected only to a single PCIe3 Optical Cable Adapter for PCIe3 Expansion Drawer.

Figure 2-21 shows the connector locations for the PCIe Gen3 I/O Expansion Drawer.

Figure 2-21   Connector locations for the PCIe Gen3 I/O expansion drawer

<!-- image -->

Figure 2-22 shows the typical optical cable connections.

Figure 2-22   Typical optical cable connections

<!-- image -->

## General rules for the PCI Gen3 I/O expansion drawer configuration

The PCIe3 Optical Cable Adapter for PCIe3 Expansion Drawer (#EJ05) is supported in slots P1-C4 and P1-C9 for the Power S922 server. This feature code is a double-wide adapter that requires two adjacent slots. If #EJ05 is installed in this slot, the external SAS port is not allowed in the system.

The PCIe3 cable adapter for the PCIe3 EMX0 expansion drawer (#EJ08) is supported in P1-C9 for the Power S914 and Power S924 single processor servers. It is supported in P1-C9, P1-C3, and P1-C4 in the Power S924 double processor servers.

Table 2-63 shows PCIe adapter slot priorities and maximum adapters that are supported in the Power S922, Power S914, and Power S924 servers.

Table 2-63   PCIe adapter slot priorities and maximum adapters that are supported

| Server                   | Feature code   | Slot priorities   |   Maximum number of adapters supported |
|--------------------------|----------------|-------------------|----------------------------------------|
| Power S922 (1 processor) | #EJ05          | 9                 |                                      1 |
| Power S922 (2 processor) | #EJ05          | 9/10, 3/4         |                                      2 |
| Power S914               | #EJ08          | 9                 |                                      1 |
| Power S924 (1 processor) | #EJ08          | 9                 |                                      1 |
| Power S924 (2 processor) | #EJ08          | 9, 3, and 4       |                                      3 |

## 2.7.3  PCIe Gen3 I/O expansion drawer system power control network cabling

There is no system power control network (SPCN) that is used to control and monitor the status of power and cooling within the I/O drawer. SPCN capabilities are integrated into the optical cables.

## 2.8  External disk subsystems

This section describes the following external disk subsystems that can be attached to the Power S922, Power S914, and Power S924 servers:

- EXP12SX SAS Storage Enclosure (#ESLL) and EXP24SX SAS Storage Enclosure (#ESLS)
- IBM Storage

## 2.8.1 EXP12SX SAS Storage Enclosure and EXP24SX SAS Storage Enclosure

The EXP24SX SAS Storage Enclosure is a storage expansion enclosure with twenty-four 2.5-inch SFF SAS bays. It supports up to 24 hot-swap HDDs or SSDs in only 2 EIA of space in a 19-inch rack. The EXP24SX SAS Storage Enclosure SFF bays use SFF Gen2 (SFF-2) carriers / trays that are identical to the carrier / trays in the previous EXP24S drawer. With AIX and Linux, or VIOS, the EXP24SX SAS Storage Enclosure can be ordered with four sets of six bays (mode 4), two sets of 12 bays (mode 2), or one set of 24 bays (mode 1). With IBM i, one set of 24 bays (mode 1) is supported.

There can be no mixing of HDDs and SSDs in the same mode 1 drawer. HDDs and SSDs can be mixed in a mode 2 or mode 4 drawer, but they cannot be mixed within a logical split of the drawer. For example, in a mode 2 drawer with two sets of 12 bays, one set can hold SSDs and one set can hold HDDs, but you cannot mix SSDs and HDDs in the same set of 12 bays.

The EXP12SX SAS Storage Enclosure is a storage expansion enclosure with twelve 3.5-inch large form factor (LFF) SAS bays. It supports up to 12 hot-swap HDDs in only 2 EIA of space in a 19-inch rack. The EXP12SX SAS Storage Enclosure SFF bays use LFF Gen1 (LFF-1) carriers / trays. Only 4-KB sector (4096 or 4224) sector drives are supported. With AIX and Linux, and VIOS, the EXP12SX SAS Storage Enclosure can be ordered with four sets of three bays (mode 4), two sets of six bays (mode 2), or one set of 12 bays (mode 1).

Four mini-SAS HD ports on the EXP12SX SAS Storage Enclosure and EXP24SX SAS Storage Enclosure or are attached to PCIe Gen3 SAS adapters or attached to an integrated SAS controller in the Power S922, Power S914, or Power S924 servers.

The following PCIe3 SAS adapters support the EXP12SX SAS Storage Enclosure and EXP24SX SAS Storage Enclosure:

- PCIe3 RAID SAS Adapter Quad-port 6 Gb x8 (#EJ0J, #EJ0M, #EL3B, or #EL59)
- PCIe3 12 GB Cache RAID Plus SAS Adapter Quad-port 6 Gb x8 (#EJ14)

Earlier generation PCIe2 or PCIe1 SAS adapters are not supported by the EXP24SX SAS Storage Enclosure.

The attachment between the EXP12SX SAS Storage Enclosure or EXP24SX SAS Storage Enclosure and the PCIe3 SAS adapters or integrated SAS controllers is through SAS YO12 or X12 cables. All ends of the YO12 and X12 cables have mini-SAS HD narrow connectors. The cable options are:

- X12 cable: 3-meter copper (#ECDJ)
- YO12 cables: 1.5-meter copper (#ECDT) or 3-meter copper (#ECDU)
- 3M 100 GbE Optical Cable QSFP28 (AOC) (#EB5R)
- 5M 100 GbE Optical Cable QSFP28 (AOC) (#EB5S)
- 10M 100 GbE Optical Cable QSFP28 (AOC) (#EB5T)
- 15M 100 GbE Optical Cable QSFP28 (AOC) (#EB5U)
- 20M 100 GbE Optical Cable QSFP28 (AOC) (#EB5V)
- 30M 100 GbE Optical Cable QSFP28 (AOC) (#EB5W)
- 50M 100 GbE Optical Cable QSFP28 (AOC) (#EB5X)
- 100M 100 GbE Optical Cable QSFP28 (AOC) (#EB5Y)

There are six SAS connectors at the rear of the EXP12SX SAS Storage Enclosure and EXP24SX SAS Storage Enclosure to which SAS adapters or controllers are attached. They are labeled T1, T2, and T3; there are two T1, two T2, and two T3 connectors.

- In mode 1, two or four of the six ports are used. Two T2 ports are used for a single SAS adapter, and two T2 and two T3 ports are used with a paired set of two adapters or a dual adapters configuration.
- In mode 2 or mode 4, four ports are used, two T2 ports and two T3 ports, to access all SAS bays.

Figure 2-23 shows connector locations for the EXP12SX SAS Storage Enclosure and EXP24SX Storage Enclosure.

Figure 2-23 Connector locations for the EXP12SX SAS Storage Enclosure and EXP24SX Storage Enclosure

<!-- image -->

For more information about SAS cabling, see the 'Connecting an ESLL or ESLS storage enclosure to your system' topic in IBM Knowledge Center.

The EXP12SX SAS Expansion Drawer and EXP24SX Expansion Drawer have many high-reliability design points:

- SAS bays that support hot-swap.
- Redundant and hot-plug power and fan assemblies.
- Dual power cords.
- Redundant and hot-plug IBM Enclosure Services Manager (ESM).
- Redundant data paths to all drives.
- LED indicators on drives, bays, ESM, and power supplies that support problem identification.
- Through the SAS adapters / controllers, drives that can be protected with RAID and mirroring and hot-spare capability.

## 2.8.2 IBM Storage

IBM Storage Systems products and offerings provide compelling storage solutions with superior value for all levels of business, from entry-level to high-end storage systems. For more information about the various offerings, see Data Storage Solutions.

The following sections highlight a few of the offerings.

## IBM Flash Storage

The next generation of IBM Flash Storage delivers the performance and efficiency that you need to succeed with a new pay-as-you-go option to reduce your costs and scale-on-demand. For more information, see Flash Storage and All Flash Arrays.

## IBM DS8880 Hybrid Storage

IBM DS8880 Hybrid Storage is a family of storage systems that includes the IBM DS8886 storage system for high-performance functions in a dense, expandable package, and the IBM DS8884 storage system to provide advanced functions for consolidated systems or multiple platforms in a space-saving design. IBM DS8880 storage systems combine resiliency and intelligent flash performance to deliver microsecond application response times and more than six-nines availability. For more information, see IBM DS8880 hybrid storage - Overview.

## IBM FlashSystem 7200

IBM FlashSystem® 7200 is an enterprise-class storage solution that offers the advantages of IBM Spectrum® Virtualize software. It can help you lower capital and operational storage costs with heterogeneous data services while optimizing performance with flash storage. IBM FlashSystem 7200 enables you to take advantage of hybrid cloud technology without replacing your current storage. For more information, see IBM FlashSystem 7200 - Overview.

## IBM FlashSystem 5000

IBM FlashSystem 5000 is a flexible storage solution that offers extraordinary scalability from the smallest to the largest system without disruption. Built with IBM Spectrum Virtualize software, it can help you lower capital and operational storage costs with heterogeneous data services. IBM FlashSystem 5000 is an easily customizable and upgradeable solution for better investment protection, improved performance, and enhanced efficiency. For more information, see

- IBM FlashSystem 5000 - Overview.

## 2.9  Operating system support

The Power S922, Power S914, and Power S924 servers support the following OSs:

- AIX
- IBM i
- Linux

In addition, on the particular configurations the Virtual I/O Server can be installed in special partitions that provide support to client partitions running AIX, IBM i, or Linux for using features such as virtualized I/O devices, PowerVM Live Partition Mobility (LPM), or PowerVM Active Memory Sharing.

## 2.9.2  IBM i

For more information about the software that is available on Power Systems, see IBM Power Systems Software.

## 2.9.1  AIX operating system

This section describes the various levels of AIX OS support.

IBM periodically releases maintenance packages (service packs or technology levels) for the AIX OS. For more information about these packages, downloading, and obtaining the installation media, see Fix Central.

The Fix Central website also provides information about how to obtain the fixes that are included on installation media.

The Service Update Management Assistant (SUMA), which can help you automate the task of checking and downloading OS downloads, is part of the base OS. For more information about the suma command, see IBM Knowledge Center.

The following minimum levels of AIX support the Power S922, Power S914, and Power S924 servers:

- If you are installing the AIX OS LPAR with any I/O configuration:
- -AIX Version 7.1 with the 7100-05 Technology Level and Service Pack 7100-05-06-2028, or later
- -AIX Version 7.2 with the 7200-03 Technology Level and Service Pack 7 (planned availability February 19, 2021)
- -AIX Version 7.2 with the 7200-04 Technology Level and Service Pack 7200-04-02-2028, or later
- If you are installing the AIX OS Virtual I/O only LPAR:
- -AIX Version 7.2 with the 7200-04 Technology Level, or later
- -AIX Version 7.2 with the 7200-03 Technology Level, or later
- -AIX Version 7.2 with the 7200-02 Technology Level and Service Pack 7200-02-02-1832, or later
- -AIX Version 7.1 with the 7100-05 Technology Level and Service Pack 7100-05-02-1832, or later

IBM i is supported on the Power S922, Power S914, and Power S924 servers with the following minimum required levels:

- IBM i 7.4 TR2
- IBM i 7.3 TR8
- IBM i 7.2 with 7.2 Licensed Machine Code - RS 720-Q, or later

Note: The Power S922 server requires the VIOS to run IBM i in the 8-,10-, or 11-core processor configuration (#EP58, #EP59, #EP5B).

The Power S922 server in 1-core processor configuration (#EP5Y) VIOS is not supported, and IBM i runs natively.

IBM periodically releases maintenance packages (service packs or technology levels) for the IBM i OS. For more information about these packages, downloading, and obtaining the installation media, see IBM Fix Central.

For compatibility information about hardware features and the corresponding AIX and IBM i Technology Levels, see IBM Prerequisites.

## 2.9.3  Linux operating system

Linux is an open source, cross-platform OS that runs on numerous platforms from embedded systems to mainframe computers. It provides an UNIX -like implementation across many computer architectures.

The supported versions of Linux on the Power S922, Power S914, and Power S924 servers are as follows:

- If you are installing the Linux OS LPAR:
- -Red Hat Enterprise Linux 8 for Power LE Version 8.1.
- -SUSE Linux Enterprise Server 15 Service Pack 1 or later.
- If you are installing the Linux OSs LPAR in non-production SAP implementations:
- -SUSE Linux Enterprise Server for SAP with SUSE Linux Enterprise 15 Service Pack 1, or later.
- -Red Hat Enterprise Linux for SAP with Red Hat Enterprise Linux 8 for Power LE version 8.1, or later. Linux supports almost all of the Power Systems I/O, and the configurator verifies support on order.

## Service and productivity tools

Service and productivity tools are available in a YUM repository that you can use to download and then install all the recommended packages for your Red Hat, SUSE Linux, or Fedora distribution. The packages are available from Service and productivity tools for Linux on Power servers.

To learn about developing on the IBM Power Architecture®, find packages, get access to cloud resources, and discover tools and technologies, see Linux on IBM Power Systems Developer Portal.

The IBM Advance Toolchain for Linux on Power is a set of open source compilers, runtime libraries, and development tools that users can use to take leading-edge advantage of IBM POWER hardware features on Linux. For more information, see Advanced Toolchain for Linux on Power.

For more information about SUSE Linux Enterprise Server, see SUSE Linux Enterprise Server.

For more information about Red Hat Enterprise Linux, see Red Hat Enterprise Linux.

## 2.9.4  Virtual I/O Server

The minimum required level of VIOS for the Power S922, Power S914, and Power S924 servers is:

- VIOS 2.2.6.65, or later.
- VIOS 3.1.1.25, or later.

IBM regularly updates the VIOS code. For more information about the latest updates, see Fix Central.

## 2.10  Power Systems reliability, availability, and serviceability capabilities

This section provides information about Power Systems reliability, availability, and serviceability (RAS) design and features.

The elements of RAS can be described as follows:

Reliability

Indicates how infrequently a defect or fault in a server occurs.

Availability

Indicates how infrequently the functioning of a system or application is impacted by a fault or defect.

Serviceability

Indicates how well faults and their effects are communicated to system managers and how efficiently and nondisruptively the faults are repaired.

Table 2-64 provides a list of the Power Systems RAS capabilities by OS. The HMC is an optional feature on scale-out Power Systems servers.

Table 2-64   Selected reliability, availability, and serviceability features by operating system

| RAS feature                                                           | AIX   | IBM i          | Linux          |
|-----------------------------------------------------------------------|-------|----------------|----------------|
| Processor                                                             |       |                |                |
| First Failure Data Capture (FFDC) for fault detection/error isolation | X     | X              | X              |
| Dynamic Processor Deallocation                                        | X     | X              | X              |
| I/O subsystem                                                         |       |                |                |
| PCIe bus enhanced error detection                                     | X     | X              | X              |
| PCIe bus enhanced error recovery                                      | X     | X              | X              |
| PCIe card hot-swap                                                    | X     | X              | X              |
| Memory availability                                                   |       |                |                |
| Memory Page Deallocation                                              | X     | X              | X              |
| Special Uncorrectable Error Handling                                  | X     | X              | X              |
| Fault detection and isolation                                         |       |                |                |
| Storage Protection Keys                                               | X     | Not used by OS | Not used by OS |
| Error log analysis                                                    | X     | X              | X              |
| Serviceability                                                        |       |                |                |
| Boot-time progress indicators                                         | X     | X              | X              |
| Firmware error codes                                                  | X     | X              | X              |
| OS error codes                                                        | X     | X              | X              |
| Inventory collection                                                  | X     | X              | X              |

| RAS feature                                                                        | AIX   | IBM i   | Linux   |
|------------------------------------------------------------------------------------|-------|---------|---------|
| Environmental and power warnings                                                   | X     | X       | X       |
| Hot-swap DASD / media                                                              | X     | X       | X       |
| Dual disk controllers / Split backplane                                            | X     | X       | X       |
| EED collection                                                                     | X     | X       | X       |
| SP/OS 'Call Home' on non-HMC configurations                                        | X     | X       | X       |
| IO adapter/device stand-alone diagnostic tests with PowerVM                        | X     | X       | X       |
| SP mutual surveillance with IBM POWER Hypervisor                                   | X     | X       | X       |
| Dynamic firmware update with HMC                                                   | X     | X       | X       |
| Service Agent Call Home Application                                                | X     | X       | X       |
| Service Indicator LED support                                                      | X     | X       | X       |
| System dump for memory, POWER Hypervisor, and SP                                   | X     | X       | X       |
| IBM Knowledge Center / IBM Systems Support Site service publications               | X     | X       | X       |
| System Service / Support Education                                                 | X     | X       | X       |
| OS error reporting to HMC Service Focal Point (SFP) application                    | X     | X       | X       |
| RMC secure error transmission subsystem                                            | X     | X       | X       |
| Healthcheck scheduled operations with HMC                                          | X     | X       | X       |
| Operator panel (real or virtual [HMC])                                             | X     | X       | X       |
| Concurrent Op Panel Display Maintenance                                            | X     | X       | X       |
| Redundant HMCs                                                                     | X     | X       | X       |
| High availability (HA) clustering support                                          | X     | X       | X       |
| Repair and Verify Guided Maintenance with HMC                                      | X     | X       | X       |
| PowerVM Live Partition / Live Application Mobility With PowerVM Enterprise Edition | X     | X       | X       |
| Early Power Off Warning (EPOW)                                                     |       |         |         |
| EPOW errors handling                                                               | X     | X       | X       |

## 2.11  Manageability

Several functions and tools help with manageability so that you can efficiently and effectively manage your system.

## 2.11.1  Service user interfaces

The service user interface enables support personnel or the client to communicate with the service support applications in a server by using a console, interface, or terminal. Delivering a clear, concise view of available service applications, the service interface enables the support team to manage system resources and service information in an efficient and effective way.

Applications that are available through the service interface are carefully configured and placed to give service providers access to important service functions.

Various service interfaces are used, depending on the state of the system and its operating environment. Here are the primary service interfaces:

- Light Path, which provides indicator lights to help a service technical find a component in need of service.
- Service processor.
- Advanced System Management Interface (ASMI).
- Operator panel.
- An OS service menu, which obtains error codes directly from the hardware.
- SFP on the HMC.

## Service processor

The service processor is a controller that is running its own OS. It is a component of the service interface card.

The service processor OS has specific programs and device drivers for the service processor hardware. The host interface is a processor support interface that is connected to the POWER processor. The service processor is always working regardless of the main system unit's state. The system unit can be in the following states:

- Standby (power off)
- Operating, ready to start partitions
- Operating with running LPARs

The service processor is used to monitor and manage the system hardware resources and devices. The service processor checks the system for errors, ensures that the connection to the management console for manageability purposes is functioning, and accepts ASMI Secure Sockets Layer (SSL) network connections. The service processor can view and manage the machine-wide settings by using the ASMI, which enables complete system and partition management from the HMC.

Analyzing a system that does not start: The FSP can analyze a system that does not start. Reference codes and detailed data are available in the ASMI and are transferred to the HMC.

The service processor uses two Ethernet ports that run at 1-Gbps speed. Consider the following information:

- Both Ethernet ports are visible only to the service processor and can be used to attach the server to an HMC or to access the ASMI. The ASMI options can be accessed through an HTTP server that is integrated into the service processor operating environment.
- Both Ethernet ports support only auto-negotiation. Customer-selectable media speed and duplex settings are not available.
- Both Ethernet ports have a default IP address, as follows:
- -Service processor eth0 (HMC1 port) is configured as 169.254.2.147.
- -Service processor eth1 (HMC2 port) is configured as 169.254.3.147.
- -DHCP by using the HMC for the HMC management networks is also possible.

The following functions are available through the service processor:

- Call Home
- ASMI
- Error information (error code, part number, and location codes) menu
- View of guarded components
- Limited repair procedures
- Generate dump
- LED Management menu
- Remote view of ASMI menus
- Firmware update through a USB key

## Advanced System Management Interface

ASMI is the interface to the service processor that enables you to manage the operation of the server, such as auto-power restart, and to view information about the server, such as the error log and Vital Product Data (VPD). Various repair procedures require connection to the ASMI.

The ASMI is accessible through the management console. It is also accessible by using a web browser on a system that is connected directly to the service processor (in this case, either a standard Ethernet cable or a crossed cable) or through an Ethernet network. ASMI can also be accessed from an ASCII terminal, but it is available only while the system is in the platform powered-off mode.

Figure 2-24 shows a method of opening ASMI on a particular server by using the HMC GUI.

Figure 2-24   Starting the Advanced System Management Interface through the HMC GUI

<!-- image -->

You are prompted for confirmation about which FSP to use, and then a login window opens, as shown in Figure 2-25.

Figure 2-25   The ASMI login window

<!-- image -->

After you are logged in (the default credentials are admin/admin), you see the menu that is shown in Figure 2-26.

Figure 2-26   An ASMI window

<!-- image -->

Tip: If you click Expand all menus , as shown in the red ring, you can then use the search function (Ctrl+f) in your browser to find quickly menu items.

Use the ASMI to change the service processor IP addresses or to apply certain security policies and prevent access from unwanted IP addresses or ranges.

You might be able to use the service processor's default settings. In that case, accessing the ASMI is not necessary. To access ASMI, use one of the following methods:

- Use a management console.

If configured to do so, the management console connects directly to the ASMI for a selected system from this task.

To connect to the ASMI from a management console, complete the following steps:

- a. Open Systems Management from the navigation pane.
- b. From the work window, select one of the managed systems.
- c. From the System Management tasks list, click Operations → Launch Advanced System Management (ASMI) .

- Use a web browser.

At the time of writing, the supported web browsers are Microsoft Internet Explorer (Version 10.0.9200.16439), Mozilla Firefox ESR (Version 24), and Chrome (Version 30). Later versions of these browsers might work, but are not officially supported. The JavaScript language and cookies must be enabled, and TLS 1.2 might need to be enabled.

The web interface is available during all phases of system operation, including the initial program load (IPL) and run time. However, several of the menu options in the web interface are unavailable during IPL or run time to prevent usage or ownership conflicts if the system resources are in use during that phase. The ASMI provides an SSL web connection to the service processor. To establish an SSL connection, open your browser and go to the following address:

https:// &lt;ip\_address\_of\_service\_processor&gt;

Note: To make the connection through Internet Explorer, click Tools Internet Options . Clear the Use TLS 1.0 check box, and click OK .

- Use an ASCII terminal.

The ASMI on an ASCII terminal supports a subset of the functions that are provided by the web interface. The ASMI is available only when the system is in the platform powered-off mode. The ASMI on an ASCII console is not available during several phases of system operation, such as the IPL and run time.

- Command-line start of the ASMI

Either on the HMC itself or when properly configured on a remote system, it is possible to start the ASMI web interface from the HMC command line. Open a terminal window on the HMC or access the HMC with a terminal emulation and run the following command:

asmmenu --ip &lt;ip address&gt;

On the HMC itself, a browser window opens automatically with the ASMI window, and when configured properly, a browser window opens on a remote system when issued from there.

## The operator panel

The service processor provides an interface to the operator panel, which is used to display system status and diagnostic information.

The operator panel has two parts: One is always installed, and the second can be optional.

The part that is always installed provides LEDs and sensors:

- Power LED:
- -Color: Green.
- -Off: Enclosure is off (AC cord is not connected).
- -On Solid: Enclosure is powered on.
- -On Blink: Enclosure is in the standby-power state.
- Enclosure Identify LED. Color: Blue.
- Enclosure Identify LED:
- -Color: Blue.
- -Off: Normal.
- -On Solid: Identify State.
- System Fault LED:
- -Color: Amber.
- -Off: Normal.
- -On Solid: Check Error Log.

- System Roll-up LED:
- -Color: Amber.
- -Off: Normal.
- -On Solid: Fault.
- Power Button.
- System Reset Switch.
- Two Thermal Sensors.
- One Pressure/Altitude Sensor.

The LCD operator panel is optional in some systems, but there must be at least one in a server in a rack containing any Power S922, Power S914, or Power S924 server. The panel can be accessed by using the switches on the front panel.

Here are several of the operator panel features:

- Two x16 character LCD displays
- Increment, decrement, and 'enter' buttons

The following functions are available through the operator panel:

- Error information
- Generate dump
- View machine type, model, and serial number
- Limited set of repair functions

The System Management Services (SMS) error log is accessible through the SMS menus. This error log contains errors that are found by partition firmware when the system or partition is starting.

The service processor's error log can be accessed on the ASMI menus.

You can also access the system diagnostics from a Network Installation Manager (NIM) server.

IBM i and its associated machine code provide dedicated service tools (DSTs) as part of the IBM i licensed machine code (Licensed Internal Code) and System Service Tools (SSTs) as part of IBM i. These interfaces can be used to check various system information. For more information, see IBM i service functions.

## Service Focal Point on the Hardware Management Console

Service strategies become more complicated in a partitioned environment. The Manage Serviceable Events task in the management console can help streamline this process.

Each LPAR reports errors that it detects and forwards the event to the SFP application that is running on the management console without determining whether other LPARs also detect and report the errors. For example, if one LPAR reports an error for a shared resource, such as a managed system power supply, other active LPARs might report the same error.

By using the Manage Serviceable Events task in the management console, you can avoid long lists of repetitive Call Home information by recognizing that they are repeated errors and consolidating them into one error.

In addition, you can use the Manage Serviceable Events task to initiate service functions on systems and LPARs, including the exchanging of parts, configuring connectivity, and managing memory dumps.

## 2.11.2 Power Systems Firmware maintenance

The IBM Power Systems Client-Managed Microcode is a methodology that enables you to manage and install microcode updates on Power Systems servers and their associated I/O adapters.

## Firmware entitlement

Since POWER8, the server firmware updates are restricted to entitled servers. A customer must be registered with IBM and entitled by a service contract. During the initial machine warranty period, the access key is installed in the machine by manufacturing. The key is valid for the regular warranty period plus some extra time. The Power Systems Firmware is relocated from the public repository to the access control repository. The I/O firmware remains on the public repository, but the server must be entitled for installation. When the lslic command is run to display the firmware levels, a new value, update\_access\_key\_exp\_date , is added. The HMC GUI and the ASMI menu show the 'Update access key expiration date'.

When the system is no longer entitled, the firmware updates fail. Some new System Reference Code (SRC) packages are available:

- E302FA06: Acquisition entitlement check failed
- E302FA08: Installation entitlement check failed

Any firmware release that was made available during the entitled time frame can still be installed. For example, if the entitlement period ends on 31 December 2019 and a new firmware release is release before the end of that entitlement period, then it can still be installed. If that firmware is downloaded after 31 December 2019 but it was made available before the end of the entitlement period, it still can be installed. Any newer release requires a new update access key.

Note: The update access key expiration date requires a valid entitlement of the system to perform firmware updates.

You can find an update access key at IBM CoD Home.

For more information, go to IBM Entitled Software Support.

## Firmware updates

System firmware is delivered as a release level or a service pack. Release levels support the general availability (GA) of new functions or features, and new machine types or models. Upgrading to a higher release level is disruptive to customer operations. IBM intends to provide no more than two new release levels per year. These release levels will be supported by service packs. Service packs are intended to contain only firmware fixes and not introduce new functions. A service pack is an update to an existing release level.

If the system is managed by an HMC, the HMC is used for the firmware updates. With the HMC, you can take advantage of the Concurrent Firmware Maintenance (CFM) when available. With CFM, IBM increases its clients' opportunity to stay on a release level for longer periods. Clients expecting maximum stability can defer the upgrade until there is a compelling reason to upgrade, such as:

- A release level is approaching its end of service date (that is, it has been available for about a year and soon service will not be supported).
- Move a system to a more standardized release level when there are multiple systems in an environment with similar hardware.

- A new release has a new function that is needed in the environment.
- A scheduled maintenance action causes a platform restart, which provides an opportunity to also upgrade to a new firmware release.

The updating and upgrading of system firmware depends on several factors, such as whether the system is stand-alone or managed by a management console, the firmware that is installed, and what OSs are running on the system. These scenarios and the associated installation instructions are comprehensively outlined in the firmware section of Fix Central.

You might also want to review the best practice white papers that are found at Service and support best practices for Power Systems.

## Firmware update steps

The system firmware consists of service processor microcode, Open Firmware microcode, and SPCN microcode.

The firmware and microcode can be downloaded and installed either from an HMC, from a running partition, or from USB port number 1 on the back, if that system is not managed by an HMC.

Power Systems Firmware has a permanent firmware boot side (A side) and a temporary firmware boot side (B side). New levels of firmware must be installed first on the temporary side to test the update's compatibility with existing applications. When the new level of firmware is approved, it can be copied to the permanent side.

For access to the initial websites that address this capability, see Support for IBM Systems. For Power Systems, select the Power link.

Although the content under the 'Popular links' section can change, click the Firmware and HMC updates link to go to the resources for keeping your system's firmware current.

If there is an HMC to manage the server, the HMC interface can be used to view the levels of server firmware and power subsystem firmware that are installed and that are available to download and install.

Each Power Systems server has the following levels of server firmware and power subsystem firmware:

- Installed level

This level of server firmware or power subsystem firmware is installed and is installed into memory after the managed system is powered off and then powered on. It is installed on the temporary side of system firmware.

- Activated level

This level of server firmware or power subsystem firmware is active and running in memory.

- Accepted level

This level is the backup level of the server or power subsystem firmware. You can return to this level of server or power subsystem firmware if you decide to remove the installed level. It is installed on the permanent side of system firmware.

Figure 2-27 shows the different levels in the HMC.

Figure 2-27   Firmware levels

<!-- image -->

IBM provides the CFM function on selected Power Systems servers. This function supports applying nondisruptive system firmware service packs to the system concurrently (without requiring a restart operation to activate changes). For systems that are not managed by an HMC, the installation of system firmware is always disruptive.

The concurrent levels of system firmware can, on occasion, contain fixes that are known as deferred . These deferred fixes can be installed concurrently but are not activated until the next IPL. Deferred fixes, if any, are identified in the Firmware Update Descriptions table of the firmware document. For deferred fixes within a service pack, only the fixes in the service pack that cannot be concurrently activated are deferred.

Table 2-65 shows the file-naming convention for system firmware.

Table 2-65   Firmware naming convention

| PPNNSSS_FFF_DDD   | PPNNSSS_FFF_DDD          | PPNNSSS_FFF_DDD          | PPNNSSS_FFF_DDD          |
|-------------------|--------------------------|--------------------------|--------------------------|
| PP                | Package identifier       | 01                       | -                        |
| NN                | Platform and class       | VL                       | Low end                  |
| SSS               | Release indicator        | Release indicator        | Release indicator        |
| FFF               | Current fix pack         | Current fix pack         | Current fix pack         |
| DDD               | Last disruptive fix pack | Last disruptive fix pack | Last disruptive fix pack |

The following example uses this convention:

01VL910,73,73 = POWER9 Entry Systems Firmware for 9009-41A, 9009-22A, and 9009-42A

An installation is disruptive if the following statements are true:

- The release levels (SSS) of the currently installed and the new firmware differ.
- The service pack level (FFF) and the last disruptive service pack level (DDD) are equal in the new firmware.

Otherwise, an installation is concurrent if the service pack level (FFF) of the new firmware is higher than the service pack level that is installed on the system and the conditions for disruptive installation are not met.

## 2.11.3 Concurrent Firmware Maintenance improvements

Since POWER6, firmware service packs (updates) are concurrently applied and take effect immediately. Occasionally, a service pack is included where most of the features can be concurrently applied, but because changes to some server functions (for example, changing initialization values for chip controls) cannot occur during operation, a patch in this area required a system restart for activation.

With the Power-On Reset Engine (PORE), the firmware can now dynamically power off processor components, change the registers, and reinitialize while the system is running without discernible impact to any applications running on a processor. With PORE, you can potentially make concurrent firmware changes in POWER9, which in earlier designs required a restart to take effect.

Activating new firmware functions requires the installation of a firmware release level (upgrades). This process is disruptive to server operations and requires a scheduled outage and full server restart.

## 2.11.4  IBM Electronic Services and IBM Electronic Service Agent

IBM transformed its delivery of hardware and software support services to help you achieve higher system availability. Electronic Services is a web-enabled solution that offers an exclusive, no additional charge enhancement to the service and support that is available for IBM servers. These services provide the opportunity for greater system availability with faster problem resolution and preemptive monitoring. The Electronic Services solution consists of two separate but complementary elements:

- Electronic Services news page
- Electronic Service Agent

## Electronic Services news page

The Electronic Services news page is a single internet entry point that replaces the multiple entry points that traditionally are used to access IBM internet services and support. With the news page, you can gain easier access to IBM resources for assistance in resolving technical problems.

## Electronic Service Agent

The Electronic Service Agent (ESA) is software that is on your server. It monitors events and transmits system inventory information to IBM on a periodic, client-defined timetable. The IBM ESA automatically reports hardware problems to IBM.

Early knowledge about potential problems enables IBM to deliver proactive service that can result in higher system availability and performance. In addition, information that is collected through the IBM ESA is made available to IBM Support Services Representatives (IBM SSRs) when they help answer your questions or diagnose problems. Installation and use of IBM ESA for problem reporting enables IBM to provide better support and service for your IBM server.

To learn how Electronic Services can work for you, see IBM Electronic Services (an IBM ID is required).

Here are some of the benefits of Electronic Services:

- Increased uptime

The IBM ESA tool enhances the warranty or maintenance agreement by providing faster hardware error reporting and uploading system information to IBM Support, which can mean less time that is wasted monitoring the symptoms, diagnosing the error, and manually calling IBM Support to open a problem record.

Its 24x7 monitoring and reporting mean no more dependence on human intervention or off-hours customer personnel when errors are encountered in the middle of the night.

- Security

The IBM ESA tool is secure in monitoring, reporting, and storing the data at IBM. The IBM ESA tool securely transmits either through the internet (HTTPS or VPN) or modem, and can be configured to communicate securely through gateways to provide customers a single point of exit from their site.

Communication is one way. Activating IBM ESA does not enable IBM to call into a customer's system. System inventory information is stored in a secure database, which is protected behind IBM firewalls. It is viewable only by the customer and IBM. The customer's business applications or business data are never transmitted to IBM.

- More accurate reporting

Because system information and error logs are automatically uploaded to the IBM Support center with the service request, customers are not required to find and send system information, decreasing the risk of misreported or misdiagnosed errors.

When inside IBM, problem error data is run through a data knowledge management system, and knowledge articles are appended to the problem record.

- Customized support

By using the IBM ID that you enter during activation, you can view system and support information by selecting My Systems at Electronic Support.

My Systems provides valuable reports of installed hardware and software by using information that is collected from the systems by IBM ESA. Reports are available for any system that is associated with the customers IBM ID. Premium Search combines the function of search and the value of IBM ESA information, providing advanced search of the technical support knowledge base. Using Premium Search and the IBM ESA information that was collected from your system, you can see search results that apply specifically to your systems.

For more information about how to use the power of IBM Electronic Services, contact your IBM SSR or see Electronic Support.

## Service Event Manager

The Service Event Manager (SEM) enables the user to decide which of the serviceable events are called home by the IBM ESA. It is possible to lock certain events. Some customers might not allow data to be transferred outside their company. After the SEM is enabled, the analysis of the possible problems might take longer.

To work with SEM, use the following commands:

- To enable SEM, run the following command:

chhmc -c sem -s enable

- To disable SEM mode and specify what state in which to leave the Call Home feature, run the following commands:

chhmc -c sem -s disable --callhome disable chhmc -c sem -s disable --callhome enable

The easiest way to set up the IBM ESA is by using the wizard in the HMC GUI, which is shown in Figure 2-28.

Figure 2-28   Accessing the Electronic Service Agent setup wizard

<!-- image -->

The wizard guides the user through the necessary steps, including entering details about the location of the system, the contact details, and other details. The user can select which HMC or HMCs should be used, as shown in Figure 2-29.

Figure 2-29   Managing which HMCs are used for Call Home

<!-- image -->

If you select a server, you can easily open the SEM, as shown in Figure 2-30.

Figure 2-30   Opening the Serviceable Events Manager for a server

<!-- image -->

You can browse the SEM menus to see the events for this server, as shown in Figure 2-31.

Figure 2-31   Serviceable events for this server

<!-- image -->

## Related publications

The publications that are listed in this section are considered suitable for a more detailed description of the topics that are covered in this paper.

## IBM Redbooks

The following IBM Redbooks publications provide more information about the topics in this document. Some publications that are referenced in this list might be available in softcopy only.

- IBM PowerAI: Deep Learning Unleashed on IBM Power Systems Servers , SG24-8409
- IBM Power System AC922 Technical Overview and Introduction , REDP-5494
- IBM Power System E950: Technical Overview and Introduction , REDP-5509
- IBM Power System E980: Technical Overview and Introduction , REDP-5510
- IBM Power System L922 Technical Overview and Introduction , REDP-5496
- IBM Power System S822LC for High Performance Computing Introduction and Technical Overview , REDP-5405
- IBM Power Systems H922 and H924 Technical Overview and Introduction , REDP-5498
- IBM Power Systems LC921 and LC922: Technical Overview and Introduction , REDP-5495
- IBM PowerVM Best Practices , SG24-8062
- IBM PowerVM Virtualization Introduction and Configuration , SG24-7940
- IBM PowerVM Virtualization Managing and Monitoring , SG24-7590

You can search for, view, download, or order these documents and other Redbooks publications, Redpapers, web docs, drafts, and additional materials, at the following website:

ibm.com /redbooks

## Online resources

These websites are also relevant as further information sources:

- IBM Fix Central website
- http://www.ibm.com/support/fixcentral/
- IBM Knowledge Center

http://www.ibm.com/support/knowledgecenter/

- IBM Knowledge Center: IBM Power Systems Hardware

http://www-01.ibm.com/support/knowledgecenter/api/redirect/powersys/v3r1m5/inde x.jsp

- IBM Knowledge Center: Migration combinations of processor compatibility modes for active Partition Mobility

http://www-01.ibm.com/support/knowledgecenter/api/redirect/powersys/v3r1m5/topi c/p7hc3/iphc3pcmcombosact.htm

- IBM Portal for OpenPOWER - POWER9 Monza Module

https://www.ibm.com/systems/power/openpower/tgcmDocumentRepository.xhtml?aliasI d=POWER9\_Monza

- IBM Power Systems

http://www.ibm.com/systems/power/

- IBM Storage website

http://www.ibm.com/systems/storage/

- IBM Systems Energy Estimator

http://www-912.ibm.com/see/EnergyEstimator/

- IBM System Planning Tool website

http://www.ibm.com/systems/support/tools/systemplanningtool/

- NVIDIA Tesla V100

https://www.nvidia.com/en-us/data-center/tesla-v100/

- NVIDIA Tesla V100 Performance Guide

http://images.nvidia.com/content/pdf/volta-marketing-v100-performance-guide-usr6-web.pdf

- OpenCAPI

http://opencapi.org/technical/use-cases/

- OpenPOWER Foundation

https://openpowerfoundation.org/

- Power Systems Capacity on Demand website

http://www.ibm.com/systems/power/hardware/cod/

- Support for IBM Systems website

http://www.ibm.com/support/entry/portal/Overview?brandind=Hardware~Systems~Power

## Help from IBM

IBM Support and downloads

ibm.com /support

IBM Global Services

ibm.com /services

<!-- image -->

Back cover

<!-- image -->

ISBN 0738458880 REDP-5595-00

<!-- image -->