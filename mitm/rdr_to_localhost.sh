sudo pfctl -F all

sudo sysctl net.inet.ip.forwarding=1
(echo "rdr pass on lo0 proto {tcp, udp} from en0 -> 127.0.0.1 port 8080"; echo "pass out on en0 route-to lo0 inet proto {tcp, udp} from en0 keep state") | sudo pfctl -evf -
