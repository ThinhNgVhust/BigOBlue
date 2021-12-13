class A(object):
    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C(A):
    def dothis(self):
        print("doing this in C")


class D(B, C):
    pass


if __name__ == '__main__':
    d_instance = D()
    d_instance.dothis()
    print(D.mro())