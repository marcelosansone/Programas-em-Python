from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)
'''É claro que também pode criar um objeto por si próprio.
Para este efeito, vamos conhecer os argumentos aceites pelo construtor da classe,
que são: days, seconds, microseconds, milliseconds, minutes, hours, e weeks.
Cada um deles é opcional e o padrão é 0.'''