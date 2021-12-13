# Functions Are Objects Too
def my_func():
    print("My function was called")


my_func.descript = " A silly function"


def second_func():
    print("Second function was called")


second_func.descript = "One more silly function"

def another_func(func):
    print()
    print("Description ",end=" ")
    print(func.descript)
    print("The name: ",end= " ")
    print(func.__name__)
    print("The class: ",end=" ")
    print(func.__class__)
    print("Now calling function")
    func()
if __name__ == '__main__':
    funcs = [my_func, second_func]
    for f in funcs:
        another_func(f)