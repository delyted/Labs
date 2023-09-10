import random
import matplotlib.pyplot as plt
simulations=100000;sum=0;game=[];money=[]
for i in range(0,simulations):
       sum=sum-0.25
       alfa=random.uniform(0,32)
       beta=random.uniform(0,32)
       alfa=alfa%4
       beta=beta%4
       if (alfa>=1)and(alfa<=3)and(beta>=1)and(beta<=3):
              sum=sum+1
       game.append(i)
       money.append(sum)
plt.plot(game, money, linewidth = 0.4);plt.show()
print("The sum: ",sum,"lei")