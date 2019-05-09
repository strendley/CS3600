bash fw_setup.sh  # to keep thes shell consistent
sudo iptables -S
sudo iptables -L
sleep 10s
systemctl reboot
sudo iptables -S
sudo iptables -L

