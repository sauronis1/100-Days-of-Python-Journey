"""
def add(*args):
    print(args[3])
    result = 0
    for n in args:
        result += n
    return result

listek = [4, 3, 35, 2]

print(add(*listek))
print(add(4,3,22,1))
"""


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make="Audi", model="nevim")
print(my_car.make)