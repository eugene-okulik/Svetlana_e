my_dict = {
    "tuple": (1, 2, 3, 4, 5),
    "list": ["Амбросов И.А.", "Иванов А.А.", "Крылов И.И", "Красовская Д.О", "Тритонова О.Ю"],
    "dict": {
        "color": "green",
        "fruit": "orange",
        "sky": "blue",
        "flower": "chamomile",
        "apple": "Red"
    },
    "set": {1.1, 2.2, 3.3, 4.4, 5.5}
}

# "tuple"
# Вывод последнего элемента из кортежа
print(my_dict["tuple"][-1])

# "list"
# Добавление нового элемента в список
my_dict["list"].append("Королев А.А.")
print(my_dict["list"])

# удалите второй элемент списка
poped = my_dict["list"].pop(1)
print(my_dict["list"])

# "dict"
# Удаление ключа "fruit" из словаря
popped = my_dict["dict"].pop("fruit")
print(my_dict["dict"])

# Добавление элемента с ключом и любым значением:
my_dict["dict"][("i am a tuple",)] = "And what have you achieved"
print(my_dict["dict"])

# set
# Добавление нового элемента в множество
my_dict["set"].add(6.6)

# Удаление любого элемента из множества
removed = my_dict["set"].pop()
print(my_dict["set"])

# вывод всего словаря
print(my_dict)
