n=int(input("enter a number to checking is a perfect number : "))
sum=0
for i in range(1,n):
     if n%i==0:
        sum+=i
if n==sum:
    print("ENTERED NUMBER ",n," IS PERFECT NUMBER")
else:
  print("ENTERED NUMBER  ",n," IS NOT PERFECT NUMBER")