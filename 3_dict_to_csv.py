import csv

"""
Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
user_data = [{'name': 'Stepan', 'age': 24, 'job': 'Python developer'}, {'name': 'Igor', 'age': 36, 'job': 'Lawyer'},
            {'name': 'Svetlana', 'age': 22, 'job': 'Dentist'}, {'name': 'Ali', 'age': 54, 'job': 'Vet'}]


def get_csv(data):
    """ Converting user dict to .cvs file """
    
    with open('people_info.cvs', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=':')
        writer.writeheader()
        for people in data:
            writer.writerow(people)



def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    get_csv(user_data)

if __name__ == "__main__":
    main()
