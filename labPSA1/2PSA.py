import random
barrel_slot_6a = [2,4,1,3,5,7]
barrel_slot_6na = [2,1,3,4,5,7]
barrel_slot_5a = [2,4,1,3,5]
barrel_slot_5na = [2,1,3,4,5]
x = int(input())
y = 0
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
count_8 = 0
m = x
for y in range(x):
    i = random.choice(barrel_slot_6a)
    j = barrel_slot_6a.index(i)
    if (i%2 == 0):
        m -= 1
    else:
        if (j == 5):
            j = -1
        i = barrel_slot_6a[j+1]
        k = random.choice(barrel_slot_6a)
        if (i%2 == 0):
            count_2 += 1
        if (k%2 == 0):
            count_1 += 1
probability_1 = round ((1-count_1/m)*100)
probability_2 = round ((1-count_2/m)*100)
m = x
for y in range(x):
    i = random.choice(barrel_slot_6na)
    j = barrel_slot_6na.index(i)
    if (i % 2 == 0):
        m -= 1
    else:
        if (j == 5):
            j = -1
        i = barrel_slot_6na[j + 1]
        k = random.choice(barrel_slot_6na)
        if (i % 2 == 0):
            count_4 += 1
        if (k % 2 == 0):
            count_3 += 1
probability_3 = round ((1-count_3/m)*100)
probability_4 = round ((1-count_4/m)*100)
m = x
for y in range(x):
    i = random.choice(barrel_slot_5a)
    j = barrel_slot_5a.index(i)
    if (i % 2 == 0):
       m -= 1
    else:
        if (j == 4):
            j = -1
        i = barrel_slot_5a[j + 1]
        k = random.choice(barrel_slot_5a)
        if (i % 2 == 0):
            count_6 += 1
        if (k % 2 == 0):
            count_5 += 1
probability_5 = round ((1-count_5/m)*100)
probability_6 = round ((1-count_6/m)*100)
m = x
for y in range(x):
    i = random.choice(barrel_slot_5na)
    j = barrel_slot_5na.index(i)
    if (i % 2 == 0):
        m -= 1
    else:
        if (j == 4):
            j = -1
        i = barrel_slot_5na[j + 1]
        k = random.choice(barrel_slot_5na)
        if (i % 2 == 0):
            count_8 += 1
        if (k % 2 == 0):
            count_7 += 1
probability_7 = round ((1-count_7/m)*100)
probability_8 = round ((1-count_8/m)*100)
print("The probabilitis that you will be alive:")
print("When there are 6 slots and 2 bullets are adjacent")
print("If you pull the trigger after spinning =",probability_1,"%")
print("If you pull the trigger without spinning =",probability_2,"%")
print("When there are 6 slots and 2 bullets are NOT adjacent")
print("If you pull the trigger after spinning =",probability_3,"%")
print("If you pull the trigger without spinning =",probability_4,"%")
print("When there are 5 slots and 2 bullets are adjacent")
print("If you pull the trigger after spinning =",probability_5,"%")
print("If you pull the trigger without spinning =",probability_6,"%")
print("When there are 5 slots and 2 bullets are NOT adjacent")
print("If you pull the trigger after spinning =",probability_7,"%")
print("If you pull the trigger without spinning =",probability_8,"%")