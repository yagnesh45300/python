a=input("enter string : ")
b=""
for i in a:
    b=i+b
if(b==a):
    print("entered string ",a ," is palindrome")
else:
    print("entered sting ",a," is not palindrome ")