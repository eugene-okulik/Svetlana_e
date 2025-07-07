secret_number = 50  # загадываем число

while True:
    user_input = input('Угадайте число от 1 до 100: ')

    try:
        guess = int(user_input)
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    if guess == secret_number:
        print('Поздравляю! Вы угадали! 🎉')
        break
    elif guess > secret_number:
        print('Попробуйте меньшее число')
    else:
        print('Попробуйте большее число')
