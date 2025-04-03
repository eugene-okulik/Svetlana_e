my_dict =  {"dict": {
        "color": "green", "fruit": "orange",  
        "sky": "Blue", "flower": "chamomile", 
        "apple": "Red" }}

#добавление элемента с ключом ('i am a tuple',) и значением, удаление любого значения
my_dict["dict"][("i am a tuple",)] = "And what have you achieved"
print(my_dict["dict"])

popped = my_dict["dict"].pop("fruit")
print(my_dict["dict"])
