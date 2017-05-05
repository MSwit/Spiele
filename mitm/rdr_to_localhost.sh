#!/bin/bash
sudo pfctl -d
sudo pfctl -F all

sudo sysctl net.inet.ip.forwarding=1



int_if="en0"
ext_if="en8"
port="8080"
protocol="{tcp, udp}"


#C1="rdr on $int_if inet proto $protocol -> 127.0.0.1 port 8080"
#(echo $C1) | sudo pfctl -evf -

#C1="set skip on lo0"
C1="rdr on $ext_if inet proto tcp to any port 80 -> 127.0.0.1 port 8080"
C2="rdr on $ext_if inet proto tcp to any port 443 -> 127.0.0.1 port 8080"

C3=""
C4=""



#C1="rdr on $int_if inet proto $protocol from any -> 127.0.0.1 port $port"
#C2="pass in on $int_if inet proto $protocol from any to 127.0.0.1 port $port keep state"
#C3="pass out on $ext_if inet proto $protocol from any keep state"

(echo $C1; echo $C2; echo $C3; echo $C4) | sudo pfctl -evf -

#C1="pass {tcp, udp} from 127.0.0.1 to any"
#C2="rdr pass on lo0 proto {tcp, udp} from en0 -> 127.0.0.1 port 8080"
#C3="pass out on en0 route-to lo0 inet proto {tcp, udp} from en0 keep state"
#(echo $C1; echo $C2; echo $C3) | sudo pfctl -evf -
