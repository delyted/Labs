import random

fair_coin = ["tail", "head"]
i = 0
k = 0
suma = 0
wining = 0
x = int(input())
for i in range(x):
    random_face = ""
    j = 0
    while random_face != "head":
        random_face = random.choice(fair_coin)
        j += 1
        if random_face == "head":
            k = j
            wining = wining-10
            wining += 2**k
            suma += 2**k
suma = suma / x
print("The amount you will be wiling to pay per game is", round(suma), "$")
print("The winnings if you would pay 10$ is", wining, "$")
