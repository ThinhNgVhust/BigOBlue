from abc import ABC, abstractmethod


# Step1:Design the interface
class IAccount(ABC):
    def __init__(self,amount):
        self.amount = amount
    @abstractmethod
    def deposite(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def transfer(self, amount):
        pass

    @abstractmethod
    def getAccountNumber(self):
        pass


# Step2: Implement the interface

class Chequing(IAccount):
    def deposite(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def transfer(self, amount):
        pass

    def getAccountNumber(self):
        pass


class Saving(IAccount):
    def deposite(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def transfer(self, amount):
        pass

    def getAccountNumber(self):
        pass


class Investment(IAccount):
    def deposite(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def transfer(self, amount):
        pass

    def getAccountNumber(self):
        pass


# Step3: Create the facade class and wrap the classes that implement the interface
class BankServices:
    def __init__(self):
        self.bankAccounts = {}  # int,IAccount
        self.count = 0
        pass

    def create_new_account(self, type, amount):
        new_acc = None
        if type == "1":
            new_acc == Chequing(amount)
        elif type == "2":
            new_acc == Saving(amount)
        elif type == "3":
            new_acc == Investment(amount)
        if new_acc is not None:
            print("Create new account ok!")
            self.count += 1
            self.bankAccounts[self.count] = new_acc
        return new_acc.getAccountNumber()

    def tranfer(self, fro, to, amount):
        from_acc = self.bankAccounts[fro]
        to_acc = self.bankAccounts[to]
        fro.tranfer(to_acc, amount)  # object implement it self
        pass


class Customer:
    def __init__(self):
        self.myBanks = BankServices()
        pass


if __name__ == '__main__':
    me = Customer()
    me.myBanks.create_new_account("1", 100)
    me.myBanks.create_new_account("2", 200)
    me.myBanks.tranfer(fro=1, to=2, amount=100)
