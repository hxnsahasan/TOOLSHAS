#!/bin/python

#module
import os, sys, time

#pembersih texs
def bersih():
    os.system("clear")

# Python 3.4.3. Using MacOS (Version 10.12.5)
# Username and Password...
# The programs purpose: A user must enter the correct username and password for a site called FaceSnap...
# The correct username is elmo and the correct password is blue.
print("                     ")
print("UNTUK USERNAME: hasan")
print("PASWORDNYA MASUKKAN YANG TADI YA BRE")
print("BUAT YANG MASIH BINGUNG CEK PW DI SINI BRO: https://ayobelajarbareng.com/lhtgRljV4Zfi")
print("                                     ")
userName = input("\n\nUsername: ") #Ask's the User for Username input
password = input("Password: ") # Ask's the user for their password


count = 0 # Create a variable, to ensure the user has limited attempts at entering their correct username and password
count += 1 # The user has already had one attempt above, therefore count has been incremented by 1 already.


while userName == userName and password == password: # The Input will always lead to this while loop, so we can see if their username and password is wrong or correct.


    if count == 3: # Counter, to make sure the user only gets a limited number (3)of attempts
        print("\nThree Username and Password Attempts used. Goodbye") # Lets the user know they have reached their limit
        break # Leave the Loop and the whole program


    elif userName == 'hasan' and password == 'WPjW_b4q4fCNDig': # The userName and password is equal to 'elmo' and 'blue', which is correct, they can enter FaceSnap!
        print("Welcome! ") # Welcomes the User, the username and password is correct
        break # Leave the loop and the whole program as the username and passowrd is correct


    elif userName != 'hasan' and password != 'WPjW_b4q4fCNDig': # The userName and password is NOT equal to 'elmo' and 'blue', the user cannot enter FaceSnap
        print("Your Username and Password is wrong!") # Lets the user know that the Username and password entered is wrong.
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # Increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet


    elif userName == 'hasan' and password != 'WPjW_b4q4fCNDig': # The userName is equal to 'elmo', but password is NOT equal to 'blue', the user cannot enter FaceSnap
        print("Your Password is wrong!") # Lets the user know that their password is wrong
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet


    elif userName != 'hasan' and password == 'WPjW_b4q4fCNDig': # The userName is NOT equal to 'elmo', however password is equal to 'blue', the user cannot enter FaceSnap
        print("Your Username is wrong!") # Lets the user know that their username is wrong
        userName = input("\n\nUsername: ") # Requests the user to have another attempt at entering their correct username
        password = input("Password: ") # Requests the user to have another attempt at entering their correct password
        count += 1 # Increments the count by 1
        continue # Continue, as the user hasn't managed to get their username and password correct yet
