# Normales WIFI-Sharing
sudo pfctl -sa
No ALTQ support in kernel
ALTQ related functions disabled
TRANSLATION RULES:
nat-anchor "com.apple/*" all
nat-anchor "com.apple.internet-sharing" all
rdr-anchor "com.apple/*" all
rdr-anchor "com.apple.internet-sharing" all

FILTER RULES:
scrub-anchor "com.apple/*" all fragment reassemble
scrub-anchor "com.apple.internet-sharing" all fragment reassemble
anchor "com.apple/*" all
anchor "com.apple.internet-sharing" all

DUMMYNET RULES:
dummynet-anchor "com.apple/*" all
