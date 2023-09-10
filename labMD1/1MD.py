'''
Subsets
Input example: [1,2,3]
'''

set=[]
s=input("Enter the set: ")
for i in range(len(s)):
    if s[i].isdigit(): 
        set.append(int(s[i]))        

subsets = [[]]
for i in set:
    for j in range(len(subsets)):
        subsets.append(subsets[j] + [i])
print(subsets)