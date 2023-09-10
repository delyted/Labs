import random
triangle=0;simulations=1000000
for i in range(0,simulations):
       x=random.uniform(0,1)
       if x<0.5:
              x=1-x
       y=random.uniform(0,x)
       a=y
       b=x-y
       c=1-x
       if (a+b>c)and(b+c>a)and(a+c>b):
              triangle+=1
print("Triangle:",(triangle/10000),"%")