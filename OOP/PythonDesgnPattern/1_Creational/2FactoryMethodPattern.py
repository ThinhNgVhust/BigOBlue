from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def show_infor(self):
        pass


class ProductA(Product):
    def show_infor(self):
        print("A type is created")
        pass


class ProductB(Product):
    def show_infor(self):
        print("B type is created")


class ProductC(Product):
    def show_infor(self):
        print("C type is created")


class Creator(ABC):#Abstract class

    def someOperation(self, knife_type):
        knife = self.factoryMethod(knife_type)
        knife.show_infor()
        return knife

    @abstractmethod
    def factoryMethod(self, knife_type):
        pass


class ConcreteCreator(Creator):
    def factoryMethod(self, knife_type):  # <--------------Here! The heart of Factory Method Pattern
        if knife_type == "A":
            return ProductA()
        elif knife_type == "B":
            return ProductB()
        elif knife_type == "C":
            return ProductC()


if __name__ == '__main__':
    print("Factory Method")
    bugget = ConcreteCreator()
    arr = [bugget.someOperation("A"), bugget.someOperation("B"), bugget.someOperation("C")]