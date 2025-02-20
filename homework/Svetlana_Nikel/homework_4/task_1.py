my_dict = {
    'tuple': ('one', 'two', 'three', 'four', 'five'),
    'list': [1, 2, 3, 4, 5],
    'dict': {
        'name_1': 'Sofia',
        'name_2': 'Alex',
        'name_3': 'Anna',
        'name_4': 'Max',
        'name_5': 'Mat'
    },
    'set': {1.5, 1.8, 2.0, 7.9, 9.3}
}
print(my_dict['tuple'][-1])  # tuple - выведите на экран последний элемент
my_dict['list'].append(6)  # list - добавьте в конец списка еще один элемент
my_dict['list'].pop(1)  # list - удалите второй элемент списка
my_dict['dict']['(i am a tuple, )'] = 'new_value'  # dict - добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict['dict'].pop('name_3')  # dict - удалите какой-нибудь элемент
my_dict['set'].add(10.15)  # set - добавьте новый элемент в множество
my_dict['set'].discard(2.0)  # set - удалите элемент из множества
print(my_dict)
