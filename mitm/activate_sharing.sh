#sudo pfctl -evf pf_local2.conf
#sudo sysctl net.inet.ip.forwarding=1

sudo networksetup -setv6off Wi-Fi
sudo networksetup -setv6off "AX88179 USB 3.0 to Gigabit Ethernet"

sudo pfctl -d
sudo pfctl -F all
sudo sysctl net.inet.ip.forwarding=1
sudo pfctl -evf pf_sharing.conf
