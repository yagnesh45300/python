def dup(y,y1):
    for num in y:
	            if num not in y1:
		             y1.append(num)
y=[1,2,3,4,5,6,1,5,2,3]
y1=[]
print("list is : ",y)
print("second list is empty : ",y1)
dup(y,y1)
print("duplicate value is eliminating ")
print(y1)