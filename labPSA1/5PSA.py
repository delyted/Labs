import hashlib
import random
x = int(input())
i = 0
count = 0

hash_list1 = []
hash_list2 = []
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22',
        '23','24','25','26','27','28','29','30','31']

for i in range(x):
    while_loop = True
    while while_loop:
        date = random.choice(days) + "." + random.choice(months)
        if (date not in [02.31,02.30,04.31,06.31,09.31,11.31]):
            while_loop = False
        else:
            date = random.choice(days) + "." + random.choice(months)
    result = hashlib.md5(date.encode())
    result = result.hexdigest()
    hash_list1.append(result)
for i in range(x):
    while_loop = True
    while while_loop:
        date = random.choice(days) + "." + random.choice(months)
        if (date not in [02.31, 02.30, 04.31, 06.31, 09.31, 11.31]):
            while_loop = False
        else:
            date = random.choice(days) + "." + random.choice(months)
    result = hashlib.md5(date.encode())
    result = result.hexdigest()
    hash_list2.append(result)

for i in range(x):
    if hash_list1[i] in hash_list2:
        while count != 1:
            date = random.choice(days) + "." + random.choice(months)
            result = hashlib.md5(date.encode())
            result = result.hexdigest()
            if result == hash_list1[i]:
                print(hash_list1[i])
                print(date)
                count +=1