# tampilan
def menu():
  bersih()
  print("\033[1;33m")
  os.system("figlet HASAN")
  print("Author: HASAN")
  print("                                    ")
  print("\033[1;32m[\033[1;37m-\033[1;32m] \033[1;36mTools Created by HXNsA (Hasan)")
  print("                                 ")
  print("                                 ")
  print("\033[1;31m[\033[1;37m::\033[1;31m] \033[1;33mPilih Daftar Menu \033[1;31m[\033[1;37m::\033[1;31m]")
  print("                                    ")
  print("                            ╔═══════════════════════╗")
  print("                            ║ \033[1;33mPR \033[1;31m║    \033[1;37mPERKENALAN    \033[1;31m║")
  print("                            ╚═══════════════════════╝")
  print("                                        ║  ")
  print("                            ╔═══════════════════════╗")
  print("                            ║ \033[1;33mUP \033[1;31m║    \033[1;37mUPDATE        \033[1;31m║")
  print("                            ╚═══════════════════════╝")
  print("                                        ║")
  print("                                        ║")
  print("                                        ║")
  print("                   ╔════════════════════║═════════════════════╗")
  print("                   ║                    ║                     ║")
  print("                   v                    v                     v")
  print("                \033[1;33mSPAMING              \033[1;33mHACKING              \033[1;33m HACKING")
  print("        \033[1;31m ╔══════════════════╗ ╔════════════════════╗ ╔══════════════════╗")
  print("         ║ \033[1;33mS1 \033[1;31m║ \033[1;37mSPAM WA     \033[1;31m║ ║ \033[1;33mH1 \033[1;31m║ \033[1;37mHACK FB BRAYEN\033[1;31m║ ║ \033[1;33mH3 \033[1;31m║ \033[1;37mHACK IG     \033[1;31m║")
  print("         ║ \033[1;33mS2 \033[1;31m║ \033[1;37mSPAM CALL WA\033[1;31m║ ║ \033[1;33mH2 \033[1;31m║ \033[1;37mHACK FB WTHAT \033[1;31m║ ║ \033[1;33mH4 \033[1;31m║ \033[1;37mHACK HASAN  \033[1;31m║")
  print("         ╚══════════════════╝ ╚════════════════════╝ ╚══════════════════╝")
  print("                                  ")
  print("\033[1;31m[\033[1;37m-\033[1;31m] \033[1;33mPilih Opsi :")
  print("         ")
  print("\033[1;31m║")
  contoh = input("\033[1;31m╚═══> \033[1;33m")
  if contoh =="PR":
    kenal=input("siapa nama kamu: ")
    print("Hay "+ kenal)
    print("                                     ")
  if contoh =="UP":
    os.system("pkg update")
    os.system("pkg upgrade")
  if contoh =="S1":
    print("SEDANG DALAM PERBAIKAN")
    os.system(python hasan.py)
  if contoh =="S2":
    print("SEDANG DALAM PERBAIKAN")
    os.system(python hasan.py)
  if contoh =="H1":
    print("MENGINSTAL SCRIPT")
    print("                            ")
    os.system("pkg update && pkg upgrade")
    os.system("pkg install python")
    os.system("pkg install git")
    os.system("pip install stdiomask")
    os.system("pip install requests")
    os.system("pip install bs4")
    os.system("pip install requests")
    os.system("pip install rich")
    os.system("pip install mechanize")
    os.system("git clone https://github.com/BrayennnXD/Brayennn3.4")
    os.system("cd /storage/emulated/0/Brayennn3.4/")
    os.system("python BrayennnFB.py")
    print("                     ")
    print("SELESAI MENGINSTAL SCRIPT")
    print("KETIKAN $cd /storage/emulated/0/Brayennn3.4/ LALU ENTER")
    print("KETIKAN LAGI $python BrayennnFB.py")
    print("!!!KETIKAN LANGKAH DI ATAS TANPA TANPA TANDA $")
  if contoh =="H2":
    os.system("pkg update && pkg upgrade")
    os.system("pkg install python")
    os.system("pkg install git")
    os.system("pip install stdiomask")
    os.system("pip install requests")
    os.system("pip install bs4")
    os.system("pip install requests")
    os.system("pip install rich")
    os.system("pip install mechanize")
    os.system("git clone https://github.com/hxnsahasan/mbasic/")
    os.system("cd /storage/emulated/0/")
    os.system("git pull")
    os.system("python mbasic2.py")
    print("KETIKAN $cd /storage/emulated/0/ LALU ENTER")
    print("KETIKAN LAGI $python mbasic2.py")
    print("!!!KETIKAN LANGKAH DI ATAS TANPA TANPA TANDA $")
  if contoh =="H3":
    os.system("pkg update && pkg upgrade")
    os.system("pkg install python")
    os.system("pkg install git")
    os.system("pip install stdiomask")
    os.system("pip install requests")
    os.system("pip install bs4")
    os.system("pip install requests")
    os.system("pip install rich")
    os.system("pip install mechanize")
    os.system("git clone https://github.com/hxnsahasan/mbasic/")
    os.system("cd mvrk")
    os.system("git pull")
    os.system("python mvrk.py")
    print("SEDANG DALAM PERBAIKAN")
    os.system(python hasan.py)
  if contoh =="H4":
    os.system("pkg update && pkg upgrade")
    os.system("pkg install python")
    os.system("pkg install git")
    os.system("pip install stdiomask")
    os.system("pip install requests")
    os.system("pip install bs4")
    os.system("pip install requests")
    os.system("pip install rich")
    os.system("pip install mechanize")
    os.system("git clone https://github.com/hxnsahasan/hxnsav2")
    os.system("cd mbasic")
    os.system("git pull")
    os.system("python hxnsav2.py")
    print("SEDANG DALAM PERBAIKAN")
    os.system(python hasan.py)
menu ()


green= '\033[1;32m'
red= '\033[1;31m'
yellow= '\033[1;33m'
white= '\033[1;37m'
blue= '\033[1;34m'
purple= '\033[1;35m'
cyan= '\033[1;36m'
