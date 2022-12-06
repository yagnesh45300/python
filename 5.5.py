a=1
b=3
ans=0
n=0
while b<=99:
    ans=a/b
    a=b
    b=b+2
    n+=ans
print(n)
# for i in range(1,99):
#     ans=a/b
#     a+=2
#     b+=2
#     print(ans)
#     n+=ans
    