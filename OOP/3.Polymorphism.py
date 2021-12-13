# MANY SHAPES

class Animal(object):
    def __init__(self, name):
        self.name = name
        pass

    def eat(self, food):
        print("{0} eat {1}".format(self.name, food))
        pass

    def show(self):
        print("Animal show")


class Dog(Animal):
    def __init__(self, name):  # Overriding method: call init of Dog class only, not calling Animal Init
        super().__init__(name)

    def fetch(self, thing):
        print("{0} goes after the {1}".format(self.name, thing))
        pass

    def show(self):
        print("Dog show")
        pass


class Cat(Animal):
    def show(self):
        print("Cat show")


if __name__ == '__main__':
    for a in [Animal("A"), Dog("Buggie"), Cat("Tom")]:
        a.show()
