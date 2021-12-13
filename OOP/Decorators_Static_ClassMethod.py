from datetime import date


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def instance_method(self):
        print("This is an instance method")
        pass

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18
if __name__ == '__main__':
    person1 = Person("mayank",20)
    person2 = Person.fromBirthYear("mayank",1996)
    print(person1.age)
    print(person2.age)
    print(Person.isAdult(20))
    person3 = person2.fromBirthYear("thinh",1992)
    print(person3.name)
    print(person3,person1)
    print(person3.isAdult(100))