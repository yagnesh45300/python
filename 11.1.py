# create text file and write string
f=open("11.txt","w")
f.write("first line when is created\n")
f.close()
# read the entire file
f=open("11.txt","r")
print(f.read())
f.close()
# write a string to a file
f=open("11.txt","w")
f.write("first sting added in file")
f.close() 
# write list of string in file
f=open("11.txt","r+")

f.write("i am a student\n")
f.write("i am studing diploma\n")
print(f.read())
f.close()
# read line by line
f=open("11.txt","r")
f.readline()
f.close()
# count line & word in file
f=open("11.txt")
line,word=0,0
for i in f:
    line+=1
    word+=len(i.split())
print("line in this file is : ",line)
print("word in this file is : ",word)