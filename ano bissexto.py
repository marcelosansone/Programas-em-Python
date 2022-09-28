year = int(input("Enter a year: "))
if year < 1582:
    print ("Este ano não faz parte do calendário Gregoriano!")
elif year % 4 != 0:
 print ("o ano", year, "é um ano comum")
elif year % 100 != 0:
    print ("o ano", year, "é um ano bissexto")
elif year % 400 != 0:
    print ("o ano", year, "é um ano comum")
else:
    print ("o ano", year, "é um ano bissexto")
