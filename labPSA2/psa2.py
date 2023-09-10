import random 
triangle=0;simulations=1000000
for i in range(0,simulations):
       x=random.uniform(0,1)
       y=random.uniform(0,1)
       if x>y:
              a=y
              b=x-y
              c=1-x
       else:
              a=x
              b=y-x
              c=1-y
       if (a+b>c)and(a+c>b)and(b+c>a):
              triangle+=1
print("Triangle:",(triangle/10000),"%")
