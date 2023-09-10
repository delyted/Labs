import random
import math
real=0;positive=0;simulations=1000000
for i in range(0,simulations):
       b=random.uniform(-1,1)
       c=random.uniform(-1,1)
       if (b-4*c)>=0:
              real+=1
              root1=((-b)+math.sqrt(b-4*c))/2
              root2=((-b)-math.sqrt(b-4*c))/2
              if (root1>0)and(root2>0):
                     positive+=1
print("Both are real:",real/(simulations/100),"%")
print("Both are positive",positive/(simulations/100),"%")