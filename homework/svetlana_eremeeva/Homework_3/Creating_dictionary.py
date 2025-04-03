my_dict = {
    "tuple": (1, 2, 3, 4, 5),
    "list": ["Амбросов И.А.", "Иванов А.А.", "Крылов И.И", "Красовская Д.О", "Тритонова О.Ю"],
    "dict": {
        "color": "green",
        "fruit": "orange",
        "sky": "blue",
        "sky": "cloud",
        "flower": "chamomile",
        "apple": "Red"
    },
    "set": {1.1, 2.2, 3.3, 4.4, 5.5}
}

# Вывод последнего элемента из кортежа
print(my_dict["tuple"][-1])

# Добавление нового элемента в список
my_dict["list"].append("Королев А.А.")
print(my_dict["list"])

# Удаление ключа "fruit" из словаря
popped = my_dict["dict"].pop("fruit")
print(my_dict["dict"])

# Добавление нового элемента в множество
my_dict["set"].add(6.6)

# Удаление любого элемента из множества
removed = my_dict["set"].pop()
print(my_dict["set"])

#вывод всего словаря
print(my_dict)
