# CCNP Enterprise – Multi-Site DMVPN Branch Edge  
**100% Ansible-Automated Overlay + Conditional Internet Breakout**

9 × CSR1000v (IOS-XE 17.3) | GNS3 | Dual-VRF 

![Lab Topology](images/topology.png)

## Design Highlights
- Dual-VRF architecture (`site_1` / `site_1_2` overlay + `underlay`)
- DMVPN Phase 3 + multipoint GRE over Internet
- Full IPsec IKEv2 protection with per-spoke pre-shared keys (Jinja2 templated)
- BGP overlay (eBGP multihop over loopbacks) 
- Conditional Internet breakout 
  → Specific routes exist → traffic goes via DMVPN tunnel  
  → No specific route → single-line default-route leak → NAT → direct ISP breakout

Everything in the overlay vrf on Edges is deployed by Ansible 

| Component                     | Deployed by Ansible Role/Playbook               | Templated |
|-------------------------------|--------------------------------------------------|-----------|
| L3 interfaces & VRFs          | `roles/l3_interfaces` → `l3_interfaces.j2`       | Yes       |
| DMVPN mGRE tunnels(           | `roles/crypto` → `dmvpn_mgre.j2`                 | Yes       |
| IPsec IKEv2 suite             | `roles/crypto` → `ipsec.j2`                      | Yes       |
| multi process OSPF            | `roles/ospf_role`  →  `ospf.j2`                  | Yes       |
| BGP overlay peers             | `roles/bgp` → `neighbor.j2`                      | Yes       |
| VRF-aware PAT                 | `source_list.yml`  `PAT.j2`                      | Yes       |
| BGP overlay peers             | `roles/bgp` → `neighbor.j2`                      | Yes       |
| QOS, 3 service-policies       | `roles/QOS`  → `access_group.yml` `inter_marking.j2` `wan_inbound.j2` `wan_outbound.j2`       | YES        |
| Vlans, L2 interfaces, LACP    | `roles/L2 & VTY`  →  `vlans.yml` `l2_interfaces.yml`  `lag.yml`  | –         |
| L2 Security(port-sec, dhcp-snooping, DIA, STP)| `roles/L2 & VTY`  →  `l2_security.j2`  | YES    |




