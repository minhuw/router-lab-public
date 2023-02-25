#!/bin/bash

set -eou pipefail

sudo ip netns exec R1 tcpdump -i eth1 -w R1-eth1.pcap &
sudo ip netns exec R1 tcpdump -i eth2 -w R1-eth2.pcap &

sudo ip netns exec R2 tcpdump -i eth1 -w R2-eth1.pcap &
sudo ip netns exec R2 tcpdump -i eth2 -w R2-eth2.pcap &

sudo ip netns exec R3 tcpdump -i eth1 -w R3-eth1.pcap &
sudo ip netns exec R3 tcpdump -i eth2 -w R3-eth2.pcap &

sudo ip netns exec R4 tcpdump -i eth1 -w R4-eth1.pcap &
sudo ip netns exec R4 tcpdump -i eth2 -w R4-eth2.pcap &
