from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())
'''A classe datetime tem vários métodos que devolvem a data e hora atuais. Estes métodos são:

today() — devolve a data e hora locais atuais com o atributo tzinfo definido para None;
now() — devolve a data e hora local atuais, tal como o método today, a menos que lhe passemos o argumento opcional tz. O argumento deste método deve ser um objeto da subclasse tzinfo;
utcnow() — devolve a data e hora UTC atuais com o atributo tzinfo definido para None.'''