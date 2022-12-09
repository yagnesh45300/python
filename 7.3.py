stu={"name":"yagnesh","roll":47,"dept":"com","add":"surat"}
print(stu)
stu["class"]="sy"
print(stu)
del stu["class"]
print(stu)
for i in stu:
    print(i)
print("iterate")
for i in stu:
    print(i)
for i in stu:
    print(stu[i])
for i in stu.values():
     print(i)
for i in stu.items():
    print(i)
ft={"name":"jaimain","dept":"com","place":"teacher"}
fs={"salary":10000,"sub":"python"}
ft.update(fs)
print(ft)