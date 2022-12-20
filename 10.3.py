import datetime
da=input(" enter date ")
mo=input(" enter month ")
yy=input(" enter year ")
c=datetime.date(yy,mo,da)
print(c)
fm=datetime.date.strftime(c,("%m-%d-%y"))
print(fm)