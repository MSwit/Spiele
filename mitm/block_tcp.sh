sudo pfctl -F all

sudo sysctl net.inet.ip.forwarding=1
echo "block proto tcp" | sudo pfctl -evf - 
