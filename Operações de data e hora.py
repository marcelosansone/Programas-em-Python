from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)
'''Mais cedo ou mais tarde, terá de efetuar alguns cálculos sobre a data e hora.
Felizmente, há uma classe chamada timedelta no módulo datetime que foi criado
precisamente para esse fim.
Para criar um objeto timedelta , basta fazer a subtração nos objetos date ou datetime,
assim como fizemos no exemplo no editor. Execute-o.'''