import calendar  

c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)
''' é o método monthdays2calendar , que toma o ano e o mês, e, em seguida, devolve uma lista de semanas
num mês específico. Cada semana é um tuple composto por números do dia e números do dia
da semana. Veja o código no editor.'''