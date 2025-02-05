num = [50, 42]
ar_average = sum(num) / len(num)
geom_average = (num[0] * num[1]) ** (1 / len(num))
print(f'Среднее арифметическое чисел {num} равно {ar_average}')
print(f'Среднее геометрическое чисел {num} равно {geom_average}')
