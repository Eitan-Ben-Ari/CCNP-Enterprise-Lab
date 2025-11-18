# CCNP Enterprise – Multi-Site DMVPN Branch Edge  
**100% Ansible-Automated Overlay + Conditional Internet Breakout**

9 × CSR1000v (IOS-XE 17.3) | GNS3 | Dual-VRF 

![Lab Topology](images/topology.png)

## Real-World Design Highlights
- Dual-VRF architecture (`site_1` / `site_1_2` overlay + `underlay`)
- DMVPN Phase 3 + multipoint GRE over Internet
- Full IPsec IKEv2 protection with per-spoke pre-shared keys (Jinja2 templated)
- BGP overlay (eBGP multihop over loopbacks) 
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







itan@CCNP-Dragon-Eitan:~/Documents/ccnp-project/ansible$ tree
.
├── ansible.cfg
├── backups
│   ├── D1.EITAN.COM
│   │   └── running_config.txt
│   ├── D2.EITAN.COM
│   │   └── running_config.txt
│   ├── D3.EITAN.COM
│   │   └── running_config.txt
│   ├── D4.EITAN.COM
│   │   └── running_config.txt
│   ├── D6.EITAN.COM
│   │   └── running_config.txt
│   ├── D7.EITAN.COM
│   │   └── running_config.txt
│   ├── D8.EITAN.COM
│   │   └── running_config.txt
│   ├── D9.EITAN.COM
│   │   └── running_config.txt
│   ├── R1.EITAN.COM
│   │   └── running_config.txt
│   ├── R2.EITAN.COM
│   │   └── running_config.txt
│   ├── R4.EITAN.COM
│   │   └── running_config.txt
│   ├── R6.EITAN.COM
│   │   └── running_config.txt
│   └── R8.EITAN.COM
│       └── running_config.txt
├── group_vars
│   └── all.yml
├── hosts
├── host_vars
│   ├── D1.EITAN.COM.yml
│   ├── D2.EITAN.COM.yml
│   ├── D3.EITAN.COM.yml
│   ├── D4.EITAN.COM.yml
│   ├── D6.EITAN.COM.yml
│   ├── D7.EITAN.COM.yml
│   ├── D8.EITAN.COM.yml
│   ├── D9.EITAN.COM.yml
│   ├── R1.EITAN.COM.yml
│   ├── R2.EITAN.COM.yml
│   ├── R4.EITAN.COM.yml
│   ├── R6.EITAN.COM.yml
│   └── R8.EITAN.COM.yml
├── inventory.yml
├── playbooks
│   ├── informational
│   │   ├── conditional_interface_info.yml
│   │   ├── fact_gathering.yml
│   │   ├── hostvars.yml
│   │   └── loop_through_ip_address.yml
│   ├── main.yml
│   └── small_tasks
│       ├── no_domain_lookup.yml
│       ├── radi_tacacs_timeout.yml
│       ├── use_gather_to_config_p2p.yml
│       └── wr+save_backup.yml
├── roles
│   ├── bgp
│   │   ├── defaults
│   │   │   └── main.yml
│   │   ├── files
│   │   ├── handlers
│   │   │   └── main.yml
│   │   ├── meta
│   │   │   └── main.yml
│   │   ├── README.md
│   │   ├── tasks
│   │   │   └── main.yml
│   │   ├── templates
│   │   │   └── neighbor.j2
│   │   ├── tests
│   │   │   ├── inventory
│   │   │   └── test.yml
│   │   └── vars
│   │       └── main.yml
│   ├── crypto
│   │   ├── defaults
│   │   │   └── main.yml
│   │   ├── files
│   │   ├── handlers
│   │   │   └── main.yml
│   │   ├── meta
│   │   │   └── main.yml
│   │   ├── README.md
│   │   ├── tasks
│   │   │   └── main.yml
│   │   ├── templates
│   │   │   ├── dmvpn_mgre.j2
│   │   │   └── ipsec.j2
│   │   ├── tests
│   │   │   ├── inventory
│   │   │   └── test.yml
│   │   └── vars
│   │       └── main.yml
│   ├── l3_interfaces
│   │   ├── defaults
│   │   │   └── main.yml
│   │   ├── files
│   │   ├── handlers
│   │   │   └── main.yml
│   │   ├── meta
│   │   │   └── main.yml
│   │   ├── README.md
│   │   ├── tasks
│   │   │   └── main.yml
│   │   ├── templates
│   │   │   └── l3_interfaces.j2
│   │   ├── tests
│   │   │   ├── inventory
│   │   │   └── test.yml
│   │   └── vars
│   │       └── main.yml
│   └── ospf_role
│       ├── defaults
│       │   └── main.yml
│       ├── files
│       ├── handlers
│       │   └── main.yml
│       ├── meta
│       │   └── main.yml
│       ├── README.md
│       ├── tasks
│       │   └── main.yml
│       ├── templates
│       │   └── ospf.j2
│       ├── tests
│       │   ├── inventory
│       │   └── test.yml
│       └── vars
│           └── main.yml
└── templates

