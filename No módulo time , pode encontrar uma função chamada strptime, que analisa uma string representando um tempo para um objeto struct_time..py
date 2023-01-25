from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
''No módulo time , pode encontrar uma função chamada strptime, que analisa
uma string representando um tempo para um objeto struct_time.
A sua utilização é análoga à do módulo strptime na classe datetime'''