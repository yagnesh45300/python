import string
def main():
    f=input("enter file name : ")
    inf=open(f,'r')
    f1=input("enter file name : ")
    opf=open(f1,'w')
    for i in inf:
        word=i.split(".")
        for k in word:
            c=0
            for j in k:
                if not j in string.punctuation:
                    c+=1
            if c==4:
                if "." in word:
                    word="****"
                elif "!" in word:
                    word="****"
                else:
                    word="****"
        print(word + " ",f =opf,end=" ")
    inf.close()
    opf.close()
if __name__ =="__main__":
    main()