def Fibo(c):
    n=int(input("enter number to print fibonacci seiras : "))
    if n <=1:
         return n
    else:
            return Fibo(n-1)+ Fibo(n-2)
Fibo(c)