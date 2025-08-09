import random


bonus = random.choice([True, False])


salary = int(input("What is your salary? "))

# рещила сделать прибавку в процентах так как ткой вариант кажется наиболее логичный в контексте прибавки к зарплате бонуса
if bonus:
    percent = random.randint(10, 30)
    salary += salary * percent // 100
    print(f"Бонус {percent}%")
else:
    print("Бонуса нет")

# Вывод результата
print(f"${salary}")
