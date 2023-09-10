import random
simulations=100000
s=0
for i in range(0,simulations):
       x=random.uniform(0,1)
       y=-1
       while(y<=x):
              s+=1
              y=random.uniform(0,1)
print("The fair entrance fee is ",round(s/simulations)-1,"$")