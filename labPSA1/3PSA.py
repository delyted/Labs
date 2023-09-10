import random
dan_serve = [2,1]
ana_serve = [2,4,6,8,10,12,14,1,3,5]
ana_win = 0
dan_win = 0
x = int(input())
i = 0
for i in range(x):
    who_serve = 'ana'
    count_dan = 0
    count_ana = 0
    while count_dan != 25 and count_ana != 25:
        if (who_serve == 'dan'):
            dan_points = random.choice(dan_serve)
            if (dan_points % 2 == 0):
                count_dan += 1
                who_serve = 'ana'
            else:
                count_ana += 1
        if (who_serve == 'ana'):
            ana_points = random.choice(ana_serve)
            if (ana_points % 2 == 0):
                count_ana += 1
                who_serve = 'dan'
            else:
                count_dan += 1
    if (count_ana == 25):
        ana_win += 1
    else:
        dan_win += 1

print("The probability that Ana will win is ",  (ana_win/x*100), "%")