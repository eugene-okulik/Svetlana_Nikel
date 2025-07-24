class Flowers:
    def __init__(self, name, color, price, lifespan):
        self.name = name
        self.color = color
        self.price = price
        self.lifespan = lifespan

    def __repr__(self):
        return f'{self.name} {self.color}, стоит {self.price} рублей, срок жизни {self.lifespan} дней'


class Gortensia(Flowers):
    def __init__(self, color, price):
        super().__init__('Гортензия', color, price, 10)


class Giacint(Flowers):
    def __init__(self, color, price):
        super().__init__('Гиацинт', color, price, 8)


class Rosa(Flowers):
    def __init__(self, color, price):
        super().__init__('Роза', color, price, 5)


class Buket:
    def __init__(self):
        self.flowers = []

    def add_flowers(self, flowers):
        self.flowers.append(flowers)

    def total(self):
        total = 0
        for flower in self.flowers:
            total += flower.price
        return total

    def lifespan(self):
        total_days = 0
        for flower in self.flowers:
            total_days += flower.lifespan
        average = total_days / len(self.flowers)
        return round(average, 0)

    def color(self, color):
        found_flowers = []
        for flower in self.flowers:
            if flower.color == color:
                found_flowers.append(flower)
        return found_flowers

    def sort(self, sort_key = 'name'):
        if sort_key == 'color':
            self.flowers.sort(key=lambda flower: flower.color)
        elif sort_key == 'price':
            self.flowers.sort(key=lambda flower: flower.price)
        elif sort_key == 'lifespan':
            self.flowers.sort(key=lambda flower: flower.lifespan)
        else:
            self.flowers.sort(key=lambda flower: flower.name)



flower1 = Giacint('желтый', 700)
flower2 = Gortensia('белый', 1000)
flower3 = Rosa('красный', 500)
flower4 = Rosa('белый', 900)

new_buket = Buket()
new_buket.add_flowers(flower1)
new_buket.add_flowers(flower2)
new_buket.add_flowers(flower3)
new_buket.add_flowers(flower4)

print('Букет стоит', new_buket.total(), 'руб.')
print('Букет будет свеж', new_buket.lifespan(), 'дней')

white_flowers = new_buket.color('белый')
if white_flowers:
    print("Белый цветок в букете -", white_flowers[0].name)
else:
    print("В букете нет белых цветов")

new_buket.sort(sort_key='price')
print("Сортировка по цене:", ", ".join(f"{flower.name} цвет {flower.color} : {flower.price} рублей" for flower in new_buket.flowers))

new_buket.sort(sort_key='color')
print("Сортировка по цвету:", ", ".join(f"{flower.name} {flower.color} цвет" for flower in new_buket.flowers))

new_buket.sort(sort_key='name')
print("Сортировка по названию:", ", ".join(f"{flower.name}" for flower in new_buket.flowers))
