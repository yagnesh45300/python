def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def seq(a):
    return a**2
def module(a,b):
    return a%b
def fact(a):
    factorial=1
    if a < 0:
        print("Sorry")
    elif a == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,a+ 1):
            factorial = factorial*i
        return factorial
        