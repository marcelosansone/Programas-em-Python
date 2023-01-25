import calendar  

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")
''''Certamente notou no grande número de 0s devolvidos como resultado do código de exemplo. Estes são dias fora do intervalo
de meses especificado, que são adicionados para manter a semana completa.
Os quatro primeiros zeros representam 28/10/2019 (segunda-feira) 29/10/2019 (terça-feira)
30/10/2019 (quarta-feira) 31/10/2019 (quinta-feira).
Os restantes números são dias no mês, exceto o último valor de 0,
que substitui a data 01/12/2019 (domingo).
Existem quatro outros métodos semelhantes na classe Calendar que
diferem nos dados devolvidos:

itermonthdates2 — devolve dias sob a forma de tuples constituídas por um número de dia do mês e um número de dia da semana;
itermonthdates3 — devolve dias sob a forma de tuples constituídas por um número do ano, um do mês e um do dia do mês. Este método está disponível a partir da versão 3.7 do Python.
itermonthdates4 — devolve dias sob a forma de tuples constituídas por um número do ano, um do mês, um do dia do mês e um do dia da semana. Este método está disponível a partir da versão 3.7 do Python.'''