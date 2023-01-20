file=input("enter file : ")
files=input("enter file : ")
data1=open(file,"r")
data2=open(files,"r")
f1=data1.read()
f2=data2.read()
f1=f1.replace("_"," ")
f2=f2.replace("_"," ")
len1=len(f1)
len2=len(f2)
Maxlen=max(len1,len2)
for i in range(Maxlen):
    if i < len1:
        print(f1[i],end=" ")
    if i < len2:
        print(f2[i],end=" ")    
print()