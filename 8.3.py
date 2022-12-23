def Fibo(n):
    if (n <=1):
         return n
    else:
          return (Fibo(n-1) + Fibo(n-2))
            
n=int(input("enter number to print fibonacci seiras : "))
Fibo(n)
for i in range(n):
     print(Fibo(i))