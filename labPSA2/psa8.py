import random
def sort():
    sort=list(range(10))
    random.shuffle(sort)
    return sort

def probability():
    a1=sort()
    a2=sort()
    a1.insert(0, a1[len(a1)-1])
    a1.append(a1[1])
    a2.insert(0, a2[len(a2)-1])
    a2.append(a2[1])
    for i in range(1, len(a1)-1):
        for j in range(1, len(a2)-1):
            if a1[i]==a2[j]:
                if a1[i-1]==a2[j-1] or a1[i+1]==a2[j+1] or a1[i+1]==a2[j-1] or a1[i-1]==a2[j+1]:
                    return False
    return True

simulations=1000000
wins=0
for i in range(simulations):
    if probability():
        wins += 1

print("The probasbiblity is: ",(wins/simulations)*100,"%")