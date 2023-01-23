import calendar  

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")
'''O código exibe todos os dias de novembro de 2019.
Como o primeiro dia de novembro de 2019 foi uma sexta-feira, os dias seguintes também são
devolvidos para obter a semana completa: 10/28/2019 (segunda-feira)
10/29/2019 (terça-feira) 10/30/2019 (quarta-feira) 10/31/2019 (quinta-feira).
O último dia de novembro de 2019 foi um sábado, portanto, para manter a semana completa,
mais um dia é devolvido 12/01/2019 (sexta-feira).'''