class MyClass(object):
    count = 0  # Class attribute

    def __init__(self, num=0):  # Constructor
        self.__age = num  # private information, also Instance Attribute
        MyClass.count += 1

    def setAge(self, num):
        self.__age = num

    def getAge(self):
        return self.__age

    def printInfor(self):
        print(self)


if __name__ == '__main__':
    zack = MyClass(11)
    queen = MyClass(12)
    king = MyClass(13)
    for obj in [zack, queen, king]:
        print(obj)
        print(obj.getAge())
        print(obj.count)
