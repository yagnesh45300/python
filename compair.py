a=int(input("enter a: "))
b=int(input("enetr b: "))
c=int(input("enter c: "))
z=(a if (a>b and a>c) else b if(b>a and b>c) else c)
print(z)
