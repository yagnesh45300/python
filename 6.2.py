from re import I


l=[(5,-6,0,6,-1,0,9)]
print([a for j,a in enumerate(l) if a>0])
print([a for j,a in enumerate(l) if a<0])
print([a for j,a in enumerate(l) if a==0])
