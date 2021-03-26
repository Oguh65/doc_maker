def edit():
	import os
	import editall
	import newfield
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
	print("\033[33m1.create new field 		2.edit all\033[0m")
	print("\n\033[33m00.exit\033[0m")
	print(" ")
	open = input("\033[31m>>> \033[0m")
	if open == "1":
		clear()
		newfield.field()

	elif open == "2":
		clear()
		editall.editall()

	elif open == "00":
		print("\033[33mthanks for use doc_maker !\033[0m")
		exit()