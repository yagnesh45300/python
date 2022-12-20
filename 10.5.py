def yagnesh(h):
    rgb=[]
    for i in (0,2,4):
        de=int(h[i:i+2],16)
        rgb.append(de)
    return tuple(rgb)
print(yagnesh('FF6347'))