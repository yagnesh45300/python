file=input("enter file name : ")
f=open(file,"r")
data=f.read()#read inside dat in file
word=data.split()
line=data.split(".")
words=0
s=0
for i in word:
    words+=len(i)
for k in line:
    s=len(k)
avgw=words/len(word)
avgl=s/len(line)
print(avgw)
print(avgl)