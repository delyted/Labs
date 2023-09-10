import random
simulations=1000000;acute=0;notacute=0
for i in range(0,simulations):
       a=random.uniform(0,1)
       b=random.uniform(0,1)
       c=random.uniform(0,1)
       if a>b:
              aux=a;a=b;b=aux
       if b>c:
              aux=b;b=c;c=aux
       if a>b:
              aux=a;a=b;b=aux
       if b>c:
              aux=b;b=c;c=aux
       ab=b-a
       ac=a+(1-c)
       bc=c-b
       if (ab>=0.5)or(bc>=0.5)or(ac>=0.5):
              notacute+=1
       else:
              acute+=1
print("Acute triangle:",acute/(simulations/100),"%")