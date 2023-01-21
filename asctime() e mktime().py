import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))
'''A primeira das funções, chamada asctime, converte um objeto struct_time ou um tuple numa string. Note-se que a função familiar gmtime é usada para obter o objeto struct_time. Se não fornecer um argumento à função asctime , o tempo devolvido pela função localtime será usado.

A segunda função chamada mktime converte um objeto struct_time ou um tuple que expressa a hora local para o número de segundos desde a época Unix. No nosso exemplo, passamos-lhe um tuple, que consiste nos seguintes valores:

2019 => tm_year
11 => tm_mon
4 => tm_mday
14 => tm_hour
53 => tm_min
0 => tm_sec
0 => tm_wday
308 => tm_yday
0 => tm_isdst'''



