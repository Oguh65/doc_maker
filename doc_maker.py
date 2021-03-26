#1/usr/bin/python3
import os
import create
import edit
def clear(): os.system('clear')
clear()
def title(): 
	os.system('figlet -c Doc Maker | lolcat -p')
title()
print("\033[31m—————————————————————V0.1—————————————————@oguh_65————————————————————————\033[0m")
print(" ")
print(" ")

print("\033[33mchose an option : \033[0m")
print(" ")
print("\033[33m1.create new file 		2.edit file\033[0m")
print("\n\033[33m00.exit\033[0m")
print(" ")
open = input("\033[31m>>> \033[0m")
if open == "1":
	clear()
	create.create()

elif open == "2":
	clear()
	edit.edit()
elif open == "00":
	print("\033[33mthanks for use doc_maker !\033[0m")
	exit()