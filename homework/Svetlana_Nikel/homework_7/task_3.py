result_1 = 'результат операции: 42'
result_2 = 'результат операции: 54'
result_3 = 'результат работы программы: 209'
result_4 = 'результат: 2'

def calc(result):
    print(int(result.split()[-1]) + 10)


calc(result_1)
calc(result_2)
calc(result_3)
calc(result_4)
