#****Linux Commands****
----------------------------------------------------------------------------------------------
#***Table of Content #TOC***
#general-version,apt,user,pass
#Network-process,pid,controlpanel,systemctl,bluetoothctl 
#awk,sed,curl
#terminal shortcuts
#howto?
-----------------------------------------------------------------------------------------------
#general
$lsb_release -a         # to check the currently running ubuntu version.
$lsb_release -i         # example output- Distributor ID:Ubuntu
$lsb_release -d         # example output- Description:Ubuntu 22.04.3 LTS
$lsb_release -r         # example output- Release:22.04
$lsb_release -c         # example output- Codename:jammy

$hostname       # pc or machine name   

$uname -a           # software name and version
$uname -a           # check the current running linux version on machine 
$uname -v           # only linux version 
$uname -r           # release info of linux

$whoami         # username

$su -           # to enter the root mode
$sudo adduser <username>
$sudo passwd <username>
    <enter the password> 
su - <username>         #switch user 
id <username>           #full user details

$shutdown -r <now/1/anynumber to delay the shutdown> 
$shutdown -r            #reboot
$shutdown -p            #poweroff 
$shutdown -c            #cancel

$ls -1     # list in single file 
$ls -a      # for hidden files

#find [path] [options] [expression]  
$find . -type f -name 
$find . -type f -name '<approxfilename>*' -exec grep -i '<findtext>' {} +  #{} is a place holder and + is to accept multipe file name entries on exec mode, exec mode is to execute additonal commands on find. 

#apt,apt-get
$apt-get update
$apt-get upgrade

$touch <filename 1> <filename 2>        # creates one or more files
$cat > <filename>       # create file and allows to edit it before closing using ctrl + D 
$cat >> <filename>      # allows to enter the text that appends to the file.
$cat -n <filename>      # get the content with line numbers
---------------------------------------------------------------------------------------------
#Network,process,pid,controlpanel,systemctl,bluetoothctl
$ip a 
$ip address 

$apt-get install iputils-ping           # ping install 
$netstat -tuln

$netstat -t: Show TCP connections.
$netstat -u: Show UDP connections.
$netstat -l: Show only listening ports.
$netstat -n: Display numerical addresses instead of resolving names
$netstat -tuln | grep 8080
#systemctl  
$systemctl list-units --type=service --state=[running/inactive/active/loaded/dead]	
$systemctl stop mysql.service 	# to stop mysql.service from running.
$systemctl status mysql.service 	# check the status of any services such as sql etc., 

$nmcli radio wifi [on/off]          # #turn on/off wifi & network manager comand line interface
$bluetoothctl          # turn on/off Bluetooth & bluetooth control panel 
 		$power [on/off] 
 		$discoverable [on/off] 
 		$devices 
 		$paired-devices 
 		$connect <device address>
 		$disconnect <device address>
 		exit
$ps 

#grep,awk,sed,curl
#grep 
$grep -H # to output filenames along with matching keywords. 
$grep -i # matches all keywords without checking case sensitivity. 
$grep -v # inverses the output.
$grep -[A/B/C] [numerical count] # gives out count of after/before/both respectively after matching keywords are found.
--------------------------------------------------------------
#terminal shortcuts
Ctrl+l -> clear terminal screen 
--------------------------------------------------------------
#howto?	 
#1.how to send an email ?   
	$sendmail <steja2396@gmail.com>           
	    |press Enter|
	    <add subject line, body etc.,> 	
	$Ctrl + D
#2.ubuntu shortcut to maximise and minimise the window 
	$Win + H #minimise the window
	$Win + up/down or side arrow keys # to maximize or place on half of the screens. 
#3.ubuntu shortcut to open terminal 
	$Ctrl + Alt + T