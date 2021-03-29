def field():	
	import os
	def clear(): os.system('clear')
	clear()
	def title(): 
		os.system('figlet -c Doc Maker | lolcat -p')
	title()
	print("\033[31m——————————————————V0.1—————————————————@oguh_65——————————————————————\033[0m")
	print(" ")
	print(" ")

	filename = input("\033[33mfile name\033[0m \033[31m>>>\033[0m ")
	fieldname = input("\033[33mfield name\033[0m \033[31m>>>\033[0m ")
	name = input("\033[33mname\033[0m \033[31m>>>\033[0m ")
	info = input("\033[33minfo\033[0m \033[31m>>>\033[0m ")
	name2 = input("\033[33mname\033[0m \033[31m>>>\033[0m ")
	info2 = input("\033[33minfo\033[0m \033[31m>>>\033[0m ")
	file = open(f"files/{filename}.txt", "a")
	file.write(f"\n{fieldname} : ")
	file.write(f"\n 	{name} : {info}")
	file.write(f"\n 	{name2} : {info2}")
	cont = input("\033[33mContinue ? (y/n) \033[0m")
	if cont == "y":
		name3 = input("\033[33mname\033[0m \033[31m>>>\033[0m ")
		info3 = input("\033[33minfo\033[0m \033[31m>>>\033[0m ")
		file.write(f"\n 	{name3} : {info3}")
		cont = input("\033[33mContinue ? (y/n) \033[0m")
		if cont == "y":
			name4 = input("\033[33mname\033[0m \033[31m>>>\033[0m ")
			info4 = input("\033[33minfo\033[0m \033[31m>>>\033[0m ")
			file.write(f"\n 	{name4} : {info4}")
		elif cont == "n":
			exit()
		else:
			cont = input("\033[33mError... Continue ? (y/n) \033[0m")
		if cont == "y":
			name3 = input("\033[33mname\033[0m \033[31m>>>\033[0m ")
			info3 = input("\033[33minfo\033[0m \033[31m>>>\033[0m ")
			file.write(f"\n 	{name3} : {info3}")
			cont = input("\033[33mContinue ? (y/n) \033[0m")
			if cont == "y":
				name4 = input("\033[33mname\033[0m \033[31m>>>\033[0m ")
				info4 = input("\033[33minfo\033[0m \033[31m>>>\033[0m ")
				file.write(f"\n 	{name4} : {info4}")
			else:
				return
		elif cont == "n":
			exit()
	elif cont == "n":
		exit()
	else:
		cont = input("\033[33mError... Continue ? (y/n) \033[0m")
		if cont == "y":
			name3 = input("\033[33mname\033[0m \033[31m>>>\033[0m ")
			info3 = input("\033[33minfo\033[0m \033[31m>>>\033[0m ")
			file.write(f"\n 	{name3} : {info3}")
			cont = input("\033[33mContinue ? (y/n) \033[0m")
			if cont == "y":
				name4 = input("\033[33mname\033[0m \033[31m>>>\033[0m ")
				info4 = input("\033[33minfo\033[0m \033[31m>>>\033[0m ")
				file.write(f"\n 	{name4} : {info4}")
			else:
				return
		elif cont == "n":
			exit()



	file.close()