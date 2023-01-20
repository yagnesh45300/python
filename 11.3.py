f=open("11.txt")
num=0
f.readline()
for i in f:
    for a in i:
        if a.isdigit()==True:
            num+=1
            print("number  :  ",a)
print("total number : ",num)
f.close()
