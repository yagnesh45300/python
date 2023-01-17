def gcd(m,n):
   if m == n:
      return m
   elif m < n:
      return gcd(n, m)
   else:
      return gcd(n, m - n)

m=int(input("enter Numner"))
n=int(input("enter Numner"))
print(gcd(m, n))