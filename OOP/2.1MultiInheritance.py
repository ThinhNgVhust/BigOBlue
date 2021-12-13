class Mother:
    def __init__(self):
        print("Mother Instance Constructor")
        pass


class Father:
    def __init__(self):
        print("Father Instance Constructor")
        pass


class Child(Mother, Father):
    pass


child = Child()
print(isinstance(child, Mother))
print(isinstance(child, Father))
print(isinstance(child, Child))
# print(issubclass(child,Child)) -> Wrong! child is a instance of class (Object), not a class
print(Child.mro())  # method resolution order
