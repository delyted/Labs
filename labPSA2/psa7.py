import random
import matplotlib.pyplot as plt
experiment=[];result=[]
for i in range(0,1000):
       h=0
       experiment.append(i)
       for j in range(0,100):
              if random.randint(1,2)==1:
                     h+=1
       result.append(h)
plt.plot(experiment,result,linewidth = 0.4);plt.show()