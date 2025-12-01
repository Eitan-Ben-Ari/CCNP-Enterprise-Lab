#  Multi-Site Enterprise Project  
**100% Ansible-Automated Overlay + Conditional Internet Breakout**

[View Full Topology Diagram](images/topology.svg)

9 × CSR1000v (IOS-XE 17.3) | GNS3/EVE-NG/

## Overview
This project is a full multi-site enterprise lab built on GNS3.
It includes Routing&Switching features such as DMVPN, IPsec, BGP, OSPF, QoS, VRFs, L2 security, which are deployed using modular Ansible roles.

## Design Highlights
- Dual-VRF architecture (`overlay`  + `underlay`)
- DMVPN Phase 3 + multipoint GRE over Internet
- Full IPsec IKEv2 protection with per-spoke pre-shared keys (Jinja2 templated)
- BGP overlay (eBGP multihop over loopbacks) 
- Conditional Internet breakout 
  → Specific routes exist → traffic goes via DMVPN tunnel  
  → No specific route → single-line default-route leak → NAT → direct ISP breakout


| Component                     | Deployed by Ansible Role/Playbook               | 
|-------------------------------|--------------------------------------------------|
| L3 interfaces                 | `roles/l3_interfaces` → `l3_interfaces.j2`       | 
| DMVPN mGRE tunnels(           | `roles/crypto` → `dmvpn_mgre.j2`                 | 
| IPsec IKEv2 suite             | `roles/crypto` → `ipsec.j2`                      | 
| multi process OSPF            | `roles/ospf_role`  →  `ospf.j2`                  | 
| BGP overlay peers             | `roles/bgp` → `neighbor.j2`                      | 
| VRF-aware PAT                 | `roles/NAT`→ `source_list.yml`  `PAT.j2`         | 
| Qos & Acls                    | `roles/QOS`  → `access_group.yml` `inter_marking.j2` `wan_inbound.j2` `wan_outbound.j2`|      
| Vlans, L2 interfaces, LACP    | `roles/L2 & VTY`  →  `vlans.yml` `l2_interfaces.yml`  `lag.yml`  | 
| L2 Security(port-sec, dhcp-snooping, DIA, STP)| `roles/L2 & VTY`  →  `l2_security.j2`  | 
| HSRP & STP                    | `roles/L2 & VTY`  →  `hsrp_stp.j2`  |
| Banner Motd                   | `small_tasks`  →  `banner_motd.yml`  |



