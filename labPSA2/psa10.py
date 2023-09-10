import random
simulations=2365;sum=0
for i in range(simulations):
       if random.randrange(1,21)==20:
              sum+=300
       elif random.randrange(1,51)==50:
              sum+=6
print("No subscription:",62365,"lei")
print("Subscription:",2680,"lei")
print("Without ticket:",sum-400,"lei")