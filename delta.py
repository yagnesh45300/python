import cmath 

a=int(input("enter value of a : "))
b=int(input("enter value of b : "))
c=int(input("enter value of c : "))
de=float((b**2)-4*(a*c))
print(de)
real1=(-b+cmath.sqrt(de)/(2*a))
real2=(-b-cmath.sqrt(de)/(2*a))
print(real1)
print(real2)    
