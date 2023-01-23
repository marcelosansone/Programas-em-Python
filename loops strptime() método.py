from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
''Ao contrário do método strftime , este cria um objeto datetime a partir
de uma string representando uma data e hora.
O método strptime requer que se especifique o formato em que se guardou 
a data e hora. Vejamo-lo num exemplo. Dê uma vista de olhos ao código no editor.'''