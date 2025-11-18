# CCNP Enterprise – Multi-Site DMVPN Branch Edge  
**100% Ansible-Automated Overlay + Conditional Internet Breakout**

Production-grade, zero-touch branch lab – exactly how enterprises do it in 2025  
9 × CSR1000v (IOS-XE 17.3) | GNS3/EVE-NG | Dual-VRF | No PBR anywhere

![Lab Topology](images/topology.png)

## Real-World Design Highlights
- Dual-VRF architecture (`site_1` / `site_1_2` overlay + `underlay`)
- DMVPN Phase 3 + multipoint GRE over Internet
- Full IPsec IKEv2 protection with per-spoke pre-shared keys (Jinja2 templated)
- BGP overlay (eBGP multihop over loopbacks) – spokes receive **default-route only from ISP**, not from hub
- Conditional Internet breakout without a single PBR statement  
  → Specific routes exist → traffic goes via DMVPN tunnel  
  → No specific route → single-line default-route leak → NAT → direct ISP breakout

Everything in the overlay is deployed by Ansible – zero manual CLI:

| Component                     | Deployed by Ansible Role/Playbook               | Templated |
|-------------------------------|--------------------------------------------------|-----------|
| L3 interfaces & VRFs          | `roles/l3_interfaces`                            | Yes       |
| DMVPN mGRE tunnels            | `roles/crypto` → `dmvpn_mgre.j2`                 | Yes       |
| Full IPsec IKEv2 suite (proposal/policy/keyring/profile/transform-set) | `roles/crypto` → `ipsec.j2` | Yes       |
| Tunnel protection             | `roles/crypto`                                   | Yes       |
| OSPF (underlay + overlay)     | `roles/ospf_role`                                | Yes       |
| BGP overlay peers             | `roles/bgp` → `neighbor.j2`                      | Yes       |
| VRF-aware NAT + default-route leak | `playbooks/main.yml`                        | Yes       |
| Post-deployment config backup | `playbooks/small_tasks/wr+save_backup.yml`       | –         |

