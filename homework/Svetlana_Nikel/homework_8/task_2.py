def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


count = 0
for number in fibonacci_generator():
    if count == 4:
        print(f"Пятое число Фибоначчи: {number}")
    elif count == 199:
        print(f"Двухсотое число Фибоначчи: {number}")
    elif count == 999:
        print(f"Тысячное число Фибоначчи: {number}")
    elif count == 99999:
        print(f"Стотысячное число Фибоначчи: {number}")
        break
    count += 1
