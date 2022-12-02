l=[1,12,3,4,5,1]
l1=[]
for num in l:
    if num not in l1:
        l1.append(num) 
print(l)
print(l1)
s=set(l)
print(s)