from datetime import datetime, timedelta


"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    
    print((datetime.today() - timedelta(days=1)).strftime('%d-%m-%Y Today'))
    print(datetime.today().strftime('%d-%m-%Y Yesterday'))
    print((datetime.today() - timedelta(days=30)).strftime('%d-%m-%Y 30 days ago'))
    


def str_2_datetime(date_string):

    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
