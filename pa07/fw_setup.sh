#!/usr/bin/env bash
#author: stbrb@mst.edu

#clear all old rules
sudo iptables -F
sudo iptables -F -t mangle
sudo iptables -F -t nat

#clear chain rules
sudo iptables -X 
sudo iptables -X -t mangle
sudo iptables -X -t nat

#set default policies for chain
sudo iptables -P FORWARD DROP

#prevent established connections from being dropped 
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

#allow local traffic
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT

#allow incoming access to static IP address via SSH
sudo iptables -A INPUT -s 10.0.2.15 -p tcp --dport 22 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

#allow outgoing access to static IP address via SSH
sudo iptables -A OUTPUT -s 10.0.2.15 -p tcp --dport 22 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

#allow incoming http(80)/https(443) tcp traffic 
sudo iptables -A INPUT -p tcp --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

#allow outgoing http(80)/https(443) tcp traffic 
sudo iptables -A OUTPUT -p tcp --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp --dport 443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

#allow incoming http(80)/https(443) udp traffic 
sudo iptables -A INPUT -p udp --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -p udp --dport 443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

#allow outgoing http(80)/https(443) udp traffic 
sudo iptables -A OUTPUT -p udp --dport 80 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p udp --dport 443 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

#drop packets that don't match the criteria
sudo iptables -P INPUT DROP
sudo iptables -P OUTPUT DROP

#allow outgoing traffic from dns
sudo iptables -A OUTPUT -p udp --dport domain -j ACCEPT

#the next part makes the rules persistent upon reboot.

#check to see if the folder exists; if it does, delete it.
if [ -d /etc/iptables/ ]; then
	sudo rm -rf /etc/iptables/
fi

#make a new iptables folder in /etc/
sudo mkdir /etc/iptables/

#check to see if a file with the rules exists; if it does, delete it.
if [ -f /etc/iptables/rules.v4 ]; then
	sudo rm -f /etc/iptables/rules.v4
fi

#make a new file to put the rules into.
sudo touch /etc/iptables/rules.v4

#export the rules into this file.
sudo iptables-save | sudo tee /etc/iptables/rules.v4 > /dev/null

#check to see if the file exists; if it does, delete it.
if [ -f /etc/network/if-pre-up.d/iptables ];  then
	sudo rm -f /etc/network/if-pre-up.d/iptables
fi

#create the file
sudo touch /etc/network/if-pre-up.d/iptables

#make the file executable
sudo chmod 777 /etc/network/if-pre-up.d/iptables

#make the file execute before loading the network
echo "#!/bin/bash" | sudo tee /etc/network/if-pre-up.d/iptables > /dev/null

#restore the rules
echo "sudo bash -c \"/sbin/iptables-restore < /etc/iptables/rules.v4\"" | sudo tee -a /etc/network/if-pre-up.d/iptables > /dev/null



