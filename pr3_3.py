print("simple int")
p=float(input("enter your principle : "))
r=float(input("enter your rate : "))
t=float(input("enter your time : "))

simple=float(p*r*t)/100
print(simple)

print("compuond int")
p=float(input("enter your principle : "))
r=float(input("enter your rate : "))
t=float(input("enter your time : "))
n=float(input("enter your number of time  : "))
c=float(p*(1+(r/(100*n)))*(n*t))
print(c)