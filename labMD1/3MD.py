'''
Longest substring
Input example: abbcib
'''

s=input()
s2=[]
s3=set()
for i in range(len(s)):
    s1=""
    for j in range(i+1,len(s)):
        if s[j] == s[i]:
            s1=s[i:j+1]
            break
    s2.append(s1)

for i in range(len(s2)):
    for j in range(i+1,len(s2)):
        if s2[i]==s2[j]:
            s3.add(s2[i])

m=max(s3, key=len)

if len(m)>0:
    print(m)
else:
    m=0
    for i in range(len(s)):
        counter=0
        e=set()
        for j in range(i+1,len(s)):
            if s[j] in e:
                break
            else:
                counter+=1
                e.add(s[j])
        m=max(m, counter)
    print(m)