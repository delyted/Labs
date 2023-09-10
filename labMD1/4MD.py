'''
Truth table solver
Input example: (!x + y) * z + (!z * y * k)
'''

A=[]
s=input("Enter the expresion please: ")
for i in range(len(s)):
    if s[i].isalpha(): 
        A.append(s[i]) 
A=list(set(A))        

n=len(A)**2;m=len(A)
print(*A, s, sep=' | ')

for i in range(len(A)):
    for j in range(len(s)):
        if A[i]==s[j]:
           s=s.replace(s[j], 'A['+str(i)+']') 
s=s.replace('+', 'or').replace('*', 'and').replace('!', 'not ')

for i in range(n):
    x=str(bin(i)[2:].zfill(m))
    for j in range(m):
        A[j]=int(x[j])
        e=eval(s)
        if e==True:
            e=1
        elif e==False:
            e=0
    print(*A, e, sep=' | ')