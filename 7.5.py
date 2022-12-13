y={"GUJRAT":"GANDHINAGAR","RAJSTHAN":"JAYPUR","MAHARASHRT":"MUMBAI","UTTARKHAND":"DEHARADUN","ASAM":"DISPUR","UTTER PRADESH":"LUKNOM","AADRAPRADESH":"AMARAVATI","JAMMU & KASHMIRT":"SRINAGAR","HIMACHALPRADESH":"SHIMLA","WEST BANGAL":"KOLKATTA","TRIPURA":"AGRATALA","TELNGANA":"HYEDRABAD","TAMIL NADU":"CHANNAI","SIKKIM":"GANGTOK","PUNJAB":"CHANDIGAHR","ODISHA":"BHUBNESWAR","NAGALAND":"KOHIMA","MIZORAM":"AIZAWL","MEGHALAY":"SRILLONG","MANIPUR":"IMPHAL"}
# n=len(y)
# print(n)
print("\nPLEASE ENTER IN UPPER CASE LATTERS")
for i in y:
        print("-----------------------------------------------------")
        print("CAPITAL OF",i)
        print("-----------------------------------------------------")
        m=input("enter answer : ")
        print("-----------------------------------------------------")
        if m==y[i]:
         print("ENTRED ANSWER ",m," IS CORRECT")
        else:
                print("ENTERED ANSWER ",m," IS WRONG")
print("-----------------------------------------------------")
print("THANK YOU!")
print("-----------------------------------------------------")
# for m in y[i]:
#         if m is not y[i]:
#                 print("correct answer")
# else:
#         print("wrong answer")
# print("THANK YOU!")
