#!/bin/bash
sudo pfctl -F all

sudo sysctl net.inet.ip.forwarding=1
sudo networksetup -setv6off Wi-Fi
sudo networksetup -setv6off Ethernet


int_if="en0"
ext_if="en8"
port="8080"
protocol="{tcp, udp}"

C1="block all"
C1=""
C2=""
#C2="set skip on lo0"

C3="rdr on lo0 proto tcp from en0 to any port { 80, 443 } -> 127.0.0.1 port 8080"
C3=""
C4="pass out on en0 route-to lo0 proto tcp from en0 to any port { 80, 443 } keep state"
C4="rdr pass on $int_if proto tcp from any to any port 80 -> 127.0.0.1 port 8080"
(echo $C1; echo $C2; echo $C3; echo $C4) | sudo pfctl -ef -

#C1="pass {tcp, udp} from 127.0.0.1 to any"
#C2="rdr pass on lo0 proto {tcp, udp} from en0 -> 127.0.0.1 port 8080"
#C3="pass out on en0 route-to lo0 inet proto {tcp, udp} from en0 keep state"
#(echo $C1; echo $C2; echo $C3) | sudo pfctl -evf -


# Second redirect now incoming traffic to localhost 8080 for all traffic that matches our host and port filter


# First route all outgoing traffic from en0 to lo0 that matches our host and port filter and user
