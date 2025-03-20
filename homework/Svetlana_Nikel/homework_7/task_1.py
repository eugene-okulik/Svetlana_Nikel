a = 58
while True:
    user_input = int(input('Угадай число'))
    if user_input == a:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('Попробуйте снова')
