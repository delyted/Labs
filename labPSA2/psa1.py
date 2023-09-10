import random
import matplotlib.pyplot as plt
simulations=1000000
x=[];y=[];z=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0,simulations):
       a=random.randint(1,6)+random.randint(1,6)+random.randint(1,6)
       z[a-3]+=1
for i in range(0,15):
       x.append(z[i])
for i in range(0,15):
       y.append(i+3)
plt.bar(y, x, width = 0.5, color = ['lightgreen', 'lightblue']);plt.show()