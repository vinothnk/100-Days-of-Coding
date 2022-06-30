def add(*args):
    for n in args:
        print(n)


add(5, 3, 7, 8)


def add(*args):
    total = 0
    for n in args:
        total += n
    print(total)
    return


add(1, 2, 3, 4, 5, 6, 7, 8, 9)


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs['add'])
    # print(kwargs['multiply'])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


# class Car():
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#
#
# my_car = Car(make='Nissan') # if model is not indicated, will have error message
# print(my_car.make)

class Car():
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')


my_car = Car(make='Nissan') # if use .get, parameter which has no value will be indicated as None
print(my_car.model)
