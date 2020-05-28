"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def file_analyzer(file):

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        print (f'Результат анализа "{file}"')
        print ('Длина строки - ' + str(len(content)))
        print ('Количество слов - ' + str(len(content.split())))

    with open(file[-5])    


def main():

    file_analyzer('referat.txt')

if __name__ == "__main__":
    main()
