from collections import Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.

def count_1():

	students = [
  	{'first_name': 'Вася'},
  	{'first_name': 'Петя'},
  	{'first_name': 'Маша'},
  	{'first_name': 'Маша'},
  	{'first_name': 'Петя'},
	]

	a = dict(Counter([student['first_name'] for student in students]))
	for key,value in a.items():
		print (f'{key}: {value}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.

def count_2():

	students = [
  	{'first_name': 'Вася'},
  	{'first_name': 'Петя'},
  	{'first_name': 'Маша'},
  	{'first_name': 'Маша'},
  	{'first_name': 'Оля'},
	]

	counted_dict = dict(Counter([student['first_name'] for student in students]))
	max_names = max(counted_dict.values())
	for keys,values in counted_dict.items():
		if values == max_names:
			print(f'Самое частое имя среди укников: {keys}')

# Пример вывода:
# Самое частое имя среди учеников: Маша


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.

def count_3():
	
	school_students = [
  	[  # это – первый класс
    	{'first_name': 'Вася'},
    	{'first_name': 'Вася'},
  	],
  	[  # это – второй класс
    	{'first_name': 'Маша'},
    	{'first_name': 'Маша'},
    	{'first_name': 'Оля'},
  	]
	]
	
	for school_class in school_students:
		res = []
		for inner_cls in school_class:
			res.append(inner_cls['first_name'])
		a = dict(Counter(res).most_common())  
		print(f'Самое часто встречающеся имя в классе {school_students.index(school_class) + 1} - {max((a))}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.

def count_4():

	school = [
  	{'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  	{'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
	]	
	is_male = {
  	'Маша': False,
  	'Оля': False,
  	'Олег': True,
  	'Миша': True,
	}


	for school_class in school:
		boys = 0
		girls = 0
		for students in school_class['students']:
			if is_male[students['first_name']]:
				boys += 1
			else:
				girls += 1
		print(f"В классе {school_class['class']} {girls} девочки and {boys} мальчика.")
	
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.

def get_total_gender_students(school,is_male):
	"""Подготавливает словарь с количеством девочек и мальчиков в классах."""

	total_gender_students = {}
	for school_class in school:
		boys = 0
		girls = 0
		for students in school_class['students']:
			if is_male[students['first_name']]:
				boys += 1
			else:
				girls += 1
		total_gender_students[school_class['class']] = {'girls':girls, 'boys':boys}
	return total_gender_students

def print_max_in_class(total_gender_students,max_girls,max_boys):
	for k in total_gender_students:
		if total_gender_students[k]['girls'] == max_girls and total_gender_students[k]['boys'] == max_boys:
			print(f'Больше всего девочек в классе {k}')
			print(f'Больше всего мальчиков в классе {k}')
			break
		elif total_gender_students[k]['boys'] == max_boys:
			print(f'Больше всего мальчиков в классе {k}')
			continue
		elif total_gender_students[k]['girls'] == max_girls:
			print(f'Больше всего девочек в классе {k}')
			break

def count_5(school,is_male):	
	""" Выводит класс где больше всего девочек и класс где больше всего мальчиков. """

	total_gender_students = get_total_gender_students(school,is_male)
	max_girls = max([total_gender_students[k]['girls'] for k,v in total_gender_students.items()])
	max_boys = max([total_gender_students[k]['boys'] for k,v in total_gender_students.items()])
	print_max_in_class(total_gender_students,max_girls,max_boys)

school = [
{'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
{'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
{'class': '5b', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
{'class': '8a', 'students': [{'first_name': 'Олег'}, {'first_name': 'Дима'}, {'first_name': 'Руслан'}, {'first_name': 'Стас'}]},
{'class': '11a', 'students': [{'first_name': 'Наташа'}, {'first_name': 'Оля'}, {'first_name': 'Света'}, {'first_name': 'Юля'}]}
]

is_male = {
'Маша': False,
'Наташа': False,
'Света': False,
'Оля': False,
'Юля': False,
'Олег': True,
'Миша': True,
'Руслан': True,
'Стас': True,
'Дима': True,
	
}
		
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a


def main():

	print("*"*10)
	count_1()
	print("*"*10)
	count_2()
	print("*"*10)
	count_3()
	print("*"*10)
	count_4()
	print("*"*10)
	count_5(school,is_male)
	print("*"*10)
	

if __name__ == "__main__":

	main()