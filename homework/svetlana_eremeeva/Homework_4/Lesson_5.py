# Задание_1 Распаковка списка

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

print(name, last_name, city, phone, country)


# Задание_2 Срез

text_a = "результат операции: 42"
text_b = "результат операции: 514"
text_c = "результат работы программы: 9"

number_a = int(text_a.split(":")[1].strip()) + 10
number_b = int(text_b.split(":")[1].strip()) + 10
number_c = int(text_c.split(":")[1].strip()) + 10

sum_result = number_a + number_b + number_c

print(sum_result)


# Задание_3 Список-Строка

students = ['Ivanov', 'Petrov', 'Sidorov']
students = " ".join(students)

subjects = ['math', 'biology', 'geography']
subjects = " ".join(subjects)

text = "study these subjects: "

print(students + text + subjects)
