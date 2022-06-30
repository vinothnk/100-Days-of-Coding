class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

foo = (1, 2)
MyClass(*foo)