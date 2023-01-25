from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53)

print("Datetime:", dt)
print("Date:", dt.date())
print("Time:", dt.time())
'''O exemplo cria um objeto datetime representando 4 de novembro de 2019 às 14:53:00. Todos os parâmetros passados para o construtor vão para atributos de classe só de leitura. São ano, mês, dia, hora, minuto, segundo, microssegundo, tzinfoe fold.

O exemplo mostra dois métodos que devolvem dois objetos diferentes. O método chamado date devolve o objeto date com o ano, mês e dia dados, enquanto o método chamado time devolve o objeto time com a hora e o minuto dados.

'''