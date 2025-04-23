# Задание_1 Распаковка списка

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

print(name, last_name, city, phone, country)

# Задание_2_срез

text_a = "результат операции: 42"
text_b = "результат операции: 514"
text_c = "результат работы программы: 9"

index_a = text_a.index(":") + 2
number_a = int(text_a[index_a:]) + 10

index_b = text_b.index(":") + 2
number_b = int(text_b[index_b:]) + 10

index_c = text_c.index(":") + 2
number_c = int(text_c[index_c:]) + 10

sum_result = number_a + number_b + number_c

print(sum_result)


# Задание_3 Список-Строка

students = ['Ivanov', 'Petrov', 'Sidorov']
students = " ".join(students)

subjects = ['math', 'biology', 'geography']
subjects = " ".join(subjects)

text = "study these subjects: "

print(students + text + subjects)
