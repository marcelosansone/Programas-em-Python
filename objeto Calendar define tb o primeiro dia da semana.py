import calendar  

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")
'''O exemplo de código usa o método de classe Calendar chamado iterweekdays,
que devolve um iterador para os números dos dias da semana.
O primeiro valor devolvido é sempre igual ao valor da propriedade firstweekday .
Visto no nosso exemplo o primeiro valor devolvido ser 6, isso significa que
a semana começa num domingo.'''

