def calc():
    amt=int(input("enter amount of the loan : ")) #amount
    year=int(input("enter year : "))#year
    rate=float(input("enter intort rate(%) : "))
    ti=(amt*year)/rate #total intrest
    tpa=amt+ti #total page amount
    emi=tpa/(12*year)
    print(tpa)
    print(emi)
calc()