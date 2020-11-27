class car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed


cars = car('red', 150)
print(cars.speed)


class CoffeShop:
    spec = 'espresso'

    def __init__(self, coffee_price):
        self.coffee_price = coffee_price

    # Instance method
    def make_coffee(self):
        print(f'Making {self.spec} coffee for ${self.coffee_price}')

    # static method
    @staticmethod
    def check_weather():
        print('Its Night')

    # Class method
    @classmethod
    def change_spec(cls, spec):
        cls.spec = spec
        print(f'Specialty changed to {spec}')


coffee = CoffeShop('5')
coffee.make_coffee()
CoffeShop.check_weather()
CoffeShop.change_spec('Java Chip')


def add_three(x):
    if x % 2 == 0:
        return True
    else:
        return False


print(add_three(5))

li = [1, 2, 3, 4, 5, 6, 7, 8]

c = [i for i in filter(add_three, li)]
print(c)
# => [2, 4, 6, 8]

li.reverse()
print(li, li[::-1])

s = 'string'
print(s[::-1])

li1 = [['a'], ['b'], ['c']]
li2 = li1
li1.append(['d'])
print(li2)

li3 = [['a'], ['b'], ['c']]
li4 = list(li3)
li3.append([4])
print(li4)

li3[0][0] = ['X']
print(li4)

import copy

li5 = [['a'], ['b'], ['c']]
li6 = copy.deepcopy(li5)
li5.append([4])
li5[0][0] = ['X']
print(li6)

s = 'A string with       white spaces'
print(" ".join(s.split()))

a = [1, 2, 3, 4, 5]
for i in a:
    if i < 3:
        continue
    print(i)

d = {'id':7, 'name':'Shiba', 'color':'brown', 'speed':'very slow'}
print(list(d.keys()))
print(list(d))