#create two diffrent sets with data
s1={1,2,1,"yag",47,5.2}
s2=set([1,2,1,"abc",42,4.4])
#print set item 
print(s1)
print(s2)
#add item
s1.add(5)
s2.add(3)
print(s1)
print(s2)
#remove item
s1.discard("yag")
s2.discard("abc")
print("after discard in set ",s1)
print("after discrad in set2",s2)
#union
print(s1|s2)
#intersection
s1.intersection(s2)
print(s1)
print(s2)
# #diference
print(s1-s2)
print(s2-s1)
print()
print(s1^s2)
#s1 is subset of a s2
print(s1>s2)
#s1 is superset of s2
print(s1<s2)