while True:
    user_input = input('Угадайте число от 1 до 100: ')

    if int(user_input) == 50:
        print('Поздравляю! Вы угадали! 🎉')
        break
    elif int(user_input) > 50:
        print('Попробуйте снова')
        print(user_input)
    elif int(user_input) < 50:
        print('Попробуйте снова')
        print(user_input)
