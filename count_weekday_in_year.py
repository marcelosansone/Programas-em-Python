﻿import calendar


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        current_month = 1
        number_of_days = 0
        while (current_month <= 12):
            for data in self.monthdays2calendar(year, current_month):
                if data[weekday][0] != 0:
                    number_of_days = number_of_days + 1

            current_month = current_month + 1
        return number_of_days

my_calendar = MyCalendar()
number_of_days = my_calendar.count_weekday_in_year(2019, calendar.MONDAY)

print(number_of_days)
'''A sua tarefa é alargar a sua funcionalidade com um novo método chamado 
count_weekday_in_year, que toma como parâmetros um ano e um dia da semana e,
em seguida, devolve o número de ocorrências de um dia da semana específico no ano.'''