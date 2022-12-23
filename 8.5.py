def gcd(a,b):
   if a == b:
      return a
   elif a < b:
      return gcd(b, a)
   else:
      return gcd(b, a - b)

a=int(input("enter Number"))
b=int(input("enter Number"))
print(gcd(a, b))