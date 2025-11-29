#!/bin/bash

ip route add 6.6.6.1/32 dev br0 via 192.168.3.7
ip route add 4.4.4.1/32 dev br0 via 192.168.3.7
ip route add 4.4.4.4/32 dev br0 via 192.168.3.7
ip route add 3.3.3.0/30 dev br0 via 192.168.3.7
ip route add 2.2.2.0/30 dev br0 via 192.168.3.7
ip route add 1.1.1.0/31 dev br0 via 192.168.3.7
ip route add 6.6.6.6/32 dev br0 via 192.168.3.7
ip route add 4.4.4.0/30 dev br0 via 192.168.3.7
ip route add 7.7.7.7/32 dev br0 via 192.168.3.7
ip route add 10.0.10.28/32 dev br0 via 192.168.3.7
ip route add 10.0.20.12/32 dev br0 via 192.168.3.7
ip route add 8.8.8.0/29 dev br0 via 192.168.3.7
ip route add 1.2.3.6/31 dev br0 via 192.168.3.7
ip route add 192.0.2.4/31 dev br0 via 192.168.3.7
ip route add 198.51.100.2/31 dev br0 via 192.168.3.7
ip route add 203.0.113.0/31 dev br0 via 192.168.3.7
