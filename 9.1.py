import random
c=random.randint(0,2)
a = "secicer"
b = "rock"
c1 = "paper"
print("0 = secicer 1 = rock 2 = paper")
u=int(input("enter your choice : "))
if c==u:
    print("it is tia")
elif c==0 and u==1:
    print(b,"beats",a,"you win")
elif c==0 and u==2:
    print(a,"beats",c1,"you lose")
elif c==1 and u==0:
    print(b,"beats",a,"you lose")
elif c==1 and u==2:
    print(a,"beats",c1,"you lose")
elif c==2 and u==0:
    print(a,"beats",c1,"you win")
elif c==2 and u==1:
    print(b,"beats",c1,"you win")
else:
    print("Invalid choice:")
print(c)