first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))


def operation(func):
    def wrapper(first, second, operation=None):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        else:
            operation = '/'

        return func(first, second, operation)

    return wrapper


@operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    

print(calc(first, second))
