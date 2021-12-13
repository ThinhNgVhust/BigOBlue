# re-use
#       Object
#         |
#       Animal
#       /    \
#      /      \
#     Cat     Dog
# Dog,Cat -> Subclass
# Animal Subclass, Also Base class
# Constructor of subclasses always called to a constructor of parent class to initialize value
# for the attributes in the parent class, then it start assign value for its attributes.

class Animal(object):
    def __init__(self,name):
        self.name = name
        pass
    def eat(self,food):
        print("{0} is eating {1}".format(self.name,food))
class Dog(Animal):
    def fetch(self,thing):
        print("{0} goes after the {1}".format(self.name,thing))
if __name__ == '__main__':
    jack = Dog("ChiHuahua")
    jack.eat("Rice")
    print(jack)
    if isinstance(jack,Dog):
        print("Jack is Dog")
    if isinstance(jack,Animal):
        print("Jack is also an Animal")