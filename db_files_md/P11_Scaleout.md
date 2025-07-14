Front cover

<!-- image -->

## IBM Power11 Scale-Out Servers: Introduction and Overview

Tim Simon

Larry Bolhuis

David Harlow

Jean-Manuel Lenez

Jaqui Lynch

Michael Miller

Dean Mussari

Steve Palazzolo

Gerd Reinhardt

Henry Vo

## IBM Power

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

IBM Redbooks

## IBM Power11 Scale-Out Servers

July 2025

Note: Before using this information and the product it supports, read the information in 'Notices' on page vii.

First Edition (July 2025)

This edition applies to 9824-42A, 9856-42H, 9824-22A, and 9856-22H

## Contents

| Notices . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                            | . vii   |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| Trademarks . . . . .                                                                                  | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                  | viii    |
| Preface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . .                                                                                                                                                                | . ix    |
| Authors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                                      | . ix    |
| . Now you can become a published author, too! . . . .                                                 | . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                                      | . xii   |
| Comments welcome. . . . . . .                                                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                  | . xii   |
| Stay connected to IBM Redbooks .                                                                      | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                            | xiii    |
| Chapter 1. Overview of Power11 . .                                                                    | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                | . 1     |
| 1.1 Power11 overview. . . . . . . . . . .                                                             | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                              | . 2     |
| 1.2 IBM Power roadmaps .                                                                              | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                | . 3     |
| 1.2.1                                                                                                 | IBM Power processor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                  | . 3     |
| 1.2.2                                                                                                 | IBM AIX roadmap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                | . 4     |
| 1.2.3                                                                                                 | IBM i roadmap. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                             | . 5     |
| 1.2.4                                                                                                 | PowerVM VIOS roadmap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                       | . 6     |
| 1.2.5                                                                                                 | Red Hat Enterprise Linux and IBM Power . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | . 6     |
| 1.2.6 SUSE Enterprise Linux and IBM Power                                                             | . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                                  | . 7     |
| 1.3 Power11 improvements from Power10. . . . . .                                                      | . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                                    | . 7     |
| 1.3.1 New Power11 server portfolio. .                                                                 | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                      | . 9     |
| 1.4 Power11: Trusted, autonomous, and modern. . . . .                                                 | . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                                            | 12      |
| 1.4.1 Building a trusted infrastructure with Quantum Safe Encryption. . . . .                         | . . . . .                                                                                                                                                                                | 13      |
| 1.4.2                                                                                                 | Protect, detect, and recover with Power Cyber Vault . . . . . . . . . . . . . . . . . .                                                                                                  | 17      |
| 1.4.3                                                                                                 | Quantum-safe compliance with one-click inventory discovery . . . . . . . . . . .                                                                                                         | 20      |
| 1.4.4                                                                                                 | Zero planned downtime and end-to-end orchestration for maintenance events.                                                                                                               | 21      |
| 1.4.5                                                                                                 | Automated data collection for faster error resolution . . . . . . . . . . . . . . . . . .                                                                                                | 24      |
| 1.4.6                                                                                                 | Smart energy scheduling options with increased efficiency reduced energy consumption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | 25      |
| 1.4.7                                                                                                 | Superior performance of up to 25% improvement for consolidation of Oracle Workloads. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 19c 29  |
| 1.4.8                                                                                                 | Day 1 availability of Power11 in PowerVS with Hybrid Billing. . . . . . . . . . . .                                                                                                      | 30      |
| 1.4.9                                                                                                 | Off-chip AI acceleration with IBM Spyre . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                          | 31      |
| 1.4.10 Red Hat OpenShift with support for expanded software ecosystem. . . .                          | 1.4.10 Red Hat OpenShift with support for expanded software ecosystem. . . .                                                                                                             |         |
| 1.5 Introducing the Power11 processor . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                                          | 33      |
| 1.6 Operating system support . . . . .                                                                | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                              | 38      |
| 1.6.1                                                                                                 | AIX operating system . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                 | 39      |
| 1.6.2                                                                                                 | IBM i operating system . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                 | 39      |
| 1.6.3                                                                                                 | Linux operating system. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                  | 40      |
| 1.6.4 VIOS                                                                                            | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                            | 40      |
| 1.7 Firmware and Hardware Management Console . . . . .                                                | . . . . . . . . . . . . . . . . . . . . .                                                                                                                                                | 41      |
| 1.7.1 HMC Requirements. . . .                                                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                          | 41      |
| 1.8 Rack support . . . .                                                                              | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                        | 41      |
| 1.8.1 New rack considerations. . .                                                                    | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                | 42      |
| Chapter 2. Power11 Scale-out Servers . .                                                              | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                          | 43      |
| 2.1 IBM Power11 scale-out servers . . . .                                                             | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                      | 44      |
| 2.1.1 Family overview . . . . . . . . . . . . 2.2 IBM Power S1122 (9824-22A) Server                   | Overview. . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                              | 45      |
| 2.2.1 Processors . . .                                                                                | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                            |         |
|                                                                                                       |                                                                                                                                                                                          | 45      |

| 2.2.2                                                                                                             | Memory. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                       | . 46      |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| 2.2.3                                                                                                             | PCIe slots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                          | . 46      |
| 2.2.4                                                                                                             | . . NVMe drives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                     | . 47      |
| 2.2.5                                                                                                             | I/O expansion drawers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                               | . 47      |
| 2.2.6                                                                                                             | Power S1122 system configuration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                       | . 48      |
| 2.2.7                                                                                                             | Comparison between S1122 and S1022 and S1022s . . . . . . . . . . . . . . . . . . .                                                                                                                                       | . 51      |
| 2.3 IBM                                                                                                           | Power S1124 (9824-42A) Server Overview. . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                             | . 52      |
| 2.3.1                                                                                                             | Processors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                        | . 54      |
| 2.3.2                                                                                                             | Memory. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                       | . 54      |
| 2.3.3                                                                                                             | PCIe slots . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                      | . 55      |
| 2.3.4                                                                                                             | NVMe drive support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                              | . 55      |
| 2.3.5                                                                                                             | I/O expansion drawers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                               | . 56      |
| 2.3.6                                                                                                             | Power S1124 system minimum configuration. . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                               | . 57      |
| 2.3.7                                                                                                             | Comparison between S1124 and S1024 . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                              | . 60      |
| 2.4                                                                                                               | Processor and Memory Activation on Power S1122 and S1124 Systems . . . . . . . .                                                                                                                                          | . 61      |
| 2.4.1                                                                                                             | Advanced Memory Functions on the Power11 Scale-Out servers . . . . . . . . . .                                                                                                                                            | . 62      |
| 2.5                                                                                                               | Environmental and Physical Specifications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                  | . 63      |
| Chapter 3. I/O Subsystem . . . . . . . . .                                                                        | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                                               | . 67      |
| 3.1 Internal I/O . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        | . . . . . . . . . . .                                                                                                                                                                                                     | . 68      |
|                                                                                                                   | Internal PCIe Gen 5 subsystem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                     | . 69      |
| 3.1.1                                                                                                             | subsystem                                                                                                                                                                                                                 |           |
| 3.1.2                                                                                                             | Internal NVMe storage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                                 | . 72      |
| 3.1.3 3.1.4                                                                                                       | NVMe backplane. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . NVMe JBOF Card. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 73 . 73 |
| 3.1.5                                                                                                             | NVMe JBOF to Backplane Cabling. . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                                       | . 75      |
| 3.2                                                                                                               | . . . . . . . Enhancing I/O Scalability with Expansion Drawers. . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                         | .         |
| 3.2.1                                                                                                             | PCIe expansion card. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                              | 76 . 77   |
| 3.2.2                                                                                                             | Supported I/O Drawers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                               | . 81      |
| 3.2.3                                                                                                             | Non-supported drawers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                 | . 82      |
|                                                                                                                   | PCIe Gen 4 I/O Expansion Drawer.                                                                                                                                                                                          |           |
| 3.2.4                                                                                                             | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . adapter list . . . . . . . .                                                                                                                            | . 82      |
| 3.3 Supported                                                                                                     | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3.1 SAN adapters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | . 88 . 88 |
| 3.3.2                                                                                                             | Network adapters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                            | . 90      |
| 3.3.3                                                                                                             | Transceiver (SFP) Replacement Support for Fibre Channel and Ethernet Adapter Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                         | . 91      |
| 3.3.4                                                                                                             | SAS and Tape adapters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                 | . 92      |
| 3.4 NVME                                                                                                          | U.2 Devices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                           | . 93      |
| 3.4.1                                                                                                             | USB adapters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                          | . 95      |
| 3.4.2                                                                                                             | Cryptographic adapters. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                               | . 96      |
| 3.4.3                                                                                                             | Graphical adapters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                            | . 98      |
| 3.5 Other                                                                                                         | device support. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                           | . 98      |
| 3.5.1                                                                                                             | No longer supported . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                             | . 99      |
| 3.5.2                                                                                                             | PCIe adapters that require increased cooling. . . . . . . . . . . . . . . . .                                                                                                                                             | . 99      |
| . . . . . . . . . Chapter 4. Artificial Intelligence Support . . . . . . . . . . . . . . . . . .                  | . . . . . . . . . . . . . . . .                                                                                                                                                                                           | 103       |
| 4.1 On chip support. . . . . . . . . . . . . . . . . .                                                            | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                                                     | 104       |
| 4.2 AI                                                                                                            | Acceleration with IBM Spyre adapter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                   | 104       |
| 4.2.1 4.2.2                                                                                                       | Deploying AI in the Enterprise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Fit for Purpose Al Acceleration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        | 105 105   |
| 4.2.3 IBM Spyre adapter .                                                                                         | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                                                                 | 107       |
| 4.3 Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . .                                                                                                                                                                                                           | 108       |
| 4.3.1 Barriers to scaling AI and the IBM Power technology advantage . . .                                         | . . . . . . . .                                                                                                                                                                                                           | 109       |
|                                                                                                                   | . . . . . . . . . . . . . . . .                                                                                                                                                                                           |           |
| 4.3.2                                                                                                             | IBM Power AI Portfolio: from Data to Business Value . . .                                                                                                                                                                 | 110       |

| 4.3.3                                                                                                  | Strategic outcomes enabled by IBM Power . . . . . . . . .                                                                                            | 110     |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| 4.3.4                                                                                                  | Uniqueness of the platform . . . . . . . . . . . . . . . . . .                                                                                       | 110     |
| Chapter 5. Automation and Management . . .                                                             | . . . . . . . . . . .                                                                                                                                | 113     |
| 5.1                                                                                                    | Hardware Management Console overview . . . . . . . . . . . .                                                                                         | 114     |
| 5.1.1                                                                                                  | HMC Options . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                              | 114     |
| 5.1.2                                                                                                  | BMC network connectivity rules for 7063-CR2 HMC                                                                                                      | 116     |
| 5.1.3                                                                                                  | High availability HMC configuration . . . . . . . . . . . . .                                                                                        | 117     |
| 5.1.4                                                                                                  | HMC code level requirements. . . . . . . . . . . . . . . . . .                                                                                       | 117     |
| 5.1.5                                                                                                  | Keeping your HMC up to date. . . . . . . . . . . . . . . . . .                                                                                       | 118     |
| 5.1.6                                                                                                  | New features. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                            | 118     |
| 5.1.7                                                                                                  | Using the Automated Maintenance tool . . . . . . . . . .                                                                                             | 119     |
| 5.2                                                                                                    | Ansible . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                | 121     |
| 5.3                                                                                                    | Terraform . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                  | 124     |
| 5.4                                                                                                    | PowerVC. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                   | 127     |
| Chapter 6. Operating Systems .                                                                         | . . . . . . . . . . . . . . . . . . . . . .                                                                                                          | 131     |
| 6.1                                                                                                    | Subscription licensing . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                       | 133     |
| 6.1.1                                                                                                  | AIX subscription licensing . . . . . . . . . . . . . . . . . . . . .                                                                                 | 133     |
| 6.1.2                                                                                                  | IBM i subscription licensing. . . . . . . . . . . . . . . . . . . .                                                                                  | 134     |
| 6.2 AIX                                                                                                | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                  | 134     |
| 6.2.1                                                                                                  | AIX 7.3 Key Features . . . . . . . . . . . . . . . . . . . . . . . .                                                                                 | 134     |
| 6.2.2 6.2.3                                                                                            | Supported Levels . . . . . . . . . . . . . . . . . . . . . . . . . . . AIX Maintenance levels . . . . . . . . . . . . . . . . . . . . . .            | 135 135 |
| 6.2.4                                                                                                  | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                          | 136     |
|                                                                                                        | Licensing. . . .                                                                                                                                     |         |
| 6.2.5 6.3 IBM i . .                                                                                    | New AIX Editions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 136 138 |
| 6.3.1                                                                                                  | Intro to IBM i . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                         | 139     |
| 6.3.2                                                                                                  | Supported levels . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                             | 140     |
| 6.3.3                                                                                                  | New IBM i Features supported by Power11 . . . . . . .                                                                                                | 140     |
| 6.3.4                                                                                                  | IBM i Software Tiers . . . . . . . . . . . . . . . . . . . . . . . . .                                                                               | 141     |
| 6.3.5                                                                                                  | IBM i Licensing . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                            | 142     |
| 6.3.6                                                                                                  | IBM i Subscription Bundles for P20 and P30 . . . . . .                                                                                               | 143     |
| 6.3.7                                                                                                  | IBM i Software Maintenance (SWMA). . . . . . . . . . . .                                                                                             | 145     |
| 6.3.8                                                                                                  | CBU and DBM Licensing Models for IBM i . . . . . . . . .                                                                                             | 145     |
| 6.3.9                                                                                                  | Upgrading an existing IBM i license to 7.6 . . . . . . .                                                                                             | 147     |
| 6.3.10 IBM i Simplification . . . . . . . . . . . 6.4 Linux on IBM Power . . . . . . . . . . . . . . . | . . . . . . . . . . . . . .                                                                                                                          | 148     |
|                                                                                                        |                                                                                                                                                      | 148     |
|                                                                                                        | 6.4.1 Supported distributions . . . . . . . . . . . . . . . . . . . . . . .                                                                          |         |
|                                                                                                        | 6.4.2 Licensing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                   | 153     |
| 6.5                                                                                                    | Red Hat OpenShift . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Intro to KVM support                                                   | 154 156 |
| 6.6 6.7                                                                                                | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . PowerVM Virtual I/O Server . . . . . . . . . . . . . . . . . . .                           |         |
|                                                                                                        | . . . . . . . . . . . . . . . . . . .                                                                                                                | 157 157 |
| 6.8 Setting your LPAR compatibility mode Chapter 7. Enterprise Solutions . . . . . .                   | . . . . . . . .                                                                                                                                      | 159     |
| . . . . . . .                                                                                          | . . . . . . .                                                                                                                                        |         |
| 7.1 High Availability and Disaster Recovery Solutions                                                  | . . . . . .                                                                                                                                          | 160     |
| 7.1.1 PowerHA SystemMirror for AIX. . . .                                                              | . . . . . . . . . . . . .                                                                                                                            | 160     |
| for i                                                                                                  | . . . . . . . . . . . . . . .                                                                                                                        | 160     |
| 7.1.2 IBM PowerHA SystemMirror 7.1.3 VM Recovery Manager (VMRM).                                       | . . . . . . . . . . . . . . .                                                                                                                        | 161     |
| 7.2 IBM Db2 . . . . . .                                                                                | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                      | 162     |
| 7.3 Oracle . . . . . . . . . . . . . . . .                                                             | . . . . . . .                                                                                                                                        | 162     |
| . . . . . . . . . . . . . . . . . 7.3.1 Running Oracle Standard Edition 2 on IBM                       | Power. .                                                                                                                                             | 164     |
| 7.4 SAP HANA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                           | . . . .                                                                                                                                              | 165     |

| 7.5 Banking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                 | 166     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| 7.6 Health Care. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                    | 168     |
| 7.6.1 Epic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                    | 169     |
| Chapter 8. Servicing Power11 . . . . . . . . . . . . . . . . . . . . .                                                                                                | 171     |
| 8.1 IBM Maintenance . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                         | 172     |
| 8.2 IBM Expert Care . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                       | 172     |
| 8.3 IBM tools and interfaces . . . . . . . . . . . . . . . . . . . . . . . .                                                                                          | 173     |
| 8.4 BMC card . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                    | 174     |
| 8.5 ASMI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                | 174     |
| 8.5.1 Additional ASMI functions . . . . . . . . . . . . . . . . . . .                                                                                                 | 176     |
| 8.6 Entitled System Support . . . . . . . . . . . . . . . . . . . . . . . .                                                                                           | 178     |
| 8.7 System firmware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                       | 178     |
| 8.7.1 Update Access Keys. . . . . . . . . . . . . . . . . . . . . . .                                                                                                 | 187     |
| Chapter 9. Virtualization . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                         | 193     |
| 9.1 PowerVM. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                    | 194     |
| 9.1.1 IBM PowerVM Hypervisor. . . . . . . . . . . . . . . . . . .                                                                                                     | 194     |
| 9.1.2 Multiple shared processor pools . . . . . . . . . . . . . .                                                                                                     | 198     |
| 9.1.3 Virtual I/O Server . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                            | 198     |
| 9.1.4 Live Partition Mobility . . . . . . . . . . . . . . . . . . . . . .                                                                                             | 200     |
| 9.1.5 Active Memory Expansion. . . . . . . . . . . . . . . . . . .                                                                                                    | 201     |
| 9.1.6 Remote Restart. . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                             | 201     |
| 9.1.7 POWER processor modes . . . . . . . . . . . . . . . . . .                                                                                                       | 201     |
| 9.1.8 Single Root I/O Virtualization . . . . . . . . . . . . . . . .                                                                                                  | 202     |
| 9.1.9 More information about virtualization features . . .                                                                                                            | 203     |
| 9.1.10 Resource groups. . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 203     |
| 9.2 KVM support . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                     | 210     |
| Chapter 10. Hybrid Cloud Solutions . . . . . . . . . . . . . . . .                                                                                                    | 213     |
| 10.1 IBM Power Private Cloud with Shared Utility Capacity                                                                                                             | 214     |
| 10.1.1 IBM Cloud Management Console. . . . . . . . . . . . 10.2 Red Hat OpenShift . . . . . . . . . . . . . . . . . . . . . . . . . . .                               | 215 216 |
| 10.2.1 Red Hat OpenShift on Power . . . . . . . . . . . . . . .                                                                                                       | 216     |
| 10.2.2 Red Hat OpenShift AI on IBM Power Servers. . .                                                                                                                 | 219     |
| 10.3 Power Private Cloud Rack Solutions . . . . . . . . . . . . .                                                                                                     | 220     |
| 10.3.1 Key Features and Components: . . . . . . . . . . . . .                                                                                                         | 220     |
| 10.3.2 Available configurations . . . . . . . . . . . . . . . . . . .                                                                                                 | 220     |
| 10.3.3 IBM Cloud Paks . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                               | 221     |
| 10.3.4 Other cloud enablement solutions . . . . . . . . . . .                                                                                                         | 224     |
| 10.4 Power Virtual Server . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                         | 224     |
| 10.4.1 Power Virtual Server options. . . . . . . . . . . . . .                                                                                                        | 225     |
| . .                                                                                                                                                                   |         |
| 10.4.2 Power Virtual Server in the Cloud. . . . . . . . . . . .                                                                                                       | 226     |
| 10.4.3 Power Virtual Server Private Cloud. . . . . . . . . . .                                                                                                        | 227     |
| Related publications . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                        | 231     |
| IBM Redbooks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Online resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 231 231 |
| Help from IBM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                                   | 232     |

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

IBM, the IBM logo, and ibm.com are trademarks or registered trademarks of International Business Machines Corporation, registered in many jurisdictions worldwide. Other product and service names might be trademarks of IBM or other companies. A current list of IBM trademarks is available on the web at 'Copyright and trademark information' at https://www.ibm.com/legal/copytrade.shtml

The following terms are trademarks or registered trademarks of International Business Machines Corporation, and might also be trademarks or registered trademarks in other countries.

<!-- image -->

AIXfi

Concertfi

Db2fi

Enterprise Storage Serverfi

IBMfi

IBM API Connectfi

IBM Cloudfi

IBM Cloud Pakfi

IBM Concertfi

IBM FlashSystemfi

IBM Garage™

IBM Researchfi

IBM Securityfi

IBM Spectrumfi

IBM Spyre™

IBM Watsonfi

IBM watsonxfi

IBM Zfi

Instanafi

Micro-Partitioningfi

Passport Advantagefi

PINfi

POWERfi

Power8fi

Power9fi

PowerHAfi

PowerPCfi

PowerVMfi

Rationalfi

Redbooksfi

Redbooks (logo)

fi

Satellite™

Spyre™

System i5fi

System zfi

SystemMirrorfi

Tivolifi

Turbonomicfi

watsonxfi

WebSpherefi

The following terms are trademarks of other companies:

Intel, Intel Xeon, Intel logo, Intel Inside logo, and Intel Centrino logo are trademarks or registered trademarks of Intel Corporation or its subsidiaries in the United States and other countries.

The registered trademark Linuxfi is used pursuant to a sublicense from the Linux Foundation, the exclusive licensee of Linus Torvalds, owner of the mark on a worldwide basis.

LTO, Ultrium, the LTO Logo and the Ultrium logo are trademarks of HP, IBM Corp. and Quantum in the U.S. and other countries.

Microsoft, Windows, and the Windows logo are trademarks of Microsoft Corporation in the United States, other countries, or both.

Java, and all Java-based trademarks and logos are trademarks or registered trademarks of Oracle and/or its affiliates.

Ansible, Fedora, OpenShift, Red Hat, are trademarks or registered trademarks of Red Hat, Inc. or its subsidiaries in the United States and other countries.

UNIX is a registered trademark of The Open Group in the United States and other countries.

Other company, product, or service names may be trademarks or service marks of others.

## Preface

IBM Power11 scale-out servers are purpose-built to meet the evolving demands of modern enterprises, offering a fully integrated, end-to-end infrastructure stack that delivers exceptional performance, security, and agility. These systems are designed to support autonomous IT operations, enabling organizations to reduce risk, streamline management, and accelerate innovation across hybrid and multicloud environments.

With a strong focus on business continuity, Power11 processor-based servers provide zero planned downtime for maintenance, automated failover using spare processor cores, and rapid ransomware detection and recovery through IBM Power Cyber Vault. They also enhance productivity and efficiency by simplifying infrastructure operations and supporting flexible consumption models such as Capacity on Demand and Power Enterprise Pools 2.0.

Critically, processor-based scale-out servers are engineered for the future with quantum-safe security capabilities. They incorporate advanced cryptographic protections, including secure boot and live partition mobility hardened against quantum-era threats, and support for the latest FIPS 140-3 certified crypto modules. These features help safeguard sensitive data and ensure long-term compliance in an increasingly complex threat landscape.

For organizations embracing AI, Power11 processor-based servers are AI-ready by design, featuring built-in hardware acceleration for machine learning and inferencing workloads. Their seamless integration with IBM Cloud enables rapid scaling and consistent performance, empowering enterprises to deploy new applications and AI use cases with confidence.

The goal of this paper is to provide a hardware architecture analysis and highlight the changes, new technologies, and major features that are introduced in these systems.

This publication is intended for the following professionals who want to acquire a better understanding of IBM Power server products:

- -IBM Power customers
- -Sales and marketing professionals
- -Technical support professionals
- -IBM Business Partners
- -Independent software vendors (ISVs)

This paper expands the set of IBM Power documentation by providing a desktop reference that offers a detailed technical description of the Power11 processor-based scale-out server models.

This book was produced by a team of specialists from around the world working with IBM Redbooks.

Tim Simon is an IBMfi Redbooksfi Project Leader in Tulsa, Oklahoma, USA. He has over 40 years of experience with IBM primarily in a technical sales role working with customers to help them create IBM solutions to solve their business problems. He holds a BS degree in Math from Towson University in Maryland. He has worked with many IBM products and has extensive experience creating customer solutions using IBM Power, IBM Storage, and IBM System zfi throughout his career.

## Authors

Larry Bolhuis is an IBM i and cloud infrastructure advisor for Service Express, an IBM Platinum business partner headquartered in Grand Rapids, MI, USA. Larry has 37 years of experience on IBM i systems with preceding experience on S/34 and S/36. Since 1988 Larry has been a volunteer for COMMON and has held nearly every position from session manager to President. Larry has been a contributing author to more than 30 IBM certifications and has earned the Advanced Technical Expert badge. Larry is internationally recognized as a speaker at COMMON and many other user groups in North America and Europe. He has been recognized as an IBM Champion for the past 6 years.

David Harlow is a Senior Solutions Architect with Converge Technology Solutions, Inc. in Spring Hill, Tennessee, United States. David has extensive pre-sales experience in architecture, system design, planning, and project management. He is also experienced with the implementation of large-scale mission-critical projects that include production system upgrades, new installations, Power Systems with IBM i upgrades, Power Systems with IBM i consolidation, IBM i with VIOS and the IBM Storwize storage family. He also has experience with busiess continuity, and disaster recovery solutions. He is experienced in implementing difficult projects, and delivers projects on time and ahead of schedule. David previously was a Redbooks author having been a part of the team that wrote IBM BladeCenter PS703 and PS704 Technical Overview and Introduction , REDP-4744.

Jean-Manuel Lenez has been a Presales Engineer since 1999 with IBM Switzerland. He specializes in UNIX, Power, IBM AIXfi, and IBM i server technologies, and associated products such as PowerVM, IBM PowerHAfi, PowerSC, Linux on Power, and IBM Cloudfi. He is heavily involved in his presales mission, where he leads projects with major customers regarding various subjects, such as artificial intelligence, deep learning, SAP HANA, server consolidation, and HADR.

Jaqui Lynch is a seasoned consultant based in the United States, bringing over 48 years of experience across a wide range of projects and operating systems. Her expertise spans multiple vendor platforms, including mainframes, UNIX systems, midrange systems, and personal workstations. Since transitioning to UNIX in 1993, she has specialized in IBM Power beginning in 1999. Jaqui spent more than 22 years as an IBM customer before joining three IBM Business Partners in the U.S. She now operates as an independent consultant, with a focus on enterprise architecture, virtualization, performance optimization, security, and solution delivery on Power running AIX and Linux. A respected voice in the technical community, Jaqui is a frequent speaker at IBM and industry conferences worldwide. She also contributes regularly to IBM TechChannel magazine. She holds a Master's degree in Philosophy from the University of Illinois Springfield.

Michael Miller is an IBM Champion and Enterprise Architect with Pellera Technologies (formerly Mainline Information Systems), an IBM Platinum Business Partner and trusted technology partner delivering innovative, best-fit technology solutions to enterprise and midmarket businesses across the US. He has 25 years of experience working with IBM i and has been working extensively with the IBM Power platform on everything from presales architecture to post sales implementations. He possesses multiple IBM certifications, covering both sales and technical areas, including a Professional Cloud Architect credential, indicating expertise in IBM cloud solutions. He is a leading industry expert in IBM Cloud and Power Virtual Server and works closely with IBM developers in shaping the future of PowerVS. He has been a speaker at conferences including IBM TechXchange and Common POWERUp. He spends his free time with his children (Christian, Elliot, Audrey  Ethan) while also enjoying time at theme parks, whether it's experiencing the thrill of the latest roller coaster or simply taking a leisurely stroll through the park. You'll find him to be a collector of Star Wars memorabilia while also being a LEGO enthusiast building on the newest LEGO sets. He holds a Bachelor of Science degree from Western Kentucky University.

Dean Mussari is an IBM Power Brand Technical Specialist serving the National Market in the United States. He brings over 35 years of experience working with IBM servers and storage solutions, primarily in large-scale retail environments. His core expertise lies in IBM Power, with a strong focus on IBM i. Before joining IBM, he built a distinguished career delivering enterprise infrastructure solutions that drive performance and reliability. He holds a Master's degree in Computer Science from Loyola University Chicago.

Steve Palazzolo is an IBM Power Brand Technical Specialist serving the U.S. National Market. He brings over 36 years of experience in designing and implementing IBM server and storage solutions, with a strong background in large-scale retail environments. Prior to joining IBM, Steve led an IBM Power implementation team at a managed service provider, further deepening his expertise in enterprise infrastructure. His primary focus is on IBM Power Servers, particularly in environments running IBM i, and on FlashSystem storage solutions. Steve holds a Bachelor of Arts degree from Barat College of DePaul University.

Gerd Reinhardt is a Hardware Product Engineer for IBM Power, based in Ehningen, Baden-Württemberg, Germany. He brings over 32 years of experience at IBM, including more than 27 years specializing in hardware support for the IBM Power family and its predecessors - System i5fi, iSeries, and AS/400. Throughout his career, he has held various roles in both front-end and back-end support.Gerd holds a certificate in electronics and an advanced technical college qualification. He also earned a diploma in Business Administration from the Academy of Bad Harzburg. Additionally, he has been recognized by the Trustforte Corporation (New York, NY) as having attained the equivalent of a Bachelor of Science degree in Information Technology. He is IBM-accredited at the Senior Level within the Product Services Profession. His areas of expertise include IBM i, IBM Power hardware, and PowerVMfi. Gerd has contributed to the development of IBM technical documentation and has co-authored several IBM Redbooks, including the IBM Systems Handbook and the IBM System Builder series.

Henry Vo is an IBM Redbooks Project Lead with a strong foundation in business and technology. He joined IBM in 2012 after earning his degree in Management Information Systems (MIS) from the University of Texas at Dallas. Since then, Henry has brought his technical expertise and business acumen to a wide range of roles within IBM. Throughout his career, Henry has contributed to solving complex business challenges through risk analysis, root-cause investigation, and the development of detailed technical plans. His experience spans project management, software testing (ST/FT/ETE), back-end development, and serving as a Department of Labor (DOL) agent for New York. Henry is known for his structured approach to problem-solving and his ability to bridge the gap between technical teams and business stakeholders. As a Redbooks Project Lead, he continues to share his knowledge and insights with the broader IBM community, helping others navigate the evolving landscape of enterprise technology.

Thanks to the following people for their contributions to this project:

Nicole Nett

IBM Chief Architect Power Servers, Austin, TX

Lyudmila Simeonova

IBM AIX IO Device Drivers/PowerVM VIOS, Sofia, Bulgaria

Milen Paiakov

IBM POWERfi Courseware Developer, Sofia, Bulgaria

Ruby Zgabay IBM Power Systems Chief Engineer, Austin, TX

Kaveh Naderi

IBM POWER System Chief Architect, Austin, TX

Paul Bastide

IBM Senior Software Engineer, Cambridge, MA

Tanya Koleva

IBM Technology Lifecycle Services, Sofia, Bulgaria

Manjunath Kumatagi

IBM Senior Software Engineer, OpenShift on Power, Bangalore, KA, India

Manoj Kumar IBM Chief Engineer, OpenShift, OpenShift AI, IBM Turbonomicfi, IBM Instanafi on Power,

Austin, TX

Pablo Pereira Ruiz

Senior Unix/AIX Administrator/Support en Interamericana de Cómputos S.A., Uruguay

To the authors of IBM Power11 E1150 Introduction and Technical Overview, SG24-8589 and IIBM Power11 E1180 Introduction and Technical Overview, SG24-8587 for sharing content freely for this publication.

## Now you can become a published author, too!

Here's an opportunity to spotlight your skills, grow your career, and become a published author - all at the same time! Join an IBM Redbooks residency project and help write a book in your area of expertise, while honing your experience using leading-edge technologies. Your efforts will help to increase product acceptance and customer satisfaction, as you expand your network of technical contacts and relationships. Residencies run from two to six weeks in length, and you can participate either in person or as a remote resident working from your home base.

Find out more about the residency program, browse the residency index, and apply online at:

ibm.com /redbooks/residencies.html

## Comments welcome

Your comments are important to us!

We want our books to be as helpful as possible. Send us your comments about this book or other IBM Redbooks publications in one of the following ways:

- /SM590000 Use the online Contact us review Redbooks form found at:

ibm.com /redbooks

- /SM590000 Send your comments in an email to:

redbooks@us.ibm.com

- /SM590000
- Mail your comments to: IBM Corporation, IBM Redbooks

Dept. HYTD Mail Station P099

## Stay connected to IBM Redbooks

- /SM590000 Find us on LinkedIn:
- https://www.linkedin.com/groups/2130806
- /SM590000 Explore new Redbooks publications, residencies, and workshops with the IBM Redbooks weekly newsletter:
- https://www.redbooks.ibm.com/subscribe
- /SM590000 Stay current on recent Redbooks publications with RSS Feeds:

https://www.redbooks.ibm.com/rss.html

<!-- image -->

Chapter 1.

1

## Overview of Power11

IBM Power11 processor-based servers represent a significant leap in enterprise computing. Building on the strengths of Power10, Power11 introduces up to 25% more cores per chip, higher clock speeds, and enhanced energy efficiency. It continues IBM's focus on reliability, availability, and serviceability (RAS), while also integrating quantum-safe security features to future-proof critical workloads. The processor is designed to support demanding enterprise applications, particularly those involving AI, analytics, and hybrid cloud environments.

POWER11 leverages Integrated Stacked Capacitor (ISC) technology and advanced 2.5D packaging to boost performance and efficiency. These innovations, combined with enhanced thermal management - such as more efficient fans and heatsinks - significantly improve system density, cooling effectiveness, and overall compute capability.

A standout feature of Power11 is its continued support for AI workloads through the Matrix-Math Assist (MMA) architecture and the integration of the IBM Spyre Accelerator, which is optimized for generative AI and complex model inference. This positions Power11 as a strong alternative to traditional GPU-heavy AI infrastructures. Additionally, Power11 strengthens its virtualization capabilities with deeper KVM integration, enhancing compatibility with Linux-native tools and hybrid cloud platforms. This makes it a versatile choice for enterprises seeking scalable, AI-ready infrastructure.

The following topics are covered in this chapter:

- /SM590000 Power11 overview
- /SM590000 IBM Power roadmaps
- /SM590000 Power11 improvements from Power10
- /SM590000 Power11: Trusted, autonomous, and modern
- /SM590000 Introducing the Power11 processor
- /SM590000 Operating system support
- /SM590000 Firmware and Hardware Management Console
- /SM590000 Rack support

## 1.1  Power11 overview

For over 35 years, IBM Power servers have been a cornerstone of enterprise computing, delivering unmatched performance, reliability, and availability for mission-critical workloads across the globe. From the original RS/6000 systems powered by the Power1 processor to the advanced Power11-based platforms, IBM Power has consistently evolved to meet the demands of modern IT infrastructure.

The Power architecture follows a consistent innovation cadence, introducing a new generation of processors approximately every three years. Each iteration brings significant enhancements more cores and threads, improved energy efficiency, increased memory bandwidth, and expanded I/O capabilities - ensuring the platform remains at the forefront of enterprise computing.

The Power11 platform is built on three foundational principles:

- /SM590000 Trusted

Delivers continuous business operations with up to 99.9999% availability (on Power E1180), zero planned downtime for maintenance, quantum-safe cryptography, and accelerated system recovery.

- /SM590000 Autonomous

Boosts operational efficiency through intelligent automation, dynamic performance tuning, and reduced manual intervention.

- /SM590000 Modern

Enables AI-infused application deployment across hybrid environments - on-premises and in the cloud - leveraging off-chip AI acceleration and seamless integration with platforms like Red Hat OpenShift and IBM watsonxfi.

The Power11 family is segmented into three primary tiers to address a wide range of workload requirements:

- /SM590000 Entry-level: Power S1122/S1124 - optimized for departmental and edge workloads
- /SM590000 Midrange: Power E1150 - ideal for enterprise consolidation and scalable virtualization
- /SM590000 High-end: Power E1180 - designed for large-scale, mission-critical, and AI-intensive workloads

Power11 introduces several key advancements across the portfolio:

- /SM590000 Up to 6 nines (99.9999%) availability on high-end systems
- /SM590000 Enhanced security with quantum-safe cryptography and secure boot enhancements
- /SM590000 Performance gains of up to 15% per core and up to 25% per thread with combined hardware and software optimizations
- /SM590000 Significant throughput improvements in midrange and entry-level systems
- /SM590000 Up to 50% increase in memory bandwidth, leveraging DDR5 and advanced memory controllers

Additionally, Power11 introduces serial number-preserving upgrades from Power10 systems (available starting Q4 2025), enabling seamless transitions without disrupting asset tracking or licensing.

This Redbook focuses on the IBM Power11 scale-out servers, the entry level offering in the Power11 lineup. It delivers a balanced combination of performance, scalability, and cost-efficiency - making it an ideal platform for enterprise workloads, virtualization, and AI integration.

## 1.2  IBM Power roadmaps

IBM continues to advance its Power architecture to address the evolving demands of artificial intelligence, hybrid cloud, and mission-critical enterprise workloads. Central to IBM's hybrid cloud strategy, the Power platform is optimized for Red Hat OpenShift, enabling containerized workloads and cloud-native application development.

IBM Power Virtual Server extends these capabilities into the cloud, allowing clients to run Power workloads either on-premises or in IBM Cloud, while benefiting from flexible consumption models and meeting data residency and compliance requirements. This hybrid approach ensures seamless workload portability and supports modernization initiatives.

The Power platform also maintains a robust ecosystem of operating systems, including IBM AIX - a UNIX-based OS with a roadmap extending beyond 2035; IBM i - an integrated OS renowned for its security, stability, and ease of use; and Linux on Power, which supports distributions such as Red Hat Enterprise Linux (RHEL) and SUSE Linux Enterprise Server (SLES), making it ideal for open-source and cloud-native environments.

Complementing its technology stack, IBM has built a strategic network of alliances that significantly expand the reach and capabilities of the Power platform. Notably, IBM Power Virtual Server is a certified platform for RISE with SAP, enabling high-performance, reliable SAP workload deployment in hybrid cloud environments. Red Hat technologies like OpenShift and Ansible are deeply integrated into Power systems, supporting automation and DevOps practices. Additionally, IBM collaborates with major cloud providers - including Microsoft, AWS, and Google Cloud - to deliver hybrid and multicloud solutions, allowing Power workloads to extend seamlessly into public cloud infrastructures.

This section discusses IBM's roadmaps for evolution for the IBM Power-based infrastructure.

## 1.2.1  IBM Power processor

IBM's Power roadmap continues to evolve with the upcoming Power11 generation, set to launch in Q3 2025. Building on the innovations of Power10, Power11 introduces enhancements across the processor architecture, packaging, and energy efficiency. A key advancement is the integration of an additional silicon layer for improved energy management, allowing for higher performance with lower power consumption. This generation also boosts core strength and count, enabling it to handle even more demanding workloads. IBM is also refining its matrix math accelerators (MMAs), which were first introduced in Power10, to further accelerate AI inferencing directly on the chip - eliminating the need for external GPUs in many scenarios.

Looking beyond Power11, IBM's roadmap emphasizes full-stack innovation and adaptability to emerging technologies. The Power11 platform is designed to be memory-agnostic, supporting both DDR4 and DDR5 via the Open Memory Interface (OMI), and it introduces improved thermal infrastructure through advanced packaging and cooling technologies. These developments not only enhance performance but also reduce operational costs in data centers. Future iterations of the Power architecture are expected to continue this trend, with a focus on hybrid cloud readiness, AI integration, and support for open-source ecosystems. IBM's long-term vision includes deeper collaboration with the OpenPOWER community and a renewed emphasis on openness, flexibility, and sustainability in enterprise computing.

Figure 1-1 shows the different generations of the Power processor family and shows the continued plans for improvements. With the release of Power11, the next generation of Power processors is already in development and additional processor designs are in the pipeline after that generation.

Figure 1-1   Power chip roadmap

<!-- image -->

## 1.2.2  IBM AIX roadmap

IBM AIX (Advanced Interactive eXecutive) operating system is a proprietary UNIX-based operating system built on open standards and specifically designed for IBM Power servers.

For over 38 years, AIX has powered mission-critical applications and databases in industries with high-performance computing needs like finance, retail, healthcare, government, manufacturing, and insurance. Paired with IBM Power11 processor-based systems, the latest AIX 7.3 expands its reach into new markets and workloads to deliver unmatched performance, security, scalability, and reliability, all while supporting digital transformation through flexible subscription models tailored to business needs, and enabling adoption of technologies like hybrid cloud, AI, and cloud-native applications.

AIX's proven binary compatibility allows applications to run unchanged and without recompilation on the newest release, safeguarding IT investments in the platform.

IBM is strongly committed to delivering an AIX release roadmap of further innovations and purposeful support that extends beyond 2035 ensuring a stable, future-proof platform for enterprise workloads.

The current roadmap is shown in Figure 1-2.

Figure 1-2   Support timeline for future generations of AIX

<!-- image -->

For more information on IBM's strategy and roadmap for IBM AIX see Strategy and Roadmap for the IBM AIX Operating System.

Additional information about AIX can be found in section 6.2, 'AIX' on page 134.

## 1.2.3  IBM i roadmap

Since 2008, IBM has consistently released new versions of IBM i approximately every three years, with IBM i 7.6 being the latest. Each release introduces new features, workload support, and language enhancements while maintaining backward compatibility - allowing customers to preserve and extend their existing investments. IBM i is recognized as one of the most secure, self-optimizing, and scalable operating systems in the world. IBM continues to deliver updates and enhancements throughout each release's lifecycle via Program Temporary Fixes (PTFs) and Technology Refreshes (TRs). A key differentiator in the enterprise OS market is IBM's long-term commitment to IBM i, demonstrated by its publicly available roadmap, which currently extends to 2035 and is updated annually - underscoring IBM's dedication to the platform's future. The roadmap is shown in Figure 1-3.

Figure 1-3   IBM i support matrix

<!-- image -->

## 1.2.4  PowerVM VIOS roadmap

PowerVM Virtual I/O Server (VIOS) is a critical component of the IBM Power Systems virtualization stack, enabling shared access to physical I/O resources for client logical partitions (LPARs). Like all IBM software, VIOS follows a defined product lifecycle that includes general availability, support phases, and end-of-support (EOS) milestones. Table 1-1 shows the VIOS release schedule as of July 2025.

Table 1-1   VIOS release schedule

| VIOS Release   | Release Date   | End of Fix Support a         | Latest FP b      | Next FP c    |
|----------------|----------------|------------------------------|------------------|--------------|
| 4.1.1          | Dec-24         | 31 December 2027 (estimated) | VIOS_FP_4.1.1.0  | 23 July 2025 |
| 4.1.0          | Nov-23         | 30 November 2026 (estimated) | VIOS_FP_4.1.0.30 | 23 July 2025 |
| 3.1.4          | Dec-22         | 30 April 2026 (estimated)    | VIOS_FP_3.1.4.50 | 23 July 2025 |
| 3.1.3          | Sept-21        | 30-Sept-24                   | VIOS_FP_3.1.3.40 | None         |
| 3.1.2          | Nov-20         | 30-Nov-23                    | VIOS_FP_3.1.2.60 | None         |

- a. 'End of Fix Support' (EoFS) is the end of the maintenance period for a VIOS Release.  Fix Packs and interim fixes will not be created for a VIOS Release after EoFS.
- b. 'Latest FP' is the most recent FP available for the VIOS Release and links to that FP on Fix Central.
- c. 'Next FP' is the target availability date for the next Fix Pack for the given VIOS Release.  After the final Fix Pack for a VIOS Release is available, further fixes for the release are provided as interim fixes.

Note: The End of Service (EOS) date for a VIOS release is not indicated in this table. EOS dates can be found on the IBM Software Lifecycle page.

For additional details regarding the PowerVM Virtual I/O Server (VIOS) roadmap, please refer to the PowerVM VIOS Lifecycle Information and System to PowerVM Virtual I/O Server maps.

## 1.2.5  Red Hat Enterprise Linux and IBM Power

Red Hat has affirmed its strong commitment to the IBM Power platform, particularly as both companies align around hybrid cloud, AI, and open-source innovation. This partnership is deeply rooted in their shared vision of delivering enterprise-grade solutions that are scalable, secure, and optimized for modern workloads.

At the Red Hat Summit 2025, Red Hat emphasized its dedication to supporting IBM Power through continued enhancements to Red Hat Enterprise Linux (RHEL) on Power Systems. This includes performance tuning for Power10 and Power11 processors, as well as deeper integration with Red Hat OpenShift for containerized and cloud-native applications. These efforts ensure that Power users can fully leverage Red Hat's open hybrid cloud technologies across both on-premises and cloud environments.

Red Hat also plays a pivotal role in enabling AI workloads on Power, with support for AI inference and acceleration technologies that align with IBM's hardware innovations like Matrix Math Assist (MMA) and the upcoming Spyre AI Accelerator. This synergy allows enterprises

to deploy AI models efficiently on Power infrastructure using Red Hat's open-source toolchains and platforms.

Furthermore, Red Hat and IBM continue to collaborate on automation and DevOps through tools like Ansible Automation Platform, which is optimized for managing Power environments. This integration simplifies operations, enhances consistency, and accelerates application delivery across hybrid infrastructures.

For more information on Red Hat Enterprise Linux support on IBM Power see 'Red Hat Enterprise Linux' on page 149.

## 1.2.6  SUSE Enterprise Linux and IBM Power

The partnership between SUSE Linux and IBM Power Systems is a long-standing and strategic collaboration focused on delivering enterprise-grade Linux solutions for mission-critical workloads, hybrid cloud, and SAP environments.

SUSE and IBM have worked together for over two decades to provide robust, scalable, and secure Linux solutions on IBM Power infrastructure. Their joint efforts are centered around:

- /SM590000 SUSE Linux Enterprise Server (SLES) for Power Systems
- /SM590000 SLES for SAP Applications, optimized for SAP HANA on Power
- /SM590000 Hybrid and multicloud enablement through container and virtualization technologies

SUSE's open-source model aligns with IBM's strategy to provide flexible, vendor-neutral solutions. This enables customers to modernize their IT environments while avoiding vendor lock-in.

For more information on SUSE Enterprise Linux see 'SUSE Linux Enterprise Server' on page 151

## 1.3  Power11 improvements from Power10

IBM Power11 scale-out servers introduce a comprehensive suite of advanced capabilities, all rooted in IBM's core strength: a full-stack, end-to-end design. By tightly integrating every layer of the infrastructure - from the POWER11 processor and system architecture to firmware, operating systems, and cloud services - IBM Power delivers a synergistic platform built for autonomous IT. This holistic approach consistently drives tangible business outcomes across three foundational pillars: unprecedented business continuity, enhanced productivity and efficiency, and accelerated growth and scalability.

## Unprecedented Business Continuity

Power11 scale-out servers redefine operational resilience with features designed to eliminate downtime and ensure continuous service delivery:

- /SM590000 Planned Downtime Elimination: Leveraging technologies such as live updates, rolling upgrades, and autonomous patching, the Power11 servers enable maintenance without taking applications offline - targeting zero hours of planned downtime.
- /SM590000 Spare Core Technology: At the silicon level, the system includes spare processor cores that can be dynamically activated in response to hardware failures. This proactive fault tolerance mechanism allows seamless failover without requiring system or application restarts, preserving compute capacity and system integrity.

- /SM590000 Power Cyber Vault: Advanced threat detection can identify ransomware attacks in under a minute. Combined with automated recovery mechanisms, this feature significantly enhances cyber resiliency. It is offered in collaboration with IBM Storage and IBM Expert Labs.
- /SM590000 Quantum-Safe Protection: The Power11 platform incorporates quantum-safe cryptography to secure system reboots and live partition mobility, ensuring future-ready data protection.
- /SM590000 Crypto Compliance: Support for the IBM 4770 Crypto Card enables FIPS 140-3 Level 4 certification, enhancing compliance with stringent security standards.
- /SM590000 Automated Diagnostics: Intelligent data collection accelerates error resolution, saving up to 8 hours per support ticket and reducing time to recovery.

## Enhanced Productivity and Efficiency

The Power11 scale-out servers are engineered to maximize IT efficiency and output:

- /SM590000 Autonomous IT Operations: With built-in automation and AI-driven management, the system reduces manual intervention and operational overhead.
- /SM590000 Integrated Monitoring and Management: Tools like HMC and PowerVC provide centralized control, enabling streamlined operations across hybrid environments.

## Accelerated Growth and Scalability

The Power11 scale-out servers support dynamic scaling and hybrid cloud integration to meet evolving business demands:

- /SM590000 IBM Power Virtual Server (PowerVS): Immediate availability of Power11 in IBM Cloud enables seamless extension of workloads to the cloud, maintaining consistent performance, security, and OS compatibility.
- /SM590000 Hybrid Cloud Agility: Enterprises can scale resources on demand, accelerate development and testing, and optimize costs through a consumption-based model.
- /SM590000 AI Acceleration with MMA: Power11 processor cores feature Matrix Multiply Assist (MMA) - a hardware acceleration unit optimized for AI and machine learning workloads. By executing matrix operations directly on-chip, MMA reduces latency and boosts throughput, making the Power11 scale-out servers ideal for deep learning inference and training tasks.

## Technical enhancements

Along with the benefits listed above, Power11 processor-based servers provide enhanced performance benefits from higher core frequencies, additional cores per server and improved memory bandwidth with reduced memory latency. Table 1-2 shows some of the benefits that these improvements can bring to your enterprise.

Table 1-2   Power11 performance benefits

| Improvement                                                                     | Benefit                                                                                                                    |
|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Up to 15-25% core performance increase with both HW and SW planned improvements | Exceed SLAs for response times and batch windows.                                                                          |
| 30-45% system performance increase with the new larger 30-Core Power11 DCMs     | Ensure that increasing business workload demands can continue to be met with improved system performance.                  |
| Memorytechnologyimprovementswithupto 50% higher data rates                      | Enhance performance and system scalability for memory intensive workloads by optimizing both memory bandwidth and latency. |

## 1.3.1  New Power11 server portfolio

The new Power11 server portfolio consists of the following offerings, providing clients the choices designed to meet their specific business requirements.

## High-End: IBM Power E1180

At the top of the portfolio is the IBM Power E1180, a high-end enterprise server built for the most demanding workloads. It delivers exceptional performance, scalability, and resiliency, making it ideal for large-scale ERP systems, core banking, and high-throughput analytics. With support for massive memory footprints, advanced RAS features, and robust virtualization capabilities, the Power E1180 is engineered for continuous availability and extreme workload consolidation.

## Midrange: IBM Power E1150

The Power E1150 serves as the midrange workhorse of the Power11 family. It brings many of the high-end capabilities of the Power E1180 - such as spare core technology, pervasive memory encryption, and quantum-safe security - into a more compact and cost-effective form factor. The Power E1150 is ideal for organizations seeking a balance between performance, scalability, and operational efficiency, especially in hybrid cloud environments.

## Entry-Level scale-out: IBM Power S1124 and S1122

For smaller enterprises or distributed environments, IBM offers the Power S1124/L1124 and Power S1122/L1122 servers. These entry-level, scale-out systems are optimized for cost-effective deployment of AIX, IBM i, and Linux workloads. The L1122 and L1124 are targeted at the Linux marketplace, but they do support up to 25% of their activated cores for AIX or IBM i workloads. They are well-suited for departmental applications, edge computing, and cloud-native workloads. Despite their compact size, these systems benefit from the same Power11 processor technology, ensuring consistent performance and security across the portfolio.

Figure 1-4 shows the new Power11 server portfolio.

Figure 1-4   Power11 portfolio

<!-- image -->

## Architectural technology Improvements

The Power11 portfolio introduces significant innovations across both the product lineup and the underlying core technologies, all aimed at delivering enhanced performance and greater value. One of the most notable advancements lies in the processor and memory architecture, where Power11 brings substantial improvements over the previous Power10 generation. These enhancements form the foundation for the next level of scalability, efficiency, and intelligent workload optimization.

## Increased core counts and spare cores

Improved thermal dissipation solutions assist in providing optimal cooling, supporting higher core densities and sustained performance.

## Increased processor frequencies

Integrated Stacked Capacitor technology improves power delivery and stability at the silicon level, enabling higher performance under sustained workloads. Refined algorithms dynamically adjust processor frequency based on workload characteristics, maximizing performance while maintaining energy efficiency.

## Increased memory frequencies

The IBM Power11 architecture introduces higher memory frequencies and increased memory bandwidth, resulting in substantial improvements in overall system performance. By supporting faster memory speeds and optimizing the memory subsystem, Power11 significantly boosts memory throughput while simultaneously reducing latency. These enhancements provide quicker data access and processing, which is especially critical for memory-intensive workloads such as real-time analytics, large-scale databases, and AI applications. The combination of higher bandwidth and lower latency enables smoother performance, better responsiveness, and more efficient use of compute resources across the entire system.

Table 1-3 provides a listing of the portfolio with a comparison to the Power10 offerings.

Table 1-3   Portfolio overview

| Segment          | Models          | Footprint Capacity                                                                                                         | Power10 Compare                                                                                                                    |
|------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| High-End (4S+):  | IBM Power E1180 | /SM590000 4 nodes (CEC) each 5U with 4 processor modules each /SM590000 Up to 64 TB - DDR5 based memory                    | Same memory capacity Introducing Resource Groups to maximize system utilization In-place upgrades                                  |
| Mid-Range (4S4U) | IBM Power E1150 | /SM590000 2-4 processors in a 4U form factor /SM590000 Up to 30 cores per module /SM590000 Up to 16 TB - DDR5 based memory | core capacity Same memory capacity Introducing Resource Groups to maximize system utilization In-place upgrades with serial number |

| Segment        | Models                          | Footprint Capacity                                                                                                                                                                                                              | Power10 Compare                                                                                                                      |
|----------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Scale-Out 2S4U | IBM Power S1124 IBM Power L1124 | /SM590000 Up to 2 processors in a 4U form factor /SM590000 Up to 30 cores per module /SM590000 Up to 8 TB - DDR5 based memory                                                                                                   | /SM590000 Up to 25% more core capacity and same memory capacity /SM590000 Introducing Resource Groups to maximize system utilization |
| Scale-Out 2S2U | IBM Power S1122 IBM Power L1122 | /SM590000 Integrating the eSCM modules into the S1122 family - four or 10 processors per eSCM /SM590000 Up to 30 cores per dual core module /SM590000 2 processors in a 2U form factor /SM590000 Up to 4 TB - DDR5 based memory | /SM590000 Up to 50% more core capacity /SM590000 Same memory /SM590000 Introducing Resource Groups to maximize system utilization    |

## Investment protection

IBM Power11 systems are designed with strong investment protection in mind, ensuring that customers can evolve their infrastructure without sacrificing prior investments. A key example of this is the ability to perform same serial number upgrades from the IBM Power E1080 to the new Power E1180 and from the Power E1050 to the Power E1150. This upgrade path allows organizations to retain their existing system identity, simplifying software licensing, asset tracking, and operational continuity.

As part of this upgrade process, customers can migrate existing memory modules and I/O adapters from their existing systems, preserving valuable hardware investments. This compatibility reduces the cost and complexity of transitioning to the latest technology, while still gaining the performance, scalability, and security benefits of the Power11 architecture.

Additionally, IBM supports Power Enterprise Pools (PEP) that include both Power10 scale-out servers and Power11scale-out servers. This mixed-system support enables organizations to gradually migrate workloads from older to newer systems within the same resource pool. It allows for dynamic sharing of processor and memory activations across both generations, providing flexibility in capacity planning and workload placement. This approach not only protects existing investments but also enables a smooth, non-disruptive path to modernization.

## Portfolio simplification

One of the most notable changes in the Power11 generation is the streamlining of the scale-out server lineup. IBM has reduced the number of scale-out models, simplifying customer choices and reducing complexity in deployment and support. This focused approach makes it easier for organizations to select the right system for their needs while still benefiting from the full-stack integration and innovation that IBM Power is known for.

Figure 1-5 shows how customers can migrate from their existing Power9 or Power10 servers to the new Power11 portfolio.

Figure 1-5   Migration path Power9 to Power11

<!-- image -->

## 1.4  Power11: Trusted, autonomous, and modern

Our vision for Power is autonomous IT, where Power11 processor-based servers can think, heal and scale on their own. This in turn supports business agility so that enterprises can respond more quickly to market changes and customer demands, rapidly deploy new services, and reduce the time to market for new products.

We are working towards this vision by building automation into the platform, and combining that automation with AI-infused workflows.

This automation spans the day-0 to day-2 IT lifecycle for Power11 processor-based servers and includes capabilities such as Infrastructure as Code with Terraform, Application Configuration Management with Red Hat Ansible and enhancements to existing platform tools such as the Hardware Management Console and Cloud Management Console. On the AI side we are building AI infused workflows with IBM watson.x and new tools like IBM Concertfi.

This section provides insights into some of the technologies and solutions that make Power11 a trusted, autonomous, and modern platform to support your business requirements.

## 1.4.1  Building a trusted infrastructure with Quantum Safe Encryption

Infrastructure built using IBM Power processor-based servers benefits from the robust security technologies integrated into both the hardware and software stacks. Power processor-based servers offer advanced security features at every level of the system, ensuring comprehensive protection for sensitive data and applications. These features include advanced encryption technologies, secure boot capabilities, and integrated firmware updates. Additionally, Power processor-based servers leverage IBM's extensive expertise in securing mission-critical workloads, making them a popular choice for organizations seeking a secure environment for their digital assets.

Workloads on Power11 processor-based servers see significant benefits from improved cryptographic accelerator performance compared to previous generations. Specifically, the Power11 chip supports accelerated cryptographic algorithms such as AES, SHA2, and SHA3, resulting in considerably higher per-core performance for these algorithms. This enhancement allows features like AIX Logical Volume Encryption to operate with minimal impact on system performance.

The processor-core technology of Power11 incorporates integrated security protections aimed at:

- /SM590000 Improved Cryptographic Performance
- Integrated cryptographic support reduces the performance impact of encrypting and decrypting your data, allowing you to make encryption pervasive to protect all your critical data.
- /SM590000 Increased Application Security:
- Hardened defenses against return-oriented programming (ROP) attacks.
- /SM590000 Simplified Hybrid Cloud Security
- Easy-to-use, setup-free hybrid cloud security administration with a single interface.
- /SM590000 Enhanced Virtual Machine Isolation
- Providing the industry's most secure virtual machine isolation technology, this technology defends against attacks that exploit operating system or application vulnerabilities in the virtual machine to access other virtual machines or the host system.

## Encryption technologies and their applications

Power11 emphasizes comprehensive security throughout its design, offering multiple encryption options. Key among these is Transparent Memory Encryption (TME), Fully Homomorphic Encryption (FHE), and Quantum-Safe Encryption (QSE).

## Transparent Memory Encryption

Transparent Memory Encryption (TME) encrypts data in memory to protect it from unauthorized access and tampering during runtime. Operating at the hardware level, TME utilizes the Power11 processor's cryptographic engines to perform encryption and decryption tasks efficiently. TME ensures pervasive protection of data in memory with minimal impact on system performance, as encryption and decryption are managed at the chip level. Its integration into normal operations is seamless and automatic.

## Fully Homomorphic Encryption

Fully Homomorphic Encryption (FHE) allows computations to be performed directly on encrypted data without decrypting it first. This ensures that sensitive data remains confidential even during processing. FHE operates at the software level and involves sophisticated mathematical algorithms to enable computations on ciphertexts.

Implementing FHE requires specialized libraries and frameworks. However, FHE is computationally intensive and can introduce performance overhead compared to conventional hardware-only encryption methods due to the complexity of the algorithms.

## Quantum-Safe Encryption

Quantum-Safe Encryption (QSE) is designed to be resistant to quantum attacks, securing data against the computational capabilities of future quantum computers that could potentially break current cryptographic algorithms. QSE employs cryptographic algorithms believed to be resistant to quantum attacks, such as lattice-based, hash-based, and multivariate-quadratic-equation-based cryptography.

Many quantum-safe algorithms are still undergoing testing and standardization to ensure they provide robust security in the face of future quantum advancements. QSE is typically used for securing long-term data, sensitive communications, and critical infrastructure.

The relevant features and differences in these technologies is shown in Table 1-4

Table 1-4   Key Differences

| Feature              | TME                                                                                                            | FHE                                                                             | QSE                                                                                                                              |
|----------------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Encryption Scope     | Secures data in memory                                                                                         | Allows computations on encrypted data                                           | Prevents against future quantum computing threats                                                                                |
| Implementation Level | Implemented in hardware                                                                                        | Implemented using a combination of hardware and software                        | Implemented using a combination of hardware and software                                                                         |
| Performance Impact   | Hardware accelerated through the Power11 cryptographic engines and designed to have minimal performance impact | Involves substantial computational overhead                                     | The impact of QSE varies; some quantum-safe algorithms may introduce performance overhead; this is a subject of ongoing research |
| Use Cases            | Used to protect data in memory                                                                                 | Used for performing secure computations on sensitive data without decrypting it | Provide long-term data protection and secure communications in the future                                                        |

## Quantum Safe compliance

Quantum-Safe Encryption, also known as Post-Quantum Cryptography (PQC), refers to encryption methods that are secure against both classical and quantum computers. As quantum computers advance, they may pose a threat to existing cryptographic systems, potentially compromising their security. Quantum-Safe Encryption (QSE) is essential for protecting sensitive data, communication channels, and user identities in the age of quantum computing.

The urgency of adopting QSE stems from two primary concerns.

- -Advanced quantum computers could allow adversaries to intercept and decrypt protected digital communications through Harvest Now, Decrypt Later (HNDL) strategies, even before reaching Q-Day. Q-Day is the anticipated point in time when quantum supremacy becomes widespread and many of the current encryption algorithms are no longer effective.

- -Transitioning to QSE might require over a decade due to the complexities of organizational structures and IT infrastructure.

Consequently, organizations should start evaluating and implementing QSE solutions immediately to ensure continued protection and maintain trust among their stakeholders.

Delaying QSE adoption could have severe consequences. Legacy cryptographic systems left unaltered could be compromised in the event of a successful quantum attack, exposing sensitive data and risking confidential business transactions and individual privacy. Financial institutions, critical infrastructure providers, and government agencies would face significant challenges in maintaining operational integrity and confidentiality. Therefore, prioritizing QSE implementation is crucial for long-term cybersecurity resilience.

Power11 is designed to support these quantum-safe algorithms, ensuring robust security even as quantum computing advances. Power11's support of Quantum-Safe features provide the following.

- /SM590000 Data Encryption Breakage Protection
- -Risk: Quantum computers could break widely used cryptographic algorithms such as RSA, ECC (Elliptic Curve Cryptography), and traditional Diffie-Hellman key exchange protocols. Shor's algorithm, for instance, could efficiently factor large integers and solve discrete logarithms, compromising the security of these algorithms.
- -Protection: Power11 is capable of supporting quantum-safe algorithms like lattice-based, zash-based, code-based, and multivariate quadratic equations-based cryptography, which are believed to be resistant to quantum attacks. The crypto engines in Power11 enhance the performance of these algorithms, ensuring secure encryption and key exchange processes with minimal performance degradation.
- /SM590000 Secure Communications
- -Risk: Quantum computers could intercept and decrypt secure communications, undermining protocols that currently rely on classical encryption methods.
- -Protection: Power11 secures communication channels with quantum-resistant protocols, ensuring data confidentiality even in the presence of quantum adversaries. End-to-end encryption is maintained throughout the data lifecycle, from storage to transmission, using algorithms resistant to quantum attacks.
- /SM590000 Data Integrity and Authenticity
- -Risk: Quantum computers could forge digital signatures or tamper with data.
- -Protection: Power11 is capable of using quantum-safe digital signature algorithms such as XMSS (eXtended Merkle Signature Scheme) and UOV (Unbalanced Oil and Vinegar), providing strong security against quantum attacks.
- /SM590000 Long-Term Data Protection
- -Risk: Sensitive data stored today could be harvested and decrypted in the future as quantum computers become more powerful, threatening long-term confidentiality.
- -Protection: Implementing quantum-safe encryption methods ensures that data remains secure over time, even as quantum computing capabilities evolve. Power11's architecture supports updates to cryptographic libraries and protocols, enabling the adoption of new quantum-safe algorithms as they are developed and standardized.
- /SM590000 Physical and Memory Attack Protection
- -Risk: Physical attacks on memory, such as cold boot attacks, could expose sensitive data if not adequately protected.
- -Protection: Power11's Transparent Memory Encryption (TME) ensures that data in memory is encrypted, protecting it from physical attacks during runtime.

## Quantum-Safe Algorithms Supported by Power11:

The following quantum-safe algorithms are supported by Power11:

- /SM590000 Lattice-Based Cryptography
- -Algorithms: ML-DSA (Dilithium), ML-KEM(Kyber) and NTRUEncrypt.
- -Characteristics: Secure against quantum attacks. Based on lattice problems Learning With Errors (LWE), and Ring-Learning With Errors (Ring-LWE). Relatively efficient for hardware and software implementations.
- /SM590000 Hash-Based Cryptography
- -Algorithms: Merkle Signature Scheme (MSS), XMSS (eXtended Merkle Signature Scheme), and SPHINCS+.
- -Characteristics: Secure based on hash functions, though generally produces larger signatures and keys.
- /SM590000 Code-Based Cryptography
- -Algorithms: McEliece Cryptosystem, BIKE (Bit Flipping Key Encapsulation), and HQC (Hamming Quasi-Cyclic).
- -Characteristics: Quantum-resistant based on decoding random linear codes, though public keys can be large.
- /SM590000 Multivariate Quadratic Equations
- -Algorithms: Unbalanced Oil and Vinegar (UOV), Rainbow.
- -Characteristics: Secure against solving systems of multivariate quadratic equations, generally efficient in signature generation but may involve larger key sizes.

## Power11 Implementation

Power11 processors support these quantum-safe algorithms through:

- /SM590000 Crypto Engines: Multiple engines per core enable efficient execution of cryptographic operations.
- /SM590000 Software Updates: The architecture allows updates to cryptographic libraries, ensuring the integration of new quantum-safe algorithms as they become standardized.

Power11's design and capabilities ensure robust security against future quantum threats by leveraging hardware acceleration and flexible software updates, maintaining high-security standards as the cryptographic landscape evolves.

## Encryption enablement in hardware

There are two options for accelerating encryption in an IBM Power11 processor-based server.

The first option is to use the built in encryption acceleration built into the Power11 chip. In addition, IBM Power supports a PCIe based encryption accelerator.

## On-chip encryption support in Power11

The Power11 processor is designed to effectively support future encryption - including Fully Homomorphic Encryption (FHE) and Quantum-Safe Cryptography - in order to be ready for the Quantum age. The Power11 processor-chip instruction set architecture (ISA) is tailored for these solutions' software libraries, which are currently available or will soon be made available in the corresponding open source communities.

Workloads on Power11 benefit from cryptographic algorithm acceleration, enabling much higher per-core performance than Power10 processor-based servers for algorithms like Advanced Encryption Standard (AES), SHA2, and SHA3. Features like AIX Logical Volume Encryption can be activated with minimal performance overhead thanks to this performance enhancement.

With four times as many AES encryption engines, Power11 processor technology is designed to offer noticeably faster encryption performance. Power11 processor-based servers are more advanced than Power10 processor-based servers, with updates for the most stringent standards of today as well as future cryptographic standards including post-quantum and fully homomorphic encryption. It also introduces additional improvements to container security. Through the use of hardware features for a seamless user experience, transparent memory encryption aims to simplify encryption and support end-to-end security without compromising performance.

## 1.4.2  Protect, detect, and recover with Power Cyber Vault

Regulatory frameworks such as the U.S. Securities and Exchange Commission (SEC) cybersecurity disclosure rules and the Digital Operational Resilience Act (DORA) are no longer distant challenges-they are active requirements. More regulations are coming, each demanding higher levels of risk management and governance, mechanisms to promptly detect anomalous activities, and resilience practices to minimize the risk of data corruption or loss. The bar is rising, and the spotlight is now on every organization's security posture.

These frameworks go beyond checklists. They are signaling a shift: cybersecurity is no longer a compliance add-on, but a foundational element of operational continuity, customer trust, and business strategy.

## Traditional Siloed Security Solutions Can No Longer Keep Pace

Most organizations still operate with fragmented security architectures - collections of tools, processes, and teams that operate in silos. While some integration has occurred over time, loosely connecting security domains still leaves critical gaps in visibility, context, and response coordination.

A siloed approach results in:

- -Limited understanding of threats across domains (e.g., linking identity misuse with network anomalies).
- -Reactive security postures measured by containment speed-not business outcomes.
- -Barriers to collaboration and innovation, as teams struggle to securely share and access data.
- -Missed opportunities to embed privacy and security into customer-facing products and services.

Even more concerning, lack of contextual awareness across tools and data streams can open the door to full-blown compromises - like ransomware attacks that paralyze operations.

Security was never meant to be siloed. It became that way out of necessity and legacy architectures. But that model is no longer sufficient. Forward-looking enterprises are rethinking their cybersecurity strategy not just as a defense mechanism, but as a business enabler. They're integrating tools, processes, and insights across domains-from access and identity to threat detection, data governance, and compliance. They're moving from isolated defenses to connected intelligence.

## Zero Trust: A Strategic Shift, Not Just a Technology Play

Many organizations are now adopting Zero Trust frameworks as the foundation for their next-generation security programs. Built on the principles of least privilege access, continuous verification, and assumed breach, Zero Trust offers a compelling blueprint.

But the blueprint alone is not enough. Applying Zero Trust effectively requires:

- -A deep understanding of your business's risk surface.
- -Alignment with regulatory and operational requirements.
- -Integration with your existing cloud and hybrid infrastructure.
- -Cultural and organizational readiness to shift to continuous governance and access control.

In essence, Zero Trust is not a product. It is an operating model for security that aligns with the way modern businesses function-dynamically, digitally, and distributed.

## The Reality of Today's Threats: Evolving, Disruptive, Costly

Cyber attacks today are fast-moving, complex, and deeply disruptive. Here's the typical incident flow:

1. Service disruption is noticed.
2. Immediate shutdowns are initiated to contain spread.
3. Search for uncompromised backups begins.
4. Slow and costly recovery efforts start.

According to recent reports, 78% of organizations take over 100 days to fully recover from a major cyber incident. That's not just downtime - it is lost trust, revenue, and opportunity.

IBM provides a unified cyber resilient solution which includes IBM Power11 processor-based servers, IBM FlashSystems storage, advanced software, and services from IBM Technology Expert Labs services to respond to evolving cyber threats and regulatory standards with IBM Power Cyber Vault.

## IBM Power Cyber Vault

IBM Power Cyber Vault keeps the business running by combining different features:

- /SM590000 Power Cyber Vault Protected Data

Automated immutable images stored in the Power Cyber Vault to protect clients' snapshots and backups

- /SM590000 Continuous Threat Detection

Near real-time filesystem monitoring, FlashSystem inline detection, and recovery data scanning. Threat Detection Time as low as 60 Seconds.

- /SM590000 Rapid Clean Room Response

Automated response to attacks, creating Power Cyber Vault clean rooms for testing and validation. Accelerated Recovery Response.

- /SM590000 Cyber Vault Assisted Recovery

Automated multi-level testing and validation of Power Cyber Vault images to accelerate system recovery. Return to full operations in hours versus months.

## Power Cyber Vault Solution Components

IBM Power Cyber Vault is a complete Cyber Resilient Solution deployed in as little as 30 days. It is composed of various elements:

- /SM590000 IBM Power11 processor based servers
- IBM Power11 processor based servers provide:
- -Industry leading threat resistance
- -PowerSC for security and compliance tracking
- -Secure boot and memory encryption built in
- -Scalable and flexible architecture from entry to enterprise servers
- /SM590000 IBM FlashSystems Storage
- IBM FlashSystems provide:
- -Immutable Copies for Data Protection
- -Ransomware Detection for real-time threat detection
- -Flash-speed recovery for rapid restore of snapshot data
- -Storage Insights Pro for comprehensive reporting
- /SM590000 IBM Technology Expert Labs Power Cyber Vault Deployment
- IBM Technology Expert Labs provides:
- -Design Workshop for client specific requirements
- -Power Cyber Vault Deployment to customize and enable the unified Power Cyber Vault to meet client needs
- /SM590000 IBM Expertise Connect
- IBM Expertise Connect is:
- -Primary Technical Point of Contact for Power Cyber Vault
- -Dedicated to client and client success
- -Available after install to help guide client's directions

## Power Cyber Vault Implementation

The implementation of the solution consists of several phases, each designed to support risk mitigation and ensure the fastest possible recovery

1. Identify - Assess Risks and Design Mitigation Solutions
- a. IBM Securityfi and Resilience Assessment

This assessment provides:

- A view of the organization, processes, and strategies regarding operational and cyber resilience
- A list of prioritized recommendations to improve overall resilience
- b. IBM Cyber Vault Solution and Design Workshop

This workshop provides:

- Create detailed solution based on customer cyber resiliency goals, infrastructure, and required services
2. Protect - Safeguarded Cyber Vault Copies and Backups

Client specific scheduled creation and protection of immutable snapshots and backups to meet RPO and RTO requirements:

- -Snapshots: FlashSystems and Storage Defender CSM save protected system snapshot state into the Cyber Vault on a regularly scheduled basis.
- -Orchestration for crash consistency
- -Application specific customization available
3. Detect - Real-Time Threat Detection

Monitoring real-time threats and cyber attack vectors to respond quickly as threats emerge via Power SC Real Time Compliance orchestration:

- -Zero Trust Execution to detect, prevent, and report unapproved executables and applications from running on Power11 based-processor servers
- -FlashSystem's integrated Ransomware Threat Detection - alerts on active attacks and reports to PowerSC via Storage Insights Pro
- -SEIM Integration to accept alerts and threat reports from SEIM systems
4. Respond and Recover - Real Time Threat Response

Routinely, or when threats are detected, a response phase is triggered to audit and recover the system:

- -Upon receiving an integrity alert, IBM Power Cyber Vault automatically initiates the validation process by creating an immutable backup of the VM within seconds and spinning up a copy of that VM in the clean room within minutes.
- -Various types of Integrity Checks are run in the clean room (including platform specific tests)
- -Power Cyber Vault reports corrupted copies, and the newest clean copies are found
- -When approved by administrator, recovery to production will commence to recover and help meet RPO and RTO requirements

## 1.4.3  Quantum-safe compliance with one-click inventory discovery

IBM PowerSC is a comprehensive security and compliance solution designed specifically for virtualized environments running on IBM Power based-processor servers with AIX, Linux, and IBM i. It integrates deeply with the Power platform to provide end-to-end protection through features such as Security and Compliance Automation, Trusted Boot, Trusted Firewall, and Trusted Logging.

PowerSC helps organizations meet stringent regulatory standards like PCI DSS, HIPAA, and SOX by automating the monitoring, auditing, and enforcement of security policies. It also includes advanced capabilities like multi-factor authentication, intrusion detection, and patch management. With tools like PowerSC Trusted Surveyor, it ensures consistent network configuration and compliance across dynamic virtual environments, helping reduce administrative overhead while maintaining strong security postures

IBM is actively involved in the development and adoption of quantum-safe cryptographic standards, including working with NIST on their Post-Quantum Cryptography Standardization project. PowerSC supports a seamless transition to NIST's forthcoming standards.

IBM PowerSC offers capabilities to help verify and manage quantum-safe encryption.

The Quantum Safety Analysis feature analyzes the quantum-safe status of your VMs to identify areas of concern, to ensure compliance with emerging quantum-safe cryptographic standards:

- /SM590000 PowerSC scans endpoints on your server to identify cryptographic artifacts and vulnerabilities related to quantum safety. These can also be scheduled.
- /SM590000 It creates an inventory of where different encryption algorithms are implemented on your system.
- /SM590000 The analysis estimates the strength of ciphers, certificates, and keys on your AIX endpoints and categorizes them as weak, strong, quantum safe, or unclassified. Note that PowerSC is a security and compliance management tool, not a cryptographic module validation tool.
- /SM590000 An Quantum Safety Analysis report in the PowerSC GUI lists the discovered cryptographic elements and their assessed strengths.

## 1.4.4  Zero planned downtime and end-to-end orchestration for maintenance events

Planned downtime remains one of the biggest challenges in IT operations - especially for critical infrastructure as Power11 is. IBM's approach is to deliver Autonomous IT by embedding extreme automation and AI-infused workflows directly into the platform. The result: a significant reduction in operational effort, minimized disruptions, and improved resilience.

Today's enterprise IT environments face increasing pressure to ensure infrastructure reliability and security without disrupting operations. Key challenges include:

- /SM590000 Operational Complexity: Maintaining firmware, I/O adapters, and Virtual I/O Servers (VIOS) is highly specialized and intricate.
- /SM590000 Service Interruptions: Routine maintenance often requires downtime, impacting application availability and business continuity.
- /SM590000 Security Risks: Delayed updates expose systems to vulnerabilities (CVEs), weakening compliance and increasing risk.
- /SM590000 Resource Drain: IT teams spend 20-40% of their time on maintenance tasks like patch evaluation, compatibility testing, and scheduling.
- /SM590000 High Downtime Costs: With downtime averaging $336,000 per hour, annual maintenance-related outages can exceed $2 million per system.

These issues force organizations into a difficult trade-off: stay current and risk downtime, or delay updates and increase exposure - an unsustainable model in today's always-on digital economy.

## What We Mean by 'Infrastructure'

In this context, infrastructure refers to the Power11 platform, encompassing firmware, I/O components, VIOS, and the operating system. To maintain performance and security, clients must:

- /SM590000 Apply patches and updates regularly
- /SM590000 Remain on supported versions
- /SM590000 Respond swiftly to security advisories
- /SM590000 Conduct preventive maintenance

However, these actions typically require planned downtime. The core dilemma: should businesses accept regular service interruptions to stay current, or defer updates and risk security and performance?

## IBM Power11: A Platform for Autonomous IT

IBM Power11 is designed to resolve this dilemma - enabling continuous business operations while keeping infrastructure secure, up-to-date, and high-performing. IBM Power11 introduces a transformative approach to infrastructure lifecycle management, purpose-built for Autonomous IT. The platform is designed to operate with minimal human intervention, leveraging embedded intelligence to monitor, diagnose, and remediate issues in real time. This enables infrastructure that is inherently resilient, adaptive, and capable of maintaining continuous service availability.

At the core of Power11 is the Automated Maintenance Framework, orchestrated by IBM Concert, an AI-driven engine that automates the full maintenance lifecycle. This includes:

- /SM590000 Unified update orchestration for system firmware, VIOS, and I/O adapters.
- /SM590000 Live Partition Mobility (LPM) to ensure uninterrupted application availability during updates.
- /SM590000 Pre-validation checks to confirm system readiness and compatibility.
- /SM590000 Flexible update sourcing from IBM repositories, SFTP, NFS, USB, or HMC-local filesystems.

Maintenance operations can be executed autonomously or manually via the Hardware Management Console (HMC), offering both automation and administrative control. This architecture transforms maintenance from a disruptive, manual process into a seamless, background operation.

## IBM Concert: AI-Powered Application Management for the Modern Enterprise

IBM Concert addresses the persistent challenge of siloed application data by harnessing the power of AI to deliver intelligent, prioritized recommendations. By streamlining issue identification and resolution, Concert significantly reduces Mean Time to Resolution (MTTR) for critical risk factors such as:

- /SM590000 Critical Vulnerability Exploits (CVEs)
- /SM590000 Certificate management issues
- /SM590000 Application compliance challenges

## What Sets IBM Concert Apart

Built on IBM watsonx, Concert uses advanced generative AI to analyze complex environments and deliver actionable insights.

- /SM590000 Data-Agnostic Integration

Designed to meet you where you are, Concert supports a wide range of data sources across networks, infrastructure, and application architectures.

- /SM590000 Hybrid Cloud by Design

Tailored for the realities of modern enterprise IT, Concert seamlessly supports hybrid cloud environments.

- /SM590000 AI-Infused Orchestration for Proactive Maintenance
- IBM Concert orchestrates maintenance operations through intelligent workflows and end-to-end automation, including:
- /SM590000 Inventory Risk Discovery

Automatically identifies assets and uncovers hidden risks across the environment.

- /SM590000
- Risk Analysis Remediation Planning
- Delivers prioritized, actionable plans to address vulnerabilities and compliance gaps.
- /SM590000 Automated Risk Resolution
- Enables triggering of automated actions to remediate issues, reducing manual effort and downtime.

Automation can be triggered directly from IBM Concert solution or from the HMC, ensuring flexibility and ease of use.

## Key Benefits of IBM Power11's Autonomous Maintenance

IBM Power11's integrated solution for Zero Planned Downtime (ZPD) delivers measurable benefits across operational, security, and financial dimensions:

- /SM590000 Business Continuity: Updates are applied without interrupting workloads, preserving uptime and service-level commitments.
- /SM590000 Operational Efficiency: Automation streamlines the maintenance lifecycle, reducing manual effort and administrative overhead.
- /SM590000 Risk Reduction: AI-driven orchestration ensures timely updates, minimizing exposure to vulnerabilities and compliance risks.
- /SM590000 Productivity Gains: IT staff benefit from a simplified, intelligent interface that reduces time-on-task from weeks to minutes.
- /SM590000 Cost Optimization: Eliminating downtime and manual labor significantly lowers the total cost of infrastructure operations.

Together, these capabilities position IBM Power11 as a foundational platform for secure, scalable, and self-managing enterprise IT infrastructure - aligned with the demands of modern digital transformation.

## The New Maintenance Model

From the IT administrator's perspective, maintenance is now part of a unified, intelligent flow:

- /SM590000 Inventory discovery risk detection
- /SM590000 Smart planning
- /SM590000 Automated download application of updates
- /SM590000 Validation
- /SM590000 VM evacuation and reintegration

This approach minimizes disruptions, ensures SLA compliance, and allows faster more frequent maintenance. Systems stay secure, stable, and aligned with evolving requirements without downtime or performance impact.

Power11's built-in Automated Maintenance Tool enables platform maintenance without application impact. This automation can be triggered via IBM Concert's orchestration, or it can be human-triggered from the Hardware Management Console (HMC), completely independent of IBM Concert.

The Automated Maintenance Tool includes:

- /SM590000 Ability to update System FW, VIOS and IO adapter from a single update flow
- -Supported for both concurrent and disruptive updates
- /SM590000 Validation for LPM and VIOS redundancy (VIOS maintenance readiness check)
- /SM590000 Ability to automatically migrate partitions and return as part of the update process
- -Option to choose to return to the source or leave on the target system
- -Option to evacuate all LPARs / choose a subset of LPARs and order of LPARs
- -Option to choose order of updates
- /SM590000 Option to either download only or download update

Different sources of updates

- -IBM Website (preferred and recommended for end-to-end automation)
- -SFTP Server
- -HMC filesystem
- -NFS Server
- -USB

The new tool appears as a Licensed Capability of the server as shown in Figure 1-6.

Figure 1-6   Power System Licensed Capabilities

<!-- image -->

For more details on using the new tool see section 5.1.7, 'Using the Automated Maintenance tool' on page 119.

## 1.4.5  Automated data collection for faster error resolution

Enterprises are increasingly adopting hybrid cloud environments, with 82% reporting usage as of 2024 (IBM Cloud Survey). This shift introduces significant operational complexity, particularly in managing infrastructure and resolving issues. Manual error resolution continues to overwhelm IT teams, with 60% of organizations citing insufficient staffing for

incident management. Moreover, the financial impact of downtime is escalating-over 90% of mid-size and large enterprises report that a single hour of downtime now exceeds $300,000 in cost.

To address these challenges, IBM has introduced enhanced support capabilities in the Power11 Hardware Management Console (HMC). This includes a streamlined case creation process and automated log collection via Call Home. Administrators can now initiate support cases directly from the HMC, with relevant FFDC (First Failure Data Capture) logs automatically gathered and transmitted to IBM Support.

## Use Case: Automated Support Workflow

Consider Louis, a system administrator at a large insurance company running critical backend applications on IBM Power infrastructure. During a routine maintenance task involving live partition mobility, Louis encounters a migration validation error. Previously, resolving such issues required manually opening a support case, coordinating with IBM Support, and collecting FFDC data-a process that could take 5 to 8 hours before investigation could begin.

With Power11, Louis can now open a support case directly from the HMC. The system automatically collects and submits the necessary diagnostic data, eliminating manual steps and reducing turnaround time. IBM Support leverages AI-enhanced diagnostic tools trained on Power processor-based servers to accelerate root cause analysis and resolution.

## Benefits of the Enhanced Support Model

Implementing this new automated data collection capability in conjunction with applied AI workflows in IBM Support results in:

- /SM590000 Reduced Time to Resolution: Automated log collection and AI-assisted diagnostics accelerate issue resolution.
- /SM590000 Improved Productivity: System administrators save hours by avoiding manual data gathering and coordination.
- /SM590000 Lower Operational Risk: Faster resolution minimizes downtime and its associated business impact.
- /SM590000 Enhanced Support Experience: A simplified, integrated workflow improves responsiveness and reduces stress for IT teams.

## 1.4.6  Smart energy scheduling options with increased efficiency reduced energy consumption

In recent years, sustainability has become a central strategic priority in the IT industry due to regulatory pressure and business value. Over the past five years, there has been an 800% increase in climate commitments among companies, indicating broader awareness and the realization that sustainable practices can enhance profitability. Currently, 83% of organizations are investing in RD for low-carbon products and services, and products with sustainability attributes are achieving revenue growth rates over 25% higher than traditional ones.

Although 95% of companies have established operational sustainability goals, only 41% have achieved measurable progress. Many companies are facing challenges in starting the implementation process. This indicates a need for more explicit guidance, enhanced governance frameworks, and improved integration of sustainability metrics into core business operations.

Power processor-based servers have consistently improved energy efficiency per watt with each generation, and Power11 continues this trend. Power11 enhances efficiency, cutting energy use, carbon emissions, and the datacenter's energy footprint.

IBM Power9 clients upgrading to Power11 can reduce energy consumption by up to 60% for the same performance. Power11 outperforms x86 systems, providing twice the performance per watt. Compared to Power10, Power11 offers up to 33% better performance per watt, with the S1122 showing the largest gain.

Figure 1-7 illustrates natural IT efficiency improvements from Power9 to Power11, offering up to a 3:1 consolidation ratio, reducing energy use and carbon emissions by approximately 60%, and cutting datacenter footprint by two-thirds.

Figure 1-7   Power9 to Power11 energy consumption reduction

<!-- image -->

Along with the base energy savings delivered with Power11, there are some exciting new features that are introduced to address some of the other feedback received from clients.

## Partition level monitoring

In mid-2024, a new monitoring and reporting capability was introduced through HMC to track energy usage, carbon emissions, and other environmental factors. Power11 enhances this capability by providing insights at the partition level as shown in Figure 1-8 on page 27.

Figure 1-8   Partition level monitoring

<!-- image -->

## Energy Efficient Mode

Power11 has introduced a new Energy Efficient mode that, when enabled, can reduce energy consumption by up to 30%, with only an approximate 10% reduction in performance. This impact will vary depending on the system and configuration. The power mode can be dynamically established through the HMC GUI, as illustrated in Figure 1-9.

Figure 1-9   Power modes

<!-- image -->

In the environmental dashboard, it is observed that in maximum performance mode, energy consumption remains almost constant even when core usage decreases.

Figure 1-10 shows the energy usage when the processor is set to maximum performance.

Figure 1-10   Energy consumption in max performance mode

<!-- image -->

Switching to energy efficiency mode, which is implemented instantaneously, results in only a 10% reduction in performance, while significantly decreasing energy consumption by up to 30%, as illustrated in Figure 1-11.

Figure 1-11   Energy efficient mode

<!-- image -->

## Power Mode Scheduling

If there is a pattern in system use, the new scheduling power mode feature can be utilized. This enables the system to activate Energy Efficient mode during designated times. As illustrated in Figure 1-12 on page 29, the Energy Efficient mode will be engaged over the weekend, starting from 8:00 PM on Friday until 5:00 AM on Monday.

Figure 1-12   Power mode scheduling

<!-- image -->

The new environmental dashboard enables energy savings whenever potential opportunities arise. The automated scheduling capabilities allow the system to transition into and out of various modes efficiently and appropriately.

## 1.4.7  Superior performance of up to 25% improvement for consolidation of Oracle 19c Workloads

At the time of writing, Oracle Database 19c is the latest long term release and version 19.12 is the latest Release Update for the AIX operating system. Oracle Database 19c includes many features over its previous database versions. Oracle Database versions for IBM AIX are upward compatible with the higher versions of AIX Technology Levels (TL) within the same major version. For certification information of Oracle Database with IBM AIX, refer My Oracle Support portal: https://support.oracle.com/ in the 'Certification' section.

Starting with Oracle Database 11g Release 2 (11.2.0.4), Oracle Database Instant Client is supported on Linux on Power (32-Bit and 64-Bit). The Instant Client version of the Oracle Database is also supported on the 19c version of the database. With Oracle Database 12c Release 1, support for little-endian was introduced for the Instant Client running on Linux on Power and with 12c Release 2 support is for little-endian only.

Oracle Database Instant Client is a light version of Oracle Database Client Binaries. Oracle Database Instant Client is available on Linux on IBM Power to allow an application deployed on Linux on Power to connect to the Oracle Database no matter what platform the database is deployed on (AIX/Power or any other platform).

Although servers based on IBM Power8fi processor technology have reached end of support, many customers have yet to benefit from a technology refresh. IBM has already demonstrated and published that migrating Oracle Database workloads from a server with IBM Power8 processors to one with IBM Power11 processors can halve the processor core requirements. The reduction in cores enables a potential reduction in Total Cost of Ownership (TCO), as it may be possible to reduce the number of required licenses. The IBM Power11 processor introduces significant performance advancements, enabling up to 25% improvement in the consolidation of Oracle Database 19c workloads compared to the previous IBM Power10 processor generation. This performance gain allows organizations to

further optimize infrastructure efficiency, reduce software licensing costs through better core utilization, and improve overall system throughput, all while having the best level of enterprise-grade reliability, availability, and serviceability (RAS) features.

Oracle is committed to release their latest products on IBM Power, to see the Oracle statement about support for 23ai on IBM Power see https://community.ibm.com/community/user/blogs/doug-bloom/2024/05/29/whats-the-lat est-with-oracle-db-23ai-and-poweraix.

## 1.4.8  Day 1 availability of Power11 in PowerVS with Hybrid Billing

As hybrid cloud adoption reaches 82% among enterprises and the number of applications is projected to surpass 1 billion by 2028, organizations are under pressure to manage growing complexities, skill shortages, and escalating infrastructure costs. IBM Power11, in combination with IBM Power Virtual Server (PowerVS), offers a compelling solution to these challenges by delivering a secure, scalable, and high-performance hybrid cloud platform purpose-built for mission-critical workloads.

A key differentiator is the day-one availability of Power11 in both public and private PowerVS environments. This immediate access allows enterprises to deploy virtual servers for development, testing, production, and disaster recovery without delay. With provisioning times under 10 minutes, organizations can accelerate time-to-value and reduce migration risk through consistent architecture and user experience across on-premises and cloud environments.

Utilizing Power11 in PowerVS also unlocks advanced enterprise-grade security features. These include quantum-safe firmware signing, encrypted Live Partition Mobility (LPM), and a significantly lower number of hypervisor vulnerabilities (CVEs) compared to x86 alternatives. These capabilities are essential for organizations operating in regulated industries or managing sensitive data. Furthermore, PowerVS integrates natively with IBM watsonx services via Satellite™ Connector, enabling enterprises to seamlessly infuse AI into their workloads and accelerate digital transformation initiatives.

PowerVS now has three generations of Power available:

- /SM590000 Power9fi
- -Soft landing for Power9 clients coming to cloud
- Substantial support life remaining (through Oct. 2028)
- -Lowest cost
- Special pricing on existing capacity
- -Clients can continue to provision and use Power9

## /SM590000 Power10

- -Work horse for production applications such as SAP RISE
- -Broad capacity availability across data centers
- -Excellent price/performance for AIX and IBM i workloads
- -Clients can continue to provision and use Power10

## /SM590000 Power11

- -No need to wait to receive Power11 on premises. Gain immediate access to Power11 via PowerVS
- -Provision in &lt;10 minutes
- -Leverage for dev/test, application qualification
- -First cloud environment to provide Power11 both in IBM Cloud and on-premises (Private)

From a business value perspective, PowerVS delivers up to 25% faster SAP workload migration compared to x86 platforms, thanks to architectural consistency and superior compute performance. Flexible consumption models, shared processor pools, and tiered storage options help reduce total cost of ownership (TCO), while automated disaster recovery, secure backup, and non-disruptive maintenance enhance operational efficiency. The platform also supports regulatory compliance with standards such as SOC2, HIPAA, and PCI-DSS.

Common use cases include application modernization through access to over 250 IBM Cloud services, enhancing business resiliency with warm disaster recovery environments, optimizing data center operations by consolidating or exiting physical infrastructure, and supporting SAP transformation initiatives with unmatched availability and scalability for large-scale HANA deployments.

PowerVS is currently available in 22 IBM Cloud data centers globally for public cloud use and can also be deployed in dedicated private cloud environments at client sites to meet stringent regulatory or operational requirements. Power11 will initially be available in four global data centers and will be fully enabled for automated disaster recovery operations. This broad availability ensures that organizations can adopt Power11 in a way that aligns with their specific business goals and compliance mandates.

## 1.4.9  Off-chip AI acceleration with IBM Spyre

IBM's Spyre™ accelerator card is a low-power, high-efficiency hardware module designed to complement Power11 processor-based servers for AI inference, analytics, and memory-intensive workloads. This feature is planned to be supported on the Power11 scale-out servers in fourth quarter of 2025.

The card is a system on a chip architecture optimized for enterprise AI workloads, with 32 low-power AI cores, and supports multi-precision for inference training: FP16/8, INT8/4.

The card is enabled for foundation models and it is planned to support the Red Hat software stack (OCP AI). It will also support popular AI Frameworks and libraries (PyTorch, vLLM). Implemented in 5nm technology, the IBM Spyre card offers high performance and low-power characteristics with only 75W of power consumed.

Figure 1-13   Spyre card physical view

<!-- image -->

Since each IBM Spyre card operates at only 75 watts, it significantly reduces the power footprint compared to traditional GPU-based acceleration, which often exceeds 300 watts per device. IBM Spyre card is planned to be supported only inside the accelerator expansion drawer. Each accelerator expansion drawer supports a maximum of eight Spyre cards. Accelerator expansion drawer support on E1150 is as follows:

- /SM590000 At initial availability, a maximum of one accelerator expansion drawer will be supported on a Power11 processor-based server;
- /SM590000 Support for additional expansion drawers is planned in 2026.

Note: The Spyre card will require an updated fan-out card in the expansion drawer.

Unlike GPUs, which typically rely on high-bandwidth memory integrated on the card itself, the Spyre card is designed to access and leverage the system's main DDR5 memory modules. This enables the use of terabytes of high-performance memory available within the Power11 processor-based server. This architectural choice provides two main advantages:

- /SM590000 lower latency data access, thanks to the shared memory model;
- /SM590000 elimination of memory duplication, avoiding the need to copy data between host and device memory, as is common with discrete GPUs.

The use of system RAM not only simplifies software development and memory management but also contributes to a more energy-efficient and thermally balanced system architecture, an increasingly important factor in modern data centers and edge environments.

This design makes the Spyre card particularly well-suited for workloads that require frequent access to large memory spaces with minimal energy cost, such as real-time analytics, AI inferencing, and high-throughput data pre-processing.

Spyre card minimum supported levels of software stack for general availability and support on Power11 processor-based server in fourth quarter of 2025 are as follows:

- /SM590000 FW1110.10;
- /SM590000 HMC1111;
- /SM590000 RHEL 9.6;
- /SM590000 Spyre software stack container;
- /SM590000 OpenShift AI (Tech Preview 4Q 2025, GA 1Q 2026).

See Chapter 4, 'Artificial Intelligence Support' on page 103 for more detailed information about use cases and solutions with Spyre card.

## 1.4.10  Red Hat OpenShift with support for expanded software ecosystem

Red Hat OpenShift on Power provides a robust, enterprise-grade container platform that empowers financial institutions to modernize applications, deploy AI workloads, and integrate with a broad ecosystem of software. By running OpenShift on Power11 systems, organizations can take advantage of the platform's performance, scalability, and security while maintaining architectural consistency across hybrid cloud environments.

One of the key advantages of OpenShift on Power is its support for a significantly expanded software ecosystem. This includes IBM Cloud Paks such as Cloud Pak for Data and Cloud Pak for Integration, Red Hat Runtimes like Quarkus and Spring Boot, and a wide range of open-source AI/ML frameworks including PyTorch, TensorFlow, and ONNX. Additionally, many independent software vendor (ISV) applications are now certified for the Power architecture, allowing banks to run containerized workloads alongside traditional AIX or IBM i systems. This co-location reduces latency, improves data gravity, and simplifies integration.

OpenShift on IBM Power also supports seamless hybrid cloud integration, particularly when deployed on IBM Power Virtual Server (PowerVS). This enables access to IBM Cloud services such as IBM Cloud Object Storage, IBM Key Protect, IBM Event Streams (Kafka), and IBM API Connectfi. These capabilities are essential for hybrid architectures where AI models may be trained on-premises and deployed in the cloud, or vice versa, depending on data locality and compliance requirements.

For developers and IT architects, OpenShift on Power offers a rich set of tools and resources. The OpenShift Container Catalog provides pre-built images and Helm charts optimized for Power, while infrastructure-as-code templates using Terraform simplify cluster provisioning on PowerVS. IBM also supports the ecosystem with community channels, technical workshops, and IBM Garage™ engagements to accelerate adoption.

By combining the strengths of IBM Power hardware with the flexibility of OpenShift and the breadth of the container ecosystem, financial institutions can build and scale AI-driven applications with confidence, agility, and enterprise-grade resilience.

## 1.5  Introducing the Power11 processor

The Power11 processor is designed to deliver higher clock speeds and adds up to 25% more cores per processor chip than comparable IBM Power10 systems. The Power11 processor builds upon the key capabilities we delivered with Power10 including stronger reliability, availability, and serviceability (RAS) characteristics, better energy efficiency, improved energy management, and improved quantum-safe security.

Beyond the processor itself, we are introducing the following improvements to packaging, memory architecture and AI acceleration:

- /SM590000 Packaging Innovation

The Power11 processor will leverage new integrated stack capacitor (ISC) technology and advanced 2.5D packaging along with innovations in cooling such as improved heatsinks and more efficient fans to optimize energy delivery, improve thread and core strength and increase system capacity.

- /SM590000 Enhanced System Architecture:

The robust memory architecture for Power11 systems will be based on the recently released DDR5 DDIMMs and enhanced OMI interfaces which enable improved memory reliability, capacity, and bandwidth. Given that OMI is technology agnostic, the Power11 portfolio built on the Power11 processor will also support OMI DDR4 memory migrated from Power10 high-end systems, enabling clients to protect their investments in memory technology.

- /SM590000 AI Acceleration

We continue to support a range of emerging enterprise AI use cases with the MMA architecture. Improvements to Power11 processor core strength and system capacity will improve the performance of the MMA for inferencing workloads. Furthermore, IBM intends to incorporate the IBM Spyre accelerator into Power11 offerings to provide additional AI inferencing capabilities. Working together, IBM Power processors and the IBM Spyre accelerator will enable the next generation infrastructure to scale demanding AI workloads for businesses.

## New Power11 Processor Details

Here are some details on the new Power11 processor design.

## Technology and Packaging:

- -602mm2 7nm Samsung (18B Devices)
- -18-layer metal stack, enhanced device
- -Single-chip or Dual-chip sockets

## Computational Capabilities:

- -Up to 16 SMT8 Cores (2 MB L2 Cache / core)
- -Up to 128 MB L3 cache (low latency Non Uniform Cache Architecture management)
- -Enterprise performance focus:
- 3x core performance relative to POWER9
- 2x thread strength relative to POWER9
- 4x L2 cache, 4xMMU/ core relative to POWER9
- 4x crypto engine / core relative to POWER9
- -AI computational Focus:
- 2x general SIMD / core relative to POWER9
- 4x matrix SIMD / core relative to POWER9
- New AI Instructions and data types

## Robust Data Plane:

- -2 TB/s raw (32GT/s) PowerAXON + OMI signaling
- -SMP interconnect for up to 16 sockets
- -2x2 OMI memory bandwidth relative to POWER9
- -64 TB OMI DDR large system memory capacity
- -x64 PCIe Gen5 / DCM:2xbandwidth relative to POWER9

Figure 1-14 shows the Power11 processor.

Figure 1-14   POWER11 Processor Diagram

<!-- image -->

Each of the cores have a L1 cache with 64KB for Data cache + 96KB for Instruction cache.

## Comparing Power11, Power10, and POWER9 processors

Table 1-5 shows a comparison of Power11 to the previous generations.

Table 1-5 Comparison of the Power11 processor technology to prior processor generations

| Characteristics                                             | Power11                                                                                                             | Power10                                                                                                             | POWER9                                                                                            |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Technology                                                  | 7 nm                                                                                                                | 7 nm                                                                                                                | 14 nm                                                                                             |
| Die size                                                    | 654mm 2                                                                                                             | 602mm 2                                                                                                             | 693 mm 2                                                                                          |
| Processor module size                                       | 68.5 mmx 77.5 mm                                                                                                    | 68.5 mm x 77.5 mm                                                                                                   | 68.5 mm x 68.5 mm                                                                                 |
| Number of transistors                                       | 30 billion                                                                                                          | 18 billion                                                                                                          | 8 billion                                                                                         |
| Maximum cores                                               | 16                                                                                                                  | 15                                                                                                                  | 12                                                                                                |
| Maximum hardware threads per core                           | 8                                                                                                                   | 8                                                                                                                   | 8                                                                                                 |
| Maximum static frequency / high performance frequency range | 3.8 - 4.4 GHz                                                                                                       | 3.75 - 4.15 GHZ                                                                                                     | 3.9 - 4.0 GHz                                                                                     |
| L2 Cache per core                                           | 2048 KB                                                                                                             | 2048 KB                                                                                                             | 512 KB                                                                                            |
| L3 Cache                                                    | 8 MB of L3 cache per core with each core having access to the full 128 MB of L3 cache, on-chip high-efficiency SRAM | 8 MB of L3 cache per core with each core having access to the full 120 MB of L3 cache, on-chip high-efficiency SRAM | 10 MBofL3cacheper core with each core having access to the full 120 MB of L3 cache, on-chip eDRAM |
| memory technology                                           | DDR5 and DDR4 a                                                                                                     | DDR4 and DDR5 b                                                                                                     | DDR4 and DDR3                                                                                     |
| I/O bus                                                     | PCIe Gen 5                                                                                                          | PCIe Gen 5                                                                                                          | PCIe Gen 4                                                                                        |

- a. DDR4 only as migration from Power10 during same serial number upgrade
- b. DDR5 support added after GA

## Chip packaging options

To provide flexibility and scalability, the Power11 chip is packaged in several ways. For the high end E1180, IBM utilizes a single chip module (SCM) which provides a single chip per socket and up to sixteen sockets per system. For the midrange E1150, the Power11 is packaged with two chips per socket in a Dual Chip Module (DCM) and supports up to four sockets per system, The DCM version is also used in the scale-out server line in the S1122 and S1124, with up to two sockets per system. There is a third packaging option, the entry Single Core Module (eSCM), which is used in the entry level processor features of the S1122 (the 4 core and the 10 core options). The eSCM is a modified DCM where the second core in the module does not have any processor capability and only adds I/O functionality.

## Dual Chip Module

The IBM Power E1150, Power S1122, and the Power S1122 utilize the advanced IBM Power11 processor architecture designated as a Dual Chip Module (DCM) design. This DCM configuration allows each socket to house two processor chips, significantly increasing core density and performance.

Figure 1-15 shows the DCM layout with two fully operational Power11 chips combined into a single socket.

Figure 1-15   Golden Dual Chip (Physical Diagram)

<!-- image -->

In the Power S1122 and the Power S1124, the DCM plays a central role in delivering scalable performance. This system is designed for midrange enterprise applications and benefits from the Power11 innovations, including the DCM's ability to support high memory bandwidth and PCIe Gen5 connectivity. The DCM enables the system to handle demanding workloads while maintaining a compact footprint, making it ideal for data centers with space and power constraints. The integration of Open Memory Interface (OMI) and Differential DIMMs (DDIMMs) further enhances memory performance and reliability, which is critical for mission-critical applications.

Both systems leverage the DCM to support IBM's broader goals of flexibility and efficiency in hybrid cloud environments. The DCM not only boosts raw performance but also supports advanced features like transparent memory encryption and dynamic resource allocation. These capabilities are essential for modern IT infrastructures that demand both security and adaptability. Whether deployed in traditional data centers or as part of a hybrid cloud strategy, the DCM-equipped Power S1122 and Power S1124 provide a solid foundation for scalable, secure, and high-performance computing

## Entry Single Chip Module

The eSCM is a special derivative of the DCM where all active compute cores run on the first chip and the second chip contributes only extra PCIe connectivity, essentially acting as a switch.

The entry level versions of the Power S1122 (the 4 core and the 10 core modules) utilize the eSCM and all other processor feature utilize the DCM format. All of the Power L1122, Power S1124 and Power L1124 processor modules utilize the DCM modules. This is shown in Table 1-6.

Table 1-6   Use of eSCM and DCM in the S1122 and L1122

| Feature Code 22A / 22H   | Processor Type   | Cores              | Frequency Range   | Supported Configurations   |
|--------------------------|------------------|--------------------|-------------------|----------------------------|
| EP3Y / EP4J              | DCM              | 30 cores + 2 spare | 2.4 to 3.95 GHz   | 60 cores                   |
| EP3H / EP4B              | DCM              | 24 cores + 2 spare | 2.65 to 4.15 GHz  | 48 cores                   |
| EP3X / EP4C              | DCM              | 16 cores + 2 spare | 3.00 to 4.2 GHz   | 32 cores                   |
| ERGQ / NA                | eSCM             | 10 cores           | 3.05 to 4.00 GHz  | 20 cores                   |
| ERGR / NA                | eSCM             | 4 cores            | 3.60 to 4.00Ghz   | 8 cores                    |

The main differences between the eSCM and the DCM structure include the following:

- /SM590000 All active cores are on chip-0 and no active cores are on chip-1.
- /SM590000 Chip-1 works with chip-0 as a switch to facilitate more I/O connections.
- /SM590000 All active OMI interfaces are on chip-0 and no active OMI interfaces on chip-1.

This is shown in Figure 1-16.

Figure 1-16   Entry single chip module logical diagram

<!-- image -->

The eSCM internal chip-to-chip connectivity, the SMP links across the eSCM in 2-socket configurations, and the PCIe Gen5 bus structure are identical to the Power11 DCM implementation.

As with the Power11 DCM, 36 X-bus lanes are used for two chip-to-chip connections. These eSCM internal connections are implemented by the interface ports OP2 and OP6 on chip-0 and OP1 and OP4 on chip-1:

- -2 × 9 OP2 lanes of chip-0 connect to 2 x 9 OP1 lanes of chip-1
- -2 × 9 OP6 lanes of chip-0 connect to 2 × 9 OP4 lanes of chip-1

The eSCM module internal chip-to-chip links exhibit the theoretical maximum full-duplex bandwidth of 256 GBps.

To connect the two eSCMs in the 2-socket eSCM configurations, the interface ports OP4 and OP7 on chip-0 and OP6 and OP7 on chip-1 of the processor module are active and used to implement direct chip-to-chip SMP connections between the two eSCM modules.

As with the DCM, the eSCM offers differential PCIe Gen 5 with a total of 64 lanes. Every chip of the eSCM contributes 32 PCIe Gen5 lanes, which are grouped in two PCIe host bridges (E0, E1) with 16 PCIe Gen5 lanes each:

- -E0, E1 on chip-0
- -E0, E1 on chip-1

As only I/O is supported on chip-0 in the eSCM, the maximum number of DDIMMs supported is 8 per socket for a maximum of 16 DDIMMs per system where for the DCM processor features, a maximum of 32 DDIMMs are available.

## 1.6  Operating system support

The Power11 processor-based Scale-Out servers support the following families of operating systems:

- /SM590000 AIX
- /SM590000 IBM i
- /SM590000 Linux
- /SM590000 Red Hat OpenShift

In addition, the Virtual I/O Server (VIOS) can be installed in special partitions that provide virtualization of I/O capabilities, such as network and storage connectivity. Multiple VIOS partitions can be installed to provide support and services to other partitions running AIX, IBM i, or Linux, such as virtualized devices and Live Partition Mobility capabilities.

For more information about the Operating System and other software that is available on Power, see IBM Power. The minimum supported levels of IBM AIX, IBM i, and Linux are described in the following sections.

IBM will make announcements about support by newer versions of the operating systems over time. It is highly recommended that you keep your operating systems up to date to enable new security capabilities and for support of new features.

## 1.6.1  AIX operating system

The Power S1122, and S1124 servers support the following minimum levels of the AIX operating system is described in this section.

## When using virtual I/O

The Power S1122, and S1124 servers support the following minimum levels of the AIX operating system when installed with virtual I/O:

- /SM590000 AIX Version 7.3 with Technology Level 7300-02 and Service Pack 7300-02-02-2420
- /SM590000 AIX Version 7.3 with Technology Level 7300-03 and Service Pack 7300-03-00-2446
- /SM590000 AIX Version 7.2 with Technology Level 7200-05 and Service Pack 7200-05-08-2420

## When using direct I/O connectivity

The Power S1122, and S1124 servers support the following minimum levels of the AIX operating system when installed by using direct I/O connectivity:

- /SM590000 AIX Version 7.3 with Technology Level 7300-02 and Service Pack 7300-02-04
- /SM590000 AIX Version 7.3 with Technology Level 7300-03 and Service Pack 7300-03-01
- /SM590000 AIX Version 7.3 with Technology Level 7300-04 and Service Pack 7300-04-00
- /SM590000 AIX Version 7.2 with Technology Level 7200-05 and Service Pack 7200-05-10

## Important:

- -AIX 7.2 instances can use physical and virtual I/O adapters, but must run in an LPAR in IBM POWER9 compatibility mode.
- -AIX 7.3 instances can use physical and virtual I/O adapters, and can run in an LPAR in native Power11 mode.

## 1.6.2  IBM i operating system

The Power S1122 and S1124 support the following minimum levels of the IBM i operating system both native and as a client of VIOS:

- /SM590000 IBM i - 7.4 TR12
- /SM590000 IBM i - 7.5 TR6
- /SM590000 IBM i - 7.6

Restriction: IBM i support is provided at a price-attractive P10 software tier even though the Power S1122 has two sockets. There are limitations to the maximum size of the partition, and all I/O must be virtualized through VIOS (VIOS is required, and IBM i partitions must be set to 'restricted I/O'). Up to four cores (real or virtual) per IBM i partition are supported. Multiple IBM i partitions can be created and run concurrently, and each individual partition can have up to four cores.

Native IBM i support is available on the IBM Power S1122 (MTM 9824-22A) only when populated with two 4-core processors (#ERGR) with a maximum of eight cores active. This configuration is available at a P10 IBM i software tier and will support IBM i natively, virtualized, or as a combination of both.

When configuring the S1122 (MTM 9824-22A) with two 4-core processors (feature #ERGR), Full IBM i native support is available. IBM i partitions with more than four cores may be used and VIOS is not required. When configuring these systems with any other processor feature the 4-core per partition limit is enforced. In addition:

- -Feature ERGR cannot be upgraded to any other processor feature.

## 1.6.4  VIOS

- -Two #ERGR 4-core processors configuration is IBM i P10 processor group/software tier. #ERGR processor is QPRCFEAT ERGR.
- -Systems with this configuration also need to include (#EEPS) - IBM i Enablement for 9824-22A with two #ERGR Processors.

## 1.6.3  Linux operating system

The Linux distributions that are listed here are fully supported on the Power S1122, and S1124 server models. Other distributions, including open source releases, can run on these servers, but do not include any formal Enterprise Grade support.

## Red Hat Enterprise Linux

The latest version of the Red Hat Enterprise Linux (RHEL) distribution from Red Hat is supported in native Power11 mode, which allows it to access all of the features of the Power11 processor and platform.

At announcement, the Power S1122, and S1124 servers support the following minimum levels of the Red Hat Enterprise Linux operating system:

- /SM590000 Red Hat Enterprise Linux 8.10 for Power LE, or later (Power10 compatibility)
- /SM590000 Red Hat Enterprise Linux 9.4 for Power LE, or later (Power10 compatibility)
- /SM590000 Red Hat Enterprise Linux 9.6 for Power LE, or later (Power11 native)

## Red Hat OpenShift Container Platform

The Red Hat OpenShift Container Platform is supported to run on IBM Power servers, including the Power11 processor-based scale-out server models.

Red Hat OpenShift Container Platform 4.18 will run in Power10 compatibility mode and Red Hat OpenShift 4.19 or later will run in Power11 native mode in the Power11 processor-based scale-out servers.

The Power S1122 and S1124 servers support the following minimum levels of the operating systems that are supported for Red Hat OpenShift Container Platform:

- /SM590000 Red Hat Enterprise Linux CoreOS 4.18 (Power10 compatibility)
- /SM590000 Red Hat Enterprise Linux CoreOS 4.19 (Power11 native)

## SUSE Linux Enterprise Server

The latest version of the SUSE Linux Enterprise Server distribution of Linux from SUSE is supported in native Power11 mode, which allows it to access all of the features of the Power11 processor and platform.

At announcement, the Power S1122 and S1124 servers support the following minimum levels of the SUSE Linux Enterprise Server operating system:

- /SM590000 SUSE Linux Enterprise Server 15 Service Pack 6, or later (Power11 native)

The minimum required level of VIOS for the Power11 scale-out servers is VIOS 4.1.1.10 when running in Power11 mode. The following levels are supported:

- /SM590000 VIOS 4.1.1.10 (Service Pack)
- /SM590000 VIOS 4.1.0.40 (Service Pack) (P10 compatibility mode)
- /SM590000 VIOS 3.1.4.60 (Service Pack) (P9 compatibility mode)

IBM regularly updates the VIOS code. For more information, see Fix Central.

## 1.7  Firmware and Hardware Management Console

The firmware on an IBM Power system is the foundational software layer that initializes hardware components, manages system resources, and provides the interface between the hardware and the operating system.

Known as the Power Firmware, it includes components like the Flexible Service Processor (FSP), PowerVM Hypervisor (PHYP), and system boot code. This firmware enables advanced features such as logical partitioning (LPARs), dynamic resource allocation, and secure boot processes. It also supports system diagnostics, error reporting, and remote management capabilities, especially when integrated with tools like the Hardware Management Console (HMC). Regular firmware updates from IBM ensure performance improvements, security patches, and compatibility with new hardware or software features.

An HMC is a dedicated appliance to configure and manage system resources on IBM Power. It can be delivered as a physical server or as a virtual appliance running in either Power VM or an x86 VM. A graphical user interface (GUI), a Command-line interface (CLI), or REST API interfaces are available.

## 1.7.1  HMC Requirements

The HMC provides basic virtualization management support for configuring logical partitions (LPARs). Most operations can be completed dynamically, including processor and memory settings.

The HMC also supports advanced service functions, including guided repair and verification, concurrent firmware updates for managed systems, and around-the-clock error reporting through IBM Electronic Service Agent (ESA) for faster support. The HMC management features help improve server usage, simplify systems management, and accelerate provisioning of server resources by using IBM PowerVM virtualization technology.

Supported HMCs for the Power11 server are'

- -7063-CR2
- -Virtual HMC running on a Power VM
- -Virtual HMC running on an x86 based VM

The minimum required HMC version for the Power scale-out servers is V11R1 M1110. V11R1 M1110 is supported on the 7063-CR2, and the Virtual HMC appliances only.

## Restriction:

- /SM590000 The 7063-CR1 and 7042 HMCs are not supported as an HMC for Power11 servers.
- /SM590000 The HMC code at V11R1M1110 cannot manage POWER8 or earlier processor-based systems.

## 1.8  Rack support

All of the currently available scale-out servers fit a standard 19-inch rack. The servers are certified and tested in the IBM Enterprise racks (7965-S42 and 7014-T42). Customers can

choose to place the server in other racks if they are confident that those racks have the strength, rigidity, depth, and hole pattern characteristics that are needed. Contact IBM Support to determine whether other racks are suitable.

Note: It is a best practice that Power11 processor-based scale-out servers be ordered with an IBM 42U enterprise rack #ECR0 (7965-S42). This rack provides a high-quality environment for IBM Manufacturing system assembly and testing, and provides a complete package.

If a system is installed in a rack or cabinet that is not from IBM, help ensure that the rack meets the requirements.

Important: The customer is responsible for helping ensure the installation of the drawer in the preferred rack or cabinet results in a configuration that is stable, serviceable, safe, and compatible with the drawer requirements for power, cooling, cable management, weight, and rail security.

## 1.8.1  New rack considerations

Consider the following points when racks are ordered:

- /SM590000 The new IBM Enterprise 42U Slim Rack 7965-S42 offers 42 EIA units (U) of space in a slim footprint.
- /SM590000 The 7014-T42 rack is no longer available to purchase with Power11 scale-out servers. Installing a Power11 scale-out server in this rack is still supported.

<!-- image -->

Chapter 2.

2

## Power11 Scale-out Servers

The IBM Power11 scale-out Servers introduce a powerful suite of capabilities built on IBM's hallmark strength: a fully integrated, end-to-end stack. From the POWER11 processor and system architecture to the firmware, operating systems, and cloud integration, IBM Power delivers innovation through deep synergy across every layer of the infrastructure. This holistic design is purpose-built to support autonomous IT operations, driving tangible business outcomes across three key pillars.

Business Continuity is at the core of the Power scale-out Servers, offering a resilient and dependable platform for mission-critical workloads. It minimizes risk exposure to threats and regulatory challenges, regardless of whether the deployment is on-premises, in the cloud, or hybrid. The system enhances productivity and efficiency by maximizing uptime and streamlining operations. This leads to reduced complexity and lower operational costs, helping organizations do more with less. The Power11 scale-out servers are designed for the future, enabling accelerated growth and scalability in the AI era. It supports the rapid deployment of diverse AI workloads and new applications, ensuring that mission-critical processes can scale securely and consistently.

This chapter contains the following topics:

- /SM590000 IBM Power11 scale-out servers
- /SM590000 IBM Power S1122 (9824-22A) Server Overview
- /SM590000 IBM Power S1124 (9824-42A) Server Overview
- /SM590000 Processor and Memory Activation on Power S1122 and S1124 Systems
- /SM590000 Environmental and Physical Specifications

## 2.1  IBM Power11 scale-out servers

IBM utilizes the Power11 chip in multiple form factors to meet the different client requirements. The IBM Power11 scale-out servers are optimized for horizontal scalability. These systems are ideal for distributed workloads, cloud-native applications, and environments where flexibility and cost-efficiency are key. They support up to two sockets and are designed to deliver high performance in compact form factors, making them suitable for businesses that need to scale incrementally or run multiple smaller workloads in parallel.

One of the standout features of the Power11 scale-out models is their support for PCIe Gen5, which significantly boosts data throughput and connectivity for high-speed adapters. Additionally, the servers utilize Open Memory Interface (OMI) technology with differential DIMM (DDIMM) memory cards, enhancing memory performance, resilience, and security. This includes transparent memory encryption, which is crucial for protecting sensitive data. The internal storage capabilities are equally impressive, with support for up to 240 TB of NVMe storage in a two-socket system, ensuring low-latency access to large datasets.

These servers are also optimized for hybrid cloud environments, offering flexible consumption-based pricing through IBM's Power Private Cloud with Shared Utility Capacity. This model allows businesses to scale resources dynamically based on workload demands, making it ideal for modern applications, including AI and containerized workloads on platforms like Red Hat OpenShift. Overall, IBM Power11 scale-out servers provide a future-ready infrastructure that balances performance, security, and cost-efficiency for enterprise IT needs.

## 2.1.1  Family overview

The Power11 scale-out server family consists of four new servers that come in two form factors:

- /SM590000 Two socket, 2U form factor servers (2S2U)
- In the 2S2U form factor IBM provides the S1122 model and the L1122. These two servers are very similar with the major differentiation that the L1122 is designed for the Linux market segment and at least 75% of the cores in the box must run Linux partitions. Up to 25% of activated cores can run AIX and IBM i.
- /SM590000 Two socket, 4U form factor servers (2S4U)
- In the 2S4U form factor IBM provides the S1124 model and the L1124. As in the L1122, the L1124 is designed for the Linux market segment and at least 75% of the cores in the box must run Linux partitions. Up to 25% of activated cores can run AIX and IBM i.

All of these servers are built on the advanced IBM Power11 processor architecture and take advantage of the performance benefits a large number of multithreading cores, high performance DDR5 memory and PCIe Gen5 adapter connectivity.

The machine types and model for the Power11 scale-out servers are listed in Table 2-1.

Table 2-1   Machine types and models of S1122, and S1124 server models

| Server name   | Machine type and model   |
|---------------|--------------------------|
| S1122         | 9824-22A                 |
| L1122         | 9856-22H                 |
| S1124         | 9824-42A                 |
| L1124         | 9856-42H                 |

## 2.2  IBM Power S1122 (9824-22A) Server Overview

The IBM Power S1122 system introduces a comprehensive array of advanced capabilities, fundamentally rooted in our core strength: an end-to-end, full-stack design. By meticulously integrating every layer of infrastructure - from the Power processor and systems to the firmware, operating systems, and ultimately the cloud - IBM Power has engineered unique and innovative solutions. This synergistic approach is centered on autonomous IT principles, consistently translating into tangible business outcomes across three core pillars.

Figure 2-1shows the Power S2122 from the front.

Figure 2-1   Front view of Power S1122

<!-- image -->

## 2.2.1  Processors

The Power11 processor is the compute engine for the next generation of Power11 processor-based scale-out servers and successor to the current Power10 processor. It offers superior performance on applications such as MMA facility to accelerate computation-intensive kernels, matrix multiplication, convolution, and discrete Fourier transform. To efficiently accelerate MMA operations, the Power11 processor core implements a dense math engine (DME) micro-architecture that effectively provides an accelerator for cognitive computing, machine learning, and AI inferencing workloads.

Two Power11 processors of the same type are allowed. The following defines the allowed quantities of processor modules:

- /SM590000 Two 4-core, typical 3.6--4.0 GHz (max), Power11 eSCM processor (#ERGR) are allowed.
- /SM590000 Two 10-core, typical 3.05--4.0 GHz (max), Power11 eSCM processor (#ERGQ) are allowed.
- /SM590000 Two 16-core, typical 3.0--4.2 GHz (max), Power11 DCM processor (#EBG8) are allowed.
- /SM590000 Two 24-core, typical 2.65--4.15 GHz (max), Power11 DCM processor (#EBG9) are allowed.
- /SM590000 Two 30-core, typical 2.4--3.95 GHz (max), Power11DCM processor (#EBGA) are allowed.

The Power S1122 offers enhanced Workload Optimized Frequency for optimum performance. This mode can dynamically optimize the processor frequency at any given time based on CPU utilization and operating environmental conditions. For a description of this feature and other power management options available for this server, see the IBM EnergyScale for Power10 Processor-Based Systems website.

## Processor Activations

Processors require an activation feature in order to be utilized. For details on the options available see section 2.3.7, 'Comparison between S1124 and S1024' on page 60.

## 2.2.2  Memory

The Power S1122 server uses the next-generation DDIMMs, which are high-performance, high-reliability, high-function memory cards that contain a buffer chip, intelligence, and 4000 MHz, or 4800 MHz DRAM memory. DDIMMs are placed in DDIMM slots in the server system.

A minimum of 32 GB of memory is required with one processor module. All Memory DIMMs must be ordered in pairs.

A minimum of 64 GB of memory is required with two processor modules. All Memory DIMMs must be ordered in quads.

Each DIMM feature code delivers two physical Memory DIMMs.

Plans for future memory upgrades should be taken into account when deciding which memory feature size to use at the time of initial system order.

For the best possible performance, it is generally recommended that memory be installed in all memory slots. IBM recommends populating all the DIMM slots, or the more as possible, mainly for OLAP and similar high bandwidth workloads.

To assist with the plugging rules, two DDIMMs are ordered using one memory feature number. Select from:

- /SM590000 64GB (2 x 32GB), (#EM54)
- /SM590000 128GB (2 x 64GB), (#EM5B)
- /SM590000 256GB (2 x 128GB), (#EM5G)

Note: DDR5 Memory DDIMMs requires FW1110.00, or later.

## 2.2.3  PCIe slots

The Power S1122 server has up to eight U.2 NVMe devices and up to ten PCIe hot-plug slots, providing excellent configuration flexibility and expandability. All of the PCIe slots and the NVMe devices are concurrently maintainable.

With both Power11 processor slots populated, ten PCIe slots are available:

- /SM590000 Four x16 Gen4 or x8 Gen5 half-height, half-length slots
- /SM590000 Four x8 Gen5 half-height, half-length slots (with x16 connectors)
- /SM590000 Two x8 Gen4 half-height, half-length slots (with x16 connectors)

The x16 slots can provide up to twice the bandwidth of x8 slots because they offer twice as many PCIe lanes. PCIe Gen5 slots can support up to twice the bandwidth of a PCIe Gen4 slot, and PCIe Gen4 slots can support up to twice the bandwidth of a PCIe Gen3 slot, assuming an equivalent number of PCIe lanes.

At least one PCIe Ethernet adapter is required on the server by IBM to ensure proper manufacture, test, and support of the server. One of the x8 PCIe slots is used for this required adapter.

These servers are smarter about energy efficiency when cooling the PCIe adapter environment. They sense which IBM PCIe adapters are installed in their PCIe slots and, if an adapter requires higher levels of cooling, they automatically speed up fans to increase airflow across the PCIe adapters. Note that faster fans increase the sound level of the server. Higher wattage PCIe adapters include the PCIe3 SAS adapters and SSD/flash PCIe adapters (#EJ10, #EJ14, and #EJ0J).

For more detail on the PCIe slots and the supported adapters see Chapter 3, 'I/O Subsystem' on page 67.

## 2.2.4  NVMe drives

Non-volatile memory express (NVMe) SSDs, in the 15-millimeter carrier U.2 2.5-inch form factor, are used for internal storage in the Power S1122 system. The Power S1122 supports up to 8 NVMe U.2 devices when two storage backplanes with four NVMe U.2 drive slots (#EJ1X) are ordered. Both 7-millimeter and 15-millimeter NVMe are supported in the 15-millimeter carrier.

For more detail on the supported NVMe drives, see Chapter 3, 'I/O Subsystem' on page 67.

## 2.2.5  I/O expansion drawers

To provide additional PCIe slots and additional NVMe capacity, the Power11 scale-out servers support I/O expansion drawers.

## NED24 NVMe Expansion Drawer

The NED24 NVMe Expansion Drawer (#ESR0) is a storage expansion enclosure with 24 U.2 NVMe bays. It supports up to 24 U.2 NVMe devices in 15 mm Gen3 carriers. The 15 mm carriers can accommodate either 7 mm or 15 mm NVME devices.

Each NED24 NVMe Expansion Drawer contains two redundant AC power supplies. The AC power supplies are part of the enclosure base.

The NED24 NVMe Expansion Drawer is connected to a Power server through dual CXP Converter adapters (#EJ24 or #EJ2A). A cable pair attaches the PCIe Cable Adapter (#EJ24) to the fanout module. Feature ECLS provides a pair of 3-meter copper cables, only copper cables are supported on the S1122. Two cables of identical length, or one feature, is required for each fanout module.

The following U.2 NVMe devices are supported in the NED24 NVMe Expansion Drawer:

- /SM590000 #ES5B - Enterprise 800GB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ES5A - Enterprise 800GB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES5C - Enterprise 1.6 TB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES5D - Enterprise 1.6 TB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ES5E - Enterprise 3.2 TB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES5F - Enterprise 3.2 TB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ES5G - Enterprise 6.4 TB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES5H - Enterprise 6.4 TB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ES4B - Enterprise 1.6 TB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES4C - Enterprise 1.6 TB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ES4D - Enterprise 3.2 TB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES4E - Enterprise 3.2 TB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ES4F - Enterprise 6.4 TB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES4G - Enterprise 6.4 TB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ECT9 - 15.3 TB Mainstream NVMe U.2 SSD 4k for AIX/Linux
- /SM590000 #ECTB - 15.3 TB Mainstream NVMe U.2 SSD 4k for IBM i

## PCIe Gen4 I/O Expansion Drawer

The PCIe Gen4 I/O Expansion Drawer (#ENZ0) is a 4U high, 19-inch wide, PCIe Gen4 based rack mountable I/O drawer that is available as a feature of Power11 Servers.

The PCIe Gen4 I/O Expansion Drawer (#ENZ0) replaces the PCIe Gen3 I/O Expansion Drawer (#EMX0). There is no upgrade path from PCIe Gen3 I/O Expansion Drawer (#EMX0) to PCIe Gen4 I/O Expansion Drawer (#ENZ0).

The PCIe Gen4 Fanout Module (#ENZF) is the fan out module (FOM) for placement in PCIe Gen4 I/O Expansion Drawer (#ENZ0). Each FOM provides six PCIe Gen4 slots (4 x16, 2 x8) slots. All six slots, including the x8 slots, use x16 connectors. A fully populated PCIe Gen4 I/O Expansion Drawer (#ENZ0) with two PCIe Gen4 Fanout Module (#ENZF) provides twelve PCIe Gen4 slots (8 x16, 4 x8). Each PCIe Gen4 FOM (#ENZF) only connects to PCIe x16 to CXP Converter Card features #EJ24 or #EJ2A.

For the Power S1122 server a cable pair attaches the PCIe Cable Adapter (#EJ24) to the fanout module. Feature ECLS provides a pair of 3-meter copper cables. Two cables of identical length, or one feature, is required for each fanout module. Copper cables have the same operating system software prerequisites as AOC cables.

## Limitations

- /SM590000 The combined maximum of NED24 NVMe Expansion Drawer (#ESR0) and PCIe Gen4 I/O Expansion Drawer (#ENZ0) is half of maximum of controller card #EJ24 or #EJ2A allowed per server.
- /SM590000 A 1 EIA (1U) of space is required in the IBM 7965-S42 rack or any OEM rack between the top of the PCIe Gen4 I/O Expansion Drawer (#ENZ0) and the bottom of a Scale-out server (9824- 22A/42A, 9856-22H/42H) or NED24 NVMe Expansion Drawer (#ESR0) when installed directly below one of these options. This applies to both factory integrated orders (#4651-#4666) and systems integrated in the field (#4650). This 1U of space is required for correct function of the cable management bracket and serviceability of the PCIe Gen4 I/O Expansion Drawer (#ENZ0).

For more details on the I/O expansion drawers refer to 3.2, 'Enhancing I/O Scalability with Expansion Drawers' on page 76.

## 2.2.6  Power S1122 system configuration

The minimum Power S1122 initial order must include two processor modules of the same type, two 32 GB DIMMs (one feature EM54 64 GB (2 x 32 GB) DDIMM), two power supplies and line cords, an operating system indicator, a cover set indicator, and a Language Group Specify. Also, it must include one of these storage options and one of these network options:

## Storage options:

- /SM590000 For boot from NVMe: One NVMe drive slot and one NVMe drive or one PCIe NVMe add in adapter.
- /SM590000 For boot from SAN: Internal SSD is not required if feature 0837 (boot from SAN) is selected. A Fibre Channel adapter must be ordered if feature 0837 is selected.

## Network options:

- /SM590000 One PCIe2 4-port 1 Gb Ethernet adapter
- /SM590000 One of the supported 10 Gb Ethernet adapters

If AIX or Linux is the primary operating system. The minimum defined initial order configuration is shown in Table 2-2.

Table 2-2   Minimum configuration for AIX or Linux

| System Feature Codes         | Feature Code   | Description                                              | Default   | Minimum Quantity   | Notes                                                                                |
|------------------------------|----------------|----------------------------------------------------------|-----------|--------------------|--------------------------------------------------------------------------------------|
| Op-Panel                     | EU0K           | Operator Panel LCD Display                               |           | 1                  | Optional with AIX/Linux. Always default Qty. 1, but can be deselected for AIX/Linux. |
| Virtualization Engine        | EPVT           | PowerVM Enterprise Edition                               | 1         | 1                  | Must select one option.                                                              |
| Virtualization Engine        | or             | or                                                       | or        | or                 | Must select one option.                                                              |
| Virtualization Engine        | EPV0           | Deactivation of LPM (Live Partition Mobility)            |           | 1                  | Must select one option.                                                              |
| Processor Modules            | ERGR           | 4-core Typical 3.6 to 4.0 GHz (max) Power11 Processor    |           | 2                  | Must select Processor Module option.                                                 |
| Processor Modules            | or             | or                                                       | or        | or                 | Must select Processor Module option.                                                 |
| Processor Modules            | ERGQ           | 10-core Typical 3.05 to 4.0 GHz(max)Power11 Processor    |           | 2                  | Must select Processor Module option.                                                 |
| Processor Modules            | or             | or                                                       | or        | or                 | Must select Processor Module option.                                                 |
| Processor Modules            | EBG8           | 16-core Typical 3.0 to 4.2 GHz(max)Power11 Processor     |           | 2                  | Must select Processor Module option.                                                 |
| Processor Modules            | or             | or                                                       | or        | or                 | Must select Processor Module option.                                                 |
| Processor Modules            | EBG9           | 24-core Typical 2.65 to 4.15 GHz (max) Power11 Processor |           | 2                  | Must select Processor Module option.                                                 |
| Processor Modules            | or             | or                                                       | or        | or                 | Must select Processor Module option.                                                 |
| Processor Modules            | EBGA           | 30-core Typical 2.40 to 3.95 GHz (max) Power11 Processor |           | 2                  | Must select Processor Module option.                                                 |
| Processor Module Activations | ERFQ           | 1 core Processor Activation for eSCM                     |           | 4                  | Minimum of50%ofCUoD Static processor core activations need to be ordered.            |
| Processor Module Activations | or             | or                                                       | or        | or                 | or                                                                                   |
| Processor Module Activations | EBF8           | 1 core Processor Activation Pools 2.0 or Static for DCM  |           | 1                  | Requires Pools 2.0 feature EP20 Power Enterprise Pools 2.0 Enablement                |

| System Feature Codes    | Feature Code   | Description                                                         | Default   | Minimum Quantity   | Notes                                                                                                                                                                                                            |
|-------------------------|----------------|---------------------------------------------------------------------|-----------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Memory                  | EM54           | 64 GB (2x32 GB) DDIMMs, 4000 MHZ or 4800 MHz, 16 Gbit DDR5 Memory   |           | 1                  | Minimum 2 DIMMs = 1 DIMM feature.                                                                                                                                                                                |
| Memory                  | or             | or                                                                  | or        | or                 | Minimum 2 DIMMs = 1 DIMM feature.                                                                                                                                                                                |
| Memory                  | EM5B           | 128 GB (2x64 GB) DDIMMs, 4000 MHz or 4800 MHz, 16 Gbit DDR5 Memory  |           | 1                  | Minimum 2 DIMMs = 1 DIMM feature.                                                                                                                                                                                |
| Memory                  | or             | or                                                                  | or        | or                 | Minimum 2 DIMMs = 1 DIMM feature.                                                                                                                                                                                |
| Memory                  | EM5G           | 256 GB (2x128 GB) DDIMMs, 4000 MHz or 4800 MHz, 32 Gbit DDR5 Memory |           | 1                  | Minimum 2 DIMMs = 1 DIMM feature.                                                                                                                                                                                |
| Active Memory Mirroring | EM8G           | Active Memory Mirroring (AMM)                                       | 0         | 0                  | Optional feature. Max. Qty. 1 per system. Memory Mirroring requires a minimum of 8 DIMMS (4 features DIMM).Minimum2DIMMs = 1 DIMM feature.                                                                       |
| Storage Backplane       | EJ1X           | Storage Backplane with four NVMe U.2 drive slots                    |           | 1                  | Must order Qty. 1 NVMe backplane feature except when #0837 or #ESCZ (iSCSI boot) is on the orderorwhenNVMePCIe add-in adapter card is used as the Load Source. Mixing NVMe devices is allowed on each backplane. |
| Bezels                  | EJBS           | Front IBM Bezel for 8 NVMe-bays Backplane Rack-Mount                |           | 1                  | When no NVMe backplane is ordered, default #EJBS.                                                                                                                                                                |
| Bezels                  | or             | or                                                                  | or        | or                 | When no NVMe backplane is ordered, default #EJBS.                                                                                                                                                                |
| Bezels                  | EJUT           | Front OEM Bezel for 8 NVMe-bays Backplane Rack-Mount                |           | 1                  | When no NVMe backplane is ordered, default #EJBS.                                                                                                                                                                |
| NVMe Devices            | ES5A           | 800GB Mainstream NVMe U.2 SSD 4k for AIX/Linux                      | 2         | 0                  | When no NVMe backplane is ordered, default #EJBS.                                                                                                                                                                |

| System Feature Codes     | Feature Code   | Description                                           | Default   | Minimum Quantity   | Notes                                                                                                                                     |
|--------------------------|----------------|-------------------------------------------------------|-----------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Required LAN adapters    | EC71           | PCIe4LP2-Port25/10/1 GbE RoCE SFP28 Adapter           | 1         | 1                  | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC71.                                               |
| Required LAN adapters    | or             | or                                                    | or        | or                 | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC71.                                               |
| Required LAN adapters    | EC85           | PCIe5 LP 2-Port 200 GbE RoCE Adapter                  |           | 1                  | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC71.                                               |
| Required LAN adapters    | or             | or                                                    | or        | or                 | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC71.                                               |
| Required LAN adapters    | EN2X           | PCIe3 LP 4-port 10GbE BaseT RJ45 Adapter              |           | 1                  | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC71.                                               |
| Required LAN adapters    | or             | or                                                    | or        | or                 | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC71.                                               |
| Required LAN adapters    | EN2Y           | PCIe LP 4-Port 1GbE Adapter                           |           | 1                  | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC71.                                               |
| Power Supply             | EB3N           | AC Power Supply - 2000W for Server (200-240 VAC)      | 2         | 2                  | Each initial order must have all power supplies present, power supplies cannot be added later on. Only 200--240V power cords can be used. |
| Power Cables             | 6458           | Power Cord 4.3m (14-ft), Drawer to IBM PDU (250V/10A) | 2         | 2                  | Qty. 2 required.                                                                                                                          |
| Language Group           | 9300           | Language Group Specify - US English                   | 1         | 1                  | Language Specify code is required.                                                                                                        |
| Primary Operating System | 2146           | Primary OS - AIX                                      |           |                    | Must select one option.                                                                                                                   |
| Primary Operating System | or             | or                                                    | or        | or                 | Must select one option.                                                                                                                   |
| Primary Operating System | 2147           | Primary OS - Linux                                    |           |                    | Must select one option.                                                                                                                   |

The racking approach for the initial order can be a MTM 7965-S42

## 2.2.7  Comparison between S1122 and S1022 and S1022s

Table 2-3 provides a comparison between the Power10 and Power11 2S2U servers.

Table 2-3   Comparison between the S1122 and the S1022 and S1022s

| Attribute                  | S1022 (22A)              | S1022s (22B)            | S1122 DCM processors   | S1122 eSCM processors   |
|----------------------------|--------------------------|-------------------------|------------------------|-------------------------|
| Processor                  | 2x P10 l DCM (5387 pins) | 2x P10 eSCM (5387 pins) | 2x P11 DCM (5387 pins) | 2x P11 eSCM (5387 pins) |
| Processor Power (max)      | 325W                     | 240W                    | 430W                   | 285W                    |
| SMP X-bus                  | 4x2B @32 Gbps            | 4x2B @32 Gbps           | 4x2B @32 Gbps          | 4x2B @32 Gbps           |
| Memory Channels per System | 32 OMI Channels          | 16 OMI Channels         | 32 OMI Channels        | 16 OMI Channels         |

| Attribute                                    | S1022 (22A)                                                                | S1022s (22B)                                                               | S1122 DCM processors                                                       | S1122 eSCM processors                                              |
|----------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------|--------------------------------------------------------------------|
| Memory DDR4 Data Rate                        | 2666 or 3200 Mbps per OMI channel                                          | 2666 or 3200 Mbps per OMI channel                                          | 4800MbpsperOMI channel                                                     | 4000MbpsperOMI channel                                             |
| MemoryBandwidth per System (max theoretical) | 818 GB/s w/ 3200 Mbps 16, 32, 64GB DDIMM 682 GB/s w/ 2666 Mbps 128GB DDIMM | 409 GB/s w/ 3200 Mbps 16, 32, 64GB DDIMM 341 GB/s w/ 2666 Mbps 128GB DDIMM | 1228 GB/s w/ 4800 Mbps 32GB DDIMMs 2456 GB/s w/ 4800 Mbps 64, 128GB DDIMMs |                                                                    |
| DIMMs per System                             | 32                                                                         | 16                                                                         | 32                                                                         | 16                                                                 |
| Memory Capacity per System (max)             | 4 TB                                                                       | 2 TB                                                                       | 4 TB                                                                       | 2TB                                                                |
| OpenCAPI Port                                | 6 ports @25 Gbps                                                           | 0                                                                          | 0                                                                          |                                                                    |
| OpenCAPI Bandwidth per System (peak)         | 300 GB/s                                                                   | N/A                                                                        | N/A                                                                        | N/A                                                                |
| PCIe Lanes per System (max)                  | 128 PCIe G4 lanes @16 Gbps                                                 | 128 PCIe G4 lanes @16 Gbps                                                 | 128 PCIe G4 lanes @16 Gbps                                                 | 128 PCIe G4 lanes @16 Gbps                                         |
| PCIe Slots per System                        | 4 PCIe G4 x16 or G5 x8 slots 4 PCIe G5 x8 slots 2 PCIe G4 x8 slots         | 4 PCIe G4 x16 or G5 x8 slots 4 PCIe G5 x8 slots 2 PCIe G4 x8 slots         | 4 PCIe G4 x16 or G5 x8 slots 4 PCIe G5 x8 slots 2 PCIe G4 x8 slots         | 4 PCIe G4 x16 or G5 x8 slots 4 PCIe G4 x8 slots 2 PCIe G4 x8 slots |
| Slots for Internal Storage                   | General                                                                    | General                                                                    | General                                                                    | Genera                                                             |
| Drives (max)                                 | 8 NVMe U.2                                                                 | 8 NVMe U.2                                                                 | 8 NVMe U.2                                                                 | 8 NVMe U.2                                                         |
| IO Expansion Drawer (max)                    | 1                                                                          | 1                                                                          | 1                                                                          | 1                                                                  |
| Service Interface                            | Enterprise BMC (eBMC)                                                      | Enterprise BMC (eBMC)                                                      | Enterprise BMC (eBMC)                                                      | Enterprise BMC (eBMC)                                              |

## 2.3  IBM Power S1124 (9824-42A) Server Overview

The IBM Power S1124 is a high-performance, 4U rack-mounted scale-out server designed for enterprise workloads requiring flexibility, scalability, and reliability. It supports one or two Power11 processors. Each processor includes 2 spare cores to enhance system availability. With both sockets populated, the server supports up to 60 active cores and 480 simultaneous threads via SMT8 (Simultaneous Multithreading). Figure 2-2 on page 53 shows the Power S1024 front view.

Figure 2-2   Power S1024 front view

<!-- image -->

The Power S1124 supports Capacity Upgrade on Demand, allowing organizations to activate additional processor cores as needed. A minimum of 50% of installed cores must be activated at purchase, with the remainder available for future upgrades. These static activations are tied to the system but can be converted to a Power Private Cloud with Shared Utility Capacity, enabling shared processor activations across a pool of systems for greater flexibility and cost efficiency.

The Power S1124 server can also be purchased as part of a Power Private Cloud with Shared Utility Capacity pool. In this case, the system can be purchased with one or more base processor activations that are shared within the pool of systems. More base processor activations can be added to the pool in the future. It is possible to convert a system with static activations to become part of a Power Private Cloud with Shared Utility Capacity pool.

The system includes 32 DDIMM slots, with 16 usable in single-socket configurations. These slots support DDR5 memory via the Power11 OMI interface, delivering up to 1228 GBps of memory bandwidth.

With both sockets populated, the server supports up to 8 TB of memory, with a minimum of 32 GB per socket. Features include:

- /SM590000 Transparent Memory Encryption
- Transparent memory encryption provides increased data security by encrypting memory with no management setup and no performance impact.
- /SM590000 Optional Active Memory Mirroring for PowerVM hypervisor resilience
- Active Memory Mirroring is available as an option to enhance resilience by mirroring critical memory that is used by the PowerVM hypervisor

The Power S1124 comes bundled with PowerVM Enterprise Edition to support robust virtualization and hybrid cloud deployments. It can run:

- /SM590000 AIX
- /SM590000 IBM i
- /SM590000 Linux, including Red Hat OpenShift Container Platform

This makes it ideal for both traditional enterprise applications and modern containerized workloads.

Internal storage for the Power S1124 is exclusively NVMe-based, which connects directly into the system PCIe lanes to deliver high performance and efficiency. A maximum of sixteen U.2 form-factor NVMe devices can be installed, which offers a maximum storage capacity of

102.4 TB in a single server. More NVMe storage can be connected to the system by way of expansion drawers via the NED24 NVMe expansion drawer (ESLS). Fibre Channel connectivity to an external storage array is also available.

## Additional features integrated into the S1124

Additional Integrated features include:

- /SM590000 System management using an Enterprise Baseboard Management Controller (eBMC).
- /SM590000 EnergyScale technology.
- /SM590000 Redundant hot-swap cooling.
- /SM590000 Redundant hot-swap AC Titanium power supplies.
- /SM590000 Up to two HMC 1 GbE RJ45 ports.
- /SM590000 One rear USB 3.0 port.
- /SM590000 One front USB 3.0 port. Nineteen-inch rack-mounting hardware (2U).

## 2.3.1  Processors

The Power11 processor is the compute engine for the next generation of Power11 processor-based systems and is a successor to the current Power10 processor. It offers superior performance on applications such as MMA facility to accelerate computation-intensive kernels, matrix multiplication, convolution, and discrete Fourier transform. To efficiently accelerate MMA operations, the Power11 processor core implements a dense math engine (DME) micro-architecture that effectively provides an accelerator for cognitive computing, machine learning, and AI inferencing workloads.

A maximum of two Power11 DUAL-CHIP processor modules of the same type are allowed.

- /SM590000 One or two 16-core, typical 3.4--4.2 GHz (max), Power11 processor (#EP3X) are allowed.
- /SM590000 Two 24-core, typical 3.05--4.15 GHz (max), Power11 processor (#EP3H) are allowed.
- /SM590000 Two 30-core, typical 2.8--3.95 GHz (max), Power11 processor (#EP3Y) are allowed.

The Matrix Math Accelerator (MMA) feature helps to perform in-core AI inferencing and machine learning where data resides.

## Processor Activations

Processors require an activation feature in order to be utilized. For details on the options available see section 2.3.7, 'Comparison between S1124 and S1024' on page 60.

## 2.3.2  Memory

The Power S1124 server uses the next-generation DDIMMs, which are high-performance, high-reliability, high- function memory cards that contain a buffer chip, intelligence, and 4000 MHz, or 4800 MHz DRAM memory.

DDIMMs are placed in DDIMM slots in the server system.

- /SM590000 A minimum 32 GB of memory is required with one processor module. All Memory DIMMs must be ordered in pairs.
- /SM590000 A minimum 64 GB of memory is required with two processor modules. All Memory DIMMs must be ordered in quads.

Each DIMM feature code delivers two physical Memory DIMMs.

Note: Plans for future memory upgrades should be taken into account when deciding which memory feature size to use at the time of initial system order.

For the best possible performance, it is generally recommended that memory be installed in all memory slots. IBM recommends populating all the DIMM slots, or as many as possible, when running high bandwidth workloads.

To assist with the plugging rules, two DDIMMs are ordered using one memory feature number. Select from:

- /SM590000 64GB (2 x 32GB), (#EM54).
- /SM590000 128GB (2 x 64GB), (#EM5B).
- /SM590000 256GB (2 x 128GB), (#EM4M).
- /SM590000 512GB (2 x 256GB), (#EM5J).

Note: DDR5 Memory DDIMMs requires FW1110.00, or later

## 2.3.3  PCIe slots

The Power S1124 servers support up to sixteen U.2 NVMe devices and up to ten PCIe slots, providing excellent configuration flexibility and expandability. All of the PCIe slots and the NVMe drives support concurrent maintenance,

With two Power11 processor DCMs, ten PCIe slots are available:

- /SM590000 Four x16 Gen4 or x8 Gen5 full-height, half-length slots
- /SM590000 Four x8 Gen5 full-height, half-length slots (with x16 connectors)
- /SM590000 Two x8 Gen4 full-height, half-length slots (with x16 connectors)

With one Power11 processor DCM, five PCIe slots are available:

- /SM590000 One PCIe x16 Gen4 or x8 Gen5, full-height, half-length slot
- /SM590000 Three PCIe x8 Gen5, full-height, half-length slots (with x16 connector)
- /SM590000 One PCIe x8 Gen4, full-height, half-length slot (with x16 connector)

The x16 slots can provide up to twice the bandwidth of x8 slots because they offer twice as many PCIe lanes. PCIe Gen5 slots can support up to twice the bandwidth of a PCIe Gen4 slot, and PCIe Gen4 slots can support up to twice the bandwidth of a PCIe Gen3 slot, assuming an equivalent number of PCIe lanes.

At least one PCIe Ethernet adapter is required on the server by IBM to ensure proper manufacture, test, and support of the server. One of the x8 PCIe slots is used for this required adapter.

These servers are smarter about energy efficiency when cooling the PCIe adapter environment. They sense which PCIe adapters are installed in their PCIe slots and, if an adapter requires higher levels of cooling, they automatically speed up fans to increase airflow across the PCIe adapters. Note that fans faster increase the sound level of the server.

## 2.3.4  NVMe drive support

The Power S1124 supports up to 16 NVMe U.2 devices when two storage backplanes with eight NVMe U.2 drive slots (#EJ1Y) are ordered. NVMe U.2 form factor drives are installed in 2.5 inch form factor, 15-millimeter carrier for internal storage in the Power S1124 system. Both 7-millimeter and 15-millimeter NVMe are supported in the 15-millimeter carrier.

## 2.3.5  I/O expansion drawers

To provide additional PCIe slots and additional NVMe capacity, the Power11 scale-out servers support I/O expansion drawers.

## NED24 NVMe Expansion Drawer

The NED24 NVMe Expansion Drawer (#ESR0) is a storage expansion enclosure with 24 U.2 NVMe bays. It supports up to 24 U.2 NVMe devices in 15 mm Gen3 carriers. The 15 mm carriers can accommodate either 7 mm or 15 mm NVME devices.

Each NED24 NVMe Expansion Drawer contains two redundant AC power supplies. The AC power supplies are part of the enclosure base.

The NED24 NVMe Expansion Drawer is connected to a Power server through dual CXP Converter adapters (#EJ24 or #EJ2A). A cable pair attaches the PCIe Cable Adapter (#EJ2A) to the fanout module. Feature ECLX provides a pair of 3-meter optical cables with transceivers. Feature ECLY provides a pair of 10-meter optical cables with transceivers. Feature ECLS provides a pair of 3-meter copper cables. Two cables of identical length, or one feature, is required for each fanout module. Optical cables are smaller diameter and more flexible and can be longer than the copper cables. Copper cables are lower cost. Copper and optical cables have the same performance and reliability characteristics.

The following U.2 NVMe devices are supported in the NED24 NVMe Expansion Drawer:

- /SM590000 #ES5B - Enterprise 800GB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ES5A - Enterprise 800GB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES5C - Enterprise 1.6 TB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES5D - Enterprise 1.6 TB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ES5E - Enterprise 3.2 TB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES5F - Enterprise 3.2 TB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ES5G - Enterprise 6.4 TB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES5H - Enterprise 6.4 TB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ES4B - Enterprise 1.6 TB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES4C - Enterprise 1.6 TB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ES4D - Enterprise 3.2 TB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES4E - Enterprise 3.2 TB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ES4F - Enterprise 6.4 TB SSD PCIe4 NVMe U.2 module for AIX/Linux
- /SM590000 #ES4G - Enterprise 6.4 TB SSD PCIe4 NVMe U.2 module for IBM i
- /SM590000 #ECT9 - 15.3 TB Mainstream NVMe U.2 SSD 4k for AIX/Linux
- /SM590000 #ECTB - 15.3 TB Mainstream NVMe U.2 SSD 4k for IBM i

## PCIe Gen4 I/O Expansion Drawer

The PCIe Gen4 I/O Expansion Drawer (#ENZ0) is a 4U high, 19-inch wide, PCIe Gen4 based rack mountable I/O drawer that is available as a feature of Power11 Servers.

The PCIe Gen4 I/O Expansion Drawer (#ENZ0) replaces the PCIe Gen3 I/O Expansion Drawer (#EMX0). There is no upgrade path from PCIe Gen3 I/O Expansion Drawer (#EMX0) to PCIe Gen4 I/O Expansion Drawer (#ENZ0).

The PCIe Gen4 Fanout Module (#ENZF) is the fan out module (FOM) for placement in PCIe Gen4 I/O Expansion Drawer (#ENZ0).

- /SM590000 Each FOM provides six PCIe Gen4 slots (4 x16, 2 x8) slots.
- /SM590000 All six slots, including the x8 slots, use x16 connectors.

- /SM590000 A fully populated PCIe Gen4 I/O Expansion Drawer (#ENZ0) with two PCIe Gen4 Fanout Module (#ENZF) provides twelve PCIe Gen4 slots (8 x16, 4 x8).
- /SM590000 Each PCIe Gen4 FOM (#ENZF) only connects to PCIe x16 to CXP Converter Card features #EJ24 or #EJ2A.

For Power S1124 servers a cable pair attaches the PCIe Cable Adapter (#EJ2A) to the fanout module.

- -Feature ECLX provides a pair of 3-meter optical cables with transceivers.
- -Feature ECLY provides a pair of 10-meter optical cables with transceivers.
- -Feature ECLS provides a pair of 3-meter copper cables.

Two cables of identical length, or one feature, is required for each fanout module. Optical cables are smaller diameter and more flexible and can be longer than the copper cables. Copper cables are lower cost. Copper and optical cables have the same performance and reliability characteristics.

## Limitations:

- /SM590000 PCIe Gen4 I/O Expansion Drawer (#ENZ0) is allowed to be ordered as MES and added to existing configurations that include the PCIe Gen3 I/O Expansion Drawer (#EMX0).
- /SM590000 Combined maximum of NED24 NVMe Expansion Drawer (#ESR0), PCIe Gen4 I/O Expansion Drawer (#ENZ0) and PCIe Gen3 I/O Expansion Drawer (#EMX0) is half of maximum of controller card #EJ24 or #EJ2A allowed per server.
- /SM590000 A 1 EIA (1U) of space is required in the IBM 7965-S42 rack or any OEM rack between the top of the PCIe Gen4 I/O Expansion Drawer (#ENZ0) and the bottom of a Scale-out server (9824- 22A/42A, 9786-22H/42H) or NED24 NVMe Expansion Drawer (#ESR0) when installed directly below one of these options. This applies to both factory integrated orders (#4651-#4666) and systems integrated in the field (#4650). This 1U of space is required for correct function of the cable management bracket and serviceability of the PCIe Gen4 I/O Expansion Drawer (#ENZ0).
- /SM590000 The PCIe Gen4 I/O Expansion Drawer (#ENZ0) is supported with firmware 1050 and HMC version 10.3.1050.

For more details on the I/O expansion drawers refer to 3.2, 'Enhancing I/O Scalability with Expansion Drawers' on page 76.

## 2.3.6  Power S1124 system minimum configuration

The minimum Power S1124 initial order must include a processor module, two 32 GB DIMMs (one feature EM54 64 GB (2 x 32 GB) DDIMM), two power supplies and line cords, an operating system indicator, a cover set indicator, and a Language Group Specify. Also, it must include one of these storage options and one of these network options:

## Storage options:

- /SM590000 For boot from NVMe: One NVMe drive slot and one NVMe drive or one PCIe NVMe add in adapter.
- /SM590000 For boot from SAN: Internal SSD is not required if feature 0837 (boot from SAN) is selected. A Fibre Channel adapter must be ordered if feature 0837 is selected.

## Network options:

- /SM590000 One PCIe2 4-port 1 Gb Ethernet adapter
- /SM590000 One of the supported 10 Gb Ethernet adapters

Table 2-4 shows the minimum configuration when AIX or Linux are the designated operating systems.

Table 2-4   Minimum configuration for S1124 with AIX or Linux

| System Feature Codes         | Feature Code   | Description                                              | Default   | Minimum Quantity   | Notes                                                                                                                                            |
|------------------------------|----------------|----------------------------------------------------------|-----------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Op-Panel                     | EU0K           | Operator Panel LCD Display                               |           | 1                  | Optional with AIX/Linux. Always default Qty. 1, but can be deselected for AIX/Linux.                                                             |
| Virtualization Engine        | EPVT           | PowerVM Enterprise Edition                               | 1         | 1                  | Must select one option.                                                                                                                          |
| Virtualization Engine        | or             | or                                                       | or        | or                 | Must select one option.                                                                                                                          |
| Virtualization Engine        | EPV0           | Deactivation of LPM (Live Partition Mobility)            |           | 1                  | Must select one option.                                                                                                                          |
| Processor Modules            | EP3X           | 16-core Typical 3.4 to 4.2 GHz(max)Power11 Processor     |           | 1                  | Must select Processor Module option.                                                                                                             |
| Processor Modules            | or             | or                                                       | or        | or                 | Must select Processor Module option.                                                                                                             |
| Processor Modules            | EP3H           | 24-core Typical 3.05 to 4.15 GHz (max) Power11 Processor |           | 2                  | Must select Processor Module option.                                                                                                             |
| Processor Modules            | or             | or                                                       | or        | or                 | Must select Processor Module option.                                                                                                             |
| Processor Modules            | EP3Y           | 30-core Typical 2.8 to 3.95 GHz (max) Power11 Processor  |           | 2                  | Must select Processor Module option.                                                                                                             |
| Processor Module Activations | EBF8           | 1 core Processor Activation for DCM                      |           | 1                  | Minimum of50%ofCUoD Static processor core activations need to be ordered. Requires Pools 2.0 feature EP20 Power Enterprise Pools 2.0 Enablement. |

| System Feature Codes    | Feature Code   | Description                                                         | Default   | Minimum Quantity   | Notes                                                                                                                                                                                                            |
|-------------------------|----------------|---------------------------------------------------------------------|-----------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Memory                  | EM54           | 64 GB (2x32 GB) DDIMMs, 4000 MHZ or 4800 MHz, 16 Gbit DDR5 Memory   |           | 1                  | Minimum 2 DIMMs = 1 DIMM feature.                                                                                                                                                                                |
| Memory                  | or             | or                                                                  | or        | or                 | Minimum 2 DIMMs = 1 DIMM feature.                                                                                                                                                                                |
| Memory                  | EM5B           | 128 GB (2x64 GB) DDIMMs, 4000 MHz or 4800 MHz, 16 Gbit DDR5 Memory  |           | 1                  | Minimum 2 DIMMs = 1 DIMM feature.                                                                                                                                                                                |
| Memory                  | or             | or                                                                  | or        | or                 | Minimum 2 DIMMs = 1 DIMM feature.                                                                                                                                                                                |
| Memory                  | EM4M           | 256 GB (2x128 GB) DDIMMs, 4000 MHz or 4800 MHz, 32 Gbit DDR5 Memory |           | 1                  | Minimum 2 DIMMs = 1 DIMM feature.                                                                                                                                                                                |
| Memory                  | or             | or                                                                  | or        | or                 | Minimum 2 DIMMs = 1 DIMM feature.                                                                                                                                                                                |
| Memory                  | EM5J           | 512 GB (2x256 GB) DDIMMs, 4000 MHz or 4800 MHz, 32 Gbit DDR5 Memory |           | 1                  | Minimum 2 DIMMs = 1 DIMM feature.                                                                                                                                                                                |
| Active Memory Mirroring | EM8G           | Active Memory Mirroring (AMM)                                       | 0         | 0                  | Optional feature. Max. Qty. 1 per system. Memory Mirroring requires a minimum of 8 DIMMS (4 features DIMM).Minimum2DIMMs = 1 DIMM feature.                                                                       |
| Storage Backplane       | EJ1Y           | Storage Backplane with eight NVMe U.2 drive slots                   |           | 1                  | Must order Qty. 1 NVMe backplane feature except when #0837 or #ESCZ (iSCSI boot) is on the orderorwhenNVMePCIe add-in adapter card is used as the Load Source. Mixing NVMe devices is allowed on each backplane. |
| Bezels                  | EJBU           | Front IBM Bezel for 16 NVMe-bays Backplane Rack-Mount               |           | 1                  | When no NVMe backplane is ordered, default #EJBU.                                                                                                                                                                |
| Bezels                  | or             | or                                                                  | or        | or                 | When no NVMe backplane is ordered, default #EJBU.                                                                                                                                                                |
| Bezels                  | EJUV           | Front OEM Bezel for 16 NVMe-bays Backplane Rack-Mount               |           | 1                  | When no NVMe backplane is ordered, default #EJBU.                                                                                                                                                                |
| NVMe Devices            | ES5A           | 800GB Mainstream NVMe U.2 SSD 4k for AIX/Linux                      | 2         | 0                  | When no NVMe backplane is ordered, default #EJBU.                                                                                                                                                                |

| System Feature Codes     | Feature Code   | Description                                               | Default   | Minimum Quantity   | Notes                                                                                                                                     |
|--------------------------|----------------|-----------------------------------------------------------|-----------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Required LAN adapters    | EC72           | PCIe4LP2-Port25/10/1 GbE RoCE SFP28 Adapter               | 1         | 1                  | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC72.                                               |
| Required LAN adapters    | or             | or                                                        | or        | or                 | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC72.                                               |
| Required LAN adapters    | EC86           | PCIe5 LP 2-Port 200 GbE RoCE Adapter                      |           | 1                  | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC72.                                               |
| Required LAN adapters    | or             | or                                                        | or        | or                 | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC72.                                               |
| Required LAN adapters    | EN2W           | PCIe3 LP 4-port 10GbE BaseT RJ45 Adapter                  |           | 1                  | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC72.                                               |
| Required LAN adapters    | or             | or                                                        | or        | or                 | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC72.                                               |
| Required LAN adapters    | EN2Z           | PCIe LP 4-Port 1GbE Adapter                               |           | 1                  | Qty. 1 of these LAN features required on all Initial orders. Default Adapter: feature EC72.                                               |
| Power Supply             | EB3S           | AC Titanium Power Supply - 1600W for Server (200-240 VAC) | 2         | 2                  | Each initial order must have all power supplies present, power supplies cannot be added later on. Only 200--240V power cords can be used. |
| Power Cables             | 6458           | Power Cord 4.3m (14-ft), Drawer to IBM PDU (250V/10A)     | 2         | 2                  | Qty. 2 required.                                                                                                                          |
| Language Group           | 9300           | Language Group Specify - US English                       | 1         | 1                  | Language Specify code is required.                                                                                                        |
| Primary Operating System | 2146           | Primary OS - AIX                                          |           |                    | Must select one option.                                                                                                                   |
| Primary Operating System | or             | or                                                        | or        | or                 | Must select one option.                                                                                                                   |
| Primary Operating System | 2147           | Primary OS - Linux                                        |           |                    | Must select one option.                                                                                                                   |

## 2.3.7  Comparison between S1124 and S1024

Table 2-5 provides a comparison between the Power S1124 and Power S1024 servers.

Table 2-5   Comparison between the S1124 and the S1024

| Attribute                  | S1124 (24A)                       | S1122 DCM processors              |
|----------------------------|-----------------------------------|-----------------------------------|
| Processor                  | 2x P10 l DCM (5387 pins)          | 2x P11 DCM (5387 pins)            |
| Processor Power (max)      | 415W                              | 500W                              |
| SMP X-bus                  | 4x2B @32 Gbps                     | 4x2B @32 Gbps                     |
| Memory Channels per System | 32 OMI Channels                   | 32 OMI Channels                   |
| Memory DDR4 Data Rate      | 2666 or 3200 Mbps per OMI channel | 4000 or 4800 Mbps per OMI channel |

| Attribute                                     | S1124 (24A)                                                                                                                | S1122 DCM processors                                                                                           |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Memory Bandwidth per System (max theoretical) | 818 GB/s w/ 3200 Mbps 16, 32, 64GB 2U_DDIMM 682 GB/s w/ 2666 Mbps 128GB 2U_DDIMM 750 GB/s w/ 2933 Mbps 128, 256GB 4U_DDIMM | 1228 GB/s w/ 4800 Mbps 32GB DDIMMs 2456 GB/s w/ 4800 Mbps 64GB DDIMMs 2048 GB/s w/ 4000 Mbps 128, 256GB DDIMMs |
| DIMMs per System                              | 32                                                                                                                         | 32                                                                                                             |
| Memory Capacity per System (max)              | 8 TB with 4U DIMM                                                                                                          | 8 TB with 4U DIMM                                                                                              |
| OpenCAPI Port                                 | 6 ports @25 Gbps                                                                                                           | 0                                                                                                              |
| OpenCAPI Bandwidth per System (peak)          | 300 GB/s                                                                                                                   | N/A                                                                                                            |
| PCIe Lanes per System (max)                   | 128 PCIe G4 lanes @16 Gbps                                                                                                 | 128 PCIe G4 lanes @16 Gbps                                                                                     |
| PCIe Slots per System                         | 4 PCIe G4 x16 or G5 x8 slots 4 PCIe G5 x8 slots 2 PCIe G4 x8 slots                                                         | 4 PCIe G4 x16 or G5 x8 slots 4 PCIe G5 x8 slots 2 PCIe G4 x8 slots                                             |
| Slots for Internal Storage                    | General                                                                                                                    | General                                                                                                        |
| Drives (max)                                  | 16 NVMe U.2                                                                                                                | 16 NVMe U.2                                                                                                    |
| IO Expansion Drawer (max)                     | 2                                                                                                                          | 2                                                                                                              |
| Service Interface                             | Enterprise BMC (eBMC)                                                                                                      | Enterprise BMC (eBMC)                                                                                          |

## 2.4  Processor and Memory Activation on Power S1122 and S1124 Systems

The IBM Power S1122 and S1124 systems support Capacity on Demand (CoD) activations for all DCM or eSCM-based processor features. However, all installed memory is automatically activated upon installation.

Note: Capacity upgrades on demand apply only to processor features. Memory features are fully activated when installed.

## Processor Activation Options

IBM offers a variety of processor activation types to suit different workloads and pricing models:

- /SM590000 Static Processor Activations
- -Permanent and support any application environment.
- -At least 50% of installed cores must be statically activated at installation unless a system is being configured for Power Enterprise Pools (#EP20), in which case, a reduced minimum of one processor core activation is allowed.
- -Additional cores can be activated later.
- /SM590000 Base Processor Activations (Pools 2.0 - #EP20)
- -Ordered for a specific server but transferable within a Power Pool.
- -Support any OS and application type.

- -Requires minimum of one activation and a maximum of the total number of processor cores in the system.
- /SM590000 Capacity Upgrade on Demand (CUoD) Static Activations
- -Available for any processor module and OS.
- -Provide flexibility to scale core usage over time.

## Shared Utility Capacity with Power Enterprise Pools 2.0

Power S1122 and S1124 systems support Shared Utility Capacity within Power Enterprise Pools 2.0. This feature enables enhanced multi-system resource sharing and minute-by-minute tracking of compute resource consumption across a pool of systems. It allows organizations to tailor their infrastructure with a mix of purchased and pay-per-use processor and software resources. By consolidating infrastructure onto Power S1122 and S1124 systems, IT teams can simplify system management and focus on optimizing business outcomes rather than reallocating resources manually.

Shared Utility Capacity resources are tracked by virtual machine (VM) and monitored by a centralized management console (CMC), which integrates with local Hardware Management Consoles (HMCs). This setup eliminates the need to overprovision capacity on individual systems, as all processor and memory resources across the pool are activated and available for use. When a pool is initiated, each system's purchased processor activations, memory, and OS entitlements become part of the pool's Base Capacity. Any additional installed resources beyond this base are considered Metered Capacity, which is activated at pool startup and monitored by the minute. Clients are only charged for metered usage that exceeds the pool's aggregate Base Capacity, with charges deducted from Capacity Credits (5819-CRD) or billed monthly, depending on availability.

## Licensing and Pool Configuration Guidelines

Pools created after July 12, 2022, require consistent IBM i license tiers across all systems. Clients with existing pools (S1022/S1024) can add Power S1122 systems and migrate applications at their own pace.

For IBM i workloads:

- /SM590000 Power S1122 systems with up to 16 cores (P20) can join pools with P20-tier systems.
- /SM590000 Power S1122 systems with 48 or 60 cores (P30) require all systems in the pool to have P30-tier IBM i licenses.

## 2.4.1  Advanced Memory Functions on the Power11 Scale-Out servers

The Power11 Scale-Out servers provide two features that enhance the usability of the memory installed in the system. Active Memory Mirroring provides additional resilience by mirroring critical memory used by the PowerVM Hypervisor and Active Memory Expansion uses compression/decompression functions to expand the usable memory capacity allocated to an AIX partition.

## Active Memory Mirroring (AMM)

AMM for the Hypervisor is available as an option (#EM8G) to enhance resilience by mirroring critical memory used by the PowerVM hypervisor so that it can continue operating in the event of a memory failure. A portion of available memory can be proactively partitioned such that a duplicate set may be utilized upon non- correctable memory errors. This can be implemented at the granularity of DIMMs or logical memory blocks.

## Active Memory Expansion (#EMBP)

AME is an innovative technology supporting the AIX operating system that helps enable the effective maximum memory capacity to be larger than the true physical memory maximum. Compression or decompression of memory content can enable memory expansion up to 100% or more. This can enable a partition to do significantly more work or support more users with the same physical amount of memory. Similarly, it can enable a server to run more partitions and do more work for the same physical amount of memory.

AME uses CPU resource to compress or decompress the memory contents. The trade-off of memory capacity for processor cycles can be an excellent choice, but the degree of expansion varies on how compressible the memory content is. It also depends on having adequate spare CPU capacity available for this compression or decompression.

Power11 chips include a hardware accelerator designed to boost AME efficiency and use less Power core resource. The Power11 accelerator includes some minor enhancements and also leverages Power11 higher bandwidth and lower latency characteristics.

You have a great deal of control over AME usage. Each individual AIX partition can turn on or turn off AME. Control parameters set the amount of expansion desired in each partition to help control the amount of CPU used by the AME function. An IPL is required for the specific partition that is turning on memory expansion. When turned on, monitoring capabilities are available in standard AIX performance tools, such as lparstat, vmstat, topas, and svmon.

A planning tool is included with AIX, enabling you to sample actual workloads and estimate both how expandable the partition's memory is and how much CPU resource is needed. Any Power model can run the planning tool. In addition, a one-time, 60-day trial of AME is available to enable more exact memory expansion and CPU measurements. You can request the trial using the Power Capacity on Demand website.

AME is enabled by chargeable hardware feature (#EMBP), which can be ordered with the initial order of the system node or as an MES order. A software key is provided when the enablement feature is ordered, which is applied to the system node. An IPL is not required to enable the system node. The key is specific to an individual system node and is permanent. It cannot be moved to a different server.

The additional CPU resource used to expand memory is part of the CPU resource assigned to the AIX partition running AME. Normal licensing requirements apply.

## 2.5  Environmental and Physical Specifications

This section outlines the environmental requirements and physical characteristics of IBM Power scale-out servers. It includes key details such as voltage requirements, thermal output, and cooling needs to ensure proper operation in data center environments. Additionally, it provides the dimensions and weight of each server model to assist with planning for rack installation, transportation, and serviceability.

## Voltage

The S1122 has an AC rated voltage and frequency(2) of 200--240 V AC at 50 or 60 Hz plus or minus 3 Hz

The S1124 has an AC rated voltage and frequency(2) of 200--240 V AC at 50 or 60 Hz plus or minus 3 Hz

## Planning for Electrical Power

Here are some considerations when planning the electrical power for the scale-out server:

1. Power supply Redundancy is supported.
2. The Power S1122 has a maximum of two power supplies. There are no specific plugging rules or plugging sequence when you connect the power supplies to the rack PDUs. All the power supplies feed a common DC bus.
3. The Power S1124 has a maximum of four power supplies. There are no specific plugging rules or plugging sequence when you connect the power supplies to the rack PDUs. All the power supplies feed a common DC bus.
4. The power supplies automatically accept any voltage with the published, rated-voltage range. If multiple power supplies are installed and operating, the power supplies draw approximately equal current from the utility (electrical supply) and provide approximately equal current to the load.
5. Power draw and heat load vary greatly by configuration. When you plan for an electrical system, it is important to use the maximum values. However, when you plan for heat load, you can use the IBM Systems Energy Estimator website. to obtain a heat output estimate based on a specific configuration.
6. To calculate the amperage, multiply the kVA by 1,000 and divide that number by the operating voltage.

## Thermal output

The thermal output of the servers is:

## S1122 and L1122

- /SM590000 Thermal output (maximum)(3): 7643 BTU/hr
- /SM590000 Maximum power consumption(3): 2240 W
- /SM590000 Maximum kVA(4): 2.31 kVA
- /SM590000 Phase: Single

## S1124 and L1124

- /SM590000 Thermal output (maximum)(3): 9383 BTU/hr
- /SM590000 Maximum power consumption(3): 2750 W
- /SM590000 Maximum kVA(4): 2.835 kVA
- /SM590000 Phase: Single

## Operating Environment

The allowable temperature and humidity ranges for both operating and non-operating systems is provided here.

## Environment (operating)

- /SM590000 ASHRAE class;
- -Allowable A3 (fourth edition)
- /SM590000 Airflow direction;
- -Recommended Front-to-back
- /SM590000 Temperature:
- -Recommended 18.0°Cfi--27.0°C (64.4°F--80.6°F);
- -Allowable 5.0°C--40.0°C (41.0°F-104.0°F)
- /SM590000 Low-end moisture:

- -Recommended 9.0°C (15.8°F) dew point;
- -Allowable -12.0°C (10.4°F) dew point and 8% relative humidity
- /SM590000 High-end moisture:
- -Recommended 60% relative humidity and 15°C (59°F) dew point;
- -Allowable 85% relative humidity and 24.0°C (75.2°F) dew point
- /SM590000 Maximum altitude:
- -3,050 m (10,000 ft)

## Allowable environment (non-operating)

- /SM590000 Temperature:
- -Recommended 5°C--45°C (41°F--113°F)
- /SM590000 Relative humidity:
- -Recommended 8% to 85%
- /SM590000 Maximum dew point:
- -Recommended 27.0°C (80.6°F)

## Physical Specifications

Table 2-6 provides the physical specifications (dimensions and weight) of the scale-out servers.

Table 2-6   Physical specifications for the scale-out servers

|                        | 2S4U S1124 L1124   | 2S2U S1122 L1122   |
|------------------------|--------------------|--------------------|
| Max Weight (lbs)       | 96 (43.5KG)        | 7O (32.2KG)        |
| Height (mm)            | 173 (6.8")         | 86.5 (3.4")        |
| Width, overall (mm) a  | 482 (18.97")       | 482 (18.97")       |
| Width w/in Rack (mm) b | 446 (17.6")        | 446 (17.6")        |
| Depth (mm) c           | 712 (28")          | 813 (32")          |
| Rack Mountable?        | Yes (4U)           | Yes (2U)           |

- a. The width is measured to the outside edges of the rack-mount bezels.
- b. The width is 446 mm (17.6 in.) for the main chassis, which fits in between a 482.6 mm (19 in.) rack mounting flanges
- c. The cable management arm with the maximum cable bundle adds 248 mm (9.8 in.) to the depth.

<!-- image -->

Chapter 3.

3

## I/O Subsystem

The internal I/O system of IBM Power processor-based systems is engineered for high-speed, low-latency data movement, ensuring optimal performance for enterprise workloads. At the heart of this architecture is the Power11 processor, which integrates advanced I/O subsystems that support massive throughput and efficient communication between processors, memory, and peripheral devices. IBM Power leverages technologies like PCIe Gen5, and NVMe to deliver ultra-fast data access and minimize bottlenecks.

Additionally, IBM Power processor-based systems utilize a modular and scalable I/O architecture, allowing for flexible configuration and expansion. The system supports SR-IOV (Single Root I/O Virtualization) for efficient sharing of I/O resources across virtual machines, and PowerVM virtualization technology enables dynamic allocation of I/O bandwidth to match workload demands.

This internal I/O design not only enhances performance but also contributes to system reliability and availability by incorporating features like redundant paths, hot-swappable components, and advanced error detection and correction. Together, these capabilities make the IBM Power internal I/O system a key enabler of high-throughput, resilient, and scalable enterprise computing. This chapter describes the I/O subsystem for the Power S1122 and the Power S1124 servers.

This chapter contains the following topics:

- /SM590000 Internal I/O
- /SM590000 Enhancing I/O Scalability with Expansion Drawers
- /SM590000 Supported adapter list
- /SM590000 NVME U.2 Devices
- /SM590000 Other device support

## 3.1  Internal I/O

The IBM Power scale-out servers - S1122, L1122, S1124 and L1124 - are built on the Power11 architecture and feature a highly advanced internal I/O subsystem designed to support high-throughput, low-latency data movement within the server. At the heart of its internal I/O is the Power11 processor's Open Memory Interface (OMI), which decouples memory from the processor and allows for flexible, high-bandwidth memory configurations. This architecture supports DDR5 memory through memory buffer chips, enabling faster data access and improved scalability. Additionally, the scale-out servers integrate PCIe Gen5 technology, which doubles the bandwidth of previous generations, allowing for faster communication between internal components such as storage controllers, and network adapters.

The internal I/O design of the Power11 scale-out servers emphasizes reliability and serviceability. The system supports NVMe drives natively, enhancing internal storage performance, and features a modular design that allows for easy expansion through I/O drawers. These drawers connect via high-speed links and can house additional PCIe slots, enabling the system to scale with growing workload demands. Overall, the internal I/O architecture of the IBM Power11 scale-out servers are engineered to deliver exceptional performance, flexibility, and resilience for mission-critical applications.

The internal I/O subsystem of the Power11 scale-out servers are connected to PCIe Express controllers on the Power11 chips in the system. Each chip features two PCI Express controllers (PECs), PEC0 and PEC1 which support up to three PCI host bridges (PHBs) that directly connect to a PCIe slot or device.

In the Power11 scale-out servers, the Power11 chip is packaged as either a Dual Chip Module (DCM), or an entry Single chip Module (eSCMs), These modules contain two Power11 chips that are integrated into a single component that plugs into a socket on the system board of the systems.

The DCM and the eSCM are discussed in 'Comparing Power11, Power10, and POWER9 processors' on page 35. The DCM is a module in which both of the Power11 chips are fully functional and provide cores, memory, and I/O, where in an eSCM only the first chip (P0) is fully functional with cores, memory, and I/O - the second chip (P1) supports I/O only.

All of the modules utilized in the 2S4U versions of the servers (S1124 and L1124) are DCMs. The 2S2U versions (S1122 and L1122) use either DCMs or eSCMs depending on the processor feature chosen. Table 3-1 shows the module type based on the processor feature chosen.

Table 3-1   Module type by feature code

| Feature Code S1122/L1122   | Number of cores   | Module Type   | Frequency Range   |
|----------------------------|-------------------|---------------|-------------------|
| EP3Y/EP4J                  | 30 + 2 spare      | DCM           | 2.4 to 3.95 GHz   |
| EP3H/EP4B                  | 24 + 2 spare      | DCM           | 2.65 to 4.15 GHz  |
| EP3/EP4C                   | 16 + 2 spare      | DCM           | 3.00 to 4.2 GHz   |
| ERGQ/ N/A                  | 10                | eSCM          | 3.05 to 4.00 GHz  |
| ERGR/ an                   | 4                 | eSCM          | 3.60 to 4.00 GHz  |

## 3.1.1  Internal PCIe Gen 5 subsystem

All of the Power11 2S2U and 4S4U scale-out server models include 10 physical PCIe adapter slots in the chassis. The number of slots that are available for use depends on the number of processor sockets in the system that are populated. The number of available slots is the same for both DCM and eSCM based processor features:

- /SM590000 With one processor socket populated, five of the PCIe adapter slots are available for use.
- /SM590000 With two processor sockets populated, all 10 of the PCIe adapter slots can be used.

These internal PCIe adapter slots support a range of different adapters. For more information, see section 3.3, 'Supported adapter list' on page 88.

The adapter slots are a mix of PCIe Gen5 and PCIe Gen4 slots, with some running at x8 speed and others at x16. All PCIe adapter slots support hot-plug capability when used with Hardware Management Console (HMC) or eBMC based maintenance procedures.

One other slot is available in the rear of each server. This slot is dedicated to the eBMC management controller for the system. This slot cannot be used for any other PCIe adapter type.

Each system requires at least one LAN adapter to support connection to local networks. This requirement allows for initial system testing and configuration, and the preinstallation of any operating systems, if required. The required network adapter is installed by default in slot C10.

All PCIe slots support hot-plug adapter installation and maintenance when service procedures are used that are activated by way of the eBMC or HMC interfaces, and enhanced error handling (EEH).

PCIe EEH-enabled adapters respond to a special data packet that is generated from the affected PCIe slot hardware by calling system firmware, which examines the affected bus, allows the device driver to reset it, and continues without a system restart. For Linux, EEH support extends to most of the frequently used devices, although some third-party PCI devices might not provide native EEH support.

All PCIe adapter slots support hardware-backed network virtualization through single root IO virtualization (SR-IOV) technology. Configuring an SR-IOV adapter into SR-IOV shared mode might require more hypervisor memory. If sufficient hypervisor memory is not available, the request to move to SR-IOV shared mode fails. The user is then instructed to free up extra memory and attempt the operation again.

The servers are smart about energy efficiency when cooling the PCIe adapter environment. They sense which IBM PCIe adapters are installed in their PCIe slots and, if an adapter \requires higher levels of cooling, they automatically speed up fans to increase airflow across the PCIe adapters. Faster fans increase the sound level of the server.

## PCIe Slot Capabilities

If both sockets in a server are populated, the maximum number of supported PCIe adapters is 10. If only one socket is populated, the maximum number of PCIe slots is 5. Table 3-2 on page 70 lists the adapter slots that are available in the Power11 processor-based scale-out servers using the DCM modules with either one or two processor modules installed.

Table 3-2   PCIe slot details for Power 2S2U and 2S4U servers with DCM based processors

| Adapter slot   | Type                        | Sockets populated   |
|----------------|-----------------------------|---------------------|
| P0-C0          | PCIe4 x16 or PCIe5 x8 slots | 2                   |
| P0-C1          | PCIe4 x8 with x16 connector | 2                   |
| P0-C2          | PCIe5 x8 with x16 connector | 2                   |
| P0-C3          | PCIe4 x16 or PCIe5 x8 slots | 2                   |
| P0-C4          | PCIe4 x16 or PCIe5 x8 slots | 2                   |
| P0-C5 a        | eBMC                        | All systems         |
| P0-C7          | PCIe5 x8 with x16 connector | 1 or 2              |
| P0-C8          | PCIe4 x8 with x16 connector | 1 or 2              |
| P0-C9          | PCIe5 x8 with x16 connector | 1 or 2              |
| P0-C10         | PCIe4 x16 or PCIe5 x8 slots | 1 or 2              |
| P0-C11         | PCIe5 x8 with x16 connector | 1 or 2              |

a. Used for eBMC only.

Table 3-3 shows the PCIe slot configuration when a Power S1122 system is populated with eSCM processor modules.

Table 3-3   PCIe slot details for Power S1122 servers with eSCM based processors

| Adapter slot   | Type                        | Sockets populated   |
|----------------|-----------------------------|---------------------|
| P0-C0          | PCIe4 x16                   | 2                   |
| P0-C1          | PCIe4 x8 with x16 connector | 2                   |
| P0-C2          | PCIe4 x8 with x16 connector | 2                   |
| P0-C3          | PCIe4 x16                   | 2                   |
| P0-C4          | PCIe4 x16                   | 2                   |
| P0-C5 a        | eBMC                        | All systems         |
| P0-C7          | PCIe4 x8 with x16 connector | 1 or 2              |
| P0-C8          | PCIe4 x8 with x16 connector | 1 or 2              |
| P0-C9          | PCIe4 x8 with x16 connector | 1 or 2              |
| P0-C10         | PCIe4 x16                   | 1 or 2              |
| P0-C11         | PCIe4 x8 with x16 connector | 1 or 2              |

- a. Used for eBMC only.

The x16 slots can provide up to twice the bandwidth of x8 slots because they offer twice as many PCIe lanes. PCIe Gen5 slots can support up to twice the bandwidth per lane of a PCIe

Gen4 slot, and PCIe Gen4 slots can support up to twice the bandwidth per lane of a PCIe Gen3 slot.

## Slot Locations

The Power S1124 and L1124 servers are 4U (EIA units), and support the installation of full-height PCIe adapters. Figure 3-1 shows the PCIe adapter slot locations for these 2S4U server models.

Figure 3-1   PCIe adapter slot locations on the Power S1124 an L1124 servers

<!-- image -->

The Power S1122 and L1122 servers are 2U (EIA units), and support the installation of low-profile PCIe adapters. Figure 3-2 shows the PCIe adapter slot locations for these 2S2U server models.

Figure 3-2   PCIe adapter slot locations on the Power S1122 and L1122 server models

<!-- image -->

## Additional PCIe Slots

The total number of PCIe adapter slots available can be increased by adding PCIe I/O expansion drawers. Each I/O expansion drawer supports either one or two fan out modules, each fan out module provides an additional six PCIe slots. The connection of each fan out module in a PCIe expansion drawer requires the installation of a PCIe optical cable adapter in one of the internal PCIe x16 adapter slots (C0, C3fi, C4, or C10).

For more information, see section 3.2, 'Enhancing I/O Scalability with Expansion Drawers' on page 76.

## DMA space allocation

The server PCIe slots are allocated DMA space that use the following algorithm:

- /SM590000 All slots are allocated a 2 GB default DMA window.
- /SM590000 All I/O adapter slots (except the embedded USB) are allocated Dynamic DMA Window (DDW) capability that is based on installed platform memory.

DDW capability is calculated assuming 4 K I/O mappings. Consider the following points:

- /SM590000 For systems with less than 64 GB of memory, slots are allocated 16 GB of DDW capability.
- /SM590000 For systems with at least 64 GB of memory, but less than 128 GB of memory, slots are allocated 32 GB of DDW capability.
- /SM590000 For systems with 128 GB or more of memory, slots are allocated 64 GB of DDW capability.
- /SM590000 Slots can be enabled with Huge Dynamic DMA Window capability (HDDW) by using the I/O Adapter Enlarged Capacity setting in the ASMI.
- /SM590000 HDDW enabled slots are allocated enough DDW capability to map all of installed platform memory by using 64 K I/O mappings.
- /SM590000 Minimum DMA window size for HDDW enabled slots is 32 GB.
- /SM590000 Slots that are HDDW enabled are allocated the larger of the calculated DDW and HDDW capability.

## 3.1.2  Internal NVMe storage subsystem

In both the IBM Power S1122 and Power S1124 systems, NVMe drives are the exclusive internal storage option, delivering high-performance, low-latency capabilities crucial for demanding workloads. These drives are housed in a 15mm carrier U.2 2.5' form factor, designed for direct integration into the system's front slots.

The connectivity of these NVMe drives is native PCIe (Peripheral Component Interconnect Express). This direct connection to the Power11 processor architecture, particularly leveraging PCIe Gen5, ensures maximum bandwidth and minimal latency, which is essential for applications requiring rapid data access such as databases, analytics, and AI inferencing. The Power S1122 and Power S1124 systems are designed to fully exploit the performance advantages of NVMe by directly connecting these flash devices to the high-speed PCIe lanes.

For advanced configurations, especially in virtualized environments using PowerVM, the NVMe drives can be managed and allocated through the Virtual I/O Server (VIOS). This allows for flexible sharing of NVMe resources across multiple logical partitions (LPARs), while still maintaining high performance. Furthermore, for enhanced redundancy and availability, the Power S1122 and Power S1124 can support multiple NVMe backplanes and controllers (e.g., through features like the 'NVMe JBOF' adapter), enabling configurations where NVMe drives are split between redundant VIOS instances to eliminate single points of failure for critical internal storage. This comprehensive approach to NVMe connectivity ensures that these Power processor-based servers can deliver both extreme performance and enterprise-grade reliability for their internal storage.

## Connectivity for internal NVMe drives

The NVMe drives connect to the system via one or two backplanes that connect either four or eight NVMe devices to one of the systems PCIe slots. Each backplane that is installed is attached to an NVMe JBOF (Just a Bunch of Flash) adapter which contains a PCIe Gen4 switch and each NVMe JBOF adapter requires a PCIe slot in the system.

The NVMe JBOF card in the Power S1122 supports up to four NVMe slots via two cables, while each NVMe JBOF card in the Power S1124 supports up to eight NVMe slots utilizing four cables. This difference in cabling explains why the Power S1122 supports a maximum of eight drives while the Power S1124 supports a maximum of 16.

Table 3-4 summarizes the available internal storage options.

Table 3-4

| Feature                         | 2S2U                        | 2S4U                        |
|---------------------------------|-----------------------------|-----------------------------|
| NVMe 4 - device backplane       | 1 or 2 Up to 8 devices      | N/A                         |
| NVMe 8-device backplane         | N/A                         | 1 or 2 Up to 16 devices     |
| NVMe U.2 7 mm device (max of 4) | 800 GB                      | 800 GB                      |
| NVMe U.2 15 mm devices          | 0.8, 1.6, 3.2, 6.4, 15,3 TB | 0.8, 1.6, 3.2, 6.4, 15,3 TB |
| Concurrently Maintainable NVMe  | Yes                         | Yes                         |

## 3.1.3  NVMe backplane

Different backplanes are provided for the 2S2U and 2S4U servers.

- /SM590000 2S2U

The Storage Backplane that supports four NVMe U.2 drive slots (# EJ1X) is the base storage backplane. You can choose to install either one or two backplanes to support up to 8 devices in the system.

- /SM590000 2S4U

The Storage Backplane that supports eight NVMe U.2 drive slots (# EJ1Y) is the base storage Backplane. You can choose to install either one or two backplanes to support up to 16 devices.

## 3.1.4  NVMe JBOF Card

The internal NVMe is attached to the processor via a plug-in PCIe NVMe JBOF (just a bunch of flash) card, The card is plugged in specifically designated PCIe slots, Up to two cards can be populated in either the S1122 or the S1124. There is a one to one correspondence between each JBOF card and the NVMe backplane.

- /SM590000 In the 2S4U, each JBOF card contains 4 connectors that are cabled to 4 connectors on a single 8-pack backplane, each cable provides signaling for 2 NVMe drives.
- /SM590000 In the 2S2U, each JBOF card contains 2 connectors that are cabled to 2 connectors on a single 4-pack backplane, each cable provides signaling for 2 NVMe drives.

The NVME JBOF card contains a 52-lane PCIe Gen4 switch. The connected NVMe devices are individually addressable, and can be allocated individually to LPARs that are running on the system.

Figure 3-3 shows the JBOF card in the 2S4U with four connectors to the 8 port backplane.

Two of these JBOF cards are supported in the 2S4U server.

Figure 3-3   4U version of the NVMe JBOF card

<!-- image -->

Similarly, Figure 3-4 shows the JBOF card in the 2S2U. For this system only 2 cables are connected to the four drive backplane. Two of the JBOF cards are supported on the 2S2U system as well.

Figure 3-4   2U version of the NVMe JBOF card

<!-- image -->

The NVMe JBOF card is treated like a regular cable card, with similar EEH support of a planar switch. The card is not concurrently maintainable, due to the cabling required to the NVMe Backplane.

| Feature                | CCIN   | FRU   | Config   | FC 2S4U   | FC 2S2U   |
|------------------------|--------|-------|----------|-----------|-----------|
| NVMe JBOF Card (4U)    | 6B87   | Yes   | Feature  | EJ1Y      | N/A       |
| NVMe U.2 8-Pak BP (4U) | 6B89   | Yes   | Feature  | EJ1Y      | N/A       |
| NVMe JBOF Card (2U)    | 6B87   | Yes   | Feature  | N/A       | EJ1X      |
| NVMe U.2 4-Pak BP (2U) | 6B89   | Yes   | Feature  | N/A       | EJ1X      |

## 3.1.5  NVMe JBOF to Backplane Cabling

There are three PCIe slots that support NVMe JBOF cards: C8, C10 and C11. Only two pf these PCIe slots can be connected to the JBOF cards at a time. PCIe slots C8 and C10 can only be cabled to NVME Backplane P1 and C11 can only be cabled to NVME backplane P2. C10 is the default location for the JBOF connected to backplane P1, but the JBOF can be moved to C8 if there is another PCIe card that needs to be plugged into C10. You can not plug a JBOF card into both slots C8 and C10.

Figure 3-5 shows the cabling options.

Figure 3-5   Cabling diagram for NVMe backplane

<!-- image -->

Table 3-5 below shows how the NVMe JBOF card are placed in the PCIe slots under various configurations.

Table 3-5   PCIe card slots for JBOF cards

| NVMe Backplanes             | NVMe Backplanes   | NVMe Backplanes   | NVMe Backplanes                                                      |
|-----------------------------|-------------------|-------------------|----------------------------------------------------------------------|
|                             | P1 (left)         | P2 (middle)       | Notes                                                                |
| Default plugging            | C10               | C11               | NVMe are plugged in x16 slot first by default Plug order:C10,C11, C8 |
| x16 Adapter required in C10 | C8                | C11               | Plug order: C8, C11                                                  |

The Figure 3-6 shows the connector numbering on the NVMe JBOF card on the left and the NVMe backplane on the right. Each connector on the JBOF cables to the corresponding connector on the backplane. On the backplane,

- -C0 provides signaling for NVME drives 0 and 1
- -C1 provides signaling for drives 2 and 3
- -C2 provides signaling for drives 4 and 5
- -C3 provides signaling for drives 6 and 7.

In the S1122 Systems only C1 and C2 are connected. The other connections on both the JBOF and the backplane are left unconnected.

Figure 3-6   Connector locations for JBOF card (left) and NVME backplane (right)

<!-- image -->

## 3.2  Enhancing I/O Scalability with Expansion Drawers

Adding I/O drawers to an IBM Power11 2S2U and 2S4U server significantly enhances the system's scalability, flexibility, and overall performance in enterprise environments. The Power11 2S2U and 2S4U support:

- /SM590000 PCIe Gen4 I/O Expansion Drawers which provide increased throughput and bandwidth for connected devices, enabling the system to handle more demanding workloads and a broader range of peripherals.
- These drawers expand the available PCIe slots beyond what is natively supported on the system board, allowing for additional network adapters, storage controllers, and accelerators to be integrated without compromising existing configurations. This is particularly beneficial for data-intensive applications, such as AI inferencing, high-speed networking, and large-scale database operations.
- /SM590000 NED24 NVMe Expansion Drawers which provide additional NVMe capacity for expanding the direct attached storage capacity of system.

The modular nature of I/O expansion drawers supports a pay-as-you-grow model, aligning with dynamic business needs and reducing upfront capital expenditure. By expanding the number and type of adapters, and the amount of internal storage that can be installed, these drawers enable more flexible system configurations. This is especially beneficial in virtualized environments where multiple virtual machines or containers require dedicated I/O resources.

The additional i/o expansion supports higher VM density and more granular resource allocation, improving overall system utilization. IBM's expansion drawers are designed with enterprise-grade reliability features, including hot-plug capabilities, redundant paths, and integration with PowerVM and the Hardware Management Console (HMC). This ensures that

I/O resources can be added or serviced without system downtime, supporting continuous operations and minimizing the risk of service disruptions.

Finally, the I/O expansion capability aligns with the Power S1122 and Power S1124 broader design goals of resilience, security, and performance. The system's architecture, including its I/O subsystem, is built to support mission-critical workloads with features like redundant paths, error recovery, and secure boot. The drawers integrate seamlessly with IBM's Hardware Management Console (HMC) and PowerVM virtualization, ensuring centralized control and simplified management. This makes the Power11 2S2U and 2S4U servers with I/O drawers an ideal platform for enterprises seeking to modernize their infrastructure while maintaining high availability and robust performance.

## 3.2.1  PCIe expansion card

The PCIe expansion function is enabled by using the PCIe Gen4 cable adapter (#EJ24). Each adapter occupies one of the PCIe Gen5 slots in the system node. A maximum of 8 adapters can be installed inside a system node and a maximum of 32 in a system with 4 system nodes. Each adapter card connects to either one ENZ0 fanout module or one NED24 Expansion Service Manager (ESM)). The cable adapter can be placed in any slot in the system node. See Table 3-8 on page 81 for the recommended adapter locations depending on the expansion drawer being attached. Figure 3-7 shows the PCIe Gen4 cable adapter (#EJ24).

Figure 3-7   PCIe Gen4 cable adapter with FC EJ24

<!-- image -->

The EJ2A adapter card (Feature Code EJ2A, CCIN 6B99) is a PCIe Gen4 x16 cable adapter designed to provide high-speed connectivity between the system and supported I/O expansion drawers. It is a full-height, half-length card featuring two ports for connecting expansion drawer cables. The adapter can be installed in either PCIe Gen4 x16 or x8 slots; however, while using x8 slots allows for greater flexibility in connecting more drawers, it delivers lower performance compared to installation in full x16 slots.

This adapter supports the attachment of:

- -One Enclosure Services Manager (ESM) in an NED24 NVMe expansion drawer
- -One PCIe4 6-slot fanout module in an ENZ0 PCIe4 expansion drawer

The EJ2A adapter is a key component for extending the PCIe bus from the IBM Power scale-out servers to external I/O resources, enabling scalable configurations for

high-performance workloads. It is equipped with two status LEDs: a green LED that indicates link status and an amber LED used for identifying the adapter during maintenance activities.

Each EJ2A adapter supports two CXP interface ports, which can be used with either optical or copper cables to connect to PCIe Gen4 expansion drawers. A single adapter connects to one fan-out module within an expansion drawer; therefore, to utilize both fan-out modules in a drawer, two EJ2A adapters are required. In the case of connecting a NED24 expansion drawer, two adapters are also necessary for full connectivity.

Internally, the EJ2A includes a built-in PCIe switch, which enables it to extend the E1080's internal PCIe Gen4 bus to external I/O drawers while maintaining bandwidth and performance integrity. The adapter's physical layout and connectivity are illustrated in Figure 3-8.

Figure 3-8   PCIe Expansion card

<!-- image -->

## Supported PCIe4 cable adapters

The supported cable card adapters for Power11 systems are listed in Table 3-6.

Table 3-6   Supported cable card adapters by system type

| System Name                      | Adapter feature code and CCIN            |
|----------------------------------|------------------------------------------|
| IBM Power System S1124 and L1124 | PCIe4 cable adapter (FC EJ2A; CCIN 6B99) |
| IBM Power System S1122 and L1122 | PCIe4 cable adapter (FC EJ24; CCIN 6B92) |

## Cables: copper vs AOC

The low-profile cable adapter (FC EJ24, CCIN 6B98) is designed for 2U systems and supports copper cables only due to thermal constraints. The full-height cable adapter (FC EJ2A, CCIN 6B99) is designed for 4U systems, supports both copper and active optical cables (AOC), and is fully supported on the IBM Power S1124 and Power L1124 servers.

Supported cable adapter feature codes for IBM Power11 servers are listed in Table 3-7.

Table 3-7   Supported PCIe cable adapters on IBM Power11 systems.

| Feature code   | CCIN   | Form Factor      | Cable Support   | Supported Systems         |
|----------------|--------|------------------|-----------------|---------------------------|
| EJ24           | 6B98   | Low-profile (2U) | Copper only     | IBM Power S1122 and L1124 |

| Feature code   | CCIN   | Form Factor      | Cable Support                   | Supported Systems         |
|----------------|--------|------------------|---------------------------------|---------------------------|
| EJ2A           | 6B99   | Full-height (4U) | Copper and Active Optical (AOC) | IBM Power S1124 and L1124 |

The choice of copper or optical cables is dependent on your specific configuration and length of cables required. Use optical AOC cables features for cables which are much thinner and can be longer such as the features ECLX (3M optical), ECLY (10M optical). Each cable feature code contains two cables.

## Active Optical Cables (AOC)

The AOC is constructed of a fiber cable and two active electrical-to-optical converter modules combined into one assembly, also known as CXP converters. The AOC has a minimum allowed bend radius of 1 in (25 mm).

Note: AOC cables are not supported on the 2S2U models due to thermal restrictions with the EJ24 adapter.

Figure 3-9 shows the AOC connector.

Figure 3-9   AOC connector

<!-- image -->

The following cables are available:

- /SM590000 (#ECLS) - 3.0M CXP x16 Copper Cable Pair for PCIe4 Expansion Drawer
- This 3.0 meter cable pair connects a PCIe4 fan-out module in the PCIe Gen4 I/O Expansion Drawer to a PCIe4 Optical Converter Adapter in the system unit. There are two identical copper cables in the cable pair, each with two CXP connectors. One of the cables attaches to the top CXP port of the PCIe4 fan-out module and to the top CXP port of the PCIe4 Optical Converter Adapter. The other cable attaches to the bottom CXP ports.
- /SM590000 (#ECLX) - 3.0M Active Optical Cable x16 Pair for PCIe4 Expansion Drawer
- The 3.0 meter active optical cable (AOC) x16 pair connects a PCIe4 module in the PCIe Gen4 I/O Expansion Drawer to a PCIe4 Optical Converter Adapter in the system unit.

There are two identical cables in the cable pair, each with two CXP connectors. One of the cables attaches to the top CXP port of the PCIe4 module and to the top CXP port of the PCIe4 Optical Converter Adapter. The other cable attaches to the bottom CXP ports.

- /SM590000 (#ECLY) - 10M Active Optical Cable x16 Pair for PCIe4 Expansion Drawer
- The 10 meter active optical cable (AOC) x16 pair connects a PCIe4 module in the PCIe Gen4 I/O Expansion Drawer to a PCIe4 Optical Converter Adapter in the system unit. There are two identical cables in the cable pair, each with two CXP connectors. One of the cables attaches to the top CXP port of the PCIe4 module and to the top CXP port of the PCIe4 Optical Converter Adapter. The other cable attaches to the bottom CXP ports.
- /SM590000 (#ECLZ) - 20M Active Optical Cable x16 Pair for PCIe4 Expansion Drawer

The 20 meter active optical cable (AOC) x16 pair connects a PCIe4 module in the PCIe Gen4 I/O Expansion Drawer to a PCIe4 Optical Converter Adapter in the system unit. There are two identical cables in the cable pair, each with two CXP connectors. One of the cables attaches to the top CXP port of the PCIe4 module and to the top CXP port of the PCIe4 Optical Converter Adapter. The other cable attaches to the bottom CXP ports.

## Note: Consider the following points:

- /SM590000 Use the 3 m cables for intra-rack installations. Use the 10 m cables for inter-rack installations.
- /SM590000 You cannot mix copper and optical cables on the same PCIe Gen4 I/O drawer. Both fan-out modules use copper cables or both use optical cables.

A PCIe Gen4 I/O expansion drawer with two I/O fanout modules is connected to one host system node via two PCIe4 cable adapters with four expansion drawer cables (two expansion drawer cable pairs). One pair is used for each of the PCIe4 6-slot fanout modules.

## Connectivity to PCIe Expansion Drawer

Figure 3-1illustrates the connection of two expansion drawer cable pairs for two PCIe4 6-slot fanout modules.

Figure 3-10   Cabling setup for PCIe Gen4 expansion drawer

<!-- image -->

## Connectivity to NED24 expansion drawer

Figure 3-11 shows the connectivity to the NED24 expansion drawer. Note that both connections to the drawer need to be populated and be from the same system.

Figure 3-11   Connectivity to NED24 drawers

<!-- image -->

## 3.2.2  Supported I/O Drawers

The Power11 2S2U and 2S4U models support the following I/O expansion drawers:

- /SM590000 PCIe Gen4 I/O Expansion Drawer (#ENZ0)

The PCIe Gen4 I/O Expansion Drawer (#ENZ0) is a 4U high, 19-inch wide, PCIe Gen4 based rack mountable I/O drawer that is available as a feature of Power11 Servers. The PCIe Gen4 I/O Expansion Drawer (#ENZ0) replaces the PCIe Gen3 I/O Expansion Drawer (#EMX0). There is no upgrade path from PCIe Gen3 I/O Expansion Drawer (#EMX0) to PCIe Gen4 I/O Expansion Drawer (#ENZ0).

- /SM590000 NED24 NVMe Expansion Drawer (#ESR0)

The NED24 NVMe Expansion Drawer (#ESR0) is a storage expansion enclosure with 24 U.2 NVMe bays. It supports up to 24 U.2 NVMe devices in 15 mm Gen3 carriers. The 15 mm carriers can accommodate either 7 mm or 15 mm NVME devices.

Within the Power11 scale-out servers, the PCIe slots are enabled to support the PCIe x16 to CXP Converter Card (FC EJ2A) that is used to attach expansion drawers. Two PCIe x16 to CXP Converter Cards are used to attach each expansion drawer. Depending on the server type, the maximum number of supported drawers are as detailed in Table 3-8.

Table 3-8 Ma ximum IO Drawer configuration

| Configuration   |   Max IO Drawers |   Max NED24 |   Max ENZ0 | Comments                   |
|-----------------|------------------|-------------|------------|----------------------------|
| 2S4U            |                2 |           1 |          2 |                            |
| 2S2U            |                1 |           1 |          1 | AOC cabling not supported. |

## 3.2.3  Non-supported drawers

The Power11 scale-out servers no longer support the following drawers:

- /SM590000 EMX0:

PCI Gen 3 I/O Expansion Drawer (#EMX0) is no longer supported with Power11. This drawer has been replaced by the PCIe Gen 4 drawer ENZ0. None of the Fanout Modules previously available with I/O expansion drawers (EMXF, EMXG, EMXH) are supported within the new PCI Gen 4 I/O Expansion Drawer (ENZ0).

- /SM590000 IBM EXP24SX:

The EXP24SX SAS storage enclosure (ESLS, ESLL) is no longer supported with Power11. For additional internal storage a new NED24 NVMe Expansion Drawer (ESR0) is available, populated with up to 24 NVMe drives.

## 3.2.4  PCIe Gen 4 I/O Expansion Drawer

The 19-inch 4 EIA (4U) PCIe Gen 4I/O Expansion Drawer (#ENZ0) and two PCIe Fanout Modules (#ENZF) provide 12 PCIe I/O full-length, full-height Gen4 PCI slots. One Fanout Module provides 6 PCIe slots that are labeled C0 - C5. C0 through C3 are x16 slots, and C4, C5 are x8 slots. PCIe Gen1, Gen2, and Gen3 full-high adapters are also supported.

Important: PCI Gen 3 I/O Expansion Drawer (EMX0) is no longer supported with Power11. None of the Fanout Modules (EMXF, EMXG, EMXH) are supported within the new PCI Gen 3 I/O Expansion Drawer (ENZ0).

A blind swap cassette (BSC) houses the full-high adapters that go into these slots. The BSC is the same as the one used with the previous generation EMX0 drawer. The drawer is shipped with a full set of BSCs.

A PCIe CXP converter adapter (#EJ24) that occupies one of the PCIe Gen5 slots in the system node and a pair of Active Optical Cables (AOCs) or Copper Cable are used for system node to Fanout Module connection. Both Fanout Modules are completely independent PCIe domains. They can be serviced independently to one another.A minimum of one Fanout Module is required in ENZ0 drawer in location P0 being placed at the left side of the drawer when viewed from behind. Each PCIe Gen 4 I/O Expansion Drawer has two power supplies.

Drawers can be added to a server dynamically. Concurrent repair and adding or removing expansion drawers and PCIe adapters is done through HMC-guided menus or by operating system support utilities.

Careful balancing of I/O, assigning adapters through redundant ENZ0 expansion drawers, and connectivity to different system nodes can help ensure high availability for I/O resources that are assigned to LPARs.

## Figure 3-12 shows a PCIe Gen 4 I/O Expansion Drawer front view

Figure 3-12   PCIe Gen 4I /O Expansion Drawer front view

<!-- image -->

Figure 3-13 shows the rear view of the PCIe Gen 4 I/O Expansion Drawer.

Figure 3-13   Rear view of a PCIe Gen 4 I/O Expansion Drawer

<!-- image -->

## Fanout modules supported by system

Each PCIe Gen4 I/O drawer supports one or two fanout modules, which must be connected to a PCIe expansion adapter in the system to extend the PCIe bus to the drawer. The number of fanout modules supported varies by system type and configuration, directly impacting how many PCIe Gen4 drawers can be connected.

For example, systems like the Power11 2S4U can support up to four fanout modules when equipped with two Dual Chip Modules (DCMs). However, if only one socket is installed, the system supports just one fanout module. In such cases, a filler is required in place of the second module.

Refer to Table 3-9 for a detailed breakdown of the maximum number of supported fanout modules and total cable requirements for each Scale-Out server model.

Table 3-9   Number of supported fanout modules per system

| System Name            |   Maximum fanout modules |   Maximum number of G4 copper cables | Maximum number of G4 AOC cables   |
|------------------------|--------------------------|--------------------------------------|-----------------------------------|
| IBM Power System S1124 |                        4 |                                    4 | 8                                 |
| IBM Power System S1122 |                        2 |                                    4 | 0 a                               |

- a. The 2S2U servers do not support optical cables

## PCI Slots available in the PCIe Gen4 expansion drawer

Table 3.1 lists the PCI slots in the PCIe Gen4 I/O expansion drawer that is equipped with two PCIe4 6-slot fan-out modules.

Table 3-10   PCIe slot configuration in the PCIe Gen4 I/O expansion drawer

| Slot                    | Location Code   | Description      |
|-------------------------|-----------------|------------------|
| Left I/O module Slot 0  | P0-C0           | PCIe x16 adapter |
| Left I/O module Slot 1  | P0-C1           | PCIe x16 adapter |
| Left I/O module Slot 2  | P0-C2           | PCIe x16 adapter |
| Left I/O module Slot 3  | P0-C3           | PCIe x16 adapter |
| Left I/O module Slot 4  | P0-C4           | PCIe x8 adapter  |
| Left I/O module Slot 5  | P0-C5           | PCIe x8 adapter  |
| Right I/O module Slot 0 | P1-C0           | PCIe x16 adapter |
| Right I/O module Slot 1 | P1-C1           | PCIe x16 adapter |
| Right I/O module Slot 2 | P1-C2           | PCIe x16 adapter |
| Right I/O module Slot 3 | P1-C3           | PCIe x16 adapter |
| Right I/O module Slot 4 | P1-C4           | PCIe x8 adapter  |
| Right I/O module Slot 5 | P1-C5           | PCIe x8 adapter  |

## Note:

- -All slots are PCIe4 slots.
- -All slots support full-length, full-height adapters or short form-factor with a full-height tailstock in single-wide, generation 3, blind-swap cassettes.
- -Slots C0 through C3 in each PCIe4 6-slot fanout module are PCIe4 x16 buses and slots C4 and C5 are PCIe4 x8 buses.
- -All slots support enhanced error handling (EEH).
- -All PCIe slots can be serviced with the power on.
- -All six slots in a PCIe4 6-slot fanout module support Single Root I/O Virtualization (SR-IOV) shared mode.
- -Only four FC EC2S, FC EC2U, or FC EC72 adapters can be in SR-IOV mode simultaneously per 6-slot fanout module.

## NED24 NVMe Expansion Drawer

IBM continues to provide industry-leading I/O capabilities with a PCIe direct-attached expansion drawer that supports NVMe drive attachment. The NED24 NVMe Expansion Drawer (#ESR0) is a storage expansion enclosure with 24 U.2 NVMe bays.

Important: The EXP24SX SAS Storage Enclosure is no longer supported with Power11.

Figure 3-14 shows the front view of a NED24 drawer with 4 NVMe Drives at slots C8-C11.

Figure 3-14   NED24 NVMe drawer front view

<!-- image -->

Figure 3-15 shows the rear view of the NED24 drawer with two power supplies and two Expansion Service Manager (ESM)

Figure 3-15   NED24 NVME drawer rear view

<!-- image -->

Each of the 24 NVMe bays in the NED24 drawer is separately addressable and can be assigned to a specific LPAR or Virtual I/O Server (VIOS) to provide native boot support for up to 24 partitions. At the time of writing, each drawer can support up to 367 TB when utilizing the 15.3 TB flash drive.

Note: Both ESMs must be connected to the same server, single connections and multiple server connections are not supported.

Each U.2 NVMe device is installed in the NED24 drawer using a 15 mm carriers. The 15-mm carriers can accommodate either 7 mm or 15 mm NVMe devices.

The NED24 drawer is supported in the Power11 2S2U and the 2S4U using the same interconnect card that is used for the PCIe Gen 4. A maximum of one NED24 NVMe expansion drawers is supported per system. When mixing the different expansion drawers, the maximum number of drawers that are supported is based on the number of EJ24 fanout cards that are supported.

## Multipath support

At initial GA the NED24 ran in Mode 1 (single connect). In Mode 1, the NVMe drives are configured as single-path devices with only 1 ESM controlling each device. The switch in each of the ESMs is configured to logically drive only 12 of the 24 NVMe drives. No device failover capability is available.

Figure 3-16 shows the NED24 drawer in single path mode.

Figure 3-16   NED24 in single path mode

<!-- image -->

When running in Mode 1, OS level mirroring is recommended to avoid a single point of failure in the connection to the drives in the NED24 enclosures. See 'Drive installation order' on page 87 for recommended drive locations within the drawer for availability and reliability. Both ESMs must be connected to the same server, single connections and multiple server connections are not supported.

Starting with firmware level FW 1060, the NED24 NVMe drawer supports multipath. The multipath functionality supports two connections for each drive as each of the ports on the multi-port drives is connected through both ESMs. This provides additional RAS and better performance. Figure 3-17 shows the multipath function of the NED24 drawer.

Figure 3-17   Multipath on NED24 drawer

<!-- image -->

Multipath is automatically enabled with the installation of FW 1060 or later and is enabled when the appropriate OS level is installed.

Multipath support is provided in the operating systems shown in Table 3-11.

Table 3-11   Multipath support by operating system

| Operating System   | Supported releases                                                                                                                                                                                                                                                                                                   |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AIX                | /SM590000 AIX Version 7.3 with the 7300-02 Technology Level and Service Pack 7300-02-02-2420, or later /SM590000 AIX Version 7.2 with the 7200-05 Technology Level and Service Pack 7200-05-08-2420, or later /SM590000 AIX Version 7.3 with the 7300-01 Technology Level and Service Pack 7300-01-04-2420, or later |
| IBM i              | /SM590000 IBM i 7.6, IBM i 7.5 TR 4, and IBM i 7.4 TR 10                                                                                                                                                                                                                                                             |
| Linux              | /SM590000 SUSE Linux Enterprise Server 15.5 or later /SM590000 Red Hat Enterprise Linux 9.2 or later                                                                                                                                                                                                                 |

## Drive installation order

While there is no performance difference for drives in any of the NED24 slots, there is a recommended order for installation of drives within the enclosure. This is to provide good separation for the suggested mirroring between drives and to also provide optimal cooling and airflow within the enclosure. Figure 3-18 shows the suggested placement for the first four drives and Table 3-12 shows the suggested placement of all drives.

Figure 3-18   Drive installation order

<!-- image -->

Table 3-12   Recommended drive installation order

|   Drive pair |   First drive slot |   Second drive slot |
|--------------|--------------------|---------------------|
|            1 |                  1 |                  13 |
|            2 |                  7 |                  19 |
|            3 |                  2 |                  14 |
|            4 |                  8 |                  20 |
|            5 |                  3 |                  15 |
|            6 |                  9 |                  21 |
|            7 |                  4 |                  16 |
|            8 |                 10 |                  22 |
|            9 |                  5 |                  17 |
|           10 |                 11 |                  23 |
|           11 |                  6 |                  18 |
|           12 |                 12 |                  24 |

## 3.3  Supported adapter list

This section discusses the various types and functions of the PCIe adapters that are supported by the following servers:

- /SM590000 Power S1122 (9824-22A)
- /SM590000 Power S1124 (9824-42A) servers

This list is subject to change as more PCIe adapters are tested and certified, or listed adapters are no longer available.

The following sections describe the supported adapters and provide tables of orderable and supported feature numbers. The tables indicate operating system support (AIX, IBM i, and Linux) for each of the adapters.

The Order type table column in the following subsections is defined as:

Initial

Denotes the orderability of a feature only with the purchase of a new system.

MES

Denotes the orderability of a feature only as part of an MES upgrade purchase for an existing system.

Both

Denotes the orderability of a feature as part of new and MES upgrade purchases.

Supported

Denotes that feature is not orderable with a system, but is supported; that is, the feature can be migrated from existing systems, but cannot be ordered new.

## 3.3.1  SAN adapters

The Power11 processor-based scale-out servers support connection to devices that use Fibre Channel connectivity directly or through a Storage Area Network (SAN). A range of PCIe-connected Fibre Channel adapters are available in low profile and full-height form factors.

All supported Fibre Channel adapters feature LC connections. If you are attaching a switch or a device with an SC type fiber connector, an LC-SC 50-Micron Fibre Converter Cable or an LC-SC 62.5-Micron Fiber Converter Cable is required.

Table 3-13 lists the low profile Fibre Channel adapters that are supported within the Power S1122.

Table 3-13   Supported SAN adapters in S1122

| Feature Code   | CCIN   | Description                                     | Operating System supported a   | Order type   |
|----------------|--------|-------------------------------------------------|--------------------------------|--------------|
| EN1K           | 579C   | PCIe4 LP 32Gb 2-port Fibre Channel Adapter      | AIX / IBM i b / Linux          | Both         |
| EN1M           | 2CFC   | PCIe4 32Gb 4-port Optical Fibre Channel Adapter | AIX / IBM i b / Linux          | Both         |
| EN2M           | 2CFC   | PCIe4 32Gb 4-port Optical Fibre Channel Adapter | AIX / IBM i b / Linux          | Both         |

| Feature Code   | CCIN   | Description                                     | Operating System supported a   | Order type   |
|----------------|--------|-------------------------------------------------|--------------------------------|--------------|
| EN2B           | 579D   | 2-PORT FIBER CHANNEL(16Gb/s), PCIe3 x8/SHORT/LP | AIX / IBM i b / Linux          | Supported    |
| EN1B           | 578F   | PCIe3 32Gb 2-port Fibre Channel Adapter         | AIX / IBM i b / Linux          | Both         |
| EN1P           | 2CFD   | PCIe4 64Gb 2-port Fibre Channel Adapter         | AIX / IBM i b / Linux          | Both         |
| EN2P           | 2F05   | PCIe4 64Gb 2-port Fibre Channel Adapter         | AIX / IBM i b / Linux          | Both         |

- a. Validate specific Operating System Requirements
- b. IBM native support only with FC #EEPS, otherwise IBM i supported through VIOS with partition size restrictions

Table 3-14 lists the full-height Fibre Channel adapters that are supported within the Power S1124 server models, and within the PCIe expansion drawer that is connected to any of the Power11 processor-based scale-out server models.

Table 3-14   Full height SAN adapters supported in S1124 and PCIe Gen4 expansion drawer

| Feature Code   | CCIN   | Description                                             | Operating System supported a   | Order type   |
|----------------|--------|---------------------------------------------------------|--------------------------------|--------------|
| EN1J           | 579C   | PCIe4 32Gb 2-port Fibre Channel Adapter                 | AIX / IBM i b / Linux          | Both         |
| EN1L           | 2CFC   | PCIe4 32Gb 4-port Optical Fibre Channel Adapter         | AIX / IBM i b / Linux          | Both         |
| EN2A           | 579D   | 2-PORT FIBER CHANNEL(16Gb/s), PCIe3 x8/SHORT/LP CAPABLE | AIX / IBM i b / Linux          | Supported    |
| EN1A           | 578F   | PCIe3 32Gb 2-port Fibre Channel Adapter                 | AIX / IBM i b / Linux          | Both         |
| EN1L           | 2CFC   | PCIe4 32Gb 4-port Fibre Channel Adapter                 | AIX / IBM i b / Linux          | Both         |
| EN1N           | 2CFD   | PCIe4 64Gb 2-port Fibre Channel Adapter                 | AIX / IBM i b / Linux          | Both         |
| EN2L           | 2F06   | PCIe4 32Gb 4-port Fibre Channel Adapter                 | AIX / IBM i b / Linux          | Both         |
| EN2N           | 2F05   | PCIe4 64Gb 2-port Fibre Channel Adapter                 | AIX / IBM i b / Linux          | Both         |

- a. Validate specific Operating System Requirements
- b. If installed in PCIe Gen4 attached to S1122, IBM native support only with FC #EEPS, otherwise IBM i supported through VIOS with partition size restrictions. For S1124, IBM i is supported natively.

## 3.3.2  Network adapters

To connect the IBM Power S1122 and S1124 server models to a local area Network (LAN), you can use the LAN adapters that are supported in the PCIe slots of the system. Various connection speeds and physical connections are supported.

Table 3-15 lists the low profile LAN adapters that are supported within the Power S1122.

Table 3-15   Network adapters supported in the Power S1122

| Feature Code   | CCIN   | Description                                                      | Operating System supported a   | Order type   |
|----------------|--------|------------------------------------------------------------------|--------------------------------|--------------|
| EN2X           | 2F04   | PCIe2 LP 4-port 10GbE Adapter                                    | AIX / IBM i b / Linux          | Both         |
| EN2Y           | 5775   | PCIe LP 4-port 1GbE Adapter                                      | AIX / IBM i b / Linux          | Both         |
| EC2T           | 58FB   | 2-Port 25/10 GB NIC ROCE SR/Cu PCIe 3.0 Adapter                  | AIX / IBM i b / Linux          | Supported    |
| EC75           | 2CFB   | 2-PORT 100Gb EN CONNECTX-6 DXQFSP56 NOCRYPTOPCIe4x16 LP ADAPTER  | AIX / IBM i b / Linux          | Supported    |
| EC71           | 2CF9   | 2-PORT 25Gb EN CONNECTX-6 Lx SFP28 NO CRYPTO PCIe4 x8 LP ADAPTER | AIX / IBM i b / Linux          | Both         |
| EC73           | 2CF8   | 2-PORT 25Gb EN CONNECTX-6 Lx SFP28 CRYPTO PCIe4 x8 LP ADAPTER    | IBM i c                        | Both         |
| EC85           | EC2C   | 2-PORT 200GbE NIC RoCE SR/Cu PCIe5x16 NO CRYPTO LP ADAPTER       | AIX / IBM i b / Linux          | Both         |

- a. Validate specific Operating System Requirements
- b. IBM native support only with FC #EEPS, otherwise IBM i supported through VIOS with partition size restrictions
- c. Supported only by IBM i native (requires FC #EEPS) and runs in dedicated mode only (no PowerVM virtualization).RoCE and IP Security (IPSEC) are only supported by IBM i Db2fi Mirror

Table 3-16 lists the full-height LAN adapters that are supported within the Power S1124 server models, and within the PCIe expansion drawer (Nimitz) that is connected to any of the Power11processor-based scale-out server models.

Table 3-16   Full height LAN adapters supported in S1124 and PCIe Gen4 expansion drawer

| Feature Code   | CCIN   | Description                | Operating System supported a   | Order type   |
|----------------|--------|----------------------------|--------------------------------|--------------|
| EN2W           | 2F04   | PCIe2 4-port 10GbE Adapter | AIX / IBM i b / Linux          | Both         |
| EN2Z           | 5775   | PCIe 4-port 1GbE Adapter   | AIX / IBM i b / Linux          | Both         |

| Feature Code   | CCIN   | Description                                                              | Operating System supported a   | Order type   |
|----------------|--------|--------------------------------------------------------------------------|--------------------------------|--------------|
| EC2U           | 58FB   | 2-Port 25/10 Gb NICROCE SR/Cu PCIe 3.0 Adapter                           | AIX / IBM i b / Linux          | Supported    |
| EC76 c         | 2CFB   | 2-PORT 100Gb EN CONNECTX-6 DXQFSP56 NOCRYPTOPCIe4x16 LP CAPABLE ADAPTER  | AIX / IBM i b / Linux          | Supported    |
| EC72           | 2CF9   | 2-PORT 25Gb EN CONNECTX-6 Lx SFP28 NO CRYPTO PCIe4 x8 LP CAPABLE ADAPTER | AIX / IBM i b / Linux          | Both         |
| EC74 c         | 2CF8   | 2-PORT 25Gb EN CONNECTX-6 Lx SFP28 CRYPTO PCIe4 x8 LP CAPABLE ADAPTER    | IBM i d                        | Both         |
| EN26           | EC2A   | 4-PORT 25/10/1 GbE NIC RoCE SR/Cu PCIe4 x16 LP CAPABLE ADAPTER           | AIX / IBM i a / Linux b        | Both         |
| EC86           | EC2C   | 2-PORT 200GbE NIC RoCE SR/Cu PCIe5x16NOCRYPTOLPCAPABLE ADAPTER           | AIX / IBM i d / Linux b        | Both         |

- a. Validate specific Operating System Requirements
- b. IBM native support only with FC #EEPS, otherwise IBM i supported through VIOS with partition size restrictions
- c. Requires x16 slot
- d. Supported only by IBM i native (requires FC #EEPS when connected to S1122) and runs in dedicated mode only (no PowerVM virtualization).RoCE and IP Security (IPSEC) are only supported by IBM i Db2 Mirror

## 3.3.3  Transceiver (SFP) Replacement Support for Fibre Channel and Ethernet Adapter Features

IBM supports the replacement of transceivers (SFPs) for certain Fibre Channel and Ethernet adapter features. However, replacement is not supported for all features. In particular, Ethernet adapters designed specifically for copper media do not support conversion to optical transceivers.

Additionally, some Fibre Channel adapter features do not support SFP replacement, even if the transceivers appear physically removable. For these adapters, a separate SFP part is not available and cannot be ordered.

This articles outlines which adapters support SFP replacement and which do not:

- /SM590000 Transceiver component (SFP) not replaceable for POWER Fibre Channel and Ethernet adapter features.
- /SM590000 Transceiver component (SFP) is replaceable for following POWER Fibre Channel and Ethernet adapter features.

## 3.3.4  SAS and Tape adapters

The internal storage in the Power11 processor-based, scale-out servers is all based on nonvolatile memory express (NVMe) devices that are connected over PCIe directly. If you need additional storage, consider using the NED24 NVMe expansion drawer. Other options for additional storage include SAN attached devices (either Ethernet based or Fiber Channel based).

For SAS Tape Support there is a four port SAS tape adapter available in both low-profile and full-height form factors.

Table 3-17 lists the low profile SAS Tape adapter that is supported within the Power S1122

Table 3-17   Low profile SAS tape adapter supported in S1122

| Feature Code   | CCIN   | Description                                             | Operating System supported a   | Order type   |
|----------------|--------|---------------------------------------------------------|--------------------------------|--------------|
| EJ2C           | 57F2   | SAS TAPE HBA W/4X HD MINISAS, LOW PROFILE PCIe3 12Gb x8 | IBM i b VIOS not supported.    | Both         |

- a. Validate specific Operating System Requirements
- b. IBM native support only with FC #EEPS, otherwise IBM i supported through VIOS with partition size restrictions

Table 3-18 lists the full-height USB adapters that is supported within the Power S1124 server models, and within the PCIe expansion drawer (Nimitz) that is connected to any of the Power11processor-based scale-out server models.

Table 3-18   Full height SAN adapters supported in S1124 and PCIe Gen4 expansion drawer

| Feature Code   | CCIN   | Description                                                     | Operating System supported a   | Order type   |
|----------------|--------|-----------------------------------------------------------------|--------------------------------|--------------|
| EJ2B           | 57F2   | SAS TAPE HBA W/4X HD MINISAS, LOW PROFILE CAPABLE PCIe3 12Gb x8 | IBM i b VIOS not supported.    | Both         |

- a. Validate specific Operating System Requirements
- b. When connected to the S1122 IBM native support only with FC #EEPS, otherwise IBM i supported through VIOS with partition size restrictions

Note: 12G SAS Tape 4 port AIX

The 12G SAS Tape Adapter was introduced in 2023, we are planning on adding AIX support for this Adapter on Power11, This will support up to four LTO tape drives.

## 3.4  NVME U.2 Devices

The list of supported NVMe devices supported in the Power11 Scale-Out servers is listed in Table 3-19.

Table 3-19   NVME U.2 Devices

| Feature Code   | CCIN   | Description                                       | OS supported                 | Order Type   |
|----------------|--------|---------------------------------------------------|------------------------------|--------------|
| EC7T           | 59B7   | 800GB NVMe U.2 15mm Carrier SSD PCIe4 (AIX/Linux) | AIX / Linux                  | Supported    |
| EC5V           | 59BA   | 6.4TB 4K NVMe U.2 15mm SSD PCIe4 (AIX/Linux)      | AIX / IBM i a / Linux        | Supported    |
| EC5W           | 59BA   | 6.4TB 4K NVMe U.2 15mm SSD PCIe4 (IBM i)          | IBM i b VIOS not supported   | Supported    |
| ES1K           | 5947   | 800G 4K NVMe U.2 15mm SSD PCIe4 (IBM i)           | IBM i b VIOS not supported   | Supported    |
| ES1E           | 59B8   | 1.6TB 4K NVMe U.2 15mm SSD PCIe4 (AIX/Linux)      | AIX / IBM i a / Linux        | Supported    |
| ES1F           | 59B8   | 1.6TB 4K NVMe U.2 15mm SSD PCIe4 (IBM i)          | IBM i j                      | Supported    |
| ES1G           | 59B9   | 3.2TB 4K NVMe U.2 15mm SSD PCIe4 (AIX/Linux)      | AIX / IBM i a / Linux        | Supported    |
| ES1H           | 59B9   | 3.2TB 4K NVMe U.2 15mm SSD PCIe4 (IBM i)          | IBM i b VIOS not supported   | Supported    |
| ES5A           | 5B53   | 800GB 4K NVMe U.2 15mm SSD PCIe4 (AIX/Linux)      | AIX / IBM i a / Linux        | Both         |
| ES5B           | 5B53   | 800GB 4K NVMe U.2 15mm SSD PCIe4 (IBM i)          | IBM i b VIOS not supported   | Both         |
| ES5C           | 5B52   | 1.6TB 4K NVMe U.2 15mm SSD PCIe4 (AIX/Linux)      | AIX / IBM i a / Linux        | Both         |
| ES5D           | 5B52   | 1.6TB 4K NVMe U.2 15mm SSD PCIe4 (IBM i)          | IBM i b VIOS not supported   | Both         |
| ES5E           | 5B51   | 3.2TB 4K NVMe U.2 15mm SSD PCIe4 (AIX/Linux)      | AIX / IBM i a / Linux        | Both         |
| ES5F           | 5B51   | 3.2TB 4K NVMe U.2 15mm SSD PCIe4 (IBM i)          | IBM i b VIOS not supported   | Both         |
| ES5G           | 5B50   | 6.4TB 4K NVMe U.2 15mm SSD PCIe4 (AIX/Linux)      | AIX / IBM i a / Linux        | Both         |
| ES5H           | 5B50   | 6.4TB 4K NVMe U.2 15mm SSD PCIe4 (IBM i)          | IBM i b VIOS not supported j | Both         |

| Feature Code   | CCIN   | Description                                  | OS supported               | Order Type   |
|----------------|--------|----------------------------------------------|----------------------------|--------------|
| ES4B c         |        | 1.6TB 4K NVMe U.2 15mm SSD PCIe4 (AIX/Linux) | AIX / IBM i a / Linux      | Both         |
| ES4C c         |        | 1.6TB 4K NVMe U.2 15mm SSD PCIe4 (IBM i)     | IBM i b VIOS not supported | Both         |
| ES4D c         |        | 3.2TB 4K NVMe U.2 15mm SSD PCIe4 (AIX/Linux) | AIX / IBM i a / Linux      | Both         |
| ES4E c         |        | 3.2TB 4K NVMe U.2 15mm SSD PCIe4 (IBM i)     | IBM i b VIOS not supported | Both         |
| ES4F c         |        | 6.4TB 4K NVMe U.2 15mm SSD PCIe4 (AIX/Linux) | AIX / IBM i a / Linux      | Both         |
| ES4G c         |        | 6.4TB 4K NVMe U.2 15mm SSD PCIe4 (IBM i)     | IBM i b VIOS not supported | Both         |
| ECT9           | 5941   | 15TB 4K NVMe U.2 15mm SSD PCIe4 (AIX/Linux)  | AIX / IBM i a / Linux      | Both         |
| ECTB           | 5941   | 15TB 4K NVMe U.2 15mm SSD PCIe4 (IBM i)      | IBM i b VIOS not supported | Both         |

- a. IBM i through VIOS only
- b. When connected to the S1122 IBM native support only with FC #EEPS
- c. This PCIe4 NVMe device can have 64 namespaces per device and works with the previous generation of NVMe devices that manage the same custom card identification number (CCIN).

## Differences between mainstream and enterprise SSD

In this section, you will learn about the differences between enterprise SSDs and mainstream SSDs (formerly known as read-intensive SSDs).

## /SM590000 Endurance and Use Case:

Enterprise SSDs are designed for high-endurance workloads, supporting up to 10 Drive Writes Per Day (DWPD), typically using durable MLC NAND (formerly called eMLC). Mainstream SSDs usually support ~1 DWPD, making them suitable for read-heavy or less write-intensive applications.

## /SM590000 Over-Provisioning and Performance:

Enterprise SSDs have more over-provisioned NAND capacity, which helps manage garbage collection, reduces write amplification, and improves random write performance and endurance. Mainstream SSDs have less over-provisioning, which reduces cost but impacts performance and lifespan during write-heavy operations.

## /SM590000 Cost:

Mainstream SSDs are more cost-effective due to lower over-provisioning and endurance specs, offering lower cost per GB but reduced performance in write-intensive tasks.

## /SM590000 Mixing in RAID Arrays:

IBM systems do not allow mixing of mainstream and enterprise SSDs in RAID arrays. The data striping performed by the PCIe SAS adapter assumes uniform endurance across all drives.

## /SM590000 Monitoring and Lifecycle Management:

Mainstream SSDs must be monitored for end-of-life (EOL) indicators. When nearing EOL, a Predictive Failure Analysis (PFA) alert is triggered. The drive should be replaced promptly to avoid degraded performance or write failures.

## /SM590000 Warranty Considerations:

Mainstream SSDs are not covered under warranty if they exceed their rated write lifecycle. Usage beyond rated endurance may result in degraded or failed write operations.

For more information see:

https://www.ibm.com/docs/en/power10?topic=drives-mainstream-solid-state https://www.ibm.com/docs/en/power11?topic=drives-mainstream-solid-state

## 3.4.1  USB adapters

Universal Serial Bus (USB) adapters are available to support the connection of devices, such as external DVD drives to the Power11 processor-based scale-out server models.

Table 3-20 lists the low profile USB adapter that is supported within the Power S1122

Table 3-20   USB adapter supported in the S1122

| Feature Code   | CCIN   | Description                             | Operating System supported                         | Order types   |
|----------------|--------|-----------------------------------------|----------------------------------------------------|---------------|
| EC6J           | 590F   | 2-PORT USB 3.0 ADPTR, PCIe2 x1/SHORT LP | AIX, Linux, IBM i Assignment to the VIOS supported | Both          |

Table 3-21 lists the full-height USB adapters that is supported within the Power S1124 server models, and within the PCIe expansion drawer (Nimitz) that is connected to any of the Power11processor-based scale-out server models.

Table 3-21   Tull height SAN adapters supported in S1124 and PCIe Gen4 expansion drawer

| Feature Code   | CCIN   | Description                                     | Operating System supported                         | Order types   |
|----------------|--------|-------------------------------------------------|----------------------------------------------------|---------------|
| EC6K           | 590F   | 2-PORT USB 3.0 ADPTR, PCIe2 x1/SHORT LP CAPABLE | AIX, Linux, IBM i Assignment to the VIOS supported | Both          |

The embedded TI TUSB7340 USB3.0 host controller is used to provide 4 USB 3.0 ports:

- /SM590000 1x USB 3.0 port in the rear
- /SM590000 1x USB 3.0 port in the front
- /SM590000 1x USB 3.0 connection to the BMC for virtual KVM (keyboard, video, mouse) USB 3.0 port

The host USB controller can be deconfigured by the customer via the Enterprise BMC System Management web interface, disabling all of the host USB ports. Individual ports cannot be disabled.

## 3.4.2  Cryptographic adapters

Two different Cryptographic coprocessors or accelerators are supported by the Power11 processor-based scale-out server models.These adapters work with the IBM Common Cryptographic Architecture (CCA) to deliver acceleration to cryptographic workloads.

For more information about the cryptographic coprocessors, the available associated software, and the available CCA, see the IBM Security IBM PCIe Cryptographic Coprocessor.

## PCIe Gen3 cryptographic coprocessor 4769

The 4769 PCIe Cryptographic Coprocessor features a PCIe local bus-compatible interface. The coprocessor holds a security-enabled subsystem module and batteries for backup power.

The hardened encapsulated subsystem contains redundant IBM PowerPCfi 476 processors, custom symmetric key and hashing engines to perform AES, DES, TDES, SHA-1 and SHA2, MD5 and HMAC, and public key cryptographic algorithm support for RSA and Elliptic Curve Cryptography.

Other hardware support includes a secure real-time clock, a hardware random number generator, and a prime number generator. It also contains a separate service processor that is used to manage self-test and firmware updates. The secure module is protected by a tamper responding design that protects against various system attacks.

It includes acceleration for: AES; DES; Triple DES; HMAC; CMAC; MD5; multiple SHA hashing methods; modular-exponentiation hardware, such as RSA and ECC; and full-duplex direct memory access (DMA) communications.

A security-enabled code-loading arrangement allows control program and application program loading and refreshes after coprocessor installation in your server. IBM offers an embedded subsystem control program and a cryptographic application programming interface (API) that implements the IBM Common Cryptographic Architecture.

The IBM 4769 is verified by NIST at FIPS 140-2 Level 4, the highest level of certification that is achievable as of this writing for commercial cryptographic devices.

This adapter is available only in full-height form factor, and is available in two variations with two different Feature Codes:

- /SM590000 #EJ35 does not include a Blind Swap Cassette (BSC) and can be installed only within the chassis of a Power S1124.
- /SM590000 #EJ37 includes a Blind Swap Cassette housing, and can be installed only in a PCIe I/O expansion drawer enclosure. This option is supported for the Power S1122 server.

## PCIe Gen3 cryptographic coprocessor 4770

4770 HSM is a Cryptographic Coprocessor, built for the quantum safe future.

- /SM590000 Next Gen HSM
- /SM590000 Higher Performance Quantum Safe Algorithms
- /SM590000 Dedicated Mode for AIX / IBM i / Linux

Typical cryptographic Applications that benefit from the strong security characteristics of the 4770 HSM are:

- /SM590000 Financial applications such as PIN generation and verification in automated teller and point-of sale transaction servers.
- /SM590000 Key management systems

- /SM590000 Internet business and Web-serving
- /SM590000 Public Key Infrastructure applications
- /SM590000 smart card applications
- /SM590000 custom proprietary solutions
- /SM590000 Secure key support for quantum-safe cryptography for both signature (ML-DSA; FIPS 204) and key encapsulation method (ML-KEM: FIPS 203)

The 4770 has enhanced hardware to perform over 300 cryptographic algorithms including Quantum Safe Algorithms. The 4770 has strong logical and physical security characteristics. It is designed to meet the highest level of security certifications.

## The 4770 HSM Attributes are

- /SM590000 Enhanced Hardware to perform asymmetric, symmetric and hashing algorithms (300+)
- /SM590000 Hardware Support for Quantum Safe Algorithms (CRYSTALS-Dilithium
- /SM590000 Common Cryptographic Architecture (CCA, PKCS #11 support via OpenCrptoki
- /SM590000 Quantum Safe protected firmware using parallel signatures (ECDSA + CRYSTALS-Dilithium)
- /SM590000 Tamper-responding secure hardware designed to meet the highest level of security for PCI HSMv4, FIPS 140-2 Level 4, Common Criteria, GBIC, AusPayNet and other certifications.
- /SM590000 X9 TR-31 key block native support, X9 TR-34 remote key load, AES and TDES PIN processing including AES DUKPT and TDES DUKPT.

Table  lists the low profile Cryptographic adapters that are supported within the Power S1122. Low profile cryptographic adapters

| Feature Code   | CCIN   | Description                  | Operating System supported                         | Order types   |
|----------------|--------|------------------------------|----------------------------------------------------|---------------|
| EPG4 a         | C138   | 4770 CRYPTO COPROCPCI3 x4 LP | AIX, Linux, IBM i Assignment to the VIOS supported | Both          |

Note: This feature is not available in China.

Table 3-22 lists the full-height Cryptographic adapters that are supported within the Power S1124 server and the PCIe expansion drawers.

Table 3-22   Full height cryptographic adapters

| Feature Code   |   CCIN | Description                                                                   | Operating System supported                         | Order types   |
|----------------|--------|-------------------------------------------------------------------------------|----------------------------------------------------|---------------|
| EJ35           |   4769 | PCIe3 Crypto Coprocessor no BSC 4769 (S1124 chassis only)                     | AIX, Linux, IBM i Assignment to the VIOS supported | Supported     |
| EJ37           |   4769 | CRYPTO COPROC PCI3 x4 LP CAPABLE IN GEN3' BLIND SWAP Cassette For I/O Drawers | AIX, Linux, IBM i Assignment to the VIOS supported | Supported     |

| Feature Code   | CCIN   | Description                                                      | Operating System supported                         | Order types   |
|----------------|--------|------------------------------------------------------------------|----------------------------------------------------|---------------|
| EPG5           | C138   | 4770 CRYPTOCOPROCPCI3 x4 LP CAPABLE                              | AIX, Linux, IBM i Assignment to the VIOS supported | Both          |
| EPG6           | C138   | 4770 CRYPTOCOPROCPCI3 x4 LP CAPABLEINGEN3'CASSETTEFOR I/O DRAWER | AIX, Linux, IBM i Assignment to the VIOS supported | Both          |

## 3.4.3  Graphical adapters

There is currently not a graphics adapter available for the Power11 servers. For applications where a local graphics terminal is required, IBM is planning on supporting a new graphics adapter for scale-out servers. The adapter is planned to provide both AIX and Linux support.

## 3.5  Other device support

This section discusses additional devices that attach to the Power11 scale-out servers.

## RDX Removable Hard Disk Cartridge

The RDX removable Hard Disk Cartridge is not supported with Power11 servers. It can not be purchased to be used with these servers.

There are alternative solutions to an RDX based Backup strategy that are being offered. Clients should consider:

- /SM590000 Cloud based Backup Services
- /SM590000 On-Premise Entry Tape Drives and Libraries

## IBM 7226 1U Multi-Media enclosure)

The IBM System Storage 7226 Model 1U3 Multi-Media Enclosure can accommodate up to two LTO tape drives, two RDX removable disk drive docking stations, or up to four DVD-RAM drives. The 7226 offers SAS, USB, and FC electronic interface drive options for attachment to the Power S1122 and S1224 servers.

The 7226-1U3 multi-media expansion enclosure is a 1U rack-mountable dual bay enclosure with storage device options of LTO7, 8, and 9 tape drives with SAS-6 / SAS-12 interface or Fibre Channel 8-Gbps interface. and offers up to 18TB single cartridge native capacity.

The 7226 also offers DVD-RAM SAS and USB drive features. The previously available RDX feature is not supported on Power11 servers. Up to two devices (or four DVD-RAM drives) can be installed in any combination in the 7226 enclosure.

The 7226 offers the following drive features:

- /SM590000 DVD Sled with DVD-RAM SATA/SAS Drive (#1420)
- /SM590000 DVD Sled with DVD-RAM USB Drive (#5762)
- /SM590000 Half-High LTO Ultrium 7 SAS Tape Drive (#8441)
- /SM590000 Half-High LTO Ultrium 7 FC Tape Drive (#8446)
- /SM590000 Half-High LTO Ultrium 8 SAS Tape Drive (#8541)

- /SM590000 Half-High LTO Ultrium 8 FC Tape Drive (#8546)
- /SM590000 Half-High LTO Ultrium 9 SAS Tape Drive (#8641)
- /SM590000 Half-High LTO Ultrium 9 FC Tape Drive (#8646)

## 3.5.1  No longer supported

Starting with Power11, IBM no longer supports attachment of the following:

- /SM590000 SAS Storage Adapters and Drawers - SAS Tape Support will remain (EJ2B/EC2C)
- /SM590000 Gen3 I/O Expansion Drawer (EMX0) and the associated Fanout Modules
- /SM590000 8Gb and 16Gb Fibre Channel Adapters
- /SM590000 All RDX Features
- /SM590000 NVME Slot Adapters

This list is not exhaustive, to validate if your device is supported, see the IBM Sales Manual.

## 3.5.2  PCIe adapters that require increased cooling

Hot PCIe adapters generate higher levels of heat and often have strict temperature limits. IBM Power scale-out servers support a variety of such adapters, and to ensure adequate cooling, the fan speed floor is increased when these adapters are installed. The minimum fan RPM varies depending on the specific adapter and the ambient temperature.

Note: Higher fan speed floors can result in a noticeable increase in overall system noise. Fan activity is often triggered by temperature readings from sensors located on the operator panel.

The IBM Power scale-out servers are equipped with three sensors located on the operator panel to measure ambient temperature. The current readings from these sensors can be viewed through the ASMI (eBMC) interface by navigating to Hardware Status and selecting Sensors, as shown in Figure 3-19.

Figure 3-19   Ambient temperature readings from three sensors located on the operator panel, as viewed through the ASMI GUI (eBMC).

<!-- image -->

The firmware uses an internal algorithm to determine which ambient sensor value to use for fan control. For example, if the readings are as follows (see Figure 3-19):

- /SM590000 Ambient 0 Temp = 23.062°C
- /SM590000 Ambient 1 Temp = 23.211°C

- /SM590000 Ambient 2 Temp = 22.92°C

The firmware will select Ambient 0 Temp as the controlling value (23.062°C), as it represents the median reading among the three sensors.

For example, on the IBM Power S1124 (eBMC) system, model 9824-42A, if the intake air temperature - measured by the front-mounted sensors is below 27°C (as shown in Figure 3-19 on page 99), the default fan speed target is set to 5000 RPM, as illustrated in Figure 3-20, assuming no hot adapters are installed.

Note: The fan speed target and the actual speed readings (in RPM), as displayed in the ASMI GUI (eBMC) under the Sensors tab, may vary slightly from the expected values. This variation is normal and can be attributed to system-specific fan control policies. For example, 2U ( S1122 ) and 4U ( S1124) systems follow different rules and ambient temperature zones, which influence their fan speed behavior.

If hot adapters are present, the fan speed behavior is adjusted based on the Hot PCIe Adapters List and the corresponding ambient temperature range, available at:

https://github.com/openbmc/phosphor-fan-presence/tree/master/control/config\_files/ p10bmc

Figure 3-20   Fan speed readings in RPM as viewed through the ASMI GUI (eBMC) under the Sensors tab.

<!-- image -->

Note: PCIe4 cable adapters (FC EJ2A and EJ24) are not treated as standard PCIe hot adapters. Their presence in the system does not automatically trigger higher fan floor speeds. Instead, these adapters are equipped with temperature sensors, and the system firmware uses predefined thresholds to determine when to increase fan speeds to ensure adequate cooling.

Table 3-23 lists the PCIe adapters that require increased cooling and will result in higher fan speeds on the IBM Power scale-out servers.

Note: The Hot Adapter List is continuously updated. To access the latest version, visit the public GitHub repository linked below. Navigate to your system specific 'com.ibm.Hardware.Chassis.Model.xxxxxx' directory and refer to the 'pcie\_cards.json' file for the most up-to-date list:

https://github.com/openbmc/phosphor-fan-presence/tree/master/control/config\_fil es/

Table 3-23   PCIe adapters that require increased cooling.

| Feature code   | Description                                                          |
|----------------|----------------------------------------------------------------------|
| EC2S/EC2R      | PCIe3 2-port 10 Gb NIC RoCE SR/Cu adapter                            |
| EC2U/EC2T      | PCIe3 2-port 25/10 Gb NIC RoCE SFP28 adapter                         |
| EC66/EC67      | PCIe4 2-port 100 GbE RoCE x16 adapter                                |
| EJ14           | PCIe3 12GB Cache RAID SAS 4 Adapter Quad-port with Advanced Features |
| EJ0L           | PCIe3 12GB Cache RAID SAS Adapter Quad-port 6Gb                      |
| EJ0J/EJ0M      | PCIe3 RAID SAS Adapter Quad-port 6Gb                                 |
| EJ10/EJ11      | Media PCIe3 4 x8 SAS Port Adapter (Tape/DVD)                         |
| EC5G/EC5B      | PCIe3 NVMe x8 1.6TB SSD Adapter                                      |
| EC5C/EC5D      | NVMe PCIe3 NVMe x8 3.2TB SSD Adapter                                 |
| EC5E/EC5F      | PCIe3 NVMe x8 6.4TB SSD Adapter                                      |
| EC6U/EC6V      | PCIe3 NVMe x8 1.6TB SSD Adapter IBM i                                |
| EC6W/EC6X      | PCIe3 NVMe x8 3.2TB SSD Adapter IBM i                                |
| EC6Y/EC6Z      | PCIe3 NVMe x8 6.4TB SSD Adapter IBM i                                |
| EJ32           | PCIe Crypto Coprocessor                                              |
| EJ1X           | PCIe JBOF for NVMe U.2 4-Pack Backplane                              |
| EJ1Y           | PCIe JBOF for NVMe U.2 8-Pack Backplane                              |
| EJ24           | PCIe x16 to CXP Converter Card 2U Gen4 for MEX IO drawer             |
| EJ2A           | PCIe x16 to CXP Converter Card 4U Gen4 for MEX IO drawer             |
| EC76/EC75      | PCIe4 2-port 100Gb RoCE EN ConnectX-6Dx Adapter                      |
| EC78/EC77      | PCIe4 2-port 100Gb RoCE EN ConnectX-6Dx Encryption Offload Adapter   |
| EC7A/EC7B      | NVMe PCIe4 NVMe x8 1.6TB SSD Adapter (AIX/Linux)                     |
| EC7C/EC7D      | NVMe PCIe4 NVMe x8 3.2TB SSD Adapter (AIX/Linux)                     |
| EC7E/EC7F      | NVMe PCIe4 NVMe x8 6.4TB SSD Adapter (AIX/Linux)                     |
| EC7J/EC7K      | NVMe PCIe4 NVMe x8 1.6TB SSD Adapter (IBM i)                         |
| EC7L/EC7M      | NVMe PCIe4 NVMe x8 3.2TB SSD Adapter (IBM i)                         |
| EC7N/EC7P      | NVMe PCIe4 NVMe x8 6.4TB SSD Adapter (IBM i)                         |

| Feature code   | Description                                                    |
|----------------|----------------------------------------------------------------|
| EJ35           | PCIe3 x7 4769 Crypto Coproc                                    |
| EN1E/EN1F      | PCIe3 x8 4-Port Fiber Channel (16Gb/s)                         |
| EN1C/EN1D      | PCIe3 16Gb 4-port Fibre Channel Adapter                        |
| EN2L           | PCIe4 32Gb 4-port Fibre Channel Adapter                        |
| EC64           | 2-Port EDR 100Gb IB ConnectX-5 GEN4 PCIe LP ADAPTER - RPQ only |
| EN26           | PCIe4x16 4-port 25/10/1GbE NICRoCE SR/Cu                       |
| EN2D           | PCIe4x16 4-port 25/10/1GbE NICRoCE SR/Cu w/ Crypto             |

Note: The availability of PCIe adapters listed in this table may vary, and not all are offered for the IBM Power scale-out servers.

<!-- image -->

Chapter 4.

4

## Artificial Intelligence Support

Artificial intelligence (AI) is becoming a cornerstone of digital transformation across industries, enabling organizations to automate processes, gain deeper insights, and deliver more personalized experiences. From predictive analytics and natural language processing to computer vision and generative AI, the demand for AI-driven solutions is rapidly growing. To support these workloads effectively, enterprises need infrastructure that can handle the computational intensity and data throughput AI requires - this is where IBM Power processor-based servers play a critical role.

IBM Power is purpose-built to support AI workloads with its high-performance architecture, including the latest Power11 processors that feature integrated AI acceleration. These processors are designed to handle low-precision arithmetic operations commonly used in AI models, significantly boosting inferencing speed without compromising accuracy. Additionally, IBM Power supports advanced technologies like IBM Spyre Accelerator, a PCIe-attached AI card optimized for enterprise AI workloads, and Power11's on-chip AI inferencing, which enables real-time decision-making at scale. These capabilities make Power processor-based servers ideal for deploying AI models in production environments where performance, reliability, and scalability are essential.

Beyond hardware, IBM Power integrates seamlessly with OpenShift AI, enabling organizations to build, train, and deploy AI models within a containerized, hybrid cloud environment. This combination allows for consistent DevOps practices, efficient resource utilization, and simplified management of AI workflows. With support for popular AI frameworks like PyTorch, TensorFlow, and vLLM, IBM Power provides a complete, enterprise-ready platform for operationalizing AI. Whether running AI at the edge, in the data center, or across hybrid cloud environments, IBM Power delivers the performance and flexibility needed to turn AI potential into real-world impact.

This chapter contains the following topics:

- /SM590000 On chip support
- /SM590000 AI Acceleration with IBM Spyre adapter
- /SM590000 Solutions

## 4.1  On chip support

With the upcoming availability of the Spyre card on IBM Power-based servers, starting with systems powered by the new IBM Power11 processor, organizations will be able to take advantage of a new class of hardware acceleration designed to support a wide spectrum of enterprise workloads. The Spyre card will deliver significant performance benefits, particularly for compute-intensive and AI-driven use cases, while aligning with the architectural strengths of the IBM Power platform.The Spyre card is not a GPU, but a dedicated hardware developed by IBM Researchfi Lab to provide superior acceleration.

A common misconception among IT decision-makers today is that one or more GPUs are always required for any workload involving artificial intelligence. This perception often leads to infrastructure decisions that prioritize GPU integration by default, regardless of the nature or scope of the AI tasks to be executed. However, GPUs are not a prerequisite for all AI use cases. Their inclusion in every server configuration may result in disproportionate acquisition costs, elevated power consumption, and increased complexity in thermal and workload management, without guaranteed benefits for the workload at hand.

Beginning with IBM Power10 chip and improved in IBM Power11, each core integrates four Matrix Math Accelerators (MMAs) capable of supporting a wide range of AI inference workloads directly on the CPU. This innovation enables customers to run AI models natively on IBM Power cores without requiring a discrete GPU. The architecture is particularly well-suited to 'traditional AI' use cases, such as fraud detection, text extraction, document analysis, domain adaptation via Retrieval-Augmented Generation (RAG), pattern recognition, forecasting, and image/video/audio processing.

The IBM Power11 processor further enhances these capabilities. While not always matching the raw throughput of high-end GPUs in certain generative AI (GenAI) scenarios, IBM Power11 technology provides excellent performance for tasks such as entity extraction, translation, summarization, and classification, all while offering lower energy consumption and improved data protection. By enabling AI workloads to run closer to where the data resides, IBM Power11 processor-based systems support secure, efficient, and scalable deployment of AI without unnecessary data movement.

Moreover, when the IBM Spyre™ card becomes available on IBM Power11 processor-based systems, it will introduce additional acceleration capabilities, complementing the on-chip features. IBM Power11 processor-based systems with their integrated AI accelerators and future support for IBM Spyre card present a highly optimized, energy-aware, and secure platform for deploying AI across a broad range of use cases, without the default dependency on discrete GPUs.

## 4.2  AI Acceleration with IBM Spyre adapter

Improvements to Power11 processor core strength and system capacity boost the performance of the MMA (Matrix-Math Accelerator) for inferencing workloads. Furthermore, with IBM Spyre accelerator into Power11 provide additional AI inferencing capabilities. Working together, IBM Power processors and the IBM Spyre accelerator will enable the next generation infrastructure to scale demanding AI workloads for businesses.

The IBM Spyre card extends the capabilities of Power11 processor-based systems by offering a low-power and high-efficiency acceleration path for workloads that demand frequent memory access and streamlined data movement.

Thanks to the advanced virtualization and workload consolidation capabilities of IBM Power processor-based servers, Spyre-based applications can be co-located with other mission-critical services within the same physical server. This allows AI inference engines, real-time analytics, or data preprocessing workloads that leverage IBM Spyre card to run in close proximity to databases or transactional systems hosted in LPARs or containers on the same server. This architectural proximity reduces latency, improves throughput, and eliminates the overhead typically associated with cross-node or cross-platform communication.

The IBM Spyre card will be uniquely positioned as the one of the only AI solutions that combines:

- -Data privacy: Data AI sovereignty on reliable, trusted on-premises infrastructure.
- -Skills: Ready-to-consume enterprise AI services.
- -Complexity: Accelerated plug play AI for business workflows.

Important: Support for the Spyre adapter on IBM Power is expected to be announced and available late in 2025. Statements regarding IBM's future direction and intent are subject to change or withdrawal without notice and represent goals and objectives only.

## 4.2.1  Deploying AI in the Enterprise

Artificial intelligence (AI) is transforming enterprise operations across industries, enabling organizations to optimize decision-making, streamline processes, and deliver personalized experiences at scale. However, the path to successful AI integration in enterprise environments is far from trivial. It demands not only the right algorithms and models but also a robust, secure, and scalable infrastructure tailored to diverse AI workloads. IBM's AI-optimized Power platform provides a unique approach to meet this challenge, offering both on-chip and off-chip acceleration capabilities for different levels of AI maturity.

Most enterprise AI adoption begins with experimentation and initial use cases, such as proof-of-concept models for customer segmentation, log analysis, or anomaly detection. These workloads typically require limited computational resources and can be efficiently handled by the on-chip AI acceleration embedded in IBM Power11 processors. This includes Matrix Math Assist (MMA) engines and SIMD vector instructions, combined with high memory bandwidth-a critical component for feeding data into AI models rapidly. On-chip acceleration enables real-time inference close to the data source, minimizing latency and reducing the need for additional hardware. It is particularly effective for traditional machine learning models, data warehouse analytics, and vector database operations (like RAG-style queries).

As enterprise AI use cases evolve to include more complex deep learning models-such as image classification, video processing, and time-series forecasting-the demands on compute performance and memory bandwidth increase significantly. At this stage, enterprises need a more flexible and powerful acceleration option, particularly as workloads move from experimentation to production.

## 4.2.2  Fit for Purpose Al Acceleration

To address this, IBM introduced IBM Spyre, a dedicated off-chip accelerator designed specifically for AI-intensive workloads. Compared to the on-chip accelerators in Power11, Spyre offers significantly higher throughput, parallelism, and model capacity, thanks to its dedicated memory architecture, optimized data paths, and ability to offload processing from the CPU. Spyre is ideal for large-scale transformer models, such as those used in generative AI applications-translation, summarization, sentiment analysis, and more. This architecture

supports massive parallel compute operations with higher efficiency than general-purpose CPUs.

A key advantage of the IBM Power platform is its ability to combine both acceleration strategies-on-chip and off-chip-within a unified, enterprise-grade ecosystem. Early AI workloads can begin on existing Power processor-based servers with no added hardware, leveraging the built-in accelerators for cost-efficiency. As demands grow, the Spyre accelerators can be seamlessly integrated to boost performance without requiring a platform change or software rewrite. This flexibility protects existing investments while enabling future scaling this is shown in Figure 4-1.

Figure 4-1   IBM's fit for purpose AI architecture for Power

<!-- image -->

In high-value use cases like AI assistants and autonomous agents, where real-time interaction, low-latency inference, and contextual awareness are essential, off-chip acceleration becomes a requirement. These applications often rely on large language models (LLMs) and need to manage vast knowledge graphs or context windows, which exceed the practical limits of CPU-based inference alone. IBM Spyre is built precisely for such scenarios, and when paired with Power11 it provides a hybrid architecture that is secure, performant, and manageable within enterprise IT constraints.

Additionally, this fit-for-purpose infrastructure aligns well with existing on-premises environments, especially those where data sovereignty, latency, and compliance are non-negotiable. Unlike cloud-only solutions, the Power + Spyre combination gives enterprises full control over their data and compute stack, all while supporting AI workloads that rival hyperscale offerings in performance.

In conclusion, the approach to enterprise AI infrastructure stands out for its modularity and adaptability. Whether you're starting with lightweight models or scaling to multimodal AI agents, IBM Power processor-based servers allow you to deploy AI on your terms. With on-chip acceleration for efficient starting points and Spyre off-chip accelerators for high-performance growth, businesses gain the ability to move from AI exploration to enterprise-wide transformation-all on a platform built for the future of AI.

## 4.2.3  IBM Spyre adapter

The IBM Spyre Accelerator is a purpose-built enterprise-grade accelerator offering scalable capabilities for complex AI models and generative AI use cases. The new accelerator features 32 individual accelerator cores onboard, and each Spyre is mounted on a PCIe card. Jointly designed by IBM Research and IBM Infrastructure, Spyre's architecture is designed for more efficient AI computation. Notably, the chip will send data directly from one compute engine to the next, leading to an efficient use of energy. This family of processors also uses a range of lower precision numeric formats (such as int4 and int8), to make running an AI model more energy efficient and far less memory intensive.

IBM Spyre Is designed with a system-on-a-chip architecture optimized for enterprise AI workloads. Spyre is implemented in 5nm technology with a high performance and low-power design with 75W consumption and provides the following capabilities:

- -32 low-power AI cores.
- -Supports multi-precision for inference training: FP16/8, INT8/4.
- -Enabled for Foundation Models and enabled in the Red Hat software stack (OCP AI)
- -Supports popular AI Framework and libraries (PyTorch, vLLM)

Figure 4-2 shows the IBM Spyre adapter.

Figure 4-2   The IBM Spyre adapter

<!-- image -->

This dedicated, enterprise-grade AI acceleration chip sits on a 75W PCIe adapter, surrounded by 128 GB of LPDDR5 memory - which is large memory to hold a wide variety of LLMs in support of the heterogeneous workloads that are typically seen on IBM Power. As a single Spyre adapter will not provide enough compute capacity for most use cases, the IBM solution will utilize current I/O expansion technology to attach a cluster of eight Spyre adapters in a single I/O expansion drawer, creating a logical cluster. The firmware on those eight cards will coordinate the distribution of compute, and transfer of data amongst the cards. Making the clusters appear to the software as one high-performance compute engine, with 1 TB of memory and 1.6TB/s of memory bandwidth.

## This is shown in Figure 4-3.

Figure 4-3   Spyre cluster in an expansion drawer

<!-- image -->

This expansion drawer with Spyre adapters can be attached to any of the announced IBM Power11 servers, the number of supported drawers is dependent on the Power11 server that it is attached to.

At announcement, Spyre is planned to be available in a fixed configuration which includes eight Spyre adapters installed in the PCIe Gen4 I/O expansion drawer. The Sypre expansion drawer can be attached to any Power11 server: S1122, S1124, E1150, E1180. One expansion drawer will be supported on all models except the E1180 which will support up to two. New I/O drawer components such as power supplies and fan-out modules will be utilized to support the additional power requirements of the Spyre adapter configuration.

The initial supported software and hardware will be:

- -FW1110.10
- -HMC1111
- -RHEL 9.6
- -Spyre software stack container
- -OpenShift AI (Tech Preview 4Q 2025, GA 1Q 2026)

## 4.3  Solutions

Artificial Intelligence is no longer an emerging trend, but it is a foundational pillar of competitive advantage. According to IBM Institute for Business Value, at the time of writing, about 72% of top-performing CEOs identify advanced generative AI as essential to their future success. However, only a fraction of enterprises have successfully moved beyond pilots and proofs of concept (PoCs) into full production deployments.

IBM Power11 processor-based server provides the AI-optimized infrastructure and integrated software stack required to scale AI workloads, secure enterprise data, and modernize mission-critical processes.

Organizations across industries are realizing tangible benefits from deploying AI on IBM Power:

- /SM590000 Logistics service providers can reduce order processing time by embedding GenAI into their ERP system;
- /SM590000 Financial institutions can accelerate anomaly detection by four times, while reducing TCO;
- /SM590000 Utility providers can reduce equipment downtime, and lower energy consumption using AI-powered visual inspection.

These outcomes highlight the value of deploying generative AI in real business workflows using the trusted IBM Power platform.

IBM Power is optimized for a wide range of AI workloads spanning key sectors:

- /SM590000 Finance and ERP:
- Fraud detection, AML, order processing, invoice compliance;
- /SM590000 Healthcare:

Medical transcription, claims-EHR matching, diagnostic imaging, assistant bots;

- /SM590000 IT Development:

Predictive ITOps, code assistants (RPG, Ansible), transcription, documentation;

- /SM590000 Cross-Industry:

Document digitization, summarization, KYC, visual quality inspection, customer churn prediction, business intelligence;

Each use case leverages the inherent strengths of IBM Power, such as resilient compute, secure data access, and scalable architecture.

## 4.3.1  Barriers to scaling AI and the IBM Power technology advantage

While the promise of AI is great, common enterprise challenges persist, as described in the following table:

Table 4-1   challenges to scale AI

| Barrier                          | Description                                                              |
|----------------------------------|--------------------------------------------------------------------------|
| Data complexity                  | Fragmented formats, distributed sources, lack of standardized connectors |
| AI integration difficulty        | Legacy workflows, lack of AI skills, software maturity                   |
| Security and privacy             | Concerns around data leakage, adversarial threats, and model protection  |
| Infrastructure and cost concerns | High cost of AI development and fears of redesigning core systems        |
| Talent and skill gaps            | Shortage of data scientists and AI engineers                             |

IBM Power addresses these challenges by offering a complete AI platform, integrated into existing systems, with hardware acceleration, data fabric, and AI assistants.

## 4.3.2  IBM Power AI Portfolio: from Data to Business Value

To scale AI in production, IBM Power provides an AI-ready portfolio including:

- /SM590000 AI-Ready Infrastructure:

Built-in accelerators, support for hybrid and cloud-native deployment (e.g., PowerVS);

- /SM590000 Optimized software stack:

Red Hat, IBM, open source, and certified ISV AI solutions;

- /SM590000 data fabric:

Secure, unified access to enterprise data across silos;

- /SM590000 AI assistants and agents:

Tools to enhance developer productivity, automate ITOps, and streamline business workflows.

This stack empowers organizations to infuse AI into core business processes while maintaining governance, performance, and security.

## 4.3.3  Strategic outcomes enabled by IBM Power

The following table describes outcome examples enabled by the implementation of AI-solutions on IBM Power processor-based server:

Table 4-2   outcomes examples enabled by IBM Power

| Objective           | Outcome example                                                        |
|---------------------|------------------------------------------------------------------------|
| Transform processes | Accelerate ERP or financial workflows integrated with AI services      |
| Boost productivity  | Roll out new application features faster with GenAI code assistants    |
| Optimize data use   | Reduce TCO and improve resource efficiency via unified data governance |

IBM Power enables clients to put AI to work today securely, efficiently, and at enterprise scale.

## 4.3.4  Uniqueness of the platform

With its AI-optimized infrastructure and enterprise-proven architecture, IBM Power is uniquely positioned to help organizations move from experimentation to real AI-driven transformation. Its scalable ecosystem (spanning hardware, software, data, and automation) makes it a reliable platform for deploying production-grade AI at scale.

A key differentiator of the IBM Power11 processor-based platform lies in its ability to deliver AI capabilities without requiring external GPUs. Unlike conventional assumptions that all AI workloads demand dedicated GPU acceleration, IBM Power11 leverages advanced on-core accelerators integrated directly within each processor core, combined with a system-wide infrastructure design optimized for AI and data-intensive tasks.

This architectural approach enables the deployment of a wide range of AI use cases, such as inferencing, predictive analytics, and cognitive automation, while maintaining enterprise-grade attributes including resilience, reliability, performance, security, and sustainability. By eliminating or reducing dependency on external GPUs, organizations

benefit from simplified infrastructure, reduced energy consumption, and lower total cost of ownership (TCO), all without compromising AI readiness. The IBM Power11 platform is purpose-built to support scalable and secure AI solutions across diverse industry environments.

<!-- image -->

5

Chapter 5.

## Automation and Management

Managing IBM Power based-processor servers effectively requires a combination of tools that provide automation, orchestration, and visibility across the infrastructure. At the core of this management stack is the Hardware Management Console (HMC), which serves as the central point for configuring and monitoring Power servers. HMC enables administrators to manage logical partitions (LPARs), perform firmware updates, and monitor system health. It provides both a graphical interface and a REST API, allowing integration with automation tools for more scalable operations.

Ansible and Terraform bring Infrastructure as Code (IaC) capabilities to IBM Power environments. Ansible is widely used for configuration management and automation of tasks such as patching, user management, and software deployment. It supports Power based-processor servers through modules and collections tailored for AIX, IBM i, and Linux on Power. Terraform complements Ansible by enabling declarative provisioning of infrastructure components, including Power Virtual Servers and PowerVC-managed resources. Together, they allow teams to automate the full lifecycle of infrastructure - from provisioning to configuration - ensuring consistency and reducing manual effort.

PowerVC (Power Virtualization Center) plays a crucial role in managing virtualized environments on IBM Power. Built on OpenStack, PowerVC provides advanced virtualization management capabilities such as image management, dynamic resource allocation, and integration with cloud platforms. It supports automation through REST APIs and integrates with both Ansible and Terraform, enabling seamless orchestration of virtual machines and workloads. By combining HMC, Ansible, Terraform, and PowerVC, organizations can build a robust, automated, and scalable management framework for their IBM Power infrastructure.

This chapter contains the following topics:

- /SM590000 Hardware Management Console overview
- /SM590000 Ansible
- /SM590000 Terraform
- /SM590000 PowerVC

## 5.1  Hardware Management Console overview

The hardware management console (HMC) is a hardware or virtual appliance that is used to configure and manage your systems. The HMC connects to one or more managed systems and provides capabilities for the following primary functions:

- /SM590000 Provide systems management functions, including the following examples:
- -Power off
- -Power on
- -System settings
- -Capacity
- -on Demand
- -Enterprise
- -Pools
- -Shared Processor Pools
- -Performance and Capacity Monitoring
- /SM590000 Starting Advanced System Management Interface (ASMI) for managed systems
- /SM590000 Deliver virtualization management through support for creating, managing, and deleting Logical Partitions, Live Partition Mobility, Remote Restart, configuring SRIOV, managing Virtual IO Servers, dynamic resource allocation, and operating system terminals.
- /SM590000 Acts as the service focal point for systems and supports service functions, including call home, dump management, guided repair and verify, concurrent firmware updates for managed systems, and around-the-clock error reporting with Electronic Service Agent for faster support.
- /SM590000 Provides appliance management capabilities for configuring network, users on the HMC, and updating and upgrading the HMC.

## 5.1.1  HMC Options

Power11 servers can be connected to either the 7063-CR2 HMC or to a Virtual HMC.

Restriction: The 7063-CR1 is not supported by the Power11 servers.

## HMC 7063-CR2

The 7063-CR2 IBM Power HMC (see Figure 2-1) is a second-generation Power processor-based HMC. It includes the following features:

- -6-core IBM Power9 130W processor chip
- -64 GB (4x16 GB) or 128 GB (4x32 GB) of memory
- -1.8 TB of internal disk capacity with RAID1 protection
- -4-ports 1 Gbps Ethernet (RJ-45), 2-ports 10 Gbps Ethernet (RJ-45), two USB 3.0 ports (front side) and two USB 3.0 ports (rear side), and 1 Gbps IPMI Ethernet (RJ-45)
- -Two 900W power supply units
- -Remote Management Service: IPMI port (OpenBMC) and Redfish application programming interface (API)

The base Warranty is 1-year 9x5 with available optional upgrades. A USB Smart Drive is not included.

Figure 5-1 is a picture of a 7063-CR2 HMC.

Figure 5-1   HMC 7063-CR2

<!-- image -->

The 7063-CR2 is compatible with flat panel console kits 7316-TF3, TF4, and TF5.

Note: The 7316-TF3 and TF4 are withdrawn from marketing

## Virtual HMC

Initially, the HMC was sold only as a hardware appliance, including the HMC firmware installed. However, IBM extended this offering to allow the purchase of the hardware appliance or a virtual appliance that can be deployed on ppc64le architectures or x86 platforms.

Any customer with a valid contract can download the HMC from the IBM Entitled Systems Support , or it can be included within an initial Power S1122 or S1124 order.

The virtual HMC supports the following hypervisors:

- /SM590000 On x86 processor-based servers
- -KVM
- -Xen
- -VMware
- /SM590000 On Power processor-based servers
- -IBM PowerVM

The following minimum requirements must be met to install the virtual HMC:

- -16 GB of Memory
- -4 virtual processors
- -2 network interfaces (maximum 4 allowed)
- -1 disk drive (500 GB available disk drive)

For an initial Power S1122 or S1124 order with the IBM configurator (e-config), the HMC virtual appliance can be found by selecting Add software → Other System Offerings (as product selections) and then choosing:

- -5765-VHP for IBM HMC Virtual Appliance for Power V10
- -5765-VHX for IBM HMC Virtual Appliance x86 V10

For more information and an overview of the Virtual HMC, see Virtual HMC appliance (vHMC) overview . For more information about how to install the virtual HMC appliance and all requirements, see Installing the HMC virtual appliance .

## 5.1.2 BMC network connectivity rules for 7063-CR2 HMC

The 7063-CR2 HMC features a baseboard management controller (BMC), which is a specialized service processor that monitors the physical state of the system by using sensors. OpenBMC that is used on 7063-CR2 provides a graphical user interface (GUI) that can be accessed from a workstation that includes network connectivity to the BMC. This connection requires an Ethernet port to be configured for use by the BMC.

The 7063-CR2 provides two network interfaces (eth0 and eth1) for configuring network connectivity for BMC on the appliance.

Each interface maps to a different physical port on the system. Different management tools name  the  interfaces  differently.  The  HMC  task Console  Management → Console Settings → Change BMC/IPMI Network Settings modifies only the Dedicated interface.

The BMC ports are listed in Table 5-1.

Table 5-1 BMC ports

| Management tool                            | Logical port   | Shared/Dedicated   | CR2 physical port    |
|--------------------------------------------|----------------|--------------------|----------------------|
| OpenBMC UI                                 | eth0           | Shared             | eth0                 |
| OpenBMC UI                                 | eth1           | Dedicated          | Management port only |
| ipmitool                                   | lan1           | Shared             | eth0                 |
| ipmitool                                   | lan2           | Dedicated          | Management port only |
| HMC task (change BMC/IPMI Network settings | lan2           | Dedicated          | Management port only |

Figure 1-15 shows the BMC interfaces of the HMC.

Figure 5-2   BMC interfaces

<!-- image -->

The main difference is that the shared and dedicated interface to the BMC can coexist. Each has its own LAN number and physical port. Ideally, the customer configures one port, but both can be configured. The rules for connecting Power based-processor servers to the HMC remain the same as for previous versions.

## 5.1.3 High availability HMC configuration

For the best manageability and redundancy, a dual HMC configuration is suggested. This configuration can be two hardware appliances, or one hardware appliance and one virtual appliance or two virtual appliances.

The following requirements must be met:

- -Two HMCs are at the same version.
- -The HMCs use different subnets to connect to the BMCs.
- -The HMCs can communicate with the servers' partitions over a public network to allow for full synchronization and function.

## 5.1.4 HMC code level requirements

The minimum required HMC version for the Power S1122, and S1124 are V11R1 M1110. V11R1 M1110 is supported on 7063-CR2, and Virtual HMC appliances only. It is not supported on the 7063-CR1 or the 7042 machine types. HMC with V11R1M1110 cannot manage POWER7 processor-based systems.

An HMC that is running V11R1M1110 includes the following features:

- /SM590000 Support for managing Power11 Systems
- /SM590000 Support for new I/O adapters
- /SM590000 VIOS Management Enhancements:
- -Resource Groups
- -IBM i Secure Boot
- -Increase in platform keystore size
- -Remove support for vTPM 1.2
- -Quantum safe LPM
- -Minimum Affinity Score and actions
- /SM590000 Console Management and User Experience Improvements
- -User experience improvements spanning
- Network Topology
- Trusted Keystore
- Import Certificate
- Multi-factor Authentication Allow list
- -Ability to advertise device information via LLDP
- /SM590000 Power Infrastructure Maintenance and Automated Power Platform Updates
- -Execute Power platform updates with minimal touchpoints to enhance simplicity and reduce the risk of human error
- -Experience seamless platform updates with one touch solutions
- -Automatic operational recovery and resiliency
- /SM590000 Autonomous Error Resolution
- -Ability to collect platform logs (FW, hypervisor, HMC, VIOS) from a single interface
- -Ability to create a case and upload logs to the case from the HMC

- /SM590000 Sustainability
- -New energy efficiency mode - higher performance/ watt
- -Partition level energy monitoring
- Real time monitoring and reporting of energy and carbon emissions at the VM/partition level
- -Scheduling of energy modes

## 5.1.5 Keeping your HMC up to date

In recent years, cybersecurity emerged as a national security issue and an increasingly critical concern for CIOs and enterprise IT managers.

The IBM Power processor-based architecture has always ranked highly in terms of end-to-end security, which is why it remains a platform of choice for mission-critical enterprise workloads.

A key aspect of maintaining a secure Power environment is ensuring that the HMC (or virtual HMC) is current and fully supported (including hardware, software, and Power firmware updates).

Outdated or unsupported HMCs represent a technology risk that can quickly and easily be mitigated by upgrading to a current release.

## 5.1.6  New features

The minimum level of the HMC required to support Power11 is V11 R1 M1110. V11 of the HMC will not be supported on the 7063-CR1. HMC V11 will run on the 7063-CR2 or the virtual HMC. Additionally, HMC V11 will not support POWER8 or earlier servers.

HMC V11.1.1110 was GA (generally available) in July 2025. Specific new features include support for managing Power11 systems and support for new I/O adapters.

## Virtualization Management new features include:

- /SM590000 Resource Groups
- /SM590000 IBM i Secure Boot
- /SM590000 Increase in platform keystore size
- /SM590000 Remove support for vTPM 1.2
- /SM590000 Quantum safe LPM
- /SM590000 Minimum Affinity Score and Actions

## Console Management and User Experience Improvements include:

- /SM590000 User experience improvements spanning
- -Network topology
- -Trusted Keystore
- -Import certificate
- -Multi-factor authentication allow list
- /SM590000 Ability to advertise device information via LLDP

## Power Infrastructure Maintenance and automated Power Platform Updates

- /SM590000 Execute Power platform updates with minimal touchpoints to enhance simplicity and reduce the risk of human error. Includes the ability to update system firmware, VIOS and I/O adapters from a single update flow.

- /SM590000 Experience seamless platform updates with our advanced one-touch solutions, designed for both evacuation and return or in-place updates, each has automatic operational recovery and resiliency
- /SM590000 Validation for LPM and VIOS redundancy (VIOS maintenance readiness check)
- /SM590000 Ability to automatically migrate partitions and return as part of the update process.

## Autonomous Error Resolution

- /SM590000 Reduce problem resolution time with ability to collect platform logs (FW, Hypervisor, HMC, VIOS) from a single Interface
- /SM590000 Ability to create a case and upload logs to the case from the HMC

## Sustainability

- /SM590000 New Energy Efficiency mode - Higher Performance/Watt
- /SM590000 Partition Level Energy Monitoring - Real-time monitoring and reporting of energy and carbon emissions at the VM/partition level.
- /SM590000 Scheduling of energy modes

## 5.1.7  Using the Automated Maintenance tool

This section shows using the new automated maintenance tool provided in the IBM Power11 HMC.

## Launch Point

Prior to launching the new automated maintenance, the system should have the latest 11.10 firmware installed.

1. To start the process, we choose the option ' Update system, VIOS, adapter levels '. which is a new action menu introduced with Firmware 11.10. This is shown in Figure 5-3.

Figure 5-3   Start update

<!-- image -->

This will start a wizard that will guide you through the process:

- -Import update files option:
- 'Import files to HMC filesystem and perform update' or 'Import files only'
- -Check System readiness:
- System needs to be in 'Ready' state in order to proceed with update process
- -Select the source file location
2. Select ' Update/Upgrade ' type as shown in Figure 5-4.
3. In order to preserve the system availability, for disruptive upgrades/updates, the partitions migration panel will be shown as in Figure 5-5.

Figure 5-4   Upgrade type

<!-- image -->

Figure 5-5   Choose Process

<!-- image -->

4. These are the options that can be selected:
2. -Remote HMC switch enables to migrate the partitions to a system managed by remote HMC. When selected partitions are not automatically migrated back to the system after the update.
3. -By default, all the partitions are selected for migration. Partitions can be individually selected to migrate by toggling Server evacuation switch.
4. -In case of selected partitions for migration, partition migration sequence can be specified for a set of partitions that needs to be migrated initially.

Finally, all the update process is automatically done, and we can see the results as shown in Figure 5-6.

Figure 5-6   Figure 5 - Update status

<!-- image -->

In conclusion this solution provides an unmatched Business Resiliency with Zero Planned Downtime delivered through platform automation capabilities integrated with IBM Concert's AI-infused workloads. It enables faster more frequent maintenance updates, keeping systems secure, stable, and compatible with evolving software and hardware requirements, lowering risks of performance degradation, security breaches or unplanned downtimes.

## 5.2  Ansible

Ansible is an open-source, cross-platform tool for resource provisioning automation that DevOps professionals use for continuous deployment (CD) of software code by leveraging an ,IAC approach. The Ansible automation platform has evolved to deliver sophisticated automation solutions for operators, administrators, and IT decision-makers across various technical disciplines. It is an enterprise automation solution with flourishing open-source software. It operates on several UNIX like platforms, and can manage systems like UNIX and Microsoft architectures. It comes with descriptive language for describing system settings.

Because of the broad acceptance of the Ansible platform, its open-source design, and its wide support for many devices and platforms, it is becoming a dominant tool in the market. However, it is also common to use other automation tools with Ansible to do more complex

automation. For example, many companies use Ansible with Terraform to provide automatic provisioning of their infrastructure.

## Ansible architecture

As shown in Figure 5-7, the Ansible architecture consists of an Ansible Controller and one or more Ansible client hosts. The controller runs automation tasks and houses Ansible collections, which contain modules, plug-ins, and roles defining the actions Ansible can perform on client nodes.

Figure 5-7   Simplified Ansible architecture

<!-- image -->

## Playbooks

The heart of Ansible Automation Ansible playbooks are YAML files that define sequences of tasks to run on remote hosts. These tasks can range from installing packages to configuring services or copying files. Playbooks enable IT teams to automate infrastructure provisioning, configuration management, application deployment, and more.

## Why choose Ansible

Ansible offers numerous benefits for IT professionals seeking to improve efficiency, scalability, and consistency in their infrastructure. Here are some key advantages:

- /SM590000 Versatility: Ansible supports a wide range of devices and can scale to accommodate growing environments and automation needs.
- /SM590000 Agentless architecture: Ansible manages devices by using Secure Shell (SSH), which eliminates the need for agents on target systems.
- /SM590000 Flexibility: Ansible can be used for simple CLI tasks and complex workflows that are defined in playbooks.
- /SM590000 Extensive module library: Ansible provides a rich collection of modules for managing various systems, cloud infrastructures, and OpenStack.
- /SM590000 Declarative approach: With the Ansible declarative syntax, you can define the state of a system, and Ansible takes the necessary steps to achieve it.

- /SM590000 Ease of learning: The Ansible YAML syntax and minimal learning curve make it accessible to IT professionals at all levels.

Ansible is a powerful automation tool that can help organizations improve efficiency, scalability, and reliability in their IT infrastructure. By leveraging Ansible playbooks, IT teams can streamline routine tasks, automate complex workflows, and help ensure consistent configurations across their environments.

## Options for implementing Ansible

As you decide to implement Ansible for IT management, it is essential to select the correct product and support level to meet your organization's needs. This section describes some of the options that are available to you.

## Ansible Community

The community versions of Ansible primarily include the following ones:

- /SM590000 Ansible Core

Ansible Core is a fundamental part of Ansible. It provides the core automation engine. It is an open-source tool that includes the basic functions for configuration management, application deployment, and task automation. Ansible Core includes modules, plug-ins, and the CLI that is needed to run playbooks and manage configurations.

- /SM590000 AWX

AWX is the upstream, open-source project that serves as the community version of Red Hat Ansible Tower. AWX provides a web-based UI, Representational State Transfer (REST) API, and task engine for managing Ansible automation at scale. AWX offers role-based access control (RBAC), job scheduling, graphical inventory management, and more. It helps users manage and scale automation efforts.

- /SM590000 Ansible Collections

Ansible Collections are pre-packaged modules, roles, and plug-ins that are created and shared by the community. With Collections, users can extend Ansible functions with more content that is often maintained by the community or specific organizations. Collections can be downloaded from Ansible Galaxy, a community hub for sharing and discovering Ansible content.

- /SM590000 Ansible Galaxy

Ansible Galaxy is a repository for sharing and discovering Ansible roles and collections. It is a community-driven platform where users can find reusable Ansible content to simplify automation tasks. It provides a searchable repository of roles and collections that are created by the Ansible community, which can be integrated into your automation workflows.

These community versions are suitable for individual users, small teams, and development environments but lack the formal support and advanced features that are provided by Red Hat Ansible Automation Platform.

## Ansible Automation Platform

Ansible Automation Platform is a subscription-based enterprise solution that combines over 20 community projects into a fully supported automation platform. Ansible Automation Platform provides curated, certified, and validated Ansible Collections and roles from partners like IBM, Juniper, Cisco, and public cloud providers.

Here are the key considerations for choosing Ansible Automation Platform:

- /SM590000 Support level: Ansible Automation Platform offers enterprise-grade support, which includes SLAs for security, compatibility, and upgrades. Community options might have limited support.
- /SM590000 Features: Ansible Automation Platform includes features beyond Ansible Core, such as a web interface and integration with other tools.
- /SM590000 Cost: Ansible Automation Platform is a subscription-based product, but community options are available at no charge. Scale and complexity: For large organizations with complex automation needs, Ansible Automation Platform might be the better choice due to its enterprise-grade features and support.

By carefully evaluating these factors, you can select the Ansible offering that best aligns with your organization's goals, budget, and support requirements.

## Using Ansible to automate your IBM Power infrastructure

Ansible is a powerful automation tool that brings significant value to managing IBM Power based-processor servers. Here are several key use cases where Ansible enhances efficiency, consistency, and scalability in Power environments:

1. System Configuration and Provisioning

Ansible automates the setup and configuration of AIX, IBM i, and Linux on Power based-processor servers. This includes tasks like user and group management, network configuration, software installation, and system tuning. By using Ansible playbooks, administrators can ensure consistent configurations across multiple systems, reducing manual errors and speeding up provisioning.

2. Patch Management and Compliance

Keeping systems up to date is critical for security and stability. Ansible can automate the patching process for AIX and IBM i, including downloading patches, applying them, and verifying system health post-update. It also supports compliance checks by validating system configurations against predefined baselines, helping organizations meet regulatory and security standards.

3. Integration with HMC and PowerVC

Ansible collections for IBM Power include modules that interact with the Hardware Management Console (HMC) and PowerVC. This enables automation of tasks such as LPAR creation, VIOS configuration, and virtual machine lifecycle management. Combined with dynamic inventory capabilities, Ansible can discover and manage Power infrastructure components in real time.

For more information on implementing automation with Ansible in an IBM Power environment refer to this IBM Redbook: Using Ansible for Automation in IBM Power Environments , SG24-8551

## 5.3  Terraform

Terraform is an open source tool originally developed by HashiCorp and now owned y IBM. It is written in the Go programming language and compiles down into an executable named Terraform. Terraform is an infrastructure as code tool that lets you build, change, and version cloud and on-premises resources safely and efficiently. Terraform provides a mechanism to access any API for any cloud provider to manage infrastructure as a service (IaaS).

Figure 5-8 shows the process involved in calling the API. The definition of which APIs to call is defined in configuration files. These configuration files are the code in that is referenced in Infrastructure as code.

Figure 5-8   Terraform functionality

<!-- image -->

Terraform allows users to define and provision infrastructure using a high-level configuration language called HashiCorp Configuration Language (HCL). With Terraform, infrastructure components such as servers, databases, networking, and storage can be described in code, enabling version control, collaboration, and repeatability. This approach eliminates the need for manual setup and reduces the risk of configuration drift across environments.

Terraform operates through a workflow that includes writing configuration files, initializing the working directory, planning changes, and applying them. The terraform init command sets up the environment by downloading necessary provider plugins. The t erraform plan command then creates an execution plan, showing what actions Terraform will take to reach the desired state. Finally, terraform apply executes the plan, making the actual changes to the infrastructure. Terraform maintains a state file that tracks the current state of the infrastructure, which is essential for determining what changes need to be made during future runs.

One of the key strengths of Terraform is its provider ecosystem, which allows it to manage resources across a wide range of platforms, including AWS, Azure, Google Cloud, Kubernetes, and many others. This makes it a powerful tool for managing hybrid and multi-cloud environments. Additionally, Terraform supports modules, which are reusable configurations that promote consistency and reduce duplication. By codifying infrastructure, Terraform enables DevOps practices such as continuous integration and delivery (CI/CD), infrastructure testing, and automated deployments.

Figure 5-9 on page 126 shows how Terraform works through defining your intended end point through configuration files which are then placed into a plan and finally applied through infrastructure providers.

Figure 5-9   Terraform process

<!-- image -->

## Track your infrastructure

Terraform generates a plan and prompts you for your approval before modifying your infrastructure. The state of your infrastructure is kept in a file named "terraform.tfstate", which can be held in Git, Gitlab or HCP Terraform to version, encrypt, and securely share it with your team. This acts as a single source of truth for your environment.

## Automate Changes

Terraform configuration files are declarative, describing the end state. So are easy to automate with tools like Ansible.

## Standardize configurations

Terraform provides standardization in modules. A module consists of a collection of .tf and .tf.json files kept together in a directory. Modules are the main way to package and reuse resource configurations with Terraform.

## Collaborate

Since Terraform can be distributed as configuration files and version controlled in applications like git, GitHub and HCP Terraform, these are ideal locations to share and collaborate.

## Combining Ansible and Terraform

Terraform connects to any provider, like Ansible, to manage you infrastructure. Browse the Terraform registry for providers. The Terraform Provider for Ansible provides a more straightforward and robust means of executing Ansible automation from Terraform rather a than local-exec 1 . Figure 5-10 shows the Ansible provider entry in the registry.

Figure 5-10   Terraform Ansible provider

<!-- image -->

The prerequisites for using the Ansible provider are as follows;

1. Install Go

For installation instructions, refer to the official installation guide .

2. Install Terraform:

Install the ppc64le version for operation on IBM Power. Installation instructions are found on the GitHub registry.

3. Install Ansible

To install Ansible refer to the Ansible official installation guide

For more information on Terraform in the IBM Power environment, refer to the IBM Redbook publication Modernization Techniques for IBM Power , SG24-8582.

## 5.4  PowerVC

IBM PowerVC is an advanced virtualization and cloud management platform built on OpenStack, specifically designed for managing virtualized workloads on IBM Power based-processor servers. It supports AIX, IBM i, and Linux operating systems and provides a unified interface for deploying, managing, and automating virtual machines (VMs) across Power environments. PowerVC simplifies the creation of private clouds and integrates seamlessly with higher-level cloud orchestrators, such as Ansible, Terraform, and Red Hat OpenShift, enabling hybrid cloud strategies.

1   https://developer.hashicorp.com/terraform/language/resources/provisioners/local-exec

PowerVC offers two editions: Standard Edition and Private Cloud Edition. The Standard Edition includes core virtualization management features such as:

- /SM590000 VM image capture, import/export, and deployment
- /SM590000 Policy-based VM placement for optimized resource utilization
- /SM590000 Snapshots and cloning for backup and testing
- /SM590000 Live VM mobility and remote restart for high availability
- /SM590000 Role-based access control and automated I/O configuration

The Private Cloud Edition builds on this by adding:

- /SM590000 A self-service portal for end users to provision VMs
- /SM590000 Approval workflows for provisioning requests
- /SM590000 Prebuilt deployment templates
- /SM590000 Cloud management policies and metering for charge back

PowerVC also supports Dynamic Resource Optimization (DRO), which automatically balances workloads based on CPU and memory usage, and Simplified Remote Restart, which ensures VMs can be restarted on alternate hosts in case of failure. These features reduce administrative overhead and improve system resilience.

NovaLink is a lightweight, Linux-based virtualization management interface that acts as a bridge between PowerVC (IBM's cloud and virtualization manager) and PowerVM (the hypervisor on IBM Power based-processor servers). It enables direct, scalable, and efficient control of virtual machines (VMs) and system resources without relying solely on the traditional Hardware Management Console (HMC).

Installed on the Power System: NovaLink runs as a service on a dedicated Linux partition (LPAR) on the same Power server it manages. This LPAR communicates directly with the PowerVM hypervisor the HMC, which manages systems externally. NovaLink has direct access to the hypervisor APIs. This allows for faster and more granular control of virtualization tasks like VM creation, deletion, migration, and resource allocation. This makes PowerVC more responsive and scalable, especially in environments with many VMs or frequent provisioning changes.

Table 5-2   Comparisons of PowerVC with HMC management:

| Feature/ Capability                 | PowerVC                                                                  | HMC                                 |
|-------------------------------------|--------------------------------------------------------------------------|-------------------------------------|
| Policy-Based Placement              | Automatically places VMs based on resource availability and policies     | Manual placement                    |
| Integration with Cloud Tools        | Integrates with OpenStack, Red Hat OpenShift, and hybrid cloud platforms | No native integration               |
| Live VM Migration                   | Fully supported and automated                                            | Supported but requires manual steps |
| Dynamic Resource Optimization (DRO) | Automatically balances workloads across hosts                            | Not available                       |
| Simplified Networking Storage Setup | Automated configuration of virtual I/O, storage, and networking          | Manual configuration required       |

| Feature/ Capability   | PowerVC                                                         | HMC                                            |
|-----------------------|-----------------------------------------------------------------|------------------------------------------------|
| NovaLink Support      | Works directly with NovaLink for faster, scalable VM operations | HMC is external and less scalable              |
| Scalability           | Designed for large-scale environments with many VMs             | Best suited for smaller or static environments |
| User Interface        | Modern, web-based UI with dashboards and templates              | Traditional interface, more administrative     |

.

<!-- image -->

Chapter 6.

6

## Operating Systems

IBM Power based-processor servers support a trio of robust operating systems - IBM i, AIX, and Linux - each tailored to meet distinct enterprise computing needs. IBM i is an integrated operating environment known for its exceptional reliability, security, and ease of management. It includes a built-in database (Db2 for i), middleware, and development tools, making it ideal for running mission-critical business applications with minimal administrative overhead. Its tight integration and backward compatibility make it a favorite for industries like finance, manufacturing, and retail.

AIX, IBM's UNIX operating system, is designed for high-performance, scalable enterprise workloads. Built on a UNIX System V base and enhanced with IBM innovations, AIX offers advanced features like dynamic system tuning, workload partitioning, and robust security. It is widely used in environments that demand stability and performance, such as ERP systems, databases, and analytics platforms. AIX is optimized for IBM Power hardware, ensuring seamless integration and efficient resource utilization.

IBM Power also supports enterprise-grade Linux distributions, including Red Hat Enterprise Linux (RHEL) and SUSE Linux Enterprise Server (SLES). These Linux environments provide flexibility and open-source innovation, making them ideal for cloud-native applications, containerized workloads, and AI/ML development. Running Linux on Power enables organizations to leverage the performance advantages of the Power architecture while maintaining compatibility with the broader Linux ecosystem. Together, these operating systems make IBM Power a versatile platform capable of supporting a wide range of modern and legacy workloads.

Complementing these operating systems is Red Hat OpenShift, a Kubernetes-based container platform that runs natively on IBM Power based-processor servers. OpenShift enables organizations to build, deploy, and manage containerized applications across hybrid cloud environments with consistency and scalability. OpenShift brings a unified DevOps experience and supports modern application architectures, including microservices and AI workloads. This integration empowers enterprises to modernize their IT infrastructure while leveraging the performance, security, and reliability of IBM Power

This chapter provides the following topics:

- /SM590000 Subscription licensing
- /SM590000 AIX
- /SM590000 IBM i

- /SM590000 Linux on IBM Power
- /SM590000 Red Hat OpenShift
- /SM590000 Intro to KVM support
- /SM590000 PowerVM Virtual I/O Server
- /SM590000 Setting your LPAR compatibility mode

## 6.1  Subscription licensing

IBM offers subscription-based licensing models for both AIX and IBM i, providing customers with greater flexibility, predictability, and cost efficiency. These models allow organizations to license the operating system and associated software on a monthly or annual basis, rather than through traditional perpetual licenses. This approach aligns with modern IT consumption trends, enabling businesses to scale usage up or down based on workload demands while simplifying budgeting and procurement processes. Subscription licensing also includes access to updates, patches, and IBM support, ensuring systems remain secure and up to date.

For IBM i, subscription licensing includes the core operating system along with integrated middleware such as Db2, security features, and application development tools. Similarly, AIX subscription licensing covers the base OS and can be bundled with additional IBM software components. These subscriptions are available for deployment on IBM Power based-processor servers, including Power11, and are particularly well-suited for hybrid cloud environments where agility and operational efficiency are key. By adopting subscription licensing, organizations can modernize their licensing strategy while continuing to leverage the reliability and performance of AIX and IBM i.

## 6.1.1  AIX subscription licensing

AIX Standard Edition, AIX Enterprise Edition, IBM Private Cloud Edition and IBM Private Cloud Edition with AIX are available under a subscription licensing model that provides access to an IBM program and IBM software maintenance for a specified subscription term (one or three years). The subscription term begins on the start date and ends on the expiration date, which is reflected at the IBM ESS website.

Customers are licensed to run the product through the expiration date of the one- or three-year subscription term and then can renew at the end of the subscription to continue using the product. This model provides flexible and predictable pricing over a specific term, with lower up-front cost.

Another benefit of this model is that the licenses are customer number entitled, which means they are not tied to a specific hardware serial number as with perpetual licenses. Therefore, the licenses can be moved between on-premises and cloud if needed, some-thing that is becoming more of a requirement with hybrid workloads.

The product IDs for the subscription licenses are listed in Table 6-1.

Table 6-1 Subscription license product IDs (one or three year terms)

| Product ID   | Description                                                 |
|--------------|-------------------------------------------------------------|
| 5765-2B1     | IBM AIX 7 Standard Edition Subscription 7.3.0               |
| 5765-2E1     | IBM AIX Enterprise Edition Subscription 1.10.0              |
| 5765-2C1     | IBM Private Cloud Edition with AIX 7 Subscription 1.10.0    |
| 5765-6C1     | IBM Private Cloud Edition Subscription 1.10.0 (without AIX) |

The subscription licenses are orderable through IBM configuration tools. The AIX perpetual and monthly term licenses for standard edition are still available.

## 6.1.2  IBM i subscription licensing

IBM offers several subscription licensing options for IBM i, designed to provide flexibility and align with modern IT consumption models. These subscriptions are typically available on IBM Power based-processor servers, including Power11, and are ideal for clients looking to simplify licensing, reduce upfront costs, and scale more easily.

- /SM590000 The core offering is the IBM i Operating System Subscription, which includes the IBM i OS along with integrated middleware such as Db2 for i, security features, and development tools. This subscription is licensed on a per-core basis and is available in monthly or annual terms, making it easier for organizations to align software costs with usage. Support and updates are included, ensuring systems remain secure and current without the need for separate maintenance agreements.
- /SM590000 In addition to the base OS subscription, IBM provides IBM i Value Packages, which bundle the operating system with additional IBM software like Rationalfi Development Studio for i, IBM Db2 Mirror for i, and IBM i Access Client Solutions. These packages are tailored to support specific workloads or modernization efforts.
- /SM590000 For cloud-based deployments, the IBM i Cloud Subscription offers a flexible, usage-based model that includes the OS, support, and infrastructure when running IBM i on platforms like IBM Power Virtual Server. This is particularly beneficial for organizations adopting hybrid or cloud-first strategies, as it enables scalable, enterprise-grade IBM i environments without the complexity of traditional licensing.

The AIX operating system is a secure, scalable, and robust open standards-based UNIX system. For over thirty years, AIX has been the cornerstone of mission-critical computing for enterprise organizations in highly complex industries, evolving to introduce a wealth of new hybrid cloud and open-source capabilities.

AIX 7.3 is the latest AIX release available in the market. It builds on a solid foundation by offering new functions and capabilities that further enhance performance, scalability, availability, and security, all while preserving application-binary compatibility to safeguard IT investments in AIX.

Coupled with the IBM Power11 processor-based systems, AIX 7.3 provides an optimized and more resilient computing platform that adapts to changing business demands, including new cloud use cases and improved economics.

## 6.2.1  AIX 7.3 Key Features

Here is a list of the key features in the latest AIX release.

- /SM590000 Workload Scalability Automation: AIX 7.3 offers enhanced workload scalability, improved cloud automation via Ansible, and over 300 open-source packages through the AIX Toolbox for Open Source Software, enabling modern application development.
- /SM590000 Live Kernel Update: Introduced in AIX 7.2 and enhanced in 7.3, this feature allows interim fixes, service packs, and technology level updates without reboots, supporting PowerVC-managed environments and Power Enterprise Pool systems for resource optimization.

## 6.2  AIX

- /SM590000 High Availability Disaster Recovery: IBM PowerHA and VM Recovery Manager provide automated recovery and multi-site replication, minimizing downtime and ensuring business continuity in hybrid or public cloud environments.
- /SM590000 AI Integration: AIX workloads are a natural source for AI. These systems host a tremendous amount of high-quality data on customer behavior and transactional information that can be further leveraged for AI development, enabling machine and deep learning for actionable insights on a unified platform.
- /SM590000 Cloud Flexibility: AIX enables private, on-premises cloud transformation with PowerVC, offering hybrid cloud functionality for seamless AIX VM import/export and software-defined infrastructure for SAN-less DevOps environments. Available via IBM Power Systems Virtual Server, AIX supports mission-critical databases with enhanced scalability, cloud automation, robust security, and flexible licensing. Workloads can run in hybrid or public clouds without refactoring, ensuring reliability and efficiency.

## 6.2.2  Supported Levels

Currently, the IBM Power11 processor-based server supports the following minimum levels of the AIX operating system when installed by using direct I/O connectivity:

- -AIX 7.3 with the 7300-03 Technology Level and Service Pack 1 or later
- -AIX 7.3 with the 7300-02 Technology Level and Service Pack 4 or later
- -AIX 7.2 with the 7200-05 Technology Level and Service Pack 10 or later

Currently, the IBM Power11 processor-based server supports the following minimum levels of AIX operating system when installed using virtual I/O:

- -AIX 7.3 with the Technology Level 7300-03 and Service Pack 0 or later
- -AIX 7.3 with the Technology Level 7300-02 and Service Pack 2 or later
- -AIX 7.2 with the Technology Level 7200-05 and Service Pack 8 or later

## Important:

- -Starting with AIX Release 7.3 Technology Level 3 Service Pack 1, AIX logical partitions operate in native Power11 processor compatibility mode, fully leveraging Power11's advanced capabilities.
- -Logical partitions running versions older than AIX Release 7.3 Technology Level 3 Service Pack 1 operate in POWER9 or Power10 processor compatibility mode on Power11 systems.
- -Logical partitions running AIX Release 7.2 can operate in POWER9 or Power10 processor compatibility mode.

## 6.2.3  AIX Maintenance levels

IBM periodically releases maintenance packages (service packs (SPs) or technology levels (TLs) for the AIX operating system. For more information about these packages, downloading, and obtaining the installation packages, see IBM Fix Central. For more information about hardware features compatibility and the corresponding AIX Technology Levels, see IBM Support.

The Service Update Management Assistant (SUMA), which can help you automate the task of checking and downloading operating system downloads, is part of the base operating system. For more information about the suma command, see Service Update Management Assistant (SUMA).

The Fix Level Recommendation Tool (FLRT) provides cross-product compatibility information and fix recommendations for IBM products. Use FLRT to plan upgrades of key components or to verify the current health of a system.

The IBM AIX Operating System Service Strategy and Best Practices is a free resource available to AIX clients and gives insight into the AIX service strategy, while also providing helpful lifecycle information to best maintain your version of AIX. For more information on AIX, visit AIX on IBM Power.

For additional information:

- /SM590000 AIX support lifecycle information

https://www.ibm.com/support/pages/aix-support-lifecycle-information

- /SM590000 System Software Maps

https://www.ibm.com/support/pages/system-software-maps

- /SM590000 System to AIX maps

https://www.ibm.com/support/pages/system-aix-maps

## 6.2.4  Licensing

The AIX operating system is available in the following editions:

- /SM590000 AIX Standard Edition
- /SM590000 AIX Enterprise Edition
- /SM590000 AIX Cloud Edition

The Enterprise and Cloud Editions include Power-related software, typically required to manage larger IBM Power environments, including those in hybrid clouds.

There are two licensing models for AIX:

- /SM590000 CPU-based licensing
- /SM590000 Subscription licensing

In the first case, AIX licenses can be ordered together with the server or purchased later as a MES upgrade for the server. The license grants you the right to use AIX on a specific server. If you require support for AIX, you must have a valid Software Maintenance Agreement (SWMA) for AIX.

Subscription licensing is a new model that offers greater flexibility in AIX acquisition. The subscription license includes access to IBM software maintenance for a specified subscription term (1 or 3 years). After this term, you can renew the subscription if you continue using AIX. This model provides flexible and predictable pricing over a specific term with lower upfront acquisition costs.

Another benefit is that the licenses are customer-number-entitled, meaning you can use the licenses on any IBM Power server you have in your environment. You can even move them between on-premises, your private cloud, and public cloud if needed.

## 6.2.5  New AIX Editions

The IBM AIX operating system is an open standards-based UNIX operating system that has been the foundation of mission-critical workloads and databases for tens of thousands of customers for over 35 years. AIX provides an enterprise-class IT infrastructure that delivers

the reliability, availability, performance, and security that is required for organizations to be successful in a global economy.

Now, IBM offers the following updates and enhancements to the AIX operating system and products that include AIX for IBM Power8, Power9, Power10 and Power11 technology based servers:

- /SM590000 IBM AIX 7 Enterprise Edition 1.13
- /SM590000 IBM Private Cloud Edition 1.13
- /SM590000 IBM Private Cloud Edition with AIX 1.13
- /SM590000 VM Recovery Manager 1.9

## IBM AIX 7 Enterprise Edition 1.13

IBM has updated the AIX 7 Enterprise Edition and its corresponding subscription offering to version 1.13. The bundled software components offered with AIX 7 Enterprise Edition 1.13 (5765-CD3 and 5765-2E1) now include:

- /SM590000 IBM AIX 7.3 TL3 or IBM AIX 7.2 TL5
- /SM590000 IBM PowerSC 2.3
- /SM590000 IBM PowerVC for Private Cloud 2.3.1
- /SM590000 IBM VM Recovery Manager HA 1.9
- /SM590000 IBM Tivolifi Monitoring 6.3

The bundle components are updated as follows:

- /SM590000 AIX 7.3 TL3 has been updated with service pack 1
- /SM590000 AIX 7.2 TL5 has been updated with service pack 10
- /SM590000 IBM PowerSC 2.3 has been updated from 2.2 to 2.3
- /SM590000 IBM PowerVC for Private Cloud has been updated from 2.3.0 to 2.3.1
- /SM590000 IBM VM Recovery Manager HA has been updated from 1.8 to 1.9

## Additional information

- /SM590000 Clients with active Software Maintenance (SWMA) or subscriptions for earlier versions of AIX Standard Edition or AIX Enterprise Edition are entitled to upgrade at no charge. To update, download, or install, see the IBM Entitled Systems Support website.
- /SM590000 Clients can choose either AIX 7.3 TL3 or AIX 7.2 TL5.
- /SM590000 Clients selecting AIX 7.2 TL5 can later upgrade to AIX 7.3 TL3 at any time, provided SWMA or subscription is current.
- /SM590000 Clients with AIX Enterprise Edition can trade up to IBM Private Cloud Edition with AIX.

## IBM Private Cloud Edition 1.13

IBM has updated the Private Cloud Edition and its corresponding subscription offering to version 1.13. The bundled software components offered with Private Cloud Edition 1.13 (5765-ECB and 5765-6C1) now include:

- /SM590000 IBM PowerSC 2.3
- /SM590000 IBM PowerVC for Private Cloud 2.3.1
- /SM590000 IBM VM Recovery Manager DR 1.9
- /SM590000 IBM Tivoli Monitoring 6.3

The bundle components are updated as follows:

- /SM590000 IBM PowerSC 2.3 has been updated from 2.2 to 2.3
- /SM590000 IBM PowerVC for Private Cloud has been updated from 2.3.0 to 2.3.1
- /SM590000 IBM VM Recovery Manager DR has been updated from 1.8 to 1.9
- /SM590000 Cloud Management Console (CMC) has been updated from 1.22 to 1.23.

## 6.3  IBM i

## IBM Private Cloud Edition with AIX 1.13

IBM has updated Private Cloud Edition with AIX and its corresponding subscription offering to version 1.13. The bundled software components offered with Private Cloud Edition with AIX 1.13 (5765-CBA and 5765- 2C1) now include:

- /SM590000 IBM AIX 7.3 TL3 or IBM AIX 7.2 TL5
- /SM590000 IBM PowerSC 2.3
- /SM590000 IBM PowerVC for Private Cloud 2.3.1
- /SM590000 IBM VM Recovery Manager DR 1.9
- /SM590000 IBM Tivoli Monitoring 6.3

The bundle components are updated as follows:

- /SM590000 AIX 7.3 TL3 has been updated with service pack 1
- /SM590000 AIX 7.2 TL5 has been updated with service pack 10
- /SM590000 IBM PowerSC 2.3 has been updated from 2.2 to 2.3
- /SM590000 IBM PowerVC for Private Cloud has been updated from 2.3.0 to 2.3.1
- /SM590000 IBM VM Recovery Manager DR has been updated from 1.8 to 1.9
- /SM590000 Cloud Management Console (CMC) has been updated from 1.22 to 1.23.

## Additional information for IBM Private Cloud Edition

- /SM590000 Private Cloud Edition 1.13 and Private Cloud Edition 1.13 with AIX 7 include an entitlement for subscription to IBM Cloud Management Console (5765-CMT) for the same term as their SWMA.
- /SM590000 Clients with active SWMA or subscriptions for earlier versions of Private Cloud Edition or Private Cloud with AIX are entitled to upgrade at no charge. To update, download, or install, see the IBM Entitled Systems Support website.
- /SM590000 Clients can choose either AIX 7.3 TL3 or AIX 7.2 TL5.
- /SM590000 Clients selecting AIX 7.2 TL5 can later upgrade to AIX 7.3 TL3 at any time, provided SWMA or subscription is current.
- /SM590000 Clients with AIX Enterprise Edition can trade up to Private Cloud Edition with AIX.

## VM Recovery Manager 1.9

VM Recovery Manager provides automated VM management in the data center and disaster recovery management between sites. In IBM Power Virtual Server public the product is called DR Automation. DR Automation provides automated disaster recover management between geographically dispersed Power Virtual Server data centers.

- /SM590000 Work group support for HA-DR-HA
- /SM590000 Failover rehearsal for IBM Power Virtual Server

IBM i is a powerful, integrated operating system designed to run on IBM Power hardware. It is known for its robustness, security, and ease of management. Over the years, it has evolved through several naming transitions, reflecting both technological advancements and IBM's strategic branding changes.

IBM i remains a premier enterprise computing platform, renowned for its robust security, scalability, and seamless integration. Its ability to support modern workloads while preserving legacy application compatibility makes it a cornerstone in industries like finance, retail, and manufacturing, where unwavering reliability and performance are paramount. IBM's ongoing innovation ensures IBM i, a key component of IBM Power, continues to empower enterprises to efficiently manage and deploy their most critical applications, building on its legacy of stability and business continuity.

## 6.3.1  Intro to IBM i

IBM i is a highly integrated and dependable platform that streamlines IT infrastructure by combining the operating system, Db2 for i database, security, and middleware into a single, cohesive environment. This deep integration minimizes the need for complex configurations and third-party components, making it easier to deploy, manage, and scale applications. As a result, organizations benefit from a lower total cost of ownership (TCO) and reduced administrative overhead - especially valuable in environments with limited IT resources.

One of IBM i's standout strengths is its exceptional reliability, availability, and serviceability (RAS). Designed to support mission-critical workloads, it offers features such as automatic error detection, self-healing capabilities, and robust high availability and disaster recovery options. These capabilities make IBM i a trusted platform across industries like finance, healthcare, and manufacturing, where system uptime and data integrity are paramount. Additionally, IBM i supports both legacy and modern application development, allowing businesses to run traditional RPG and COBOL applications alongside modern languages like Java, Python, and Node.js, while integrating with open-source tools and cloud-native services.

Since 2008, IBM has consistently released new versions of IBM i approximately every three years, with IBM i 7.6 being the latest. Each release introduces new features, workload support, and language enhancements while maintaining backward compatibility - allowing customers to preserve and extend their existing investments. IBM i is recognized as one of the most secure, self-optimizing, and scalable operating systems in the world. IBM continues to deliver updates and enhancements throughout each release's lifecycle via Program Temporary Fixes (PTFs) and Technology Refreshes (TRs). A key differentiator in the enterprise OS market is IBM's long-term commitment to IBM i, demonstrated by its publicly available roadmap, which currently extends to 2035 and is updated annually - underscoring IBM's dedication to the platform's future. The roadmap is shown in Figure 6-1.

Figure 6-1   IBM i support matrix

<!-- image -->

For more information on IBM i and its latest functions refer to the IBM Redbook IBM i 7.6 features and function , SG24-8588

## 6.3.2  Supported levels

For the Power S1122, VIOS is required for IBM i support. The IBM i partitions must be set to 'restricted I/O' mode and there are limitations to the maximum size of the partition - up to four cores per IBM i partition are supported. Multiple IBM i partitions can be created and run concurrently, and each individual partition can have up to four cores.

The minimum levels supported are:

- /SM590000 IBM i 7.6 with Power11 GA PTF Group, or later
- /SM590000 IBM i 7.5 TR6, or later
- /SM590000 IBM i 7.4 TR12, or later

The Power S1124 supports the following minimum levels of the IBM i operating system both native and as a client of VIOS:

- /SM590000 IBM i - 7.4 TR12

- /SM590000 IBM i - 7.5 TR6

- /SM590000 IBM i - 7.6

## 6.3.3  New IBM i Features supported by Power11

IBM i 7.6 Power11 GA PTF Group, IBM i 7.5 Hardware Technology Refresh 6, and IBM i 7.4 Hardware Technology Refresh 12 all support the new IBM i Power based-processor servers with Power11 technology and their new I/O offerings.

There are several new features that are available only with the new servers with Power11 technology and newer code levels for IBM i:

- /SM590000 IBM i 7.6 adds an NVMe Hot Spare feature to allow immediate replacement of a mirror-protected disk unit under a failing NVMe device. For more information on this feature see NVMe Hot Spare.
- /SM590000 IBM i 7.6 Secure boot feature is used to verify the authenticity of the boot process. Security administrators can extend the existing secure boot technology used to verify the integrity of PowerVM firmware, including hostboot, PowerVM Hypervisor (PHYP), and partition firmware (PFW) to also include IBM i Licensed Internal Code (LIC) through digital signatures. The IBM i operating system can verify the integrity of the boot chain up through the IBM i LIC prior to its execution by using a digital signature and a hardware-protected asymmetric key.
- /SM590000 IBM i Common Cryptographic Architecture Cryptographic Service Provider (CCA CSP), delivered as IBM i Option 35 with IBM i 7.6, 7.5, and 7.4, supports the IBM 4770 Cryptographic Coprocessor with release 8.4.x for CCA.
- /SM590000 IBM i 7.5 and 7.6 enable NX-accelerated compression for PASE programs on Power11 servers. Using the zlibNX library, as supported in AIX, IBM i now accelerates DEFLATE compression in PASE, with the pigz program automatically benefiting. This can reduce CPU usage by up to 95% and significantly speed up compression tasks.
- /SM590000 With IBM i 7.6, support for Tape Library Virtualization has been extended to include IBM 3584 tape libraries when running on Power10 and Power11 servers. This enhancement builds on existing virtualization capabilities previously available for libraries such as the 3572, 3573, and 3555. Tape Library Virtualization allows multiple IBM i partitions to share a single physical tape library, significantly reducing infrastructure costs by eliminating the need for a dedicated tape drive per LPAR. Additionally, this support extends to Virtual Tape Libraries (VTLs) that emulate the 3584 model. This enhancement is described in the IBM i Removable Media: Tape Library Virtualization landing page.

## 6.3.4  IBM i Software Tiers

The IBM i software tiers for the S1122 and S1124 range from P10 to P30 depending on the configuration of your server.

## Power S1122 SW tiers for IBM i

All of the Power S1122 configurations are designated as IBM i software tier P10. IBM i support is provided at a price-attractive P10 software tier even though the Power S1122 has two sockets.

There are limitations to the maximum size of the partition, and all I/O must be virtualized through VIOS (VIOS is required, and IBM i partitions must be set to 'restricted I/O'). Up to four cores (real or virtual) per IBM i partition are supported. Multiple IBM i partitions can be created and run concurrently, and each individual partition can have up to four cores.

Native IBM i support is available on the IBM Power S1122 (MTM 9824-22A) only when populated with two 4-core processors (#ERGR) with a maximum of eight cores active. This configuration is available at a P10 IBM i software tier and will support IBM i natively, virtualized, or as a combination of both.

When configuring the S1122 (MTM 9824-22A) with two 4-core processors (feature #ERGR), IBM i partitions with more than four cores may be used. When configuring these systems with any other processor feature the 4-core per partition limit is enforced.

- -Feature ERGR cannot be upgraded to any other processor feature.
- -Two #ERGR 4-core processors configuration is IBM i P10 processor group/software tier. #ERGR processor is QPRCFEAT ERGR.
- -Systems with this configuration also need to include (#EEPS) - IBM i Enablement for 9824-22A with two #ERGR Processors.

## Power S1124 SW tiers for IBM i

All Power S1124 are either P20 or P30 software tiers. Table 6-1 shows the details.

Table 6-1   S1124 IBM i software tiers

|   Number of Cores | Feature Code   |   Number of Processor Modules | QPRCFEAT   | IBM i SW Tier   |
|-------------------|----------------|-------------------------------|------------|-----------------|
|                16 | EP3X           |                             1 | EP3X       | P20             |
|                32 | EP3X           |                             2 | EP3X       | P20             |
|                48 | EP3H           |                             2 | EP3H       | P30             |
|                64 | EP3Y           |                             2 | EP3Y       | P30             |

Note: There is not currently a Power11 server with P05 support. If you need P05 support consider one of these options:

- -Power S1012 (9028-21B) 1-core or 4-core processors
- -Power S1014 (9105-41B) 4-core processor

It is expected that IBM will produce a Power11 replacement for the Power S1012 which will support the P05 tier sometime in the future.

## 6.3.5  IBM i Licensing

On Power11, IBM i licenses will only be available via subscription, with the exception of customers doing MES or serial number upgrades from E1080 to E1180 where there will be no change in licensing.

For Power10 new purchases, IBM announced the withdrawal of perpetual IBM i licenses for P20 and P30 software tiers in July 2025 with an effective date of January 1st 2026. New Power10 purchases prior to January 2026 can:

- -Purchase new subscription licenses
- -Purchase new perpetual licenses
- -Transfer existing perpetual licenses

IBM had previously withdrawn new perpetual licenses for P05 and P10 tiers.

When an IBM i license is acquired, license keys are generated which are unique to the server on which the license is acquired. These licenses can be grouped into two categories with respect to the license keys that are fulfilled:

- /SM590000 Non-expiring (also called 'perpetual') - meaning that the license keys have no expiration date
- /SM590000 Subscription - meaning that the license keys have an expiration date for the duration of the subscription term.

IBM i licenses are also categorized into Software Tiers, also known as Processor Groups.

These tiers relate to the size of the hardware platform on which the operating system runs. The Software Tiers are P05, P10, P20, and P30. For a list of Power machines and their software tiers, refer to section 6.3.4, 'IBM i Software Tiers' on page 141.

The IBM i licensing metric is different between the various tiers:

- -P05 - based on number of cores and number of users
- -P10 - based on number of cores and number of users
- -P20 - based on number of cores
- -P30 - based on number of cores

For many customers, IBM i 7.6 will be their first experience of subscription-based licensing. This is because on 7th May 2024, IBM migrated to subscription-only licenses when a customer buys specific P05 and P10 tier machines.

Note: IBM's general direction is that all software tiers will move to this subscription model in the future.

## User Licensing

For IBM i licenses for the P05 and P10 tiers, clients can choose how many users to license for IBM i. IBM i users are ordered in bundles of 10, or an unlimited user license is available. As stated in the list above, the P20 and P30 tiers are licensed solely core. Customers at P20 and P30 tiers can have any number of IBM i users.

For more information on IBM i subscription licensing, including a comprehensive Frequently Asked Questions (FAQ) section, refer to:

https://public.dhe.ibm.com/systems/support/planning/transfer/IBM.i.Transformation. FAQ.pdf

## 6.3.6  IBM i Subscription Bundles for P20 and P30

Subscription bundles combine multiple products under a single product ID. All products share the same start and end dates for the subscription, and each product retains its own terms. This simplifies licensing by streamlining purchase decisions, license compliance and increases flexibility to deploy capabilities. It accelerates innovation as you gain more capabilities from the start, to help modernize your infrastructure. It also reduces total investment as bundles are priced lower than individual licenses, reducing upfront and ongoing investments.

P20 and P30 customers have the options to buy either Standalone (ala carte) subscriptions or Subscriptions bundles,

- /SM590000 IBM i P20 Standard Edition
- /SM590000 IBM i P30 Enterprise Edition.

## IBM i P20 Standard Edition

The IBM i P20 Standard Edition bundle is a simplified bundle with core capabilities. IBM created the subscription bundles to simplify the acquisition of IBM i and IBM i value-added enterprise capabilities.

Figure 6-2 shows the contents of the P20 Standard Edition bundle.

Figure 6-2   P20 Bundle contents

<!-- image -->

Note: * Designates License for assets only.

## IBM i P30 Enterprise Edition

The P30 Enterprise Edition is strategic bundle that offers comprehensive IBM i enterprise capabilities to enhance availability and cyber resilience, improve productivity through automation and modernize application development and utilize AI. Figure 6-3 on page 144 shows the contents of the P30 bundle.

Figure 6-3   P30 bundle contents

<!-- image -->

## Note:

* Designates License for assets only.
- **  Red Hat Ansible Automation: 1 year support for 100 managed nodes with a minimum purchase of 10 P30 Enterprise Edition cores

## Subscription bundles and Power Enterprise Pools 2.0

Power Enterprise Pools 2.0 (PEP2.0) enables IBM i OS and PowerHA SystemMirrorfi sharing across systems. For information about Power Enterprise Pools see section 10.1, 'IBM Power Private Cloud with Shared Utility Capacity' on page 214

- /SM590000 In a Pool, clients can mix systems with
- -Subscription licenses
- Subscription Bundles: IBM i P30 Enterprise Edition, P20 Standard Edition
- Standalone Subscriptions
- -Perpetual licenses

Each system must be of a single license type, Subscription or Perpetual. They will be shared as Base Capacity or available as Metered Capacity by the minute in a Pool.

- /SM590000 Other IBM i Licensed Program Products (LPP) must be licensed per system based on their peak usage
- They are not shared as Base Capacity or available as Metered Capability by the minute in a Pool

Note: On a given serial number, a system can have either OS subscription or OS perpetual license. but not both.

## Rational Development Studio for i (RDS) named user license

RDS named user licenses acquired through IBM i P30 Enterprise Edition may be shared across each system with Enterprise Edition licenses.

## For example:

- /SM590000 A client has 3 systems with 10 cores each: 30 total cores.
- -They are entitled to 150 total named users (5 users per core).

- -These 150 named users can be on any or all 3 systems.

## IBM i License Terms

There is no change in IBM i License Terms based on subscriptions, subscription bundles, and perpetual licenses.

Determine the number of processors used by the Program in a machine using the smaller value of either of the following methods:

1. The total number of activated processors in the machine.
2. The sum of a and b as follows (any remaining fraction of a processor must be rounded up to a full processor in the final aggregation):
- a. When IBM i is run in partitions with dedicated processors, the sum of the processors assigned to those partitions.
- b. When IBM i is run in partitions that are members of a shared processing pool, for each shared processor pool, the sum of the smaller of i or ii :
- i. The maximum capacity of the shared processor pool.
- ii. The sum of the virtual processors of each uncapped partition plus the processing units assigned in each capped partition running the Program

## 6.3.7  IBM i Software Maintenance (SWMA)

IBM i Software Maintenance (SWMA) is included in the Subscription licenses. On the other hand, for non-expiring licenses, one year of SWMA is included with the purchase of the license, and then additional years of SWMA are charged separately.

IBM i SWMA is important for your business. Not only does it allow you to engage with IBM's support centers around the world but it also entitles you to software updates (which on IBM i are called Program Temporary Fixes, or PTFs) and new releases of the operating system. These PTFs provide a variety of new functions and enhancements across the IBM i portfolio, e.g., security, database, and high availability enhancements, performance improvements, and more.

## 6.3.8  CBU and DBM Licensing Models for IBM i

In addition to the IBM i licensing model described above. IBM has additional licensing models that IBM i customers.

- /SM590000 Capacity Back Up (CBU)

The CBU offering provides the ability for a customer, when ordering a new IBM i server with the CBU feature, that will facilitate the temporary transfer of IBM i license entitlements between an IBM i production server and the CBU. The production and CBU servers must both be owned by the same company. CBU provides a cost-effective backup server

The Power S1122 and Power S1124 CBU designation enables you to temporarily transfer IBM i processor license entitlements and IBM i user license entitlements purchased for a primary machine to a secondary CBU-designated system for high availability (HA) and disaster recovery (DR) operations. Temporarily transferring these resources instead of purchasing them for your secondary system may result in significant savings. Processor activations cannot be transferred.

The CBU specify feature 0444 or feature 4891 is available only as part of a new server purchase. Certain system prerequisites must be met, and system registration and approval are required before the CBU specify feature can be applied on a new server. Standard IBM i terms and conditions do not allow either IBM i processor license entitlements or IBM i user license entitlements to be transferred permanently or

temporarily. These entitlements remain with the machine they were ordered for. When you register the association between your primary and on-order CBU system, you must agree to certain terms and conditions regarding the temporary transfer.

After a new CBU system is registered as a pair with the proposed primary system and the configuration is approved, you can temporarily move your optional IBM i processor license entitlement and IBM i user license entitlements from the primary system to the CBU system when the primary system is down or while the primary system processors are inactive. The CBU system can then support failover and role swapping for a full range of test, DR, and HA scenarios. Temporary entitlement transfer means that the entitlement is a property transferred from the primary system to the CBU system and may remain in use on the CBU system if the registered primary and CBU system are in deployment for the high availability or disaster recovery operation. The intent of the CBU offering is to enable regular role-swap operations.

Before you can temporarily transfer IBM i processor license entitlements from the registered primary system, you must have more than one IBM i processor license on the primary machine and a minimum of one IBM i processor license on the CBU server depending on the workload. To comply, the CBU will be configured in such a manner that there will be no out-of-compliance messages prior to a failover. An activated processor must be available on the CBU server to use the transferred entitlement. You can then transfer any IBM i processor entitlements above the minimum, assuming the total IBM i workload on the primary system does not require the IBM i entitlement you would like to transfer during the time of the transfer or post transfer when replication is reversed. During this temporary transfer, the CBU system's internal records of its total number of IBM i processor license entitlements are not updated, and you may see IBM i license noncompliance warning messages from the CBU system. These warning messages in this situation do not mean you are not in compliance. In the case of PowerHA, there will be a minimum of one IBM i and one PowerHA and the total number of PowerHA temp keys equal to the number of PowerHA licenses on the primary. Note that with PowerHA for IBM i you can get out of compliance message suppression keys.

The minimum number of permanent entitlements on the CBU is one; however, you are required to license all permanent workload, such as replication workload. If, for example, the replication workload consumes four processor cores at peak workload, then you are required to permanently license four cores on the CBU.

The servers with P20 or higher software tiers do not have user entitlements that can be transferred, and only processor license entitlements can be transferred. The following systems are eligible primary systems for Power S1122 and Power S1124 CBU systems.

- -For a Power S1122 CBU which is in the P10 software tier, the following are eligible primary systems:
- The 4-and 8-core processor servers (#ERGR, QPRCFEAT ERGR) are IBM i SW tier P10.
- The 10-and 20-core processor servers (#ERGQ, QPRCFEAT ERGQ) are IBM i SW tier P10.
- The 32-core processor server (#EBG8, QPRCFEAT EBG8) is IBM i SW tier P10.
- The 48-core processor server (#EBG9, QPRCFEAT EBG9) is IBM i SW tier P10.
- The 60-core processor server (#EBGA, QPRCFEAT EBGA) is IBM i SW tier P10.
- -For a Power S1124 CBU which is in the P20 software tier, the following are eligible primary systems:
- Power S1124 (9824-42A) with 32 or 12 cores
- Power E1080 (9080-HEX)
- Power S1024 (9105-42A) with 48, 32, 24, or 12 cores
- Power E1080 (9080-HEX)
- Power S1024 (9105-42A) with 48, 32, 24, or 12 cores

- -For a Power S1124 CBU which is in the P30 software tier, the following are eligible primary systems:
- Power S1124 (9824-42A) with 48 or 60 cores
- Power E1080 (9080-HEX)
- Power E980 (9080-M9S)
- Power S1024 (9105-42A) with 32 or 48 cores

During the temporary transfer, the CBU system's internal records of its total number of IBM i processor entitlements are not updated, and you may see IBM i license noncompliance warning messages from the CBU system. Prior to a temporary transfer, the CBU will be configured in such a manner that there are not out of compliance warning messages.

If your primary or CBU machine is sold or discontinued from use, temporary entitlement transfers must be returned to the machine on which they were originally acquired. For CBU registration, terms and conditions, and further information, see the IBM Power Systems: Capacity BackUp website.

- /SM590000 Dedicated Backup Machine (DBM)

This is licensing scenarios that facilitates backup environments. One key difference is that a DBM licensed machine does not have to belong to the same company as the production server for which it is backing up. Another difference between CBU and DBM machines is that for DBM server, IBM i license entitlement is acquired for all cores which use IBM i on the server.

For information regarding temporary keys for IBM i Licensed Program Products (LPPs) for CBU and DBM, refer to Request for designation of a primary and backup pairing at https://www.ibm.com/support/pages/ibm-power-systems-capacity-backup

## 6.3.9  Upgrading an existing IBM i license to 7.6

If you have active IBM i SWMA, you can upgrade your IBM i license to 7.6 at no extra charge.

If you have IBM i Subscription licenses at 7.5 or earlier, for upgrade information, refer to the IBM i Subscription Transformation FAQ, and search for 'upgrade'.

https://public.dhe.ibm.com/systems/support/planning/transfer/IBM.i.Transformation.FAQ.pdf

If you have IBM i non-expiring licenses at 7.5 or earlier, upgrade IBM i via the IBM Entitled Systems Support (ESS) Website, using My Entitled Software → Software Updates function. Here you will select your IBM System via IBM customer number server model and serial number, then take the option to upgrade it from the current release to7.6. Once this process completes, you will be directed to the Software Download section of this site and you can download your installation media, ready to install or upgrade your system.

Once you have upgraded your IBM i non-expiring or subscription licenses to 7.6, use the ESS website to download copies of your IBM i license keys for 7.6. Until license keys are installed, a 70-day evaluation period is available. Failure to install the license keys can result in the IBM i and/or LPPs being no longer usable until the appropriate license keys are installed.

Your licensing model will not change by the upgrade process. Regardless of whether you have a non-expiring or subscription license before the upgrade, you will have the same license type afterwards.

When performing the upgrade to IBM i 7.6 on your server, upgrades to IBM i 7.6 are supported from IBM i 7.4 and 7.5.

## 6.3.10  IBM i Simplification

IBM i and many of the IBM i portfolio LPPs require license keys to assure that the software is properly licensed. With recent simplification, the number of products requiring keys has been reduced. For more information on the IBM i Simplification, visit IBM i Portfolio Simplification

## 6.4  Linux on IBM Power

Linux is a powerful, open-source, cross-platform operating system that runs on a broad spectrum of hardware - from embedded devices to mainframes - delivering a consistent, UNIX-like environment across diverse architectures. Its compatibility with IBM Power offers a flexible and cost-effective alternative for running a wide range of applications, while taking full advantage of the platform's renowned performance, availability, and reliability.

As a free and open-source solution, Linux significantly reduces total cost of ownership by eliminating licensing fees and enabling deep customization. It supports modern technologies such as containers, Kubernetes, and cloud-native applications, making it ideal for building scalable, agile IT environments. Its high portability allows it to run seamlessly on architectures like x86, ARM, and IBM Power, and it is supported by a vast, active global community that provides extensive documentation, tools, and peer support.

IBM has been a leading advocate for Linux for over two decades, integrating it deeply into its enterprise ecosystem - including IBM Power based-processor servers, IBM Zfi mainframes, and IBM Cloud. The company collaborates closely with major Linux distributions such as Red Hat, SUSE, and Canonical to ensure optimized performance and seamless integration. Through initiatives like LinuxONE and ongoing contributions to the Linux kernel and open-source projects, IBM continues to position Linux as a cornerstone of secure, modern infrastructure.

Security is another key strength of Linux. Its robust user privilege model, combined with community-driven updates and tools like SELinux and AppArmor, helps protect systems from vulnerabilities and malware. Linux is also highly efficient and lightweight, capable of running on everything from low-powered IoT devices to high-performance enterprise servers. Its modularity allows users to tailor the system to their specific needs - whether that means a minimal installation or a fully featured desktop environment.

Additionally, Linux provides access to a vast ecosystem of tools and software, some of which are exclusive or better supported on Linux than on other operating systems. Its open-source nature allows for greater flexibility and adaptability, making it easier to align with specific business or technical requirements. Linux also serves as a solid foundation for hybrid cloud infrastructure, supporting application modernization and deployment at scale. Its scalability, reliability, and cost-effectiveness make it especially well-suited for large enterprise environments and mission-critical workloads.

## 6.4.1  Supported distributions

The Linux distributions that are described next are supported on the Power scale-out servers. Other distributions, including open source releases, can run on these servers, but do not include any formal Enterprise Grade support.

## Red Hat Enterprise Linux

The latest version of the Red Hat Enterprise Linux (RHEL) distribution from Red Hat is supported in native Power11 mode, which allows it to access all of the features of the Power11 processor and platform.

At announcement, the Power S1122, and S1124 servers support the following minimum levels of the Red Hat Enterprise Linux operating system:

- /SM590000 RHEL 10 with native Power11 support, fully leveraging the architecture's advanced features.
- /SM590000 RHEL 9.6 for Power LE or later (Power11 native support)
- /SM590000 RHEL 9.4 for Power LE or later (Power10 compatibility)
- /SM590000 RHEL 8.10 for Power LE or later (Power10 compatibility)

## Red Hat Enterprise Linux roadmap

IBM Power servers support Linux workloads while leveraging POWER hardware's performance, reliability, and availability. This section outlines supported enterprise Linux distributions. While other distributions may run on Power, only select enterprise versions offer formal support.

Red Hat Enterprise Linux (RHEL) is a leading open-source platform for Linux, hybrid cloud, containers, and Kubernetes. It provides secure, transparent, and proactive lifecycle management, supporting autonomous operations. Lifecycle planning is essential for customers, partners, ISVs, and the broader ecosystem. Starting with RHEL 8, the lifecycle includes three phases: Full Support, Maintenance Support, and Extended Life. Red Hat also shares projected release time lines and extended support details for minor versions. RHEL 8, 9, and 10 each offer a 10-year lifecycle across the first two phases, followed by Extended Life.

Figure 6-4   Red Hat Enterprise Linux support lifecycle

<!-- image -->

Note: The Red Hat Enterprise Linux life cycle phases are designed to minimize changes within each major release over time and ensure predictable availability and content.

- /SM590000 Full Support Phase

During this phase, Red Hat provides updates for:

- -Security issues (CVEs with CVSS greater or equal to 7) via RHSAs
- -Urgent and select high-priority bugs via RHBAs
- -Additional errata as needed

New or improved hardware support and select software enhancements may be included, typically in minor releases. These minor releases are cumulative and focus on resolving medium or higher-priority issues. Updated installation images are also provided.

- /SM590000 Maintenance Support Phase

For RHEL 8, 9, and 10, Red Hat continues releasing:

- -Security updates (CVEs with CVSS ? 7)
- -Urgent and selected high-priority bug fixes

New features and hardware support are not included during this phase.

- /SM590000 Extended Life Phase

Customers retain access to existing content via the Red Hat Customer Portal, including documentation and migration guidance. Only limited technical support is available - no new fixes, hardware support, or root-cause analysis is provided. Support applies to existing installations only, and Red Hat may end support at its discretion.

## Release Cadence

To provide predictability, minor RHEL releases are scheduled every six months during the Full Support Phase. Details on Extended Update Support (EUS) and SAP-specific services are included per release. Figure 6-5 shows the planned release schedule for RHEL8.

Figure 6-5   Release schedule for RHEL8

<!-- image -->

Figure 6-6 shows the planned release schedule for RHEL9.

Figure 6-6   Release schedule for RHEL9

<!-- image -->

Figure 6-7 shows the release schedule for RHEL10.

Figure 6-7   Release schedule for RHEL10

<!-- image -->

For additional details regarding the RHEL roadmap, please refer to the Red Hat Enterprise Linux Life Cycle. To find the latest Red Hat certified IBM Power servers, please refer to the Red Hat Certified Hardware catalog and System to Red Hat Enterprise Linux maps.

## SUSE Linux Enterprise Server

The latest version of the SUSE Linux Enterprise Server distribution of Linux from SUSE is supported in native Power11 mode, which allows it to access all of the features of the Power11 processor and platform.

At announcement, the Power E1050 servers support the following minimum levels of the SUSE Linux Enterprise Server operating system:

- /SM590000 SUSE Linux Enterprise Server 15 Service Pack 6, or later (Power11 native)

## SUSE roadmap

SUSE Linux Enterprise Server (SLES) is designed with long-term enterprise stability and support in mind. Its product lifecycle provides predictable and reliable maintenance phases, enabling organizations to plan deployments, updates, and migrations effectively.

- /SM590000 Lifecycle Duration

SLES offers a total lifecycle of 13 years per major release, divided into two main phases:

- -General Support (10 years): This phase includes full maintenance, security patches, bug fixes, hardware enablement, and new certified third-party software. It is ideal for production environments requiring continuous updates and active support.
- -Extended Support (3 years): After General Support ends, Extended Support offers critical security updates and selected bug fixes, allowing customers more time to transition to newer versions while maintaining operational security.
- /SM590000 Release Cadence
- -Major Releases: Every 4 years, introducing new features, platform support, and architectural improvements.
- -Service Packs (SPs): Released every 12 to 14 months, these include incremental updates, feature enhancements, and hardware enablement.

Each Service Pack is supported for six months after the release of the subsequent SP, providing customers time to validate and upgrade within a consistent and predictable window.

Figure 6-8 shows the service pack schedule.

Figure 6-8   SLES major releases and service packs

<!-- image -->

Figure 6-9 shows the release lifecycle, including long term service pack support.

Figure 6-9   SLES long-term service pack support.

<!-- image -->

For additional details regarding the SUSE roadmap, please refer to the SUSE Linux Enterprise Server Documentation and Product Support Lifecycle. To find the latest SUSE certified IBM Power servers, please refer to the System to SUSE Linux Enterprise Server maps and SUSE YES Certified Hardware - Bulletin Search.

## Linux and Power11 technology

The Power11 specific toolchain is available in the IBM Advance Toolchain for Linux version 15.0, which allows customers and developers to use all new Power11 processor-based technology instructions when programming. Cross-module function call overhead was reduced because of a new PC-relative addressing mode.

One specific benefit of Power11 technology is a 10x to 20x advantage over Power9 processor-based technology for AI inferencing workloads because of increased memory bandwidth and new instructions. One example is the new special purpose-built matrix math accelerator (MMA) that was tailored for the demands of machine learning and deep learning inference. It also supports many AI data types.

## 6.4.2  Licensing

Linux licensing on IBM Power follows the same foundational principles as on other platforms, but with considerations tailored to enterprise environments. The Linux kernel itself is licensed under the GNU General Public License version 2 (GPLv2), which ensures that the software remains free and open-source, allowing users to run, study, modify, and distribute it. On IBM Power, several major Linux distributions are supported, including Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), and Ubuntu. Each of these distributions adheres to open-source licensing models but may differ in how they package and deliver their software.

For example, RHEL and SLES provide access to source code under open-source licenses but require a paid subscription for access to precompiled binaries, updates, and enterprise support. This model allows organizations to benefit from open-source flexibility while receiving the stability and support needed for mission-critical workloads.

On IBM Power based-processor servers, these distributions are optimized to take advantage of the architecture's performance, scalability, and reliability features, and licensing terms typically include support for virtualization technologies like PowerVM.

## Red Hat Licensing

Red Hat Enterprise Linux is sold on a subscription basis, with initial subscriptions and support available for one, three, or five years. Support is available directly from Red Hat or IBM Technical Support Services.

Red Hat Enterprise Linux 8 for Power LE subscriptions covers up to four cores and up to four LPARs, and can be stacked to cover a larger number of cores or LPARs.

When you order RHEL from IBM, a subscription activation code is automatically published in Enterprise Storage Server. After retrieving this code from Entitled Systems Support (ESS), you use it to establish proof of entitlement and download the software from Red Hat.

Red Hat Licensing information can be found here.

## SUSE Linux Enterprise Server Licensing

SUSE Linux Enterprise Server is sold on a subscription basis, with initial subscriptions and support available for one, three, or five years. Support is available directly from SUSE or from IBM Technical Support Services.

SUSE Linux Enterprise Server 15 subscriptions cover up to one socket or one LPAR, and can be stacked to cover a larger number of sockets or LPARs.

When you order SLES from IBM, a subscription activation code is automatically published in Entitled Systems Support (ESS), you use it to establish proof of entitlement and download the software from SUSE.

Clients are required to register the Linux offering purchased at the Distributor's website with the activation code. After registered, clients are able to download the software packages electronically and obtain the latest upgrades available for the product purchased.

SLES Licensing Information can be found here.

## Linux and Power11 technology

The Power11 specific toolchain is available in the IBM Advance Toolchain for Linux version 15.0, which allows customers and developers to use all new Power11 processor-based technology instructions when programming. Cross-module function call overhead was reduced because of a new PC-relative addressing mode.

One specific benefit of Power11 technology is a 10x to 20x advantage over Power9 processor-based technology for AI inferencing workloads because of increased memory bandwidth and new instructions. One example is the new special purpose-built matrix math accelerator (MMA) that was tailored for the demands of machine learning and deep learning inference. It also supports many AI data types.

## 6.5  Red Hat OpenShift

Red Hat OpenShift on IBM Power provides a powerful platform for building, deploying, and managing containerized applications across hybrid cloud environments. Leveraging the performance and reliability of IBM Power architecture, OpenShift enables enterprises to modernize their IT infrastructure with cloud-native technologies like Kubernetes, containers, and microservices. With support for AIX, IBM i, and Linux, organizations can co-locate containerized workloads alongside traditional applications, reducing latency and improving data access. OpenShift's integration with IBM Cloud services and automation tools simplifies cluster provisioning, scaling, and lifecycle management, making it easier for developers to focus on innovation rather than infrastructure.

The latest release, Red Hat OpenShift 4.18, brings enhanced capabilities to IBM Power, including improved networking with User Defined Networks (UDNs), advanced Operator Lifecycle Management (OLM), and deeper GitOps integration 1. These features support more secure, scalable, and flexible deployments, whether on-premises or in the IBM Power Virtual Server cloud. OpenShift on Power also supports IBM Cloud Paks and AI workloads, enabling enterprises to accelerate digital transformation while maintaining enterprise-grade security and performance. This combination of technologies empowers businesses to innovate faster, optimize resource usage, and build a resilient hybrid cloud foundation.

For more details on how Red Hat OpenShift can improve your hybrid cloud experience see section 10.2, 'Red Hat OpenShift' on page 216.

## Licensing

Red Hat OpenShift Container Platform is offered via subscription, with terms available for 1, 3, or 5 years. Subscriptions are sold in increments covering two processor cores and can be stacked to match workload requirements. Support is available either directly from Red Hat or through IBM Technical Support Services.

When ordering OpenShift Container Platform for Power from IBM, the client receives a subscription activation code via the IBM Entitled Systems Support (ESS) portal. This code serves as proof of entitlement and is used to download the software directly from the Red Hat Customer Portal.

For further information and documentation, refer to the official Red Hat OpenShift Documentation.

## Supported Levels

The IBM Power scale-out servers supports Red Hat OpenShift Container Platform 4.18 and later. Red Hat OpenShift 4.18 will support IBM Power11 when running with Power10 Compatibility mode at GA.

Full support for IBM Power11 native mode is planned for Red Hat OpenShift version 4.19.

## Red Hat OpenShift Container Platform roadmap

Red Hat provides a defined product life cycle for OpenShift Container Platform (OCP) to help customers and partners plan, deploy, and support their infrastructure. This life cycle is published for transparency, though exceptions may occur.

OpenShift v4 follows a phased, time-based life cycle, with at least four minor versions supported concurrently. Each minor version has a fixed support period, offering varying levels of maintenance. Red Hat targets a release cadence of every four months to support customer planning. All errata remain available to active subscribers throughout the life cycle.

Figure 6-10   Figure 4. OCP Life Cycle Phases

<!-- image -->

## Full Support

Begins at GA of a minor version and ends 6 months later or 90 days after the next minor version GA-whichever is later.

## During this phase:

- /SM590000 Full and Development Support are provided per the Scope of Coverage and SLA.
- /SM590000 Critical and Important security fixes (RHSAs) are released as needed.
- /SM590000 Urgent and high-priority bug fixes (RHBAs) are released promptly; others may be included in periodic updates.
- /SM590000 Customers must stay on a supported micro version (e.g., 4.x.z) to receive updates.

## Maintenance Support

Starts after Full Support and ends 18 months after the minor version GA.

## During this phase:

- /SM590000 Critical and Important RHSAs continue.
- /SM590000 Select urgent RHBAs may be released.
- /SM590000 Other fixes and enhancements (RHEAs) may be issued at Red Hat's discretion.
- /SM590000 No technical support is provided after this phase, except assistance with upgrading.
- /SM590000 Access to hosted services for unsupported versions is not guaranteed.

## Extended Update Support (EUS)

Even-numbered minor versions (e.g., 4.8, 4.10) are designated as EUS releases, offering extended support phases to simplify upgrades and reduce node reboots.

EUS Add-On - Term 1 (6 Months)

- /SM590000 Optional support following Maintenance Support:
- /SM590000 Includes Critical/Important security updates and urgent bug fixes.
- /SM590000 Allows customers to stay on a minor release for up to 24 months.
- /SM590000 Included with Premium subscriptions (x86\_64) and available as an add-on to Standard. Contact your Red Hat Sales Representative for access or guidance.

## EUS Add-On - Term 2 (12 Months)

- /SM590000 Optional support after Term 1:
- /SM590000 Includes Critical/Important updates and urgent fixes for platform-aligned Operators and selected OCP components.

With both Term 1 and Term 2, support extends up to 36 months for stable, mission-critical environments.

Table 6-2shows the dates for current versions of Red Hat OpenShift Container Platform.

Table 6-2   OCP Life Cycle Dates

| Version                                                                | General availability                                                   | Full support ends                                                      | Maintenanc e support ends                                              | Extended Update Support Add-On - Term 1 ends                           | Extended Update Support Add-On - Term 2 ends                           | Extended life phase ends                                               |
|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Full Support OpenShift Container Platform 4 Full Support               | Full Support OpenShift Container Platform 4 Full Support               | Full Support OpenShift Container Platform 4 Full Support               | Full Support OpenShift Container Platform 4 Full Support               | Full Support OpenShift Container Platform 4 Full Support               | Full Support OpenShift Container Platform 4 Full Support               | Full Support OpenShift Container Platform 4 Full Support               |
| 4.19                                                                   | 17-Jun-25                                                              | GA of 4.20 + 3 Months                                                  | 17-Dec-26                                                              | N/A                                                                    | N/A                                                                    | N/A                                                                    |
| 4.18                                                                   | 25-Feb-25                                                              | 17-Sep-25                                                              | 25-Aug-26                                                              | 25-Feb-27                                                              | 25-Feb-28                                                              | N/A                                                                    |
| Maintenance Support OpenShift Container Platform 4 Maintenance Support | Maintenance Support OpenShift Container Platform 4 Maintenance Support | Maintenance Support OpenShift Container Platform 4 Maintenance Support | Maintenance Support OpenShift Container Platform 4 Maintenance Support | Maintenance Support OpenShift Container Platform 4 Maintenance Support | Maintenance Support OpenShift Container Platform 4 Maintenance Support | Maintenance Support OpenShift Container Platform 4 Maintenance Support |
| 4.17                                                                   | 1-Oct-24                                                               | 25-May-25                                                              | 1-Apr-26                                                               | N/A                                                                    | N/A                                                                    | N/A                                                                    |
| 4.16                                                                   | 27-Jun-24                                                              | 1-Jan-25                                                               | 27-Dec-25                                                              | 27-Jun-26                                                              | 27-Jun-27                                                              | N/A                                                                    |
| 4.15                                                                   | 27-Feb-24                                                              | 27-Sep-24                                                              | 27-Aug-25                                                              | N/A                                                                    | N/A                                                                    | N/A                                                                    |
| Extended Support OpenShift Container Platform 4 Extended Support       | Extended Support OpenShift Container Platform 4 Extended Support       | Extended Support OpenShift Container Platform 4 Extended Support       | Extended Support OpenShift Container Platform 4 Extended Support       | Extended Support OpenShift Container Platform 4 Extended Support       | Extended Support OpenShift Container Platform 4 Extended Support       | Extended Support OpenShift Container Platform 4 Extended Support       |
| 4.14                                                                   | 31-Oct-23                                                              | 27-May-24                                                              | 1-May-25                                                               | 31-Oct-25                                                              | 31-Oct-26                                                              | N/A                                                                    |
| 4.12                                                                   | 17-Jan-23                                                              | 17-Aug-23                                                              | 17-Jul-24                                                              | 17-Jan-25                                                              | 17-Jan-26                                                              | N/A                                                                    |

Note: Red Hat OpenShift Container Platform (RHOCP) 4 uses Red Hat Enterprise Linux CoreOS (RHCOS) as its managed node operating system. RHCOS is updated during cluster upgrades, which may include changes between RHEL minor versions.

For additional details regarding the Red Hat OpenShift Container Platform roadmap, please refer to the Red Hat OpenShift Container Platform Life Cycle Policy

## 6.6  Intro to KVM support

KVM stands for Kernel Virtual Machine, and its a widely spread virtualization technology in X86\_64, and also can be used in Power Servers. Even when IBM remains committed to the PowerVM being the premier enterprise virtualization software in the industry.

With KVM on Power, IBM will be targeting x86 customers on entry servers but will offer both KVM and PowerVM to meet the varying virtualization needs of Power Linux customers. However, KVM virtualization technology represents an opportunity to simplify customer's virtualization infrastructure with a single hypervisor and management software across multiple platform.

The KVM Guests may run within a PowerVM LPAR, KVM can be used to run KVM guests. These guests are essentially VMs that run on top of the LPAR, using the existing resources of the LPAR.

On of the Benefits is that this approach combines the advantages of PowerVM's virtualization capabilities with the power and flexibility of KVM.

KVM guests running in a PowerVM LPAR have a unique runtime architecture, different from other virtualization mechanisms on IBM POWER system. For more details on KVM support on IBM Power11 see 9.2, 'KVM support' on page 210.

## 6.7  PowerVM Virtual I/O Server

IBM PowerVM software is a virtualization environment that can run AIX, IBM i and Linux virtual machines on IBM Power servers. Businesses are turning to server virtualization to consolidate multiple workloads onto fewer systems, increase server utilization and reduce costs. PowerVM provides a secure and scalable server virtualization environment for your applications, built upon the advanced RAS features and leading performance of the IBM Power systems platform.

PowerVM is designed to protect and isolate critical workloads through a highly secure, enterprise-grade hypervisor. It enforces strong workload isolation and I/O integrity, ensuring the reliability of mission-critical applications. With robust automation capabilities, PowerVM accelerates service delivery by streamlining the provisioning and management of virtual machines and storage resources, making it well-suited for cloud-based infrastructures. It also enhances operational efficiency and maximizes return on investment through features like live partition mobility, which enables zero-downtime workload migration, and resource optimization tools that improve the utilization of compute and storage infrastructure.

The Virtual I/O Server (VIOS) is part of the PowerVM Editions hardware feature. The VIOS is a software that is located in a logical partition and facilitates the sharing of physical I/O resources between client logical partitions within the server.

Currently, the IBM Power11 processor-based server supports the following minimum levels of the PowerVM VIOS operating system:

- /SM590000 VIOS 4.1.1.10
- /SM590000 VIOS 4.1.0.40
- /SM590000 VIOS 3.1.4.60

## 6.8  Setting your LPAR compatibility mode

IIBM Power Processor Compatibility Mode is a feature that enables newer IBM Power based-processor servers to run applications and operating systems originally compiled for earlier generations of Power processors. This is especially important when transitioning to the latest hardware, such as Power11, where some operating systems and applications may not yet support native execution. In such cases, compatibility mode allows these workloads to run

in a Power10 (or earlier) environment, ensuring continuity and minimizing disruption during upgrades.

The compatibility mode is defined at the logical partition (LPAR) level during the creation of the LPAR. Administrators can specify which processor generation the partition should emulate, allowing multiple workloads to operate in different compatibility modes on the same physical server. This flexibility is particularly useful in mixed environments where not all software has been updated to support the latest architecture.

While running in a previous-generation compatibility mode helps maintain application portability and eases the migration process, it may restrict access to newer processor features and performance enhancements. For this reason, IBM recommends using compatibility mode as a transitional solution. The long-term goal should be to recompile applications and upgrade operating systems to fully leverage the advanced capabilities and performance improvements of the latest Power processor architecture.

Figure 6-11 shows how to set compatibility mode in your LPAR definition.

Figure 6-11   Set Lpar processor compatibility mode

<!-- image -->

<!-- image -->

Chapter 7.

7

## Enterprise Solutions

IBM Power servers are engineered to support a wide range of enterprise workloads that demand high availability, performance, and scalability. These systems are ideal for mission-critical applications such as SAP HANA, Oracle, and IBM Db2, where consistent uptime and fast transaction processing are essential. With advanced RAS (Reliability, Availability, and Serviceability) features and capabilities like live partition mobility, Power servers ensure minimal downtime and seamless workload management. They are also well-suited for enterprise resource planning (ERP) and customer relationship management (CRM) systems, offering the processing power and memory capacity needed to handle large-scale, real-time data operations.

In addition to traditional workloads, IBM Power servers are optimized for modern enterprise needs, including artificial intelligence (AI), machine learning, and hybrid cloud deployments. Built-in accelerators and support for containerized environments like Red Hat OpenShift allow organizations to run AI models and cloud-native applications efficiently. These servers also excel in high-performance computing (HPC) scenarios, such as financial modeling, scientific research, and healthcare analytics, thanks to their high core counts and memory bandwidth. With robust security features like transparent memory encryption and secure boot, IBM Power is a trusted platform for industries with strict compliance requirements. Overall, Power servers provide a flexible, secure, and cost-effective foundation for evolving enterprise IT landscapes.

This chapter contains the following topics:

- /SM590000 High Availability and Disaster Recovery Solutions
- /SM590000 IBM Db2
- /SM590000 Oracle
- /SM590000 SAP HANA
- /SM590000 Banking
- /SM590000 Health Care

## 7.1  High Availability and Disaster Recovery Solutions

IBM offers a suite of high availability and disaster recovery (HA/DR) solutions tailored to its Power based-processor servers platform, each designed to meet different operational needs and workloads. PowerHA SystemMirror for AIX is a clustering solution that ensures application uptime through an active-standby model, enabling fast failover and minimal disruption during outages or maintenance. For IBM i environments, PowerHA SystemMirror for i provides tightly integrated HA/DR capabilities using features like Independent Auxiliary Storage Pools (IASPs) and real-time data replication to protect mission-critical workloads. Complementing these is VM Recovery Manager (VMRM), a flexible solution that supports AIX, IBM i, and Linux workloads by managing full LPAR recovery across systems. VMRM is ideal for environments where full system recovery is acceptable, offering automated failover and disaster recovery without requiring application-level configuration. Together, these tools provide a comprehensive HA/DR strategy across the IBM Power ecosystem.

## 7.1.1  PowerHA SystemMirror for AIX

PowerHA SystemMirror for AIX, generally known as PowerHA, is a high availability clustering solution to ensure application uptime and fast recovery. It is considered an active-standby or active-passive system of application availability. It is also known as an application restart model, where an application and its resources (a file system with data, an IP address, application scripts, a volume group, etc.) are logically combined and operate as a single entity on a VM or LPAR (known as a 'node') in a cluster. That group of resources are moved as a unit to a standby VM or LPAR, and the application is restarted. In the event of a planned outage - PowerHA can gracefully quiesce the application on the primary node. In any case, the outage lasts just as long as it takes to acquire the resources and restart the application this might be measured in minutes. It is also considered to be a warm standby method of high availability, in that the target node already has a running version of AIX.

PowerHA for AIX can also be used across data centers, where data is replicated through the storage subsystem or, using the AIX Geographic Logical Volume Manager (GLVM) subsystem, over IP to the target node.

In any case - within or across data centers - the failover process can be automated to reduce application outages. Applications can be moved to another running node to allow for maintenance, allowing for near-zero downtime - although the PowerHA application can be maintained with a live kernel update.

PowerHA for AIX is tightly integrated with the AIX operating system's inherent reliability, and IBM Power's hardware features such as virtual I/O, concurrent hardware maintenance, dynamic resizing of LPARs, etc. PowerHA supports critical enterprise apps, like Oracle, SAP, Db2, and Epic systems - all common workloads. Licensing is on a n+1 model per cluster, where n is the number of cores in the production online copy of the application, with 1 additional core added for the standby. For example, on a 24-core Power system, if two clusters are created, one supporting an LPAR with 4 cores and another with 5, a total of 11 cores will need to be licensed - 4+1=5 and 5+1=6.

## 7.1.2  IBM PowerHA SystemMirror for i

PowerHA for IBM i is IBM's high-availability and disaster recovery (HA/DR) solution designed specifically for the IBM i operating system. It provides automated failover capabilities and data replication to ensure business continuity in the event of planned or unplanned outages. PowerHA integrates tightly with IBM i's native features, such as the Independent Auxiliary

Storage Pool (IASP), to enable fast and efficient switching between systems with minimal downtime.

At the core of PowerHA is its ability to replicate data in real time between primary and backup systems using technologies like Geographic Mirroring or IBM's Storage-based replication. This ensures that critical applications and data remain available even if the primary system becomes unavailable. PowerHA supports both local high availability within a single data center and remote disaster recovery across geographically dispersed locations, offering flexibility for various business continuity strategies.

PowerHA also includes tools for monitoring, automation, and management, making it easier for IT administrators to configure and maintain HA/DR environments. With features like role-based access, cluster resource groups, and automated failover policies, PowerHA helps reduce the complexity of managing high-availability systems. It is a key component for organizations that rely on IBM i to run mission-critical workloads and require continuous access to their data and applications.

## 7.1.3  VM Recovery Manager (VMRM)

VM Recovery Manager (aka VMR or VMRM) operates on an active-inactive model, where the entire definition of an VM or LPAR Is recreated onto a target Power system and then restarted. It supports any workload running on a Power System - AIX, IBM I, and Linux. Recovery will take longer than an application restart model because the entire LPAR must be restarted after being redefined, instead of just restarting the application.

In HA mode, VMRM uses the Live Partition Mobility to dynamically move an LPAR to a system that shared an HMC. In DR mode, it will manage the data replication process from the storage provider to a set of disks at the target system. The LPAR only exists in one place at any given time, except in some limited circumstances where a disaster exercise can be tested on the target system.

As with PowerHA, VMRM helps automate disaster recovery - it can detect when a VM or entire Power System is done and initiate policy-based failover to a single target or to a group of targets. It can coexist with PowerHA - where a cluster of LPARs can be failed as a group over to Power based-processor servers at an alternate site. It is often used to provide simple DR support for Linux VMs - no software installation or OS configuration required; the Linux VM will be restarted.

The ideal use cases for VM Recovery Manager are development, test, and sandbox environments that may not require the same RTO requirements as production systems, and Linux on Power. It integrates well with solutions like SAP HANA and Oracle. No configuration work is required on the individual operating systems being managed, although there are some agents that can be installed to check for application failures and trigger a failover of the LPAR.

Similarly to PowerHA; it is licensed based on the number of production cores in use, not on an entire Power system. However, unlike PowerHA, no standby licenses are required. On a 24-core Power system, if the VMs needing VMRM support have 9 cores, then only n=9 cores need to be procured.

## 7.2  IBM Db2

In today's data-driven world, organizations across industries - including manufacturing, healthcare, and the public sector - must extract maximum value from rapidly growing volumes of information. Whether the goal is to uncover actionable insights from customer data or accelerate the processing of high-volume online transactions, businesses need solutions that are optimized for performance, scalability, and cost-efficiency. These solutions must support mission-critical workloads with high availability while keeping operational costs under control.

By combining IBM Db2 with IBM Power based-processor servers built on the advanced POWER11 architecture, organizations can meet these demands with confidence. This integrated, workload-optimized stack delivers exceptional performance for both transactional and analytical workloads. Db2 leverages cutting-edge database innovations to maximize efficiency and throughput, earning top rankings in industry benchmarks such as TPC-C, TPC-H, and SAP SD 3-Tier. Power based-processor servers provide the robust hardware foundation, offering superior price/performance and the ability to handle over a million transactions per minute at a cost of less than $1 per transaction. Db2 automatically exploits POWER11's parallelism and large page sizes, simplifying deployment and enabling cost-effective scaling for web applications, messaging backbones, and workload consolidation.

Beyond performance, the combination of Db2 and Power based-processor servers ensures high availability and operational efficiency. Power based-processor servers are engineered with built-in redundancy, error-handling, and reliability features, while IBM PowerHA SystemMirror adds automated monitoring and recovery to minimize downtime. Cost control is further enhanced through Db2 Deep Compression, which reduces storage needs, and IBM PowerVM virtualization, which allows for efficient resource utilization and workload consolidation. These capabilities reduce hardware, energy, and management costs, enabling a more agile and cost-effective IT infrastructure. Together, Db2 and IBM Power based-processor servers offer a powerful, scalable, and resilient platform for modern data-driven enterprises.

For more information on IBM Db2fi high availability see the IBM Redbook IBM PowerHA SystemMirror for AIX Cookbook , SG24-7739

## 7.3  Oracle

For over 35 years, clients have relied on IBM Power to deploy their Oracle database and application workloads. Organizations, both big and small, can take advantage of Power's class leading reliability and security as well as its advanced recovery, self-healing and diagnostic capabilities designed to reduce application downtime.

IBM Power11 servers, fully certified by Oracle software, can enable organizations the ability to consolidate multiple workloads on fewer servers - increasing overall system utilization and lowering overall costs. This efficiency can also lead to less Oracle licenses required. For example, IBM Power S1124 servers running Oracle Database SE2 can help reduce application cost per database instance by up to 33% compared to fourth- generation Intel Xeon scalable processors, and reduce the overall number of servers needed to improve energy costs.

The cost of security breaches continues to grow, averaging at USD 4 million per breach.2 IBM Power technology is built to protect businesses against cyberthreats with end-to-end security protocols, including new transparent memory encryption that doesn't impact performance. Power servers may be considered 60 times more secure than unbranded white box servers.2

IBM Power servers, combined with IBM AIX Trusted Execution (TE), you can verify the integrity of your system and implement advance security policies to enhance the trust level of the complete system.

As data continues to rapidly expand, organizations may struggle when it comes to modernizing their IT infrastructure. IBM Power servers and the IBM AIX operating system (OS) create a solid foundation for the modernization of traditional Oracle database workloads, new application developments and workload consolidation. With the Red Hat Ansible Automation Platform, clients can manage Oracle workloads on IBM Power servers as part of their wider enterprise automation strategy.

Mission-critical workloads need a server and OS with reliability, high availability and the ability to scale without impacting mission-critical performance. IBM Power servers can offer 2.5 times better core than compared to x86 servers, enabling Oracle workloads to grow linearly without hitting bottlenecks.

Oracle certifies its products on Power based-processor servers, delivering a host of benefits including comprehensive end-to-end support, portability and efficiency. IBM Power servers provide 99.999% of reliability to maintain maximum availability. The combined design of the AIX OS on Power servers with IBM PowerHA technology can bring clients stunning uptime, and the ability manage and monitor availability to prevent both planned and unplanned outages.

## Benefits of running Oracle on Power11

Here are some benefits of running your Oracle database workloads on IBM Power11:

- /SM590000 Industry-leading security
- IBM Power and AIX keep your critical Oracle workloads protected and available while reducing costs.2
- /SM590000 Simplified management

Automatically deploy a 'cloud ready' OS capable of meeting any organization's private cloud requirements with IBM PowerVC.

- /SM590000 Unmatched uptime
- IBM Power supports the most demanding workloads and provides 99.999% of reliability to maintain maximum availability.1
- /SM590000 Improved workload cost-effectiveness
- Leverage Power LPAR and DLPAR eligibility for Oracle hard partitioning, clients can license only this Power cores available to Oracle software.
- /SM590000 Standards-based automation

Improve manageability and scalability ensuring consistent and repeatable outcomes by leveraging our enhanced and expanded automation portfolio for Oracle workloads, built on Ansible.

- /SM590000 Data Protection

Benefit from Top-to-Bottom security in Power with trusted boot, main memory encryption, run-time verification of OS files, and role-based access and execution control with PowerSC

For additional information on running Oracle on Power reference the IBM Redbook publication Oracle on IBM Power Systems , SG24-8485.

## 7.3.1  Running Oracle Standard Edition 2 on IBM Power

Oracle Standard Edition 2 (SE2) is a database option suitable for many business needs and can be used on IBM Power servers. SE2 offers a full-featured database with ease of use, power, and performance, including features like relational, JSON, and XML data handling, and Real Application Clusters for clustering services. SE2 is licensed on servers with up to two sockets, with licensing costs remaining the same regardless of the number of cores within each socket.

## Key aspects of using Oracle Standard Edition 2 on IBM Power servers

Here are some key benefits of running Oracle Standard Edition 2 on IBM Power:

- /SM590000 Licensing:

SE2 can be licensed with either the processor metric or the Named User Plus metric. Licensing rules include a maximum of two occupied sockets and a maximum of 16 CPU threads per socket, effectively limiting the number of cores.

- /SM590000 Power System Compatibility:

Oracle Database Standard Edition 2 is compatible with IBM Power based-processor servers, and IBM has even designed specific Power10 servers (Power S1012 and Power S1014) to compete with x86 engines in the two-socket space, catering to Oracle's need for SE2 to be cost-competitive with SQL Server. It is expected that IBM will provide a Power11 server similar to the S1012 in the future that will support Oracle Standard Edition 2.

## Benefits of IBM Power for Oracle Workloads:

IBM Power offers several advantages for Oracle databases, including main memory encryption, runtime verification of OS files, role-based access control, and advanced recovery, self-healing, and diagnostic capabilities.

- /SM590000 High Availability:

Starting with Oracle Database 19c Release Update 19.7, Standard Edition High Availability is supported on IBM AIX on Power based-processor servers. This feature provides cluster-based database failover for Standard Edition Oracle Databases 19c.

- /SM590000 Other Features:

SE2 offers a range of features for building business applications, including support for relational, JSON, XML, spatial, graph, and unstructured data, as well as Oracle Multi-tenant Architecture.

## Licensing and implementation

Consider the following as you plan for your Oracle Standard Edition 2 implementation:

- /SM590000 While the number of cores in each socket does not affect the license price, it is important to adhere to the maximum number of CPUs allowed for the cluster, which is not per node.
- /SM590000 Standard Edition High Availability provides cluster-based failover for single-instance Standard Edition Oracle Databases using Oracle Clusterware.
- -Oracle Standard Edition High Availability benefits from the cluster capabilities and storage solutions that are already part of Oracle Grid Infrastructure, such as Oracle Clusterware, Oracle Automatic Storage Management (Oracle ASM) and Oracle ASM Cluster File System (Oracle ACFS).
- -Using integrated, shared, and concurrently mounted storage, such as Oracle ASM and Oracle ACFS for database files as well as for unstructured data, enables Oracle Grid Infrastructure to restart an Oracle Database on a failover node much faster than any cluster solution that relies on failing over and remounting volumes and file systems.

- -Starting with Oracle Database 19c Release Update (19.13), Standard Edition High Availability is supported on IBM AIX on Power based-processor servers (64-bit).

## 7.4  SAP HANA

IBM Power has a variety of options to meet clients where they are on their journey to SAP S/4HANA. Whether you are considering SAP HANA or the next-generation S/4HANA, IBM Power offers on-premises, off-premises or fully-managed (RISE with SAP) solutions, built to run mission-critical applications like SAP, help accelerate your ERP and application deployments, and help maximize the impact they can have on your data management, data integration, automation and business processes.

IBM and SAP have partnered for over 50 years:

- /SM590000 Over 4,800 clients are running SAP HANA on IBM Power servers
- /SM590000 Over 120 external client references for SAP HANA on IBM Power
- /SM590000 39 SAP Pinnacle Awards won by IBM
- /SM590000 30,000 organizations run essential workloads such as SAP on IBM Power

The key to IT efficiency and business continuity is a platform that integrates with your current infrastructure while simultaneously supporting digital transformation. IBM Power servers are purpose built for data-intensive applications such as SAP HANA and S/4HANA that require large amounts of in-memory computing but still let you maintain the high availability and flexibility required for your hybrid cloud.

## Benefits of running SAP HANA on IBM Power

With global data volumes set to grow to more than 180 zettabytes in 2025, organizations across every sector are facing tremendous pressure to manage, process, store and extract valuable insights from their critical data. By running SAP HANA on IBM Power servers, businesses can:

- /SM590000 Provision Faster
- Simplify system management and boost business agility. 0.01 cores, 1GB memory Create new environments flexibly by allocating incrementally starting as low as 0.01 cores and 1GB memory.
- /SM590000 Maximize uptime

Minimize disruption to business-as-usual activities. #1 Best-in-class reliability for 15 years. 99.999% Five-nines server reliability score achieved during independent testing. 2x Two-times better memory RAS than Industry-Standard DIMMs

- /SM590000 Cut Energy Usage

Reduce datacenter costs and enhance environmental sustainability. 50% less energy IBM Power11 scale-out servers provide comparable performance and requires half the amount of energy used by compared x86-based server. 54% performance boost IBM Power11 scale-out servers uses 15% less energy and provides 54% more performance at maximum input power than the compared x86-based server

- /SM590000 Scale affordably

Reduce the risk of over-provisioning with flexible hybrid cloud solutions, instant scaling, and pay-per-use consumption options. 40TB Scale up capacity - the largest supported for SAP S/4HANA and SAP BW.

- /SM590000 Strengthen security
- Protect critical data and applications from cyberthreats with end-to-end security, including new transparent memory encryption with no performance impact. 60x More secure than unbranded commodity servers.
- /SM590000 Gain Faster Insights

Make rapid decisions to maximize business efficiency. 2.5x Better per core performance than compared x86 servers.

## 7.5  Banking

As financial institutions accelerate digital transformation, IT architects are tasked with designing platforms that are secure, scalable, and AI-ready. IBM Power based-processor servers - particularly Power10 and Power11 - offer a robust foundation for deploying AI workloads in banking environments. With built-in AI acceleration, enterprise-grade RAS features, and seamless integration with hybrid cloud and container platforms, Power based-processor servers enable architects to modernize legacy infrastructure while embedding intelligence into core banking workflows.

## Hybrid Cloud Deployment Models for AI in Banking

Hybrid cloud is the preferred architecture for modern banking platforms, enabling agility, regulatory compliance, and cost optimization. IBM Power based-processor servers support hybrid cloud deployments through:

- /SM590000 IBM Power Virtual Server (PowerVS) for public cloud scalability
- /SM590000 Red Hat OpenShift for container orchestration across environments
- /SM590000 IBM Cloud Pakfi for Data and watsonx for AI lifecycle management

## Banking use cases utilizing AI on IBM Power

Here is a list of some of the use cases for AI for banks and other financial institutions:

- /SM590000 On-Premises AI Training with Cloud-Based Inference
- Banks often need to train AI models on-premises to comply with strict data residency and regulatory requirements. Using IBM Power10 or Power11 systems, financial institutions can securely train models on sensitive customer or transactional data. Once trained, these models are deployed to IBM Power Virtual Server (PowerVS) for inference, enabling scalable, real-time decision-making in the cloud. This hybrid approach is ideal for applications like real-time credit scoring or fraud detection, where data privacy is paramount but rapid response times are also critical.
- /SM590000 End-to-End AI on PowerVS with Secure On-Premises Data Access
- In this model, banks run the full AI lifecycle - training, tuning, and inference - on IBM PowerVS, while maintaining secure access to on-premises data sources. This setup allows institutions to leverage the scalability and flexibility of the cloud without moving sensitive data offsite. For example, a bank might deploy a generative AI model on PowerVS to automate the summarization of complex financial reports, pulling data securely from internal systems. This ensures compliance with data governance policies while accelerating insights and reporting.
- /SM590000 Distributed AI Microservices Across Hybrid Cloud

Some banks adopt a microservices architecture, distributing AI components across both on-premises IBM Power based-processor servers and PowerVS in the cloud. This model supports modular, scalable AI applications that can operate across environments. For

instance, asset valuation engines or personalized client engagement tools can run inference in the cloud while accessing real-time data from on-premises systems. This approach enables agility and performance, especially for institutions managing diverse workloads across geographies or business units.

- /SM590000 AI for Risk and Compliance on IBM Power

Global Tier-1 banks are increasingly turning to AI to automate risk management and compliance processes. By deploying generative AI and machine learning models on IBM Power based-processor servers, these institutions can continuously monitor transactions, flag anomalies, and generate regulatory reports with minimal human intervention. This model supports high-throughput, low-latency processing, making it ideal for meeting stringent regulatory requirements such as anti-money laundering (AML), know-your-customer (KYC), and Basel III compliance.

- /SM590000 AI-Enhanced Core Banking Applications

IBM Power based-processor servers also support the integration of AI directly into core banking platforms. This enables real-time intelligence within mission-critical applications such as loan underwriting, treasury operations, and fraud analytics. For example, a bank might use AI models running on Power11 to detect unusual transaction patterns or predict liquidity needs, enhancing operational efficiency and decision-making. This model ensures that AI capabilities are embedded where they can deliver the most immediate business value.

## Integrating IBM watsonx with IBM Power based-processor servers

IBM watsonx is a modular AI and data platform designed to accelerate the deployment of enterprise-grade AI. When integrated with IBM Power10 and Power11 systems, watsonx enables financial institutions to build, deploy, and govern AI models across hybrid cloud environments - including IBM PowerVS.

Here are the components of watsonx:

- /SM590000 watsonx.ai: Model training and inference
- /SM590000 watsonx.data: Data lakehouse integration
- /SM590000 watsonx.governance: Model risk and compliance
- /SM590000 watsonx.orchestrate: AI agents and workflow automation

IBM Power based-processor servers are high-performance servers optimized for data-intensive workloads. The integration between watsonx and IBM Power enables:

- /SM590000 Accelerated AI Workloads: Power11 processors are optimized for AI inference and training, making them ideal for running watsonx models efficiently.
- /SM590000 Hybrid Cloud Flexibility: watsonx can run on IBM Power in hybrid cloud environments, allowing businesses to keep sensitive data on-premises while leveraging cloud-native AI capabilities.
- /SM590000 Enterprise-Grade Security and Reliability: Power based-processor servers provide robust security and uptime, aligning with watsonx's focus on trustworthy AI.
- /SM590000 Tight Integration with Red Hat OpenShift: Both watsonx and IBM Power support OpenShift, enabling containerized AI workloads to run seamlessly across environments.

## 7.6  Health Care

IBM Power based-processor servers provide a secure, high-performance, and resilient infrastructure that enables healthcare organizations to manage and protect digital health data, drive data-informed decisions, and meet regulatory requirements with confidence. Designed for mission-critical workloads, Power empowers healthcare providers to improve patient outcomes, enhance operational efficiency, and reduce risk.

## Security and Compliance

Healthcare organizations handle sensitive patient data that must be protected under regulations such as HIPAA. IBM Power delivers advanced security features including secure boot, role-based access control, and encryption at rest and in transit. With quantum-safe firmware signing and encrypted Live Partition Mobility (LPM), Power ensures data integrity and privacy. According to ITIC, organizations using Power experience an average of just 3.3 minutes of unplanned downtime per year due to security issues - demonstrating its industry-leading resilience.

## Unmatched Reliability for Clinical Systems

Power is engineered for continuous availability of mission-critical applications such as EHRs, PACS, and healthcare information systems. Features like predictive failure analysis, dynamic resource allocation, and system redundancy contribute to its 99.9999% availability rating, as reported by 1,900 C-level executives in ITIC's global reliability survey. Power has held the title of the most reliable non-mainframe server platform for over 15 years.

## High-Performance Computing for Healthcare Analytics

Healthcare workloads - from medical imaging to genomics and real-time analytics - demand exceptional compute power. Power11-based servers deliver up to 2.5x more performance per core than previous generations, enabling faster insights for research, drug discovery, and personalized medicine.

## Scalable and Flexible Infrastructure

Healthcare environments often face unpredictable demand. IBM Power supports dynamic scaling to accommodate workload fluctuations, whether driven by seasonal surges or new clinical initiatives. Its support for multiple operating systems and virtualization technologies allows healthcare IT teams to run diverse workloads efficiently on a single platform.

## AI-Ready for Clinical Innovation

IBM Power is optimized for AI and machine learning workloads, with on-chip Matrix Math Accelerators (MMAs) that enable real-time inferencing at the point of care. Power S1122 servers can process up to 42% more batch queries per second than comparable x86 systems under peak load, with sub-second inferencing latency - ideal for applications like diagnostic imaging, predictive analytics, and treatment optimization.

## Seamless Integration with Healthcare Ecosystems

IBM Power integrates with a wide range of healthcare applications, including EMRs, imaging platforms, analytics tools, and telemedicine systems. It supports interoperability and data exchange across systems, and works closely with leading ISVs such as Epic to certify hardware for industry-standard healthcare software.

## 7.6.1  Epic

Epic is a Healthcare Information System (HIS) provider that develops and delivers a comprehensive electronic medical record (EMR) system covering all aspects of the medical healthcare profession. The Epic solution includes a variety of applications that cover areas, such as medical billing, emergency room, radiology, outpatient, inpatient, and ambulatory care.

IBM and Epic Systems maintain a strategic partnership that enables healthcare organizations to run Epic's electronic health record (EHR) platform on IBM infrastructure, particularly IBM Power based-processor servers and IBM Storage solutions. This collaboration is designed to support the performance, security, and compliance needs of healthcare providers managing mission-critical clinical workloads.

IBM Power based-processor servers are certified to run Epic Operational Database (ODB) workloads, with best practices published for tuning AIX environments to meet Epic's stringent performance requirements. These configurations are optimized for high throughput, low latency, and high availability - critical for real-time clinical operations. Currently, IBM Power10 servers are certified by Epic Systems, supporting key infrastructure components on both AIX and Linux for large healthcare deployments, primarily in the database and backend services tier. These platforms are used to host InterSystems CachØ or IRIS for Health, which serve as the core databases behind Epic's EHR system.

It is expected that IBM and Epic will partner to certify Power11 configurations after the Power11 systems are available.

## Supported Products

Here is a list of currently supported Epic products:

- /SM590000 InterSystems CachØ / IRIS for Health
- -Officially supported by Epic on both AIX and Linux (RHEL) on Power10.
- -Deployed in production for the Epic operational database (Chronicles).
- /SM590000 Epic Production and Reporting Database Tiers
- -Most often run on AIX or RHEL on Power10 for performance and reliability.
- /SM590000 Other backend services, such as database copies used for Clarity extracts, may also run on AIX or Linux, depending on the customer's architecture.

Note: The Epic application layer (Hyperspace, Interconnect, etc.) typically runs on Windows or Linux on x86. Power-based AIX or Linux deployments are focused on the infrastructure and database tiers.

Required OS and Firmware Levels for Power10:

- /SM590000 AIX:
- -AIX 7.2 TL5 SP4 or later
- -AIX 7.3 TL1 or later
- Certified by both Epic and InterSystems for Power10 compatibility.
- /SM590000 Linux:
- -Red Hat Enterprise Linux (RHEL) 8.6 or later on Power10 (ppc64le)
- Certified by InterSystems for IRIS for Health on Power.
- Required for newer installations using containerized services or performance-optimized Linux environments.

- /SM590000 Virtualization:
- -Both AIX and Linux deployments use IBM PowerVM for LPAR management.
- -Linux LPARs can also be deployed using OpenShift on Power for modern container-based workloads.
- /SM590000 Storage:
- -High-performance SAN such as IBM FlashSystem is commonly used, with tuning for CachØ/IRIS.
- /SM590000 HA/DR:
- -PowerHA for AIX,
- -Linux HA tools (including IBM VM Recovery Manager),
- -InterSystems mirroring for resilience.

<!-- image -->

Chapter 8.

8

## Servicing Power11

The goal of serviceability is to enable efficient system repair while minimizing or avoiding any disruption to operations. It encompasses system installation, upgrades or downgrades (Miscellaneous Equipment Specification or MES), and ongoing maintenance or repair activities. Depending on the system configuration and warranty agreement, service tasks may be performed by the client, an IBM technician, or an authorized service provider.

IBM Power based-processor servers are designed with advanced serviceability features to support a highly efficient maintenance environment. These features help streamline service operations and reduce downtime by incorporating the following key attributes:

- -Simplified installation and upgrade processes
- -Support for concurrent maintenance and guided repair
- -Automated diagnostics and error reporting
- -End-to-end service workflows, from issue detection to resolution.

The following topics are covered in this chapter:\

- /SM590000 IBM Maintenance
- /SM590000 IBM Expert Care
- /SM590000 IBM tools and interfaces
- /SM590000 BMC card
- /SM590000 ASMI
- /SM590000 Entitled System Support
- /SM590000 System firmware

## 8.1  IBM Maintenance

IBM offers a comprehensive global maintenance and support framework for its Power based-processor servers, designed to ensure high availability, rapid issue resolution, and minimal disruption to business operations. Maintenance services are available under various service level agreements (SLAs), tailored to meet the needs of different environments - from standard business hours to mission-critical 24/7 operations. IBM's support infrastructure includes remote diagnostics, on-site service, and proactive monitoring, all backed by a global network of skilled service professionals and parts depots.

Customers can choose between 8x5 and 24x7 service coverage. The 8x5 option provides support during standard business hours (typically 8 a.m. to 5 p.m., Monday through Friday, excluding holidays), which is ideal for non-critical systems or environments with internal IT support. For systems that require continuous uptime, the 24x7 service option ensures around-the-clock support, including weekends and holidays. This level of coverage is essential for industries such as finance, healthcare, and manufacturing, where downtime can have significant operational or financial consequences.

IBM also defines response time targets based on the selected service level. For example, under a 24x7 agreement, IBM may commit to a 2-hour or 4-hour on-site response for critical hardware issues, depending on the location and contract terms. These response times are supported by IBM's extensive global logistics and service infrastructure, which includes strategically located parts centers and field engineers in over 170 countries.

This worldwide coverage ensures that IBM Power based-processor servers customers receive consistent, high-quality support regardless of their geographic location. IBM's maintenance services are further enhanced by features such as call-home diagnostics, automated error reporting, and remote problem determination, which help accelerate issue resolution and reduce the need for manual intervention. Combined, these capabilities provide a robust and reliable maintenance ecosystem that supports both traditional on-premises deployments and modern hybrid cloud environments.

## 8.2  IBM Expert Care

Managing your IBM Power based-processor servers should be seamless and efficient. Power Expert Care delivers immediate access to a curated bundle of high-value services trusted by the Power community - eliminating the delays and complexity of traditional procurement processes. With this preselected service package, clients benefit from streamlined support, enhanced by AI-driven tools that accelerate response times, improve case resolution, and elevate overall satisfaction.

What sets Power Expert Care Premium apart is its focus on mission-critical environments where downtime is not an option. Backed by the same experts who helped design and build the Power11 platform, this service tier ensures your infrastructure is supported by unmatched technical depth and operational excellence.

Key Features of the Premium Bundle:

- /SM590000 30-minute response time for both hardware and software support cases
- /SM590000 4-hour on-site response target for urgent issues
- /SM590000 System and microcode compatibility guidance to ensure optimal performance
- /SM590000 Dedicated Technical Account Manager and mission-critical support resources

- /SM590000 Automated case creation and log analysis for faster issue resolution
- /SM590000 Health checks for hardware, OS, and applications (available as add-ons)
- /SM590000 Zero planned downtime support with proactive planning and TAM assistance

For non-mission-critical systems IBM offers the Advanced Expert Care bundle providing 24x7 standard response times on repair and maintenance cases.

## Technical Account Manager

The Technical Account Manager (TAM) plays a vital role in delivering proactive, product-based support for IBM Power based-processor servers. Acting as the primary point of contact, the TAM provides strategic guidance and direct engagement for both hardware and software within the scope of your support agreement. TAM services are delivered in English during the client's business hours, with support in other languages available upon request and mutual agreement, subject to availability.

TAMs help streamline operations and reduce downtime through a wide range of responsibilities, including:

- /SM590000 Enabling Call Home for proactive error reporting, Autonomous Error Resolution (AER), and Zero Planned Downtime (ZPD) - available on Power11
- /SM590000 Activating Support Insights for predictive analytics and delivering monthly reports
- /SM590000 Providing firmware and microcode compatibility analysis (exclusive to Power11 Premium clients)
- /SM590000 Sharing software lifecycle and roadmap updates
- /SM590000 Delivering HIPER alerts to help avoid high-impact issues
- /SM590000 Offering best practices documentation and priority handling of Severity 1 and 2 cases
- /SM590000 Leading complex case resolution and managing case progression
- /SM590000 Coordinating welcome calls, support planning, monthly reporting, and quarterly reviews
- /SM590000 Engaging IBM resources for Remote Code Load on Power10 and Power11 systems (on-site code load available separately for Power11)
- /SM590000 Supporting change management by communicating planned events to relevant teams

For clients running SAP HANA on Power10 or Power11, the TAM also:

- /SM590000 Advises on SAP HANA best practices
- /SM590000 Coordinates troubleshooting across the full software/hardware stack
- /SM590000 Provides technical recommendations for error identification, environment optimization, and known defect mitigation

## 8.3  IBM tools and interfaces

Servicing IBM Power servers relies on a robust combination of proactive maintenance, intelligent diagnostics, and modern remote management tools - all designed to ensure high availability and system reliability. At the heart of this ecosystem is the Hardware Management Console (HMC), which serves as the central hub for monitoring system health, managing logical partitions (LPARs), and coordinating service activities. Complementing the HMC is the service processor, a dedicated hardware component that operates independently of the main system. It continuously monitors hardware status, logs errors, and enables early detection of potential issues. Features like call-home support and automated error reporting further

## 8.5  ASMI

streamline the support process by alerting IBM support teams to critical events - often before they impact operations.

The service processor can be accessed and managed through the HMC, but also directly via the Advanced System Management Interface (ASMI), which provides low-level control and additional troubleshooting capabilities. For modern, automated environments, the service processor also supports DMTF Redfish APIs, enabling secure, standardized remote management and integration with broader data center orchestration tools. Together, these technologies form a resilient and intelligent service infrastructure that supports both on-premises and hybrid cloud deployments, helping ensure that IBM Power based-processor servers remain secure, efficient, and continuously operational.

## 8.4  BMC card

The Power11 scale-out systems use an eBMC for system service management, monitoring, maintenance, and control. The eBMC also provides access to the system event log files (SEL). The eBMC controller is card is in a dedicated slot (C5).

The eBMC is a specialized service processor that monitors the physical state of the system by using sensors. A system administrator or service representative can communicate with the BMC through an independent connection.

ASMI is the GUI to the eBMC. It is similar in terms of its function to the ASMI with Flexible Service Processor (FSP)-managed servers, but it is a complete redesign of the UI that was driven by customer feedback that was received during a Design Thinking workshop.

To enter the ASMI GUI, you can use the HMC by selecting the server and then selecting Operations → Launch Advanced System Managemen t. A window opens that displays the name of the system; model, type, and serial; and the IP of the service processor (eBMC).

Click OK and the ASMI window opens.

If the eBMC is connected to a network that also is accessible from your workstation, you can connect directly by entering https://&lt;eBMC IP&gt; in your web browser. Figure 8-3-1 shows the ASMI login window.

Figure 8-1   ASMI login window

<!-- image -->

After you log in, the Overview window is shown, which includes server, firmware, network, power, and status information. When you log in for the first time, the default username and password is admin, but invalidated. That is, after the first login, you must immediately change the admin password.

This change also must be made after a factory reset of the system. This policy change helps to enforce that the eBMC is not left in a state with a well-known password, which improves the security posture of the system. The password must meet specific criteria (for example, a password of abcd1234 is invalid).

The new ASMI for eBMC managed servers feature some important differences from the ASMI version that is used by FSP-based systems. It also delivers some valuable new features:

- /SM590000 Update system firmware

A firmware update can be installed for the server by using the ASMI GUI, even if the system is managed by an HMC. In this case, the firmware update always is disruptive.

To install a concurrent firmware update, the HMC must be used, which is not possible by using the ASMI GUI.

- /SM590000 Download memory dumps

Memory dumps can be downloaded by using the HMC. Also, they also download them from the ASMI menu if necessary. It is also possible to start a memory dump from the ASMI. Click Logs → Dumps and then, select the memory dump type and click Initiate memory dump. The following memory dump types are available:

- -BMC memory dump (nondisruptive)
- -Resource memory dump
- -System memory dump (disruptive)
- -Network Time Protocol (NTP) server support
- -Lightweight directory access protocol (LDAP) for user management
- -Host console

By using the host console, you can monitor the server's start process. The host console can also be used to access the operating system when only a single LPAR uses all of the resources.

- /SM590000 User management

You can create your own users in the eBMC. This feature can also be used to create an individual user that can be used for the HMC to access the server.

A user features one of the following privileges:

- -Administrator
- -Read Only (you cannot modify anything (except the password of that user); therefore, a user with this privilege level cannot be used for HMC access to the server.
- /SM590000 IBM security by way of Access Control Files

To get 'root access' to the service processor by using the user celogin in FSP-managed servers, the IBM support team generated a password by using the serial number and the date.

In eBMC managed systems, the support team generates an Access Control File (ACF). This file must be uploaded to the server to get access. This procedure is needed (for example) if the admin password must be reset. This process requires physical access to the system.

- /SM590000 Jumper reset

Everything on the server can be reset by using a physical jumper. This factory reset process resets everything on the server, such as LPAR definitions, eBMC settings, and the NVRAM.

## 8.5.1  Additional ASMI functions

This section discusses some additional functions of the ASMI.

## Realtime progress indicator

The ASMI of an eBMC server also provides a real-time progress indicator to see the operator panel codes. To open the window that shows the codes, click Logs → Progress logs and then, click View code in real time .

## Inventory and LEDs

Under Hardware status → Inventory and LEDs , you can find most of the hardware components with their current state, and controls for an identification LED for each component, the system identification LED, and the system attention LED. You can switch all identification LEDs on and off individually. The system attention LED can be turned off only.

A component can also be displayed. This feature is helpful to see details; for example, the size of a DDIMM or the part number of a component if something must be exchanged.

## Sensors

The ASMI features data from various sensors that are available within the server and many components by clicking Hardware status → Sensors . The loading of the sensor data takes some time, during which you see a progress bar on the top of the window.

## Network settings

The default network settings for the two eBMC ports are to use DHCP. Therefore, when you connect a port to a private HMC network with the HMC as a DHCP server, the new system

receives its IP address from the HMC during the start of the firmware. Then, the new system automatically appears in the HMC and can be configured.

Note: DHCP is the recommended way to attach the eBMC of a server to the HMC.

If you do not use DHCP and want to use a static IP, you can set the IP in the ASMI GUI. However, before you can make this change, you must connect to the ASMI. Because no default IPs are the same for every server, you first must determine the configured IP.

To determine the configured IP, use the operator window. This optional component includes the recommendation that one operator window is purchased per rack of Power11 processor-based scale-out servers.

In the control window, complete the following steps:

1. Use the Increment or Decrement options to scroll to function 02.
2. Click Enter until the value changes from N (normal) to M (manual). This process activates access to function 30.
3. Scroll to function 30 and click Enter until 30** appears.
4. Scroll to 3000 and click Enter , which displays the IP of the ETH0 port. If you scroll to 3001 and click Enter , the IP of ETH1 is displayed.
5. After you determine the IP, scroll again to function 02 and set the value back from M to N.

For more information about function 30 in the operator window, see Function 30: Service processor IP address and port location. REPLACE WITH NEW LINK FOR POWER11

Now that you have determined the IP, you can configure any computer with a web browser to an IP in the same subnet (class C) and connect the computer to the correct Ethernet port of the server.

After connecting the cable, you can now use a web browser to access the ASMI with https://&lt;IP address&gt; and then, configure the network port address settings.

To configure the network ports, click Settings → Network and select the correct adapter to configure.

Before you can configure a static IP address, switch off DHCP. Several static IPs can be configured on one physical Ethernet port.

In the ASMI network settings window, you cannot configure the VMI address. The VMI address is another IP that is configured on the physical eBMC Ethernet port of the server to manage the Virtualization of the server. The VMI address can be configured in the HMC only.

## Using an Access Control File

If you lose the access password for the ASMI service user, you can access the ASMI by using an ACF. The ACF is a digital certificate that is provided by IBM support when you open a support case. To use the ACF, the system must be enabled at the server by using the operator panel.

Complete the following steps:

1. On the operator panel, use the Increment or Decrement buttons to scroll to function 74.
2. Click Enter and then, select 00 to accept the function (FF rejects it). Now, the ACF function is active for 30 minutes. To use it, complete the following steps:
- a. Enter the ASMI login window.
- b. Click Upload service login certificate to upload the ACF into the system and allow the user to enter the ASMI with the associated password that also is supplied by IBM support.

For more information, see Function 74: Authentication Override for ACF upload.

## Policies

In Security and access → Policies, you can switch security-related functions on and off.

For example,

- /SM590000 Whether management over Intelligent Platform Management Interface (IPMI) is enabled.
- /SM590000 Switch off Host USB enablement.Some customers require that the USB ports of the server must be disabled. This change can be made in the Policies window.

## 8.6  Entitled System Support

IBM Enterprise Storage Server is available to view and manage Power and Storage software and hardware. In general, most products that are offered by IBM Systems that are purchased through our IBM Digital Sales representatives or Business Partners are accessed on this site when the IBM Configurator is used.

The site features the following three main sections:

- /SM590000 My entitled software

Activities are listed that are related to Power and Storage software, including the ability to download licensed, free, and trial software media, place software update orders, and manage software keys.

- /SM590000 My entitled hardware

Activities are listed related to Power and Storage hardware including the ability to renew Update Access Keys, buy and use Elastic Capacity on Demand, assign or buy credits for new and existing pools in a Power Private Cloud environment (Enterprise Pools 2.0), download Storage Capacity on-Demand codes, and manage Hybrid Capacity credits.

- /SM590000 My inventory

Activities related to Power and Storage inventory including the ability to browse software license, software maintenance, and hardware inventory, manage inventory retrievals by way of Base Composer or generate several types of reports.

## 8.7  System firmware

System firmware provides low-level control for the system hardware. New features and fixes are introduced with new firmware release levels. Fixes are often bundled into service packs. A service pack is referred to as an update level. A new release is referred to as an upgrade level. All system firmware is available for download in IBM FixCentral.

## Terminology

Release Level:

A major new function (introduction of new hardware models and significant function and features enabled via firmware). This firmware upgrade is disruptive.

Service Pack (SP):

Primarily firmware fixes and minor function changes applicable to a specific Release Level. These firmware updates are usually concurrent.

Concurrent:

A code update that allows the operating system(s) running on the Power system to continue running while the update is installed and activated.

Deferred:

A code fix that is installed concurrently, but does not activate until the system is restarted.

Partition Deferred:

A code fix that is installed concurrently but does not activate until the partition is restarted.

Disruptive:

A code fix which requires a system restart during the code update process.

## Service pack severity

The severity classification is specific for each service pack that becomes available in FixCentral. All types are listed below:

NEW:

New features and functions. This is considered a new release level for a product.

PE (PTF in error):

This service pack addresses minor issues. It can be installed when convenient.

ATT (attention):

This service pack addresses low impact and low potential issues. It should be installed at the customer's earliest convenience.

SPE (special attention):

This Service Pack addresses high impact but low potential issues. It should be installed at earliest convenience.

HIPER (high impact / pervasive):  This service pack addresses high impact and/or pervasive issues with significant customer impacts, and therefore should be installed as soon as possible.

For more details refer to: https://www.ibm.com/support/pages/glossary

## System Firmware Update Strategy for IBM Power11 Systems

The system management model determines the appropriate firmware update strategy for IBM Power11 systems.

- /SM590000 For managed systems, the recommended method for updating system firmware is via the Hardware Management Console (HMC).
- /SM590000 For unmanaged systems, the preferred method is to update the system firmware directly through the operating system.

While these are the recommended approaches, it is also possible to update the system firmware using the embedded BMC (eBMC).

The update method impacts the type of update:

- /SM590000 Firmware updates from the HMC can be either concurrent or disruptive, depending on the firmware version.
- /SM590000 Firmware updates from the operating system or eBMC are always disruptive.

A concurrent firmware update does not require a system restart. This is indicated in the firmware description file under the Service Pack Summary, which categorizes the update as either Disruptive Service Pack, Deferred Service Pack, or Concurrent Service Pack.

However, any fixes marked as DEFERRED in the Service Pack Summary will not take effect until the next system IPL (Initial Program Load). Fixes labeled as DEFERRED: PARTITION\_DEFERRED will require a partition reboot to take effect.

Depending on the system management model, the following firmware update options are available:

- /SM590000 HMC-managed systems: Firmware updates can be performed using the HMC or the eBMC ASMI interface.
- /SM590000 Co-managing a system with both PowerVM NovaLink and the Hardware Management Console (HMC): Firmware updates can be performed using the HMC, the NovaLink partition, or the eBMC/ASMI interface. However, to perform the update through the HMC, the system must first be transitioned from PowerVM NovaLink management to HMC management.
- /SM590000 Unmanaged systems running IBM i: Updates can be applied using PTFs or via the eBMC ASMI interface.
- /SM590000 Unmanaged systems running AIX: Firmware updates are supported through AIX system diagnostics or the eBMC ASMI interface.
- /SM590000 All IBM Power11 systems also support system firmware updates via the eBMC USB port.

Note: The responsibility for performing system firmware updates resides with the customer. If the customer requests that a IBM Support Service Representative (SSR) carry out the firmware update, the request will be considered a billable service - unless the customer has a valid support agreement that explicitly includes on-site firmware update coverage.

The firmware description file available on IBM Fix Central provides essential information about dependencies between HMC versions, AIX APARs, IBM i PTFs, and system firmware levels. Before installing a new system firmware release or service pack, it is strongly recommended to review the firmware description package.

For cross-version compatibility details, refer to the IBM Power based-processor servers Fix Level Recommendation Tool (POWER code matrix).

## Updating System Firmware from the HMC

To update or upgrade the system firmware using the Hardware Management Console (HMC), follow the steps below:

1. In the System View, select the system you want to update.
2. Click on the Firmware menu.
3. Choose Update System Firmware.

The Update System Firmware Wizard will guide you through the necessary steps to complete the firmware update process, as shown in Figure 8-2 on page 181.

Figure 8-2   Launch the Update System Firmware wizard.

<!-- image -->

The Firmware Update Wizard guides you through the process of updating your system. It begins with accepting the license agreement, followed by performing a system health check using the Readiness Check. Next, you will provide the required firmware files and select the firmware level to be applied. The final step involves monitoring the update progress and confirming its successful completion. Figure 8-3 through 3-6 illustrate these key steps in the update process.

Figure 8-3   The license agreement is displayed for the user to review and accept the terms.

<!-- image -->

Figure 8-4 on page 182 shows that the System Readiness Check has completed successfully for the IBM Power11 system firmware update process.

Figure 8-4   shows that the System Readiness Check completed successfully.

<!-- image -->

Figure 8-5 illustrates the 'Choose source files location' drop-down menu, which is used to update the system firmware. Several options are available for loading the required update files, including:

- /SM590000 IBM Website
- /SM590000 FTP Server
- /SM590000 SFTP Server
- /SM590000 Mount Point on the HMC
- /SM590000 CD/DVD
- /SM590000 USB Drive

Figure 8-5   the 'Choose Source File Location' drop-down menu used for updating the system firmware.

<!-- image -->

As shown in Figure 8-6 on page 183, click the 'Search Available Levels' button to locate the new system firmware on the installation media. On the following screen, use the drop-down menu under the 'Target eBMC Level' column to select the desired system firmware level.

Figure 8-6   System Firmware Target Level Selection Screen. This screen allows you to choose between a firmware update or upgrade.

<!-- image -->

## Import Update Files from HMC

The Import Update Files wizard in the HMC GUI, as shown in Figure 8-7, guides you through the necessary steps to import firmware update or upgrade files. These files can then be reused to update the firmware on other IBM Power11 systems.

Figure 8-7   The 'Import Update Files' option in the HMC GUI.

<!-- image -->

## Delete Files from Import Location

The Delete Files from Import Location wizard in the HMC GUI, as shown in Figure 8-8 on page 184, guides you through the steps to delete imported firmware files. This allows you to manage and clean up firmware files stored on the HMC.

Figure 8-8   The 'Delete Files from Import Location' option in the HMC GUI.

<!-- image -->

## SR-IOV Shared Mode Adapter Firmware Management

SR-IOV capable adapters running in Shared mode use a different firmware versioning mechanism compared to those operating in Dedicated mode.

## SR-IOV Configuration Requirements

- /SM590000 Ensure that the managed system includes PCIe adapter(s) that support SR-IOV functionality.
- /SM590000 Each SR-IOV-capable adapter must be installed in a PCIe slot that supports SR-IOV. Refer to the adapter placement guidelines in the IBM Documentation.
- /SM590000 Verify that the system is running a supported level of:
- -System firmware
- -HMC or PowerVM NovaLink
- -Operating system (with SR-IOV driver support)
- /SM590000 Configure the adapter(s) in SR-IOV Shared Mode using either the HMC or NovaLink interface.

## In SR-IOV (Shared mode):

- /SM590000 The adapter firmware and driver are integrated with the system firmware.
- /SM590000 Firmware updates and accompanying ReadMe documentation are available on IBM Fix Central.
- /SM590000 When an adapter is configured in SR-IOV Shared mode, its firmware and driver are automatically updated to the latest versions included with the system firmware. This update occurs during standard maintenance operations such as a system IPL, adapter replacement, or when switching the adapter mode between Shared and Dedicated.
- /SM590000 Additionally, if system firmware updates are installed concurrently, selective manual updates of SR-IOV adapter firmware can be performed using the Hardware Management Console (HMC).

https://www.ibm.com/docs/en/power10/7063-CR1?topic=firmware-update-sr-iov

Note: You may update either the adapter firmware alone or both the adapter driver and firmware. During the firmware update process, network traffic on the configured logical ports of the SR-IOV adapter may be temporarily disrupted. Updating each SR-IOV adapter typically takes between 2 to 5 minutes. The update is performed sequentially across all SR-IOV adapters in the system.

Figure 8-9 displays the 'View SR-IOV Firmware Levels' and 'Update SR-IOV Firmware' options available in the HMC GUI.

Figure 8-9   'View SR-IOV Firmware Levels' and 'Update SR-IOV Firmware' options available in the HMC GUI.

<!-- image -->

## Updating System Firmware via eBMC

The eBMC ASMI (Advanced System Management Interface) can be used to update the system firmware on both managed and unmanaged systems. To perform a firmware update via eBMC ASMI, the system must be powered off. The firmware package includes multiple files, but only the firmware image with the.tar file extension is required for the update process. For example, refer to Figure 8-10.

Figure 8-10   Firmware Update via eBMC ASMI.

<!-- image -->

## I/O Microcode Update Strategy

Microcode updates are the responsibility of the customer, unless the services are provided under a Microcode Support Services contract.

Device microcode can be updated using the following methods:

- /SM590000 HMC (Hardware Management Console):

The 'Update I/O Firmware' feature available in the HMC GUI allows administrators to apply microcode updates to supported I/O devices.

## /SM590000 Diagnostic Menus (AIX and VIOS):

Microcode updates can be performed using either the system diagnostics or stand-alone diagnostics utilities, from a USB key or a network location. This method is applicable to AIX and VIOS environments.

## /SM590000 Linux:

Refer to the microcode README files available on IBM FixCentral for detailed instructions on updating microcode on Linux systems. These instructions may include the use of additional vendor-provided tools, depending on the I/O devices.

- /SM590000 IBM i (PTFs):

This method is applicable only to IBM i systems. Microcode updates are delivered through Program Temporary Fixes (PTFs), which can be downloaded from IBM FixCentral.

## Viewing or Updating I/O Firmware from the HMC

The Hardware Management Console (HMC) can be used to view the current I/O firmware levels for a system and to update those levels using a firmware repository. The HMC does not have direct access to log in to the partitions to perform I/O firmware updates. Instead, it relies on the Resource Monitoring and Control (RMC) infrastructure also used for features like Dynamic Logical Partitioning (DLPAR) and Service Focal Point to facilitate communication between the HMC and the partitions. On each partition, the invscout command handles the query and update process. Invscout exchanges inventory and update-related files with the HMC over the RMC interface.

Figure 8-11 displays the 'View I/O Firmware Levels' and 'Update I/O Firmware' options available in the HMC GUI.

Figure 8-11   'View I/O Firmware Levels' and 'Update I/O Firmware' options available in the HMC GUI.

<!-- image -->

Figure 8-12 on page 187 displays the 'View I/O Firmware Levels' panel, which shows I/O firmware information for both FSP and eBMC-based systems, as available in the HMC GUI.

Figure 8-12   'View I/O Firmware Levels' panel available in the HMC GUI.

<!-- image -->

Figure 8-13 illustrates the 'Choose Source Files Location' drop-down menu, which is used to specify the source location for updating the microcode on I/O devices. Several options are available for loading the required update files, including:

- /SM590000 IBM Website
- /SM590000 FTP Server
- /SM590000 SFTP Server
- /SM590000 Mount Point on the HMC
- /SM590000 CD/DVD
- /SM590000 USB Drive

Figure 8-13   Update I/O firmware screen

<!-- image -->

For additional information on how to view or update the I/O firmware from the HMC, please refer to the following technical document: 'View or Update the I/O Firmware from the HMC'.

## 8.7.1  Update Access Keys

Since the introduction of the IBM Power8 processor-based servers, IBM uses the concept of an Update Access Key (UAK) for each server.

When system firmware updates are applied to the system, the UAK and its expiration date are checked. System firmware updates include a release date. If the release date for the firmware

updates is past the expiration date for the update access key when attempting to apply system firmware updates, the updates are not processed.

## Managing Update Access Keys

The system uses an Update Access Key (UAK) to control the application of system firmware updates. Each UAK includes an expiration date, while firmware updates include a release date. When a firmware update is applied, the system checks whether the update's release date is later than the UAK's expiration date. If it is, the firmware update will not be processed. When a UAK expires, it must be replaced using either the Hardware Management Console (HMC) or the eBMC ASMI interface. Importantly, the expiration of a UAK does not affect I/O microcode updates these can still be applied even if the UAK has expired. Customers can obtain a new UAK by opening a case with IBM Support and requesting a renewal key, or by downloading it directly from the IBM Entitled Systems Support (ESS) website:

https://www.ibm.com/servers/eserver/ess/landing/landing-page

By default, newly delivered systems include an UAK that expires after three years. Thereafter, the UAK can be extended every six months, but only if a current hardware maintenance contract exists for that server. The contract can be verified on the Enterprise Storage Server web page.

The validity and expiration date of the current UAK can be checked using either the HMC or eBMC graphical interfaces, as well as through their respective command-line interfaces. Additionally, the expiration date can also be retrieved from the operating system level.

## Verifying the Expiration Date of UAKs Using HMC

The current Update Access Key (UAK) expiration date is visible on the View current system firmware levels of the HMC, as shown in Figure 8-14.

Figure 8-14   UAK expiration date displayed on the HMC View current system firmware levels page.

<!-- image -->

The Hardware Management Console (HMC) or vHMC (Virtual HMC Software Appliance) can be used to configure the Automatic Firmware Update Access Key. For more information, refer to the documentation titled 'How to Automatically Update the Access Key'.

## Verifying the Expiration Date of UAKs Using eBMC ASMI

The current Update Access Key (UAK) expiration date is visible on the Firmware and Overview pages of the eBMC ASMI, as shown in Figure 8-15 on page 189 and Figure 8-16 on page 189.

Figure 8-15   UAK expiration date displayed on the eBMC Firmware page.

<!-- image -->

Figure 8-16   UAK expiration date displayed on the eBMC Overview page.

<!-- image -->

## Verifying the Expiration Date of UAKs Using AIX

There are multiple methods of checking the UAK expiration date within AIX:

- /SM590000 The first option utilizes the lscfg command. Use the following command:

lscfg -vpl sysplanar0 |grep -p "System Firmware"

The output is similar to the output that is shown in Example 8-1.

```
lscfg -vpl sysplanar0 |grep -p "System Firmware" System Firmware: Code Level, LID Keyword.....Phyp_1 21372025061280A00701 Code Level, LID Keyword.....PFW 21212025060681CF0681 Code Level, LID Keyword.....FSP_Fil 16112025061681E00109 Code Level, LID Keyword.....FipS_BU 16112025061681E00208 Microcode Image.............RK1110_058 RK1110_057 RK1110_058 Microcode Level.............FW1110.00 FW1110.00 FW1110.00 Microcode Build Date........20250725 20250725 20250725
```

Example 8-1   Output of the lscfg command to check UAK expiration date.

```
Update Access Key Exp Date..20301014 Hardware Location Code......U9080.HEU.DEN0013-Y1 Physical Location: U9080.HEU.DEN0043-Y1
```

- /SM590000 Alternatively, you can grep on Access Key as shown in Example 8-2.
- /SM590000 A third option on AIX 7.3 is the lparstat command which is shown in Example 8-3.

```
# lscfg -vpl sysplanar0 | grep "Access Key"
```

Example 8-2   Output of the lscfg command to check UAK expiration date

```
Update Access Key Exp Date..20301014
```

```
# lparstat -u FW Update Access Key Expiration  (YYYYMMDD):  20301014 AIX Update Access Key Expiration (YYYYMMDD):  20301014 AIX Image Date                   (YYYYMMDD):  20250725
```

Example 8-3   Output of the lparstat command to check UAK expiration date

## Verifying the Expiration Date of UAKs Using Linux

There isn't a single Linux command to view a UAK directly. Instead, UAKs are managed through IBM's tools and interfaces, like ESA, ASMI and HMC.

## Managing the UAK with IBM i

IBM Electronic Service Agent (ESA) on IBM i has introduced a new feature to help clients easily manage the refreshment of their update access keys (UAK) for IBM i stand-alone partitions. There are two ways of using this UAK management feature:

Manual: A system administrator can manually launch the process of checking UAK's expiration date, downloading UAK, and applying UAK. This is accomplished by running the WRKSRVAGT TYPE(*UAK) command. This can also be accomplished by running the GO SERVICE command to access the Electronic Service Agent on IBM i main menu, then selecting Option 20. Check and refresh Update Access Key, as shown in Figure 8-17 and Figure 8-18 on page 191.

Figure 8-17   Electronic Service Agent on IBM i main menu option 20

<!-- image -->

Help instructions on option 20 can help clients to understand this feature.

Figure 8-18   Help information on Electronic Service Agent on IBM i main menu option 20

<!-- image -->

Automatic: The Change Service Agent Attribute (CHGSRVAGTA) command can be used to enable automatic checking. The CHGSRVAGTA command parameter (REFRESHUAK) can be used to establish automatic UAK management. By default, a job named QS9UAK, will be run every Sunday, but can be easily customized.

## Enablement steps:

- /SM590000 Enter CHGSRVAGTA and press F4.
- /SM590000 Enter Yes for Enable.
- /SM590000 Press Page Down.

At this point, the Change Service Agent Attribute panel appears as shown in Figure 3. Specify the weekday and time to use for UAK refresh processing.

Figure 8-19   Change Service Agent Attribute - refresh UAK configuration panel

<!-- image -->

<!-- image -->

Chapter 9.

9

## Virtualization

Virtualization on IBM Power based-processor servers is a cornerstone of its enterprise computing strategy, offering robust, scalable, and secure environments for running multiple workloads on a single physical server. At the heart of this capability is PowerVM, IBM's enterprise-grade virtualization technology. PowerVM enables the creation of logical partitions (LPARs), allowing multiple operating systems such as AIX, IBM i, and Linux to run concurrently on the same hardware. It supports advanced features like live partition mobility, dynamic resource allocation, and micro-partitioning, which help maximize hardware utilization and reduce operational costs.

In addition to PowerVM, IBM Power based-processor servers also support KVM (Kernel-based Virtual Machine), an open-source virtualization option. KVM on Power provides a flexible and cost-effective alternative for Linux-based workloads, particularly in cloud-native and containerized environments. It integrates well with modern orchestration tools and supports features like nested virtualization and SR-IOV for high-performance networking. KVM is ideal for organizations looking to leverage open-source technologies while still benefiting from the performance and reliability of IBM Power hardware.

A key component of virtualization efficiency on Power based-processor servers is the use of Shared Processor Pools (SPPs). SPPs allow multiple LPARs to share a pool of physical processors, enabling dynamic allocation of CPU resources based on workload demand. With Power11 PowerVM add support for Resource Groups to further enhance the processor sharing capabilities and add additional efficiencies. Processor Pools add to the capabilities of Shared Processor Pools to improve processor utilization and enhance the isolation and control by capping the maximum CPU resources available to each pool. When combined with PowerVM or KVM, SPPs help optimize performance, reduce licensing costs, and ensure consistent service levels across virtual environments.

This chapter contains the following topics:

- /SM590000 PowerVM
- /SM590000 KVM support

## 9.1  PowerVM

The PowerVM platform is the family of technologies, capabilities, and offerings that delivers industry-leading virtualization for enterprises. It is the umbrella branding term for Power processor-based server virtualization, that is, IBM PowerVM Hypervisor, logical partitioning, IBM Micro-Partitioningfi, Virtual I/O Server (VIOS), Live Partition Mobility (LPM), and more. PowerVM is a combination of hardware enablement and software.

## 9.1.1  IBM PowerVM Hypervisor

Power processor-based servers are combined with PowerVM technology and offer the following key capabilities that can help to consolidate and simplify IT environments:

- /SM590000 Improve server usage and share I/O resources to reduce the total cost of ownership (TCO) and better use IT assets.
- /SM590000 Improve business responsiveness and operational speed by dynamically reallocating resources to applications as needed to better match changing business needs or handle unexpected changes in demand.
- /SM590000 Simplify IT infrastructure management by making workloads independent of hardware resources so that business-driven policies can be used to deliver resources that are based on time, cost, and service-level requirements.

Combined with features in the Power11 scale-out servers, the IBM PowerVM Hypervisor delivers functions that enable other system technologies, including logical partition (LPAR) technology, virtualized processors, IEEE virtual local area network (VLAN)-compatible virtual switch, virtual SCSI adapters, virtual Fibre Channel adapters, and virtual consoles.

The PowerVM Hypervisor is a basic component of the system's firmware and offers the following functions:

- /SM590000 Provides an abstraction between the physical hardware resources and the LPARs that use them.
- /SM590000 Enforces partition integrity by providing a security layer between LPARs.
- /SM590000 Controls the dispatch of virtual processors to physical processors.
- /SM590000 Saves and restores all processor state information during a logical processor context switch.
- /SM590000 Controls hardware I/O interrupt management facilities for LPARs.
- /SM590000 Provides VLAN channels between LPARs that help reduce the need for physical Ethernet adapters for inter-partition communication.
- /SM590000 Monitors the Flexible Service Processor (FSP) and performs a reset or reload if it detects the loss of one of the FSP, notifying the operating system if the problem is not corrected.

The PowerVM Hypervisor is always active, regardless of the system configuration or whether it is connected to the managed console. It requires memory to support the resource assignment of the LPARs on the server. The amount of memory that is required by the PowerVM Hypervisor firmware varies according to several factors:

- /SM590000 Memory usage for hardware page tables (HPTs)
- /SM590000 Memory usage to support I/O devices
- /SM590000 Memory usage for virtualization

## Memory usage for hardware page tables

Each partition on the system includes its own HPT that contributes to hypervisor memory usage. The HPT is used by the operating system to translate from effective addresses (EAs) to physical real addresses in the hardware. This translation from effective to real addresses allows multiple operating systems to run simultaneously in their own logical address space. Whenever a virtual processor for a partition is dispatched on a physical processor, the hypervisor indicates to the hardware the location of the partition HPT that can be used when translating addresses.

The amount of memory for the HPT is based on the maximum memory size of the partition and the HPT ratio. The default HPT ratio is 1/128th (for AIX, VIOS, and Linux partitions) of the maximum memory size of the partition. AIX, VIOS, and Linux use larger page sizes (16 KB and 64 KB) instead of using 4 KB pages. The use of larger page sizes reduces the overall number of pages that must be tracked; therefore, the overall size of the HPT can be reduced. For example, the HPT is 2 GB for an AIX partition with a maximum memory size of 256 GB.

When defining a partition, the maximum memory size that is specified is based on the amount of memory that can be dynamically added to the dynamic logical partition (DLPAR) without changing the configuration and restarting the partition.

In addition to setting the maximum memory size, the HPT ratio can be configured. The hpt\_ratio parameter for the chsyscfg Hardware Management Console (HMC) command can be issued to define the HPT ratio that is used for a partition profile. The valid values are 1:32, 1:64, 1:128, 1:256, or 1:512.

Specifying a smaller absolute ratio (1/512 is the smallest value) decreases the overall memory that is assigned to the HPT. Testing is required when changing the HPT ratio because a smaller HPT might incur more CPU consumption because the operating system might need to reload the entries in the HPT more frequently. Most customers choose to use the IBM provided default values for the HPT ratios.

## Memory usage for I/O devices

In support of I/O operations, the hypervisor maintains structures that are called the translation control entities (TCEs), which provide an information path between I/O devices and partitions. The TCEs provide the address of the I/O buffer, indications of read versus write requests, and other I/O-related attributes. Many TCEs are used per I/O device, so multiple requests can be active simultaneously to the same physical device. To provide better affinity, the TCEs are spread across multiple processor chips or drawers to improve performance while accessing the TCEs.

For physical I/O devices, the base amount of space for the TCEs is defined by the hypervisor that is based on the number of I/O devices that are supported. A system that supports high-speed adapters can also be configured to allocate more memory to improve I/O performance. Linux is the only operating system that uses these extra TCEs so that the memory can be freed for use by partitions if the system uses only AIX.

## Memory usage for virtualization features

Virtualization requires more memory to be allocated by the PowerVM Hypervisor for hardware statesave areas and various virtualization technologies. For example, on Power11 processor-based systems, each processor core supports up to eight simultaneous multithreading (SMT) threads of execution, and each thread contains over 80 different registers.

The PowerVM Hypervisor must set aside save areas for the register contents for the maximum number of virtual processors that are configured. The greater the number of

physical hardware devices, the greater the number of virtual devices, the greater the amount of virtualization, and the more hypervisor memory is required. For efficient memory consumption, wanted and maximum values for various attributes (processors, memory, and virtual adapters) must be based on business needs, and not set to values that are higher than actual requirements.

## Predicting memory that is used by the PowerVM Hypervisor

The IBM System Planning Tool (SPT) is a resource that can be used to estimate the amount of hypervisor memory that is required for a specific server configuration. After the SPT executable file is downloaded and installed, you can define a configuration by selecting the correct hardware platform and the installed processors and memory, and defining partitions and partition attributes. SPT can estimate the amount of memory that is assigned to the hypervisor, which assists you when you change a configuration or deploy new servers.

The PowerVM Hypervisor provides the following types of virtual I/O adapters:

- /SM590000 Virtual SCSI

The PowerVM Hypervisor provides a virtual SCSI mechanism for the virtualization of storage devices. The storage virtualization is accomplished by using two paired adapters: a virtual SCSI server adapter and a virtual SCSI customer adapter.

- /SM590000 Virtual Ethernet

The PowerVM Hypervisor provides a virtual Ethernet switch function that allows partitions fast and secure communication on the same server without any need for physical interconnection or connectivity outside of the server if a Layer 2 bridge to a physical Ethernet adapter is set in one VIOS partition, also known as Shared Ethernet Adapter (SEA).

- /SM590000 Virtual Fibre Channel

A virtual Fibre Channel adapter is a virtual adapter that provides customer LPARs with a Fibre Channel connection to a storage area network through the VIOS partition. The VIOS partition provides the connection between the virtual Fibre Channel adapters on the VIOS partition and the physical Fibre Channel adapters on the managed system.

- /SM590000 Virtual (TTY) console

Each partition must have access to a system console. Tasks, such as operating system installation, network setup, and various problem analysis activities, require a dedicated system console. The PowerVM Hypervisor provides the virtual console by using a virtual TTY or serial adapter and a set of hypervisor calls to operate on them. Virtual TTY does not require the purchase of any other features or software, such as the PowerVM Edition features.

## Logical partitions

LPARs and virtualization increase the usage of system resources and add a level of configuration possibilities.

Logical partitioning is the ability to make a server run as though it were two or more independent servers. When you logically partition a server, you divide the resources on the server into subsets, called LPARs . You can install software on an LPAR, and the LPAR runs as an independent logical server with the resources that you allocated to the LPAR.

LPAR is also referred to in some documentation as a virtual machine (VM), which makes it look similar to what other hypervisors offer. However, LPARs provide a higher level of security and isolation and other features that are described in this chapter.

Processors, memory, and I/O devices can be assigned to LPARs. AIX, IBM i, Linux, and VIOS can run on LPARs. VIOS provides virtual I/O resources to other LPARs with general-purpose operating systems.

LPARs share a few system attributes, such as the system serial number, system model, and processor Feature Codes. All other system attributes can vary from one LPAR to another.

## Micro-Partitioning

When you use the Micro-Partitioning technology, you can allocate fractions of processors to an LPAR. An LPAR that uses fractions of processors is also known as a shared processor partition or micropartition . Micropartitions run over a set of processors that is called a shared processor pool (SPP), and virtual processors are used to enable the operating system manage the fractions of processing power that are assigned to the LPAR.

From an operating system perspective, a virtual processor cannot be distinguished from a physical processor, unless the operating system is enhanced to determine the difference. Physical processors are abstracted into virtual processors that are available to partitions.

On the Power11 processor-based server, a partition can be defined with a processor capacity as small as 0.05 processing units. This number represents 0.05 of a physical core. Each physical core can be shared by up to 20 shared processor partitions, and the partition's entitlement can be incremented fractionally by as little as 0.05 of the processor. The shared processor partitions are dispatched and time-sliced on the physical processors under the control of the PowerVM Hypervisor. The shared processor partitions are created and managed by the HMC.

## Processing mode

When you create an LPAR, you can assign entire processors for dedicated use, or you can assign partial processing units from an SPP. This setting defines the processing mode of the LPAR.

## Dedicated mode

In dedicated mode, physical processors are assigned as a whole to partitions. The SMT feature in the Power11 processor core allows the core to run instructions from two, four, or eight independent software threads simultaneously.

## Shared dedicated mode

On Power11 processor-based servers, you can configure dedicated partitions to become processor donors for idle processors that they own, which allows for the donation of spare CPU cycles from dedicated processor partitions to an SPP. The dedicated partition maintains absolute priority for dedicated CPU cycles. Enabling this feature can help increase system usage without compromising the computing power for critical workloads in a dedicated processor mode LPAR.

## Shared mode

In shared mode, LPARs use virtual processors to access fractions of physical processors. Shared partitions can define any number of virtual processors (the maximum number is 20 times the number of processing units that are assigned to the partition). The PowerVM Hypervisor dispatches virtual processors to physical processors according to the partition's processing units entitlement. One processing unit represents one physical processor's processing capacity. All partitions receive a total CPU time equal to their processing unit's entitlement. The logical processors are defined on top of virtual processors. Therefore, even with a virtual processor, the concept of a logical processor exists, and the number of logical processors depends on whether SMT is turned on or off.

## 9.1.2  Multiple shared processor pools

MSPPs are supported on Power11 processor-based servers. This capability allows a system administrator to create a set of micropartitions with the purpose of controlling the processor capacity that can be used from the physical SPP.

Micropartitions are created and then identified as members of the default processor pool or a user-defined SPP. The virtual processors that exist within the set of micropartitions are monitored by the PowerVM Hypervisor. Processor capacity is managed according to user-defined attributes.

If the Power server is under heavy load, each micropartition within an SPP is assured of its processor entitlement, plus any capacity that might be allocated from the reserved pool capacity if the micropartition is uncapped.

If specific micropartitions in an SPP do not use their processing capacity entitlement, the unused capacity is ceded and other uncapped micropartitions within the same SPP can use the extra capacity according to their uncapped weighting. In this way, the entitled pool capacity of an SPP is distributed to the set of micropartitions within that SPP.

All Power servers that support the MSPP capability have a minimum of one (the default) SPP and up to a maximum of 64 SPPs.

This capability helps customers reduce TCO significantly when the cost of software or database licenses depends on the number of assigned processor-cores.

Shared Processor Pools: Can be used in conjunction with Resource Groups. Such configuration can improve performance and isolation significantly.

## 9.1.3  Virtual I/O Server

The VIOS is part of PowerVM. It is the specific appliance that allows the sharing of physical resources among LPARs to allow more efficient usage (for example, consolidation). In this case, the VIOS owns the physical I/O resources (SCSI, Fibre Channel, network adapters, or optical devices) and allows customer partitions to share access to them, which minimizes and optimizes the number of physical adapters in the system.

The VIOS eliminates the requirement that every partition owns a dedicated network adapter, disk adapter, and disk drive. The VIOS supports OpenSSH for secure remote logins. It also provides a firewall for limiting access by ports, network services, and IP addresses.

Figure 9-1 shows an overview of a VIOS configuration.

Figure 9-1   Architectural view of the VIOS

<!-- image -->

It is a best practice to run dual VIO servers per physical server.

## Shared Ethernet Adapter

A SEA can be used to connect a physical Ethernet network to a virtual Ethernet network. The SEA provides this access by connecting the PowerVM Hypervisor VLANs to the VLANs on the external switches. Because the SEA processes packets at Layer 2, the original MAC address and VLAN tags of the packet are visible to other systems on the physical network. IEEE 802.1 VLAN tagging is supported.

By using the SEA, several customer partitions can share one physical adapter. You can also connect internal and external VLANs by using a physical adapter. The SEA service can be hosted only in the VIOS (not in a general-purpose AIX or Linux partition) and acts as a Layer 2 network bridge to securely transport network traffic between virtual Ethernet networks (internal) and one or more (Etherchannel) physical network adapters (external). These virtual Ethernet network adapters are defined by the PowerVM Hypervisor on the VIOS.

## Virtual SCSI

Virtual SCSI is used to view a virtualized implementation of the SCSI protocol. Virtual SCSI is based on a customer/server relationship. The VIOS LPAR owns the physical I/O resources and acts as a server or, in SCSI terms, a target device. The client LPARs access the virtual SCSI backing storage devices that are provided by the VIOS as clients.

The virtual I/O adapters (a virtual SCSI server adapter and a virtual SCSI client adapter) are configured by using an HMC. The virtual SCSI server (target) adapter is responsible for running any SCSI commands that it receives, and is owned by the VIOS partition. The virtual SCSI client adapter allows a client partition to access physical SCSI and SAN-attached devices and LUNs that are mapped to be used by the client partitions. The provisioning of virtual disk resources is provided by the VIOS.

## iSCSI

The Internet Small Computer Systems Interface (iSCSI) disk is supported in the Virtual I/O Server (VIOS) 3.1.0, or later

The Internet Small Computer Systems Interface (iSCSI) disk provides block-level access to storage devices by carrying SCSI commands over an Internet Protocol network. The iSCSI disk is used to facilitate data transfers over the internet by using TCP, a reliable transport mechanism that uses either IPV6 or IPV4 protocols. The iSCSI disk is used to manage storage over long distances.

The iSCSI support in VIOS allows iSCSI disks to be exported to client logical partitions as virtual disks (vSCSI disks). This support is available in VIOS version 3.1, and later,

VIOS version 3.1 enables Multipath I/O (MPIO) support for the iSCSI initiator. With MPIO support, you can configure and create multiple paths to an iSCSI disk, similar to other protocols. The client logical partition can run either an AIX or Linux operating system.

VIOS version 3.1.1 enables support for multiple iSCSI initiators on the VIOS. This support also includes performance enhancements for the iSCSI driver. With multiple iSCSI initiator support, you can create multiple iSCSI software initiator devices on a single AIX operating system instance.

## N\_Port ID Virtualization

N\_Port ID Virtualization (NPIV) is a technology that allows multiple LPARs to access one or more external physical storage devices through the same physical Fibre Channel adapter. This adapter is attached to a VIOS partition that acts only as a pass-through that manages the data transfer through the PowerVM Hypervisor.

Each partition features one or more virtual Fibre Channel adapters, each with their own pair of unique worldwide port names. This configuration enables you to connect each partition to independent physical storage on a SAN. Unlike virtual SCSI, only the client partitions see the disk.

For more information and requirements for NPIV, see IBM PowerVM Virtualization Managing and Monitoring, SG24-7590 .

## 9.1.4  Live Partition Mobility

LPM enables you to move a running LPAR from one system to another without disruption. Inactive partition mobility allows you to move a powered-off LPAR from one system to another one.

LPM provides systems management flexibility and improves system availability by avoiding the following situations:

- /SM590000 Planned outages for hardware upgrade or firmware maintenance.
- /SM590000 Unplanned downtime. With preventive failure management, if a server indicates a potential failure, you can move its LPARs to another server before the failure occurs.

For more information and requirements for LPM, see IBM PowerVM Live Partition Mobility&lt;Default ‹' Font&gt;, SG24-7460 .

HMCV10R1 and VIOS 3.1.3 or later provide the following enhancements to the LPM Feature:

- /SM590000 Automatically choose the fastest network for LPM memory transfer.
- /SM590000 Allow LPM when a virtual optical device is assigned to a partition.

## 9.1.5  Active Memory Expansion

Active Memory Expansion (AME) is an optional Feature Code (#&lt;&lt; Add FC once known&gt;&gt;) that belongs to the technologies under the PowerVM umbrella and enables memory expansion on the system.

AME is an innovative technology that supports the AIX operating system. It helps enable the effective maximum memory capacity to be larger than the true physical memory maximum. Compression and decompression of memory content can enable memory expansion up to 100% or more. This expansion can enable a partition to complete more work or support more users with the same physical amount of memory. Similarly, it can enable a server to run more partitions and do more work for the same physical amount of memory.

AME uses CPU resources to compress and decompress the memory contents. The trade off of memory capacity for processor cycles can be an excellent choice, but the degree of expansion varies about how compressible the memory content is. It also depends on having adequate spare CPU capacity available for this compression and decompression.

The Power E1080 includes a hardware accelerator that is designed to boost AME efficiency and uses less processor core resources. Each AIX partition can turn on or turn off AME. Control parameters set the amount of expansion that is wanted in each partition to help control the amount of CPU used by the AME function.

An IPL is required for the specific partition that is turning memory expansion. When enabled, monitoring capabilities are available in standard AIX performance tools, such as lparstat , vmstat , topas , and svmon .

A planning tool is included with AIX, which enables you to sample workloads and estimate how expandable the partition's memory is and much CPU resource is needed. The feature can be ordered with the initial order of the Power E1080 or as a Miscellaneous Equipment Specification (MES) order. A software key is provided when the enablement feature is ordered, which is applied to the system node. An IPL is not required to enable the system node. The key is specific to an individual system and is permanent. It cannot be moved to a different server.

IBM i does not support AME.

## 9.1.6  Remote Restart

Remote Restart is a high availability option for partitions. If an error occurs that causes a server outage, a partition that is configured for Remote Restart can be restarted on a different physical server. At times, it might take longer to start the server, in which case the Remote Restart function can be used for faster reprovisioning of the partition. Typically, Remote Restart can be done faster than restarting the server that stopped and then restarting the partitions. The Remote Restart function relies on technology that is similar to LPM where a partition is configured with storage on a SAN that is shared (accessible) by the server that hosts the partition.

HMC V10R1 provides an enhancement to the Remote Restart Feature that enables remote restart when a virtual optical device is assigned to a partition.

## 9.1.7  POWER processor modes

Although they are not virtualization features, the POWER processor modes are described here because they affect various virtualization features.

On Power servers, partitions can be configured to run in several modes, including the following modes:

- /SM590000 Power9

This native mode for Power9 processors implements Version 3.0 of the IBM Power ISA. For more information, see IBM Documentation.

- /SM590000 Power10

This native mode for Power10 processors implements Version 3.1 of the IBM Power ISA. For more information, see IBM Documentation.

- /SM590000 Power11

This native mode for Power11 processors implements Version 3.X of the IBM Power ISA. For more information, see I&lt;&lt; Add URL once known&gt;&gt;.

Figure 9-2 shows the available processor modes on a Power11 based server.

Figure 9-2   Processor modes

<!-- image -->

Processor compatibility mode is important when LPM migration is planned between different generations of servers. An LPAR that might be migrated to a machine that is managed by a processor from another generation must be activated in a specific compatibility mode.

Note: Migrating an LPAR from a POWER9 processor-based server to Power11 based server by using LPM is not supported; however, the following steps can be completed to accomplish this task:

1. Migrate LPAR from POWER9 processor-based server to Power10 processor-based server by using LPM.
2. Migrate then the LPAR from Power10 processor-based server to Power11.

## 9.1.8  Single Root I/O Virtualization

Single Root I/O Virtualization (SR-IOV) is an extension to the Peripheral Component Interconnect Express (PCIe) specification that allows multiple operating systems to

simultaneously share a PCIe adapter with little or no runtime involvement from a hypervisor or other virtualization intermediary.

SR-IOV is a PCI standard architecture that enables PCIe adapters to become self-virtualizing. It enables adapter consolidation through sharing much like logical partitioning enables server consolidation. With an adapter capable of SR-IOV, you can assign virtual slices of a single physical adapter to multiple partitions through logical ports without using a VIOS.

## 9.1.9  More information about virtualization features

The following IBM Redbooks publications provide more information about the virtualization features:

- /SM590000 IBM PowerVM Best Practices, SG24-8062
- /SM590000 IBM PowerVM Virtualization Introduction and Configuration, SG24-7940
- /SM590000 IBM PowerVM Virtualization Managing and Monitoring, SG24-7590
- /SM590000 IBM Power Systems SR-IOV: Technical Overview and Introduction, REDP-5065

## 9.1.10  Resource groups

Resource Groups are a new feature introduced with IBM Power11, designed to enhance system performance by up to 25% through improved workload optimization and resource affinity. While Shared Processor Pools (SPPs) already provide compute capacity isolation by capping the maximum resources available to each pool, Resource Groups take this further by introducing advanced affinity-based optimizations for more efficient workload dispatching.

Early performance evaluations indicate that, when configured effectively, Resource Groups can deliver shared processor performance that closely matches that of dedicated processors - particularly in large, partitioned environments.

## Resource Groups Properties

With the introduction of Resource Groups in IBM Power11, system administrators gain a powerful new tool for organizing and optimizing compute resources. Designed for flexibility and performance, Resource Groups allow for the grouping of both dedicated and shared processor partitions, enabling more granular control over resource allocation and workload management. This feature enhances system efficiency, supports dynamic reconfiguration, and integrates seamlessly with existing technologies like Shared Processor Pools, Live Partition Mobility, and PEP 2.0.

The core features of resource groups are:

- /SM590000 Performance Optimization:
- -Resource Groups improve workload affinity, enabling shared processor performance nearly equivalent to dedicated processors.
- /SM590000 Flexible Configuration:
- -Can include both dedicated processor partitions and shared processor partitions.
- -Resource group configuration will specify the number of general purpose cores (AIX/IBM i/Linux/VIOS) and IFL cores (Linux/VIOS).
- -Powered-off partitions can be reassigned between groups.
- -Resources not assigned to a user defined group are placed in the default resource group.
- -Cores can be dynamically reallocated among groups.

- /SM590000 Affinity and Isolation:
- -Each resource group has its own set of shared processor pools.
- -Enhances compute capacity isolation and affinity-based dispatching.
- /SM590000 Monitoring Management:
- -Utilization metrics available for Resource Groups, SPPs, and the overall system.
- -Dynamic Platform Optimizer (DPO) can run at system or group level.
- /SM590000 Mobility Compatibility:
- -When using Live Partition Mobility the resource group on the target system can be selected.
- -Fully compatible with PEP 2.0.

## Resource Groups use cases

There are multiple scenarios in which Resource Groups can deliver significant benefits to customers. In this section, we provide several example use cases, but beyond the examples provided, use cases can also be combined to maximize functionality and tailor performance to specific business needs.

## Consolidation across multiple lines of business

Figure 9-3 illustrates how resources are allocated and shared across multiple lines of business on Power11 systems. With the introduction of Resource Groups in Power11, resource allocation becomes significantly more efficient, enabling better workload isolation and improved performance across the system.

Figure 9-3   Example where Resource Groups consolidate multiple lines of business

<!-- image -->

## Isolation of production workloads from test/dev workloads

In this example, the development and test LPARs are restricted to using resources only from the default Resource Group, limiting their access to shared system resources and isolating them from production workloads.

Figure 9-4 shows how resource groups are used to provide this isolation of development and test workloads.

Figure 9-4   Example where Resource Groups isolate workloads

<!-- image -->

## Improve application performance by grouping workload tiers into resource groups

In this example, performance is enhanced through improved affinity between the database and application server, allowing for more efficient resource utilization and faster communication within the same Resource Group.

Figure 9-5 shows how grouping workloads into different resource groups can improve application affinity and improve performance.

Figure 9-5   Example where Resource Groups improve performance by grouping workload tiers

<!-- image -->

## System-level isolation in multi-server consolidation scenarios

Resource Groups enable effective workload isolation on IBM Power11 systems. This allows organizations to consolidate multiple smaller servers into a single, more powerful Power11 system while logically separating workloads into distinct groups. Each group can be managed independently, ensuring performance, security, and resource control across different business functions or environments. Figure 9-6 shows how using resource groups can help maintain system level isolation while doing server consolidation.

Figure 9-6   Example where Resource Groups provides additional layer of workload isolation

<!-- image -->

## Improved performance by mapping Shared Processor Pools into Resource Groups

Shared Processor Pools (SPPs) and Resource Groups can be used together on IBM Power11 systems to simultaneously optimize application performance and reduce total cost of ownership (TCO). This combination allows for precise control over resource allocation and workload isolation, ensuring efficient utilization of compute capacity while maintaining performance consistency across diverse workloads. Figure 9-7 on page 207 shows how SPPs and Resource Groups enhance your performance and reduces your TCO.

Figure 9-7   Example where Resource Groups improve performance by mapping Shared Processor Pools into Resource Groups.

<!-- image -->

## Resource Groups Advisor

Resource Groups Advisor (RGA) is a web-based tool designed to assist with the configuration of resource groups on IBM Power based-processor servers. Offered as a free service, RGA analyzes a customer's server setup and provides tailored recommendations for optimal resource group configurations. It helps model and validate configurations to ensure efficient resource allocation and system performance.

## RGA is available at:

https://www.ibm.com/it-infrastructure/resources/resource-groups-advisor . The welcome screen for RGA is shown in Figure 9-8.

Figure 9-8   Welcome screen

<!-- image -->

After selecting Getting Started, you see a screen where you can choose to create a new configuration or upload a previously saved version. Selecting New Configuration brings up the screen shown in Figure 9-9.

Figure 9-9   New configuration screen

<!-- image -->

After providing the system configuration parameters, press Next to be presented with the resource group configuration planned for your system. This is shown in Figure 9-10. The default resource group is always configured, but you can choose to add additional resource groups to your configuration.

Figure 9-10   Resource group definitions

<!-- image -->

After defining your resource groups, you will be given the opportunity to define the LPAR details. Selecting Add LPAR allows you to enter the details about each LPAR such as whether it is running in Shared or Dedicated mode, the processor and memory allocations, and which resource group the LPAR is assigned to. LPARs can also be added from the IBM System Planning Tool.

When all of your LPARs are defined, you will see an LPAR summary screen similar to Figure 9-11.

Figure 9-11   LPAR configuration

<!-- image -->

After entering all of the LPAR information, press Submit to get the model's output similar to what is shown in Figure 9-12.

Figure 9-12   Output from the tool

<!-- image -->

You can save the configuration at this point, or start a new model.

Note: RGA simulates how PowerVM would create resource groups and allocate resources to LPARs on a system, all based on the provided input configurations. No 'customer data' is being pulled off actual servers and assessed.

## 9.2  KVM support

IBM Power11 processor based servers can utilize Kernel-based Virtual Machine (KVM) within a PowerVM logical partition (LPAR). This allows for the creation and management of lightweight Linux virtual machines (VMs) using standard KVM tools, while still leveraging the existing resources of the PowerVM LPAR. Essentially, KVM becomes an additional virtualization option alongside PowerVM on IBM Power.

KVM on IBM Power11 processor based servers is not a replacement for PowerVM, but rather an additional capability that brings the power, speed, and flexibility of the KVM virtualization technology to a PowerVM logical partition (LPAR).

KVM-enabled LPARs can host PPC64-LE KVM guests, which are essentially Linux VMs. The KVM guests within the LPAR utilize resources (CPU, memory, I/O) that have been allocated to the LPAR by the PowerVM hypervisor. This approach offers flexibility in deploying Linux workloads and can be more cost-effective than other virtualization solutions, especially for organizations already invested in the Linux ecosystem. KVM's integration with the Linux kernel can lead to high performance, especially when running Linux-based workloads. This setup enables use cases such as running standard Linux distributions, containers, and other workloads that benefit from the KVM virtualization stack and the benefit to consolidate in one or more IBM Power11 processor based servers different kind of workloads (see Figure 9-13 for an example). In essence, KVM on Power11 provides a way to leverage the strengths of both PowerVM and KVM, offering a powerful and flexible virtualization environment for Linux workloads.

Figure 9-13   IBM Power stack for KVM

<!-- image -->

About capabilities, KVM in a PowerVM LPAR utilizes the industry standard Linux KVM virtualization stack and can easily integrate within an existing Linux virtualization ecosystem. KVM in an LPAR is enabled by:

- /SM590000 IBM Power architecture and Power11 implementation has advanced virtualization capabilities to run multiple operating system (OS) instances that share the same hardware resources while providing isolation. The Radix MMU architecture provides the capability to independently manage page tables for the LPAR and the KVM guest instances on the LPAR.
- /SM590000 PowerVM industry-leading virtualization stack provides new functions to create and manage KVM guests. These changes extend the Power platform architecture to include new hypervisor interfaces.
- /SM590000 Linux kernel that includes the KVM kernel module (KVM) provides core virtualization infrastructure to run multiple virtual machines in a Linux host LPAR. Upstream kernels and enabled downstream distributions such as Fedora and Ubuntu use the newly introduced Power architecture extensions to create and manage KVM guests in the PowerLinux LPAR.
- /SM590000 QEMU: user space component that implements virtual machines on the host that use KVM functions.
- /SM590000 LibVirt provides a toolkit for virtual machine management.

Figure 9-14   Industry Standard Linux Virtualization Stack

<!-- image -->

KVM support on IBM Power11 processor based server requires:

- /SM590000 Partition must be a Linux partition that runs in Power10 processor compatibility mode;
- /SM590000 Partition must be enabled for KVM:
- -For HMC-managed systems, you must set the partition to KVM Capable;
- -For unmanaged systems, you must set the default partition environment to Linux KVM on the BMC;

- /SM590000 Partition must be running in Radix mode (default MMU mode for Linux LPARs);
- /SM590000 partition must be assigned with dedicated CPUs with processor sharing set to Never Allow;

The following features are not supported on KVM logical partitions:

- /SM590000 Shared processors
- /SM590000 vPMEM LUNs
- /SM590000 Platform keystore
- /SM590000 Live partition migration (LPM)
- /SM590000 Dynamic platform optimization
- /SM590000 Add or Remove memory, processor, and I/O DLPAR

The following KVM features for guests are not supported:

- /SM590000 PCI pass-through of LPAR-attached PCI devices to KVM guests. This feature will be supported in future releases.

## See also

https://www.ibm.com/docs/en/linux-on-systems?topic=servers-kvm-in-powervm-lpar for additional references.

<!-- image -->

Chapter 10.

10

## Hybrid Cloud Solutions

This chapter explores IBM Power servers as a foundational platform for hybrid cloud environments, emphasizing their ability to support mission-critical workloads with exceptional performance, security, and flexibility. Built on the advanced Power11 architecture, IBM Power based-processor servers deliver significant improvements in compute efficiency and operational cost savings. These systems are engineered to integrate seamlessly across on-premises, private, and public cloud infrastructures, supporting a wide range of enterprise operating systems including AIX, IBM i, and Linux.

The chapter also highlights IBM's strategic approach to hybrid cloud, showcasing how Power servers enable scalable, cloud-native application development using Kubernetes and Red Hat OpenShift. Key management tools such as IBM PowerVC, IBM Cloud Management Console, and Power Enterprise Pools 2.0 are discussed for their roles in simplifying virtualization, optimizing resource allocation, and enhancing operational agility. Additionally, the chapter introduces IBM Power Virtual Server (PowerVS), a cloud-based extension of Power based-processor servers that allows organizations to modernize at their own pace. PowerVS offers flexible, pay-as-you-go access to virtualized Power infrastructure, enabling seamless workload migration, rapid provisioning, and robust business continuity capabilities.

This chapter contains the following topics:

- /SM590000 IBM Power Private Cloud with Shared Utility Capacity
- /SM590000 Red Hat OpenShift
- /SM590000 Power Virtual Server

## 10.1  IBM Power Private Cloud with Shared Utility Capacity

IBM Power Private Cloud with Shared Utility Capacity introduces a flexible and efficient approach to resource management through Power Enterprise Pools (PEP) 2.0. This innovation allows multiple IBM Power based-processor servers to operate as a unified resource pool, enabling shared compute capacity across systems. Designed for clients deploying private cloud infrastructure, PEP 2.0 enhances operational agility by supporting dynamic, minute-by-minute consumption of compute resources.

In this model, each system within the pool is provisioned with a set number of base processor and memory activations. When configured as a Power Enterprise Pool, these base activations and their associated operating system entitlements are aggregated to define the pool's baseline capacity. Simultaneously, all hardware resources across the pool are fully activated and made available for workload deployment - allowing usage to exceed the base capacity when needed. IBM Cloud Management Console continuously monitors average resource usage across the pool and compares it to the base entitlement. Any usage beyond the base is billed as metered capacity, either through Prepaid Capacity Credits or monthly billing. PEP 2.0 eliminates the need for manual reallocation of activations between systems, offering granular resource sharing, improved cost efficiency, and simplified management for enterprise IT environments.

Power Enterprise Pools with Shared Utility Capacity on Power S1122 and S1124 systems provides enhanced multi-system resource sharing and by-the-minute tracking and consumption of compute resources across a collection of Power S1122 and S1124 and S1022 and S1024 systems within a single Power Enterprise Pools (2.0). Shared Utility Capacity provides a complete range of flexibility to tailor initial system configurations with the right mix of purchased and pay-for-use consumption of processor, memory, and software. Clients with existing Power Enterprise Pools 2.0 of Power S1022 and S1024 systems can simply add one or more S1122 and S1124 systems into their pool and migrate to them at the rate and pace of their choosing, as any Power S1122 and S1124 and Power S1022 and S1024 systems may seamlessly inter-operate and share compute resources within the same pool. Clients with Mobile Capacity on a Power S1122 and S1124 may easily upgrade their system to support Power Enterprise Pools 2.0 to leverage Shared Utility Capacity resources.

With Cloud Management Console V1.20, IBM i license entitlement are monitored and metered by each software tier based upon the processor usage and tier of systems within a pool. Clients can deploy a mix of 2-socket scale-out Power based-processor servers with processors requiring P10, P20 and/or P30 tiers of IBM i license entitlement within the same pool without having to acquire all Base Capacity IBM i license entitlements at the highest tier required for processors within the pool. Idle Base IBM i Capacity of one software tier may offset minutes of IBM i consumption exceeding Base IBM i entitlement of an equal or smaller software tier (e.g. idle P20 Base IBM i may offset usage exceeding P20 or P10 Base IBM i).

A Power infrastructure consolidated onto Power S1122 and S1124 systems has the potential to greatly simplify system management so IT teams can focus on optimizing their business results instead of moving resources around within their data center. Shared Utility Capacity resources are easily tracked by virtual machine (VM) and monitored by a CMC, which integrates with local HMCs to manage the pool and track resource use by system and VM, by the minute, across a pool.

Clients need not over-provision capacity on each individual system to support growth, as all available processor and memory on all systems in a pool are activated and available for use. On Power S1122 and S1124 systems, Mobile and Shared Utility Capacity capabilities are now offered through the purchase of a Power Enterprise Pools Subscription (5765-P2E) for each Power S1122 or S1124 system being configured for use in a Power Enterprise Pool.

When a Power Enterprise Pool 2.0 pool is started, each eligible Power S1122 and S1124 system's purchased processor activations, memory activations, and supported operating system entitlement resources become Base Capacity resources as part of the Power Enterprise Pool and are aggregated across a defined pool of systems for consumption monitoring. Metered Capacity is the additional installed processor and memory resource above each system's Base Capacity. It is activated and made available for immediate use when a pool is started, then monitored by the minute by a CMC.

Metered resource usage is charged only for minutes exceeding the pool's aggregate Base resources, and usage charges are debited in real-time against a client's Capacity Credits (5819-CRD) on account or may be billed monthly, in arrears, where available.

Important: Note: Only two consecutive generations of Power servers are supported in the same Power Enterprise Pool. Customers who want to add Power11 to their existing pool with Power9 and Power10 processor-based systems, are recommended to reach out to their IBM representatives or IBM Expert Labs to discuss transition planning and best practices.

## 10.1.1  IBM Cloud Management Console

As private and hybrid cloud deployments continue to expand, enterprises require deeper management insights into these increasingly complex environments. Tools that deliver unified analytics and consolidated information are essential for ensuring smooth and efficient infrastructure operations.

The IBM Cloud Management Console offers a comprehensive view of your Power cloud environment - regardless of the number of systems or data centers involved. It provides:

- /SM590000 Centralized inventory management of systems and virtual components
- /SM590000 Consolidated performance metrics to help optimize resource utilization and system performance across all data centers
- /SM590000 Aggregated logging and analytics for enhanced operational insights

This unified approach empowers IT teams to manage their infrastructure more effectively and make informed decisions with confidence. The IBM Cloud Management Console (CMC) now offers full support for IBM Power11 systems, ensuring compatibility with the latest advancements in Power architecture.

The IBM Cloud Management Console (CMC) is also used to monitor and manage Power Enterprise Pool 2.0 pools in your enterprise. The CMC Enterprise Pools 2.0 application helps you to monitor base and metered capacity across a Power Enterprise Pool 2.0, with summary and sophisticated drill-down views of real-time and historical resource consumption by the logical partition.

CMC provides a cloud-based interface to monitor, manage, and optimize IBM Power infrastructure. It supports AIX, IBM i, and Linux VM workloads, and is accessible through a secure, web-based dashboard.   The IBM Cloud Management Console is a cloud-based portal that allows clients to:

- /SM590000 View health and performance of IBM Power servers.
- /SM590000 Monitor capacity and performance metrics.
- /SM590000 Get insights into firmware levels and configurations.
- /SM590000 Receive proactive support and alerts.

For organizations with limited IT staff or those looking to streamline infrastructure oversight, CMC offers a way to perform essential monitoring and management tasks without requiring complex, locally hosted solutions.

CMC integrates with the Hardware Management Console (HMC) and provides advanced insights into performance, capacity, firmware compliance, patch planning, and system health. With Power11's scalability and built-in virtualization, CMC helps administrators maintain control over increasingly complex hybrid IT environments, whether on-premises or connected to IBM Cloud or other supported clouds.

CMC is offered through a software-as-a-service (SaaS) model and is licensed on a per-server subscription basis. Power11 systems are registered to IBM CMC through their HMCs, which securely transmit telemetry and configuration data to the cloud portal. IBM provides both a no-cost base offering and optional chargeable add-ons that include more advanced features, such as predictive analytics, patch automation, and longer data retention for historical performance views. Customers can choose monthly or annual billing, and entitlement can be managed through IBM Passport Advantagefi or directly through the IBM Cloud portal.

## 10.2  Red Hat OpenShift

With the growing demand for digital services and the continuous release of new offerings, organizations face the challenge of delivering exceptional customer experiences while maintaining resilient and highly available services. To meet these demands, they must innovate - by developing new applications, modernizing existing ones, and ensuring seamless scalability.

So how can organizations achieve this? By embracing cloud technologies - whether through full cloud migration, developing cloud-native applications, or adopting a hybrid cloud approach.

Red Hat OpenShift on IBM Power empowers both developers and IT operations teams with the flexibility and speed needed to build, deploy, and manage applications across diverse environments - on-premises, in the cloud, or across multiple infrastructures. This platform accelerates digital transformation by simplifying scalability and enhancing security.

## 10.2.1  Red Hat OpenShift on Power

Red Hat OpenShift Container Platform is fully supported on IBM Power Servers, offering a robust and scalable environment for running cloud-native applications and modernizing traditional workloads on the IBM Power architecture (ppc64le). This integration enhances the IBM Power software ecosystem by enabling enterprise-grade container orchestration for building, deploying, and managing containerized applications with OpenShift.

OpenShift on IBM Power provides a flexible and efficient platform for hybrid IT environments, enabling the seamless coexistence of cloud-native applications with traditional VM-based workloads. By leveraging the same infrastructure, it allows collocation of containerized workloads alongside existing applications running on AIX, IBM i, or Linux, ensuring low-latency communication between applications and data IBM Power servers provide an extremely resilient and secure platform and how they can be an excellent platform for your cloud implementation using OpenShift. We then describe the benefits of using a multi-architecture cluster and provide implementation guidelines and advice to assist the reader in implementing a multi-architecture cluster using IBM Power control plane nodes and x86 or AMD-based worker nodes.

Red Hat OpenShift is a leading enterprise Kubernetes platform that provides a robust foundation for developing, deploying, and scaling cloud-native applications. It extends Kubernetes with additional features and tools to enhance productivity and security, making it an ideal choice for businesses looking to leverage container technology at scale.

Red Hat OpenShift is a unified platform to build, modernize, and deploy applications at scale. Work smarter and faster with a complete set of services for bringing apps to market on your choice of infrastructure. Red Hat OpenShift delivers a consistent experience across public cloud, on-premise, hybrid cloud, or edge architecture.

Red Hat OpenShift offers you a unified, flexible platform to address a variety of business needs spanning from an enterprise-ready Kubernetes orchestrator to a comprehensive cloud-native application development platform that can be self-managed or used as a fully managed cloud service

## Red Hat OpenShift clusters

A Red Hat OpenShift Container Platform cluster consists of multiple nodes, which can run on either physical or virtual machines. At a minimum, the following node requirements apply:

- /SM590000 Three control plane nodes to manage and maintain the cluster
- /SM590000 Two worker nodes to run containerized workloads
- /SM590000 A temporary bootstrap node used during installation to host configuration and installation files

In OpenShift Container Platform 4.18, the bootstrap and control plane nodes must run Red Hat Enterprise Linux CoreOS (RHCOS), a minimal, immutable container host OS derived from Red Hat Enterprise Linux (RHEL). Compute nodes can run either RHCOS or standard RHEL, depending on the deployment architecture. RHEL machines are deprecated in OpenShift Container Platform 4.16 and will be removed in a future release.

## Multiple Architecture Compute clusters

Enterprises expanding their operations often deploy applications in heterogeneous environments utilizing different types of hardware. A prime example includes data centers using x86\_64 servers and Power servers, while edge locations might feature ARM-based devices due to their power efficiency. We discussed why IBM Power is an ideal choice for running Red Hat OpenShift clusters. However, it is possible that some applications within the environment aren't compatible with IBM Power architecture nodes. You can retain the benefits of IBM Power while retaining simpler cluster management and efficient resource utilization by incorporating both IBM Power and x86\_64 architecture nodes in the same cluster.

The release of Red Hat OpenShift 4.14 brought the OpenShift Container Platform Multiple-Architecture Compute feature to IBM Power. Multi-Arch Compute provides a single heterogeneous cluster, enabling fit-for-purpose computing so clients can align tasks and applications to CPU strengths and software availability rather than one architecture. This support was expanded in Red Hat OpenShift 4.15 which enabled a Red Hat OpenShift cluster to support an IBM Power control plane and add x86 architecture worker nodes.

Multi-Arch Compute for OpenShift Container Platform lets you use a pair of compute architectures, such as ppc64le and amd64, within a single cluster. This exciting feature opens new possibilities for versatility and optimization for composite solutions that span multiple architectures.

Multi-architecture capability offers several benefits:

- /SM590000 Platform independence
- Multi-Arch Compute enables applications to function flawlessly across various hardware platforms, including Intel servers in data centers, ARM-based Raspberry Pis in remote locations, and IBM Power based-processor servers in corporate settings.
- /SM590000 Reduced complexity through standardizing application deployment across architectures
- Streamlines operations and eliminates the need to maintain separate stacks for different hardware. Cost efficiency: Differing hardware architectures provide varying cost-to-performance ratios, which can be exploited to minimize overall infrastructure expenses.
- /SM590000 Multi-architecture support facilitates optimal resource usage

Organizations can select the most cost-effective architecture for each specific workload. For instance, ARM servers could be more affordable for lightweight services, whereas x86\_64 or IBM Power servers might excel at handling heavy computational tasks.

- /SM590000 Energy efficiency
- Specific architectures, like ARM, are renowned for their low power consumption, which can substantially decrease energy costs, notably in scale-out scenarios like IoT and mobile services.
- /SM590000 Scalability and flexibility

Implementing applications on multiple architectures enhances scalability and operational agility, which is vital for businesses experiencing fluctuating loads.

Multi-architecture support allows companies to:

- /SM590000 Scale elastically across platforms: Multi-Arch Compute enables businesses to dynamically allocate resources among different types of hardware to handle surges in demand without being restricted to a single architecture.
- /SM590000 Escape vendor lock-in: With Multi-Arch Compute, corporations are unshackled from a single supplier or type of hardware, thus avoiding vendor lock-in and empowering more bargaining power during procurement decisions.
- /SM590000 Optimize performance: Each architecture boasts unique strengths and weaknesses contingent upon the application or workload. Multi-Arch Compute maximizes performance by aligning application requirements with the architectural advantages.
- /SM590000 Create tailored solutions: Select applications might gain from the high I/O throughput of IBM Power based-processor servers, while others could perform optimally on the high-throughput, multi-core processors of x86\_64 architectures.

Meet specialized computing needs: Certain tasks may necessitate specialized hardware, such as GPUs for machine learning work flows, which might be more accessible or better supported on particular architecture.

## Single Node clusters

For a simpler and more accessible deployment experience, OpenShift now supports a Single Node cluster where all of the management and worker functions are installed on a single node. This approach is especially suitable for development, testing, or edge computing environments.

However, it's important to recognize the inherent limitations of a single-node configuration most notably, the absence of built-in high availability. If the node fails, the entire cluster becomes unavailable, potentially resulting in downtime and data loss. That said, the robust

high availability features of IBM Power infrastructure, when properly architected with redundant power, networking, and storage, can significantly mitigate these risks.

## 10.2.2  Red Hat OpenShift AI on IBM Power Servers

OpenShift AI brings enterprise-grade capabilities for artificial intelligence and machine learning directly into the Red Hat OpenShift platform, enabling organizations to build, train, deploy, and monitor AI models within a unified, containerized environment. Red Hat OpenShift AI is built on Red Hat OpenShift, an enterprise-grade Kubernetes platform designed to support AI/ML workloads across hybrid and multi-cloud infrastructures. By integrating AI workflows into the same infrastructure used for traditional applications, OpenShift AI simplifies operations, accelerates development cycles, and ensures consistent governance and security across the entire AI lifecycle. Red Hat OpenShift AI (RHOAI) enables organizations to build, deploy, and manage AI-enabled applications at scale across hybrid cloud environments.

OpenShift AI (RHOAI) Self-Managed is available by installing the Red Hat OpenShift AI Operator and configuring it to manage the standalone components of the platform. RHOAI Self-Managed is supported on Red Hat OpenShift Container Platform across multiple architectures, including ppc64le (IBM Power), s390x (IBM Z) and x86\_64. This includes support for the following infrastructure providers:

- /SM590000 IBM Power (Technology Preview)
- /SM590000 IBM Z (Technology Preview)
- /SM590000 IBM Cloud
- /SM590000 Red Hat OpenStack
- /SM590000 Bare Metal
- /SM590000 Hosted control planes on Bare Metal
- /SM590000 Amazon Web Services
- /SM590000 Google Cloud Platform
- /SM590000 Microsoft Azure
- /SM590000 VMware vSphere
- /SM590000 Oracle Cloud

IBM Power Servers, renowned for their high performance, scalability, and reliability, are particularly well-suited for compute-intensive AI workloads. The integration of RHOAI with IBM Power Servers enables enterprises to take advantage of both platforms' capabilities for robust, production-grade AI deployments.

As of RHOAI version 2.20 (Self-Managed), the IBM Power architecture (ppc64le) is available as a Technology Preview. Currently, model deployments on IBM Power are supported only in standard mode. RHOAI provides an integrated platform for developing, training, serving, and monitoring AI/ML models. I Support for vLLM is also available on the IBM Power architecture as a Technology Preview, with vLLM runtime templates accessible for experimentation and development.

When deployed on IBM Power based-processor servers, OpenShift AI benefits from the platform's high-performance architecture, which is optimized for data-intensive and compute-heavy workloads. The latest IBM Power processors feature built-in AI inferencing capabilities, delivering faster insights and reduced latency for real-time applications. This will further be enhanced with the planned availability and support of the IBM Spyre Accelerator in IBM Power servers. The Spyre adapter is a PCIe-attached AI card engineered for low-precision AI arithmetic and enterprise-grade AI algorithms, making it ideal for deploying large-scale models and generative AI frameworks.

Together, OpenShift AI and IBM Power provide a scalable, production-ready foundation for modern AI initiatives. Whether running models built with PyTorch, TensorFlow, or vLLM, this integrated stack supports hybrid cloud deployments and enables enterprises to operationalize AI with confidence - ensuring performance, efficiency, and flexibility across diverse workloads and environments.

## 10.3  Power Private Cloud Rack Solutions

The IBM Power Private Cloud Rack Solution is a pre-integrated, turnkey infrastructure offering designed to simplify the deployment and management of private cloud environments on IBM Power based-processor servers. Built on IBM Power11 technology, this solution combines compute, storage, networking, and management components into a single rack-based system optimized for enterprise workloads such as Db2 Warehouse, SAP HANA, and other data-intensive applications.

## 10.3.1  Key Features and Components:

Preconfigured Architecture: Includes Power11-based compute nodes, IBM FlashSystem storage, management and fabric switches, and power distribution units (PDUs), all pre-integrated and validated for performance and reliability.

Cloud-Ready Software Stack: Bundled with IBM PowerVC, Red Hat OpenShift, and optional IBM Cloud Pak solutions to support containerized and virtualized workloads.

High Availability and Security: Designed with built-in redundancy, secure boot, and compliance-ready configurations to meet enterprise-grade uptime and data protection requirements.

Simplified Management: Centralized tools allow administrators to monitor and manage multiple Power environments from a single dashboard, with support for automation and self-service provisioning.

This solution is ideal for organizations seeking to modernize their infrastructure with a cloud-like experience on-premises, while maintaining control over data locality, security, and performance.

## 10.3.2  Available configurations

The two available configurations are discussed in this section.

## IBM Power Private Cloud Rack Solution

The Power Private Cloud Rack Solution is offered in a preconfigured setup; this is an optimized full stack for a production-level environment. It leverages the unique virtualization technologies of PowerVM to accommodate all the software stack required in just three servers. Additional nodes can be added on the initial configuration as needed.

A minimum configuration includes:

- /SM590000 Hardware stack
- -Three Power S1122 servers
- -One FlashSystem 5200 storage enclosure with a minimum of 9.6 TB
- -Two SAN24B-6 switches with 24 FC ports and industry-leading Gen 6 FC technology

- -Optional IBM Ethernet switch with high-performance Gigabit Ethernet Layer 2 and Layer 3 switch featuring 52 ports
- -One IBM Enterprise slim rack with 42 EIA units of vertical mounting space and 19-inch rack enclosure
- /SM590000 Software stack
- -RHEL 8 for Power11
- -IBM PowerVM Enterprise Edition
- -IBM PowerVC for Private Cloud 2.0
- -Red Hat OpenShift Container Platform
- -IBM Spectrumfi Scale Data Access Edition or IBM Spectrum Scale Data Management Edition

If you have Red Hat entitlements for OpenShift Container Platform or RHEL 8, they can be deselected from the solution edition in e-config. A proof of entitlement for each software license will be requested and is mandatory in order to authorize the manufacturing and shipping of the solution.

## IBM Power Private Cloud Starter Solution

The Power Private Cloud Starter Solution includes:

- /SM590000 Hardware stack
- -At least one Power S1122 server node
- -Optional IBM FlashSystem 5200 storage enclosure
- /SM590000 Software stack
- -Red Hat Enterprise Linux (RHEL) 8 for Power9
- -Optional PowerVC for Private Cloud 2.0
- -PowerVM Enterprise Edition
- -Red Hat OpenShift Container Platform

If you have Red Hat entitlements for OpenShift Container Platform or RHEL 8, they can be deselected from the solution edition in e-config. A proof of entitlement for each software license will be requested and is mandatory in order to authorize the manufacturing and shipping of the solution.

## 10.3.3  IBM Cloud Paks

IBM Cloud Paks are a suite of modular, containerized software solutions designed to accelerate digital transformation. Built on Red Hat OpenShift, they enable organizations to modernize applications, automate business operations, manage data, and integrate AI across hybrid cloud environments with consistency and scalability.

Each Cloud Pak includes a combination of IBM middleware, open-source technologies, Kubernetes operators, and enterprise-grade security, providing a robust foundation for innovation and agility in the cloud. IBM Cloud Paks take a bundled approach that allows you to accelerate your modernization journey by packaging everything you need to get started.

There are three main benefits of IBM Cloud Paks:

- /SM590000 They are comprehensive and easy to use.
- /SM590000 They are supported by IBM.
- /SM590000 They run anywhere Red Hat OpenShift runs.

## IBM Cloud Paks on IBM Power

Optimized for deployment on IBM Power based-processor servers, IBM Cloud Paks deliver high performance and efficiency for containerized workloads. They support a wide range of use cases - from data and automation to AI and security - while ensuring seamless integration across on-premises and cloud environments.

IBM Power enhances the value of Cloud Paks by offering superior performance, scalability, and cost-efficiency for modern workloads. Combined with Red Hat's open-source ecosystem, it empowers businesses to both modernize legacy applications and build new cloud-native solutions on a unified, enterprise-ready platform.

There are several IBM Cloud Paks that are currently supported on IBM Power, each focused on a specific domain:

- /SM590000 Cloud Pak for Applications
- /SM590000 Cloud Pak for Data
- /SM590000 Cloud Pak for Integration
- /SM590000 Cloud Pak for AIops

## IBM Cloud Pak for Applications

IBM Cloud Pak for Applications is an enterprise-ready, containerized software solution designed to modernize existing applications and develop new cloud-native apps. Built on IBM WebSpherefi offerings and Red Hat OpenShift Container Platform, it provides a comprehensive set of tools to help organizations transition between public, private, and hybrid clouds.

IBM Cloud Pak for Applications includes IBM Cloud Transformation Advisor, an AI-powered tool which assists in refactoring and rearchitecting legacy applications. The solution includes automated vulnerability assessment and identification, ensuring continuous security compliance across all deployment environments. It also automates audit reporting, simplifying compliance management. Developers can use their preferred IDEs to build and deploy applications, with support for modern runtimes and DevOps workflows. This integration streamlines the development process and enhances productivity.

## IBM Cloud Pak for Data

IBM Cloud Pak for Data allows you to unify and simplify data collection, organization, and analysis. It is ideal for AI and analytics workloads. IBM Cloud Pak for Data is a unified, pre-integrated data and AI platform designed to help organizations collect, organize, analyze, and infuse AI into their data. Running natively on the Red Hat OpenShift Container Platform, it supports deployment across various cloud environments, including IBM Cloud, Amazon Web Services (AWS), and Microsoft Azure.

The platform allows secure access to data at its source, eliminating the need for data migration and reducing data silos, ensuring seamless data integration. It creates a trusted, business-ready analytics foundation, simplifying data preparation, policy enforcement, security, and compliance, while automating data governance and the AI lifecycle. IBM Cloud Pak for Data provides tools for building, deploying, and managing AI and machine learning models, scaling these capabilities consistently across the organization to enable comprehensive data analysis and insights.

By operationalizing AI throughout the business with trust and transparency, the platform supports the end-to-end AI workflow, ensuring effective integration of AI into business processes. Offering a single interface for end-to-end analytics with built-in governance, IBM Cloud Pak for Data simplifies the management of data and AI capabilities, while its scalable Kubernetes environment allows organizations to grow their data and AI capabilities as

needed. Supporting multi-cloud deployments, it provides agility and avoids vendor lock-in, making it a powerful tool for accelerating the journey to AI and unlocking the value of data for AI-driven digital transformation.

## IBM Cloud Pak for Integration

IBM Cloud Pak for Integration is a comprehensive, AI-powered hybrid integration platform designed to connect applications, data, systems, and services across any environment. It provides a unified experience with a suite of integration tools that streamline the creation, management, and deployment of integrations. Running on Red Hat OpenShift, IBM Cloud Pak for Integration supports both cloud and on-premises deployments, ensuring scalability and security. The platform includes components such as IBM API Connect for managing APIs, IBM App Connect for no-code integration, and IBM Event Streams for real-time data processing. By leveraging AI and automation, IBM Cloud Pak for Integration accelerates the integration process, reduces manual workflows, and enhances responsiveness to real-time events. This makes it an ideal solution for organizations looking to modernize their integration capabilities and drive digital transformation.

## IBM Cloud Pak for Business Automation

IBM Cloud Pak for Business Automation is a modular set of integrated software components designed to automate work and accelerate business growth. Built for any hybrid cloud, it simplifies complex workflows, facilitates records management, and enhances overall productivity. The platform uses AI to identify gaps and build low-code and no-code automations, making it easier to streamline operations. Running on Red Hat OpenShift, IBM Cloud Pak for Business Automation supports containerized deployments across various cloud environments, providing flexibility and scalability. Key features include automating case and process workflows, converting unstructured content into valuable data, and using software robots to complete tasks based on AI insights. This comprehensive automation solution helps organizations improve efficiency, reduce operational costs, and drive continuous process improvements.

## IBM Cloud Pak for AIOps

IBM Cloud Pak for AIOps is an advanced, AI-powered platform designed to enhance IT operations (ITOps) by leveraging artificial intelligence and machine learning. It integrates seamlessly with existing ITOps toolchains to provide comprehensive visibility, proactive incident management, and automated remediation. By analyzing data from various sources, such as logs, metrics, and events, IBM Cloud Pak for AIOps helps IT teams predict and resolve issues before they impact business operations. The platform supports hybrid cloud environments, enabling organizations to manage their IT infrastructure across on-premises, cloud, and containerized environments. Key features include event correlation and compression, anomaly detection, root cause analysis, and automated runbooks, all aimed at reducing mean time to resolution (MTTR) and improving overall operational efficiency. With its collaborative tools and real-time insights, IBM Cloud Pak for AIOps empowers IT teams to innovate faster, reduce operational costs, and ensure the reliability of mission-critical workloads.

For more information about IBM Cloud Paks see this IBM documentation.

## 10.3.4  Other cloud enablement solutions

From a Red Hat software perspective, there is also a comprehensive set of software solutions to accelerate your modernization efforts, including Red Hat Runtimes, Red Hat 3scale API Management, Red Hat Fuse and Red Hat AMQ.

## 10.4  Power Virtual Server

IBM Power Virtual Server is a cloud-based infrastructure-as-a-service (IaaS) offering that allows businesses to run IBM Power based-processor servers workloads in a flexible, scalable, and secure virtual environment. Built on the same architecture as IBM Power based-processor servers used on-premises, it enables seamless hybrid cloud integration, making it ideal for enterprises looking to modernize their IT infrastructure without completely abandoning their existing investments. With support for AIX, IBM i, and Linux operating systems, Power Virtual Server provides a versatile platform for mission-critical applications. It provides an excellent platform for moving AIX, IBM i, and Linux on Power workloads to the cloud without a time consuming and risky migration of those workloads to a different platform.

One of the key advantages of IBM Power Virtual Server is its ability to deliver high performance and reliability for enterprise workloads. It leverages IBM's Power processors, which are optimized for data-intensive tasks and high-throughput computing. The platform also offers features such as dynamic resource allocation, automated scaling, and integrated backup and disaster recovery options. These capabilities help organizations maintain business continuity and meet demanding service-level agreements (SLAs).

Additionally, IBM Power Virtual Server integrates with a wide range of IBM Cloud services and third-party tools, enabling users to build and manage hybrid cloud environments with ease. It supports DevOps practices, containerization with OpenShift, and AI/ML workloads, making it suitable for both traditional enterprise applications and modern cloud-native development. With its pay-as-you-go pricing model and global availability, IBM Power Virtual Server offers a cost-effective and agile solution for businesses aiming to innovate and grow in a digital-first world.

Power Virtual Server allows you to run IBM i, AIX, and Linux workloads in a cloud experience giving you fast, self-service provisioning, flexible compute, memory, and storage resources. PowerVS is designed to help organizations modernize their infrastructure, migrate to hybrid cloud models, and optimize their data center resources.

Key features and benefits of PowerVS include:

- /SM590000 Flexible and Scalable:
- Users can easily adjust compute, memory, and storage resources on demand, scaling up or down as needed.
- /SM590000 Pay-as-you-use:
- Billing is based on consumption, allowing organizations to manage cost effectively.
- /SM590000 Hybrid Cloud Integration:
- PowerVS facilitates seamless integration of AIX and IBM i workloads with cloud-native applications and services.
- /SM590000 Performance and Security:

PowerVS leverages the performance and security features of IBM Power based-processor servers while offering the agility of cloud computing.

- /SM590000 Managed Infrastructure:

PowerVS offers managed infrastructure, where IBM handles the hardware maintenance, allowing organizations to focus on their workloads from a software and application standpoint.

- /SM590000 Disaster Recovery:

PowerVS can be used to implement disaster recovery solutions for critical applications.

- /SM590000 Simplified Cloud Adoption:

PowerVS streamlines the cloud adoption process for IBM i, AIX, and other Power based-processor servers workloads.

## 10.4.1  Power Virtual Server options

Power Virtual Server is a single offering that can be delivered in two variations; off-premises, where the infrastructure components are located in IBM data centers, and on-premises, where the infrastructure components are located in the client's data center. The on-premises variation is known as IBM Power Virtual Server Private Cloud. Both variations provide a cloud-based consumption model, where you pay for resources as they are consumed, and are managed with the same management interfaces.

Figure 10-1 shows the two different implementations of IBM Power Virtual Server.

Figure 10-1   IBM Power Virtual Server options

<!-- image -->

Power Virtual Server Private Cloud is discussed in section 10.4.3, 'Power Virtual Server Private Cloud' on page 227.

## Use cases for Power Virtual Server

IBM Power Virtual Server supports a wide range of use cases, particularly for enterprises that rely on IBM Power based-processor servers for mission-critical workloads. Here are some of the most common and impactful scenarios:

## 1. Hybrid Cloud Modernization

Organizations with on-premises IBM Power based-processor servers can extend their infrastructure to the cloud using Power Virtual Server. This enables a hybrid cloud model where workloads can be moved or replicated to the cloud for scalability, disaster recovery, or testing - without needing to replatform or rewrite applications. It's especially useful for businesses running AIX or IBM i environments that want to modernize gradually.

## 2. Disaster Recovery and High Availability

Power Virtual Server provides a reliable platform for disaster recovery (DR) by allowing businesses to replicate their on-prem workloads to the cloud. In the event of a failure, workloads can be quickly restored in the cloud, minimizing downtime. It also supports high availability configurations, ensuring business continuity for critical applications.

## 3. Development and Testing Environments

Developers can use Power Virtual Server to quickly spin up isolated environments for application development, testing, and quality assurance. This is particularly valuable for teams working on AIX, IBM i, or Linux-based applications, as it eliminates the need for dedicated on-prem hardware and allows for faster iteration and deployment cycles.

## 4. SAP HANA and ERP Workloads

IBM Power Virtual Server is certified to run SAP HANA and other SAP ERP applications. Enterprises can migrate or extend their SAP environments to the cloud for better scalability, performance, and cost-efficiency - especially when paired with IBM's high-performance Power11 processors.

## 5. AI and Machine Learning

Power Virtual Server supports AI/ML workloads, particularly those requiring high compute power and memory bandwidth. It integrates with IBM Watsonfi and Red Hat OpenShift, allowing data scientists to build, train, and deploy models using familiar tools while leveraging the performance of Power based-processor servers.

## 6. Database Hosting

Many organizations use Power Virtual Server to host enterprise-grade databases like IBM Db2, Oracle, or PostgreSQL. The platform offers high I/O throughput and reliability, making it ideal for transaction-heavy applications such as banking, retail, and logistics.

## 7. Legacy Application Hosting

For businesses with legacy applications running on AIX or IBM i, Power Virtual Server provides a cloud-based alternative to aging on-prem hardware. This allows companies to extend the life of critical applications while gradually modernizing their infrastructure.

## 8. Compliance and Data Sovereignty

Organizations in regulated industries (e.g., healthcare, finance, government) use Power Virtual Server to meet strict compliance and data residency requirements. IBM offers regional data centers and compliance certifications to help meet these needs.

## 10.4.2  Power Virtual Server in the Cloud

In this variation, IBM Power Virtual Server resources reside in IBM data centers with dedicated networking and storage area network (SAN) attached storage. Customers can choose from one of the currently 21 different data centers, choosing the data center that is

closest to their users. IBM Power clients who rely on private cloud infrastructure can now quickly and economically extend their Power IT resources on the cloud.

In these IBM data centers, Power Virtual Server resources are separated from the rest of IBM cloud servers with separate networks and direct attached storage. In this offering, customers are given flexibility to choose from different IBM Power server models, an IBM supplied OS image, and different tiers for storage based on your specific workload requirements. Customers are also given to choose their own image as Bring Your Own License (BYOL) so that they can bring already configured images from their enterprise infrastructure onto Power Virtual Server. This offering also supports distinctive features such as shared processor pools, public connectivity of VMs, placement groups, and global replication service (GRS) which can be consumed based on customer's requirements.

For more information on IBM PowerVS: Getting Started with IBM Power Virtual Server

## 10.4.3  Power Virtual Server Private Cloud

For those clients that want a cloud experience running on IBM Power servers, but have requirements to keep control of their data and applications (whether those requirements are regulatory, security based, or perhaps performance based). For those clients, IBM designed an offering where we bring the Power Virtual Server offering to a data center of your choice.

Power Virtual Server Private Cloud extends all the benefits of IBM Power Virtual Server into your (or a partner's) data center. The enhanced capabilities of IBM Power Virtual Server Private Cloud provide managed infrastructure as a service at client locations, with metered consumption and no upfront costs to support Hybrid by Design delivery of services.

The IBM Power Virtual Server Private Cloud offering is engineered to:

- /SM590000 Maintain customer data and workloads on your own site.
- Enterprises may have workloads or data that is regulated and cannot be hosted off-premises. In some cases, enterprises can have workloads that are sensitive or with ultra-short latency requirements that are better served on site and in very close in proximity with other on-site workloads.
- /SM590000 Maintain customer data in region and specific geographies in the location of their choice.
- Country sovereignty regulations are requiring some data and workloads to stay in country. According to a recent IBM Institute of Business Value study, 61% of cloud leaders cite security or compliance as reasons for moving certain workloads from public clouds to private clouds or on-premises data centers.
- /SM590000 Provide a seamless hybrid cloud experience.
- Enterprises can foster a unified hybrid cloud landscape by seamlessly integrating Power Virtual Server running both at an IBM site and at a client site location with the ability to manage all the virtual machines (VMs) and infrastructure effortlessly through a unified user interface. Clients can receive the flexibility utilizing as-a-service with intentional workload placement on and off premises.
- /SM590000 Deliver predictable charging model with committed monthly spend combined with flexible consumption with metered usage-based pricing.
- Both Power Virtual Server offerings, off-premises running at an IBM location and on-premises running at the client site, include compute, memory, storage, and operating system licenses that are fully metered by the hour allowing clients to pay for how much they use each month with no upfront payment.
- /SM590000 Streamline IT operations.

Whether in the cloud or at an enterprise's site, IBM manages the infrastructure, freeing enterprises to focus on business outcomes and less on managing infrastructure. IBM will own, deliver, and set up the Power Virtual Server in datacenter of choice, and provide a fully managed solution, including monitoring, security, firmware updates, and infrastructure management.

- /SM590000 Provide enhanced security and control of data.

IBM Power Virtual Server is designed to provide comprehensive security for IBM Power infrastructure by integrating with IBM Cloud tooling to manage security. This alleviates the need to manage Power infrastructure security with the added benefit of maintaining sensitive data and workload on-premises.

The physical infrastructure is delivered as a point of delivery (pod) which will be deployed in customer's data center. A pod is the physical component which resides within the client datacenter and contains the compute, storage and network components. A pod contains one or more racks where each of the components are installed. The racks are interconnected to provide a completely self-contained infrastructure, including both customer usable components, spare components, and management components.

This pod will be maintained by IBM site reliability engineering (SREs) and managed through IBM Cloud platform. Each pod is associated with an IBM Cloud satellite location that is owned by customer's IBM cloud account. This architecture provides the ability to scale your private cloud infrastructure horizontally by adding more pods to meet your workloads requirements.

For more information about Power Virtual Server Private Cloud refer to the IBM Redpaper Introduction to IBM Power Virtual Server Private Cloud , REDP-5745.

## 10.4.4  Introducing IBM Power11 in the Cloud

Power11 will be available on the day of announcement in IBM Power Virtual Server and IBM Power Virtual Server Private Cloud. With the launch of IBM Power11, clients and ISVs gain immediate access to the latest Power hardware in the cloud - enabling faster innovation and greater flexibility. Whether you're modernizing applications or enhancing business continuity, Power11 in PowerVS delivers a seamless hybrid cloud experience.

Key benefits include:

- /SM590000 Rapid Deployment - Launch Power11 virtual servers in the cloud in under 10 minutes.
- /SM590000 Accelerated Modernization - Enable agile development and testing on the latest Power infrastructure.
- /SM590000 Enhanced Business Resiliency - Strengthen continuity strategies with cloud-based Power11 resources.
- /SM590000 Data Sovereignty Compliance - Meet regulatory and sensitive data requirements with on-premises options.
- /SM590000 Consistent Hybrid Cloud Experience - Enjoy unified operations across on-premises and cloud environments.

Figure 10-2 shows the initial implementation of Power11 processors in Power Virtual Server on announcement day.

Figure 10-2   Availability of Power11 in Power Virtual Server

<!-- image -->

Power11 technology in Power Virtual Server allows you to immediately take advantage of the new functionality without a requirement for initial capital investment. You can safely implement workloads taking advantage of the Trusted security capabilities of Power11 like:

- /SM590000 Quantum-safe infrastructure compliance with optional workload cryptographic inventory discovery
- /SM590000 A unified cyber resiliency solution responding to evolving cyber threats and regulatory standards with optional 3rd party services

In addition, you can immediately take advantage of the improved performance of Power11 as shown in Figure 10-3.

Figure 10-3   Potential performance benefits from Power in PowerVS

<!-- image -->

## Related publications

The publications listed in this section are considered particularly suitable for a more detailed discussion of the topics covered in this book.

## IBM Redbooks

The following IBM Redbooks publications provide additional information about the topic in this document. Note that some publications referenced in this list might be available in softcopy only.

- /SM590000 Modernization Techniques for IBM Power , SG24-8582
- /SM590000 IBM i 7.6 features and function , SG24-8588
- /SM590000 IBM Power Security Catalog , SG24-8568
- /SM590000 Creating OpenShift Multiple Architecture Clusters with IBM Power , SG24-8565
- /SM590000 Introduction to IBM Power Virtual Server Private Cloud , REDP-5745
- /SM590000 Using Ansible for Automation in IBM Power Environments , SG24-8551
- /SM590000 IBM PowerHA SystemMirror and IBM VM Recovery Manager Solutions Updates , REDP-5694

You can search for, view, download or order these documents and other Redbooks, Redpapers, Web Docs, draft and additional materials, at the following website:

ibm.com /redbooks

## Online resources

These websites are also relevant as further information sources:

- /SM590000 Red Hat OpenShift AI: Supported Configurations
- https://access.redhat.com/articles/rhoai-supported-configs
- /SM590000 Red Hat OpenShift AI Self-Managed 2.20 - Documentation

https://docs.redhat.com/en/documentation/red\_hat\_openshift\_ai\_self-managed/2.20 /pdf/release\_notes/Red\_Hat\_OpenShift\_AI\_Self-Managed-2.20-Release\_notes-en-US.p df

- /SM590000 Red Hat OpenShift AI Self-Managed Life Cycle

https://access.redhat.com/support/policy/updates/rhoai-sm/lifecycle

- /SM590000 Red Hat OpenShift AI Self-Managed 2.20

https://docs.redhat.com/en/documentation/red\_hat\_openshift\_ai\_self-managed/2.20

- /SM590000 Red Hat OpenShift AI Service Definition
- https://access.redhat.com/articles/7102731
- /SM590000 OpenShift Operator Life Cycles

https://access.redhat.com/support/policy/updates/openshift\_operators

- /SM590000 RHEL Versions Utilized by RHEL CoreOS and OCP

https://access.redhat.com/articles/6907891

- /SM590000 Red Hat OpenShift for IBM Power

https://www.redhat.com/en/resources/openshift-ibm-power-systems-datasheet#:~:te xt=Red%20Hat%20OpenShift%20and%20IBM,on%20IBM%20Power%20are%20supported

## Help from IBM

IBM Support and downloads

ibm.com /support

IBM Global Services

ibm.com /services

(0.1'spine) 0.1'&lt;-&gt;0.169' 53&lt;-&gt;89 pages

(0.2'spine) 0.17'&lt;-&gt;0.473' 90&lt;-&gt;249 pages

<!-- image -->

## IBM Power11 Scale-Out Servers: Introduction and Overview

(0.5' spine) 0.475'&lt;-&gt;0.873' 250 &lt;-&gt; 459 pages

## IBM Power11 Scale-Out Servers: Introduction and Overview

ISBN

SG24-8590-00

<!-- image -->

(1.0' spine) 0.875'&lt;-&gt;1.498' 460 &lt;-&gt; 788 pages

<!-- image -->

## IBM Power11 Scale-Out Servers: Introduction and Overview

ISBN

SG24-8590-00

<!-- image -->

(1.5' spine) 1.5'&lt;-&gt; 1.998' 789 &lt;-&gt;1051 pages

<!-- image -->

## IBM Power11 Scale-Out Servers: Introduction and Overview

ISBN

SG24-8590-00

<!-- image -->

1052 &lt;-&gt; 1314 pages

2.0' &lt;-&gt; 2.498'

(2.0' spine)

<!-- image -->

## IBM Power11 Scale-Out Servers: Introduction and Overview

ISBN

SG24-8590-00

<!-- image -->

(2.5' spine) 2.5'&lt;-&gt;nnn.n' 1315&lt;-&gt; nnnn pages

<!-- image -->

Servers: Introduction and

## IBM Power11 Scale-Out

ISBN

SG24-8590-00

<!-- image -->

<!-- image -->

Back cover

<!-- image -->

SG24-8590-00

ISBN

<!-- image -->