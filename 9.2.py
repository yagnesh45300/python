import math
def mean(num):
    return sum(num)/len(num)
def sd(num):
    n= len(num)
    mean_value=mean(num)
    sqd=sum((x-mean_value)**2 for x in num)
    return math.sqrt(sqd/(n-1))
num=[10,20,30,40,55,96]
print(mean(num))        
print(sd(num))

