my_dict =  {
    "tuple": ( 1, 2, 3, 4, 5 ), 
    "list": ["Амбросов И.А.", "Иванов А.А.", "Крылов И.И", "Красовская Д.О", "Тритонова О.Ю"],
    "dict": {
        "color": "green", "fruit": "orange",  
        "sky": "Blue", "flower": "chamomile", 
        "apple": "Red" }, 
    "set": {1.1, 2.2, 3.3, 4.4, 5.5}}


#добавление элемента в лист, удаление второго элемента из листа
my_dict["list"].append("Королев А.А.")
print(my_dict["list"])

poped = my_dict["list"].pop(1)
print(my_dict["list"])


#вывод последнего значения
print(my_dict["tuple"][-1])



#добавление элемента с ключом ('i am a tuple',) и значением, удаление любого значения
my_dict["dict"][("i am a tuple",)] = "And what have you achieved"
print(my_dict["dict"])

popped = my_dict["dict"].pop("fruit")
print(my_dict["dict"])


#добавление нового элемента в множество, удаление из множества
my_dict["set"].add(6.6)
poped = my_dict["set"].pop()
print(my_dict["set"])


print(my_dict)
