from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)
'''Note que tanto os dias como as horas foram multiplicados por 2.
Outra operação interessante usando o objeto timedelta é a adição.
No exemplo, adicionamos o objeto timedelta à data e datetime objetos.
Como resultado destas operações, recebemos data e objetos datetime~
aumentados em dias e horas armazenados no timedelta objeto.
A operação de multiplicação apresentada permite-lhe aumentar rapidamente
o valor do objeto timedelta , enquanto a multiplicação pode também ajudá-lo
a obter uma data no futuro.
Claro, as classes timedelta, date, e datetime suportam muitas mais operações.
Encorajamo-lo a familiarizar-se com elas na documentação.'''


