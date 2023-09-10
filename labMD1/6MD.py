import random
from PIL import Image, ImageDraw 

im = Image.new('RGB', (1000, 1000), (128, 128, 128)) 
draw = ImageDraw.Draw(im)

def rule_110(x,y,z):
    if x==0 and y==0 and z==0:
        return 0
    if x==0 and y==0 and z==1:
        return 1
    if x==0 and y==1 and z==0:
        return 1
    if x==0 and y==1 and z==1:
        return 1
    if x==1 and y==0 and z==0:
        return 0
    if x==1 and y==0 and z==1:
        return 1
    if x==1 and y==1 and z==0:
        return 1
    if x==1 and y==1 and z==1:
        return 0

a=[]
b=[]
for i in range(200):
    a.append(random.randint(0,1))

print(*a)
s=0;p=0;size=5
for i in range(200):
    a.insert(0,0)
    a.append(0)
    for j in range(1,len(a)-1):
        b.append(rule_110(a[j-1],a[j],a[j+1]))
    print(*b)
    a=b.copy()
    for i in range(len(a)): 
        if a[i] == 0: 
            draw.rectangle((p, s, p+size, s+size), fill=(0, 0, 0), outline=(255, 255, 255)) 
        else: 
            draw.rectangle((p, s, p+size, s+size), fill=(255, 255, 255), outline=(255, 255, 255)) 
        p+=size
    p = 0 
    b.clear()
    im.save('pillow_imagedraw.jpg', quality=95) 
    s += size