# Задание_1 Распаковка списка

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

print(name, last_name, city, phone, country)


# Задание_2 Срез

text_a = "результат операции: 42"
text_b = "результат операции: 514"
text_c = "результат работы программы: 9"

print(text_a.index("42"))
print(text_b.index("514"))
print(text_c.index("9"))

number_1 = 20
number_1 += 10

number_2 = 20
number_2 += 10

number_3 = 20
number_3 += 10

sum = number_1 + number_2 + number_3

print(sum)


# Задание_3 Список-Строка

students = ['Ivanov', 'Petrov', 'Sidorov']
students = " ".join(students)

subjects = ['math', 'biology', 'geography']
subjects = " ".join(subjects)

text = "study these subjects: "

print(students + text + subjects)
