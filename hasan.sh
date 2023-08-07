#!/bin/bash

clear

#logo

figlet LOGIN TOOLS
echo "by HXNsAHasan"
echo "             "
echo "             "
echo "CEK PASSWORDNYA DI SINI YA BRO: https://ayobelajarbareng.com/lhtgRljV4Zfi"
echo "           "
echo "           "

#pasword
	read -p "[•]Masukan Username : " username
	read -p "[•]Masukan Pasword : " pass

echo $pass $username
sleep 1
echo
if [ $pass = "WPjW_b4q4fCNDig" ]
	then
	echo [•] "Password Benar"
	sleep 2
clear
	else
	echo [•]" Password Salah"
	echo [•]"Ulangi Lagi "
	sleep 3
	sh hasan.sh
	sleep 4
fi
sleep 2
        echo "CIAH BELUM SUBSCRIBE"
        read -p "[•]Subscribe dulu ya $username : " subs

echo "Thanks" $username
sleep 3
echo
        sleep
        xdg-open https://youtube.com/@BERO_Hasan
        sleep 4
	pkg update && pkg upgrade
        apt update && apt upgrade
        pkg install git
        pkg install python-pip
        pip install lolcat
        rm -rf TOOLSHAS
        git clone https://github.com/hxnsahasan/TOOLSHAS
        cd TOOLSHAS
        python hasan.py
        sleep 5
        echo "ketikan cd /storage/emulated/0/TOOLSHAS/"
	echo "lalu ketikan lagi python hasan.py'
