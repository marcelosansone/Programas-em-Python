year = int(input("Enter a year: "))

if year < 1582:
	print("Não pertence ao calendário Gregoriano")
else:
	if year % 4 != 0:
		print("Ano normal")
	elif year % 100 != 0:
		print("Ano bissexto")
	elif year % 400 != 0:
		print("Ano comum")
	else:
		print("Ano bissexto")
