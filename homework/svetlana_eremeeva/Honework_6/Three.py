text_a = "результат операции: 42"
text_b = "результат операции: 514"
text_c = "результат работы программы: 9"


def add_10(text):
    number = int(text.split(":")[1].strip())
    print(number + 10)


add_10(text_a)
add_10(text_b)
add_10(text_c)
