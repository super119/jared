#!/bin/bash
wget "https://raw.githubusercontent.com/fivesheep/chnroutes/master/chnroutes.py"
chmod 755 chnroutes.py
# chnroutes.py has stopped updating since 2018 since it needs python2
python2 ./chnroutes.py -p mac
echo "/ip firewall address-list" > ros-domestic-ips.rsc
grep "route add" ip-up >> ros-domestic-ips.rsc
sed -i -e "s/route add /add address=/g" -e 's/"${OLDGW}"/disabled=no list=domestic/g' ros-domestic-ips.rsc
sed -i "/add address=10.0.0.0/d" ros-domestic-ips.rsc
sed -i "/add address=172.16.0.0/d" ros-domestic-ips.rsc
sed -i "/add address=192.168.0.0/d" ros-domestic-ips.rsc
rm -f ip-up ip-down chnroutes.py
echo "Done."
