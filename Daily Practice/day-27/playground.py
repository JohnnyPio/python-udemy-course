# def add(*args):
#     print(args[0])
#     return sum(args)
#
#
# print(add(1, 2, 3, 4))

def calculate(n, **kwargs):
    print(kwargs)
    # for key in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(model="GT-R")
print(my_car.make)
