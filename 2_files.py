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
    """Анализируем полученный переданный в функцию файл и создаём результат с новым именем."""

    with open(file, 'r', encoding='utf-8') as f:

        content = f.read()
        content_str_len = len(content)
        content_words_len = len(content.split())
        result = f'Результат анализа "{file}."\nДлина строки - {content_str_len} символов.\nКоличество слов - {content_words_len}.'

        new_file_name = str(file.split('.')[-2]) + '2.txt'
        with open(new_file_name, 'w', encoding='utf-8') as f:
            f.write(result)
        
def main():

    file_analyzer('referat.txt')

if __name__ == "__main__":
    main()
