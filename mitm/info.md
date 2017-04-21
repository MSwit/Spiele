# forwarding aktivieren
sudo sysctl net.inet.ip.forwarding=1


# starten
sudo pfctl -evf pf.conf

#stoppen
sudo pfctl -F all -f /etc/pf.conf


# ipforwarding
sudo sysctl -w net.inet.ip.forwarding=1


echo "
rdr pass inet proto tcp from any to any port 80 -> 127.0.0.1 port 8080
" | sudo pfctl -ef -




# displays the forwarding rules
 sudo pfctl -s nat
