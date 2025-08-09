def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


targets = [5, 200, 1000, 100000]  # позиции, которые нужны

for index, num in enumerate(fib_generator(), start=1):
    if index in targets:
        print(f"{index}-е число Фибоначчи: {num}")
    if index == max(targets):
        break
