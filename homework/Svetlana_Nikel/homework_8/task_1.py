import random

def calc():
    salary = int(input("Какая у вас заработная плата?"))
    bonus = random.choice([True, False])
    if bonus:
        random_bonus = random.randint(0, 1000)
        total_salary = salary + random_bonus
    else:
        total_salary = salary
    print(f'{salary}, {bonus} - ${total_salary}')

calc()
