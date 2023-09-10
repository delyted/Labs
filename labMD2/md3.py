low="abcdefghijklmnopqrstuvwxyz"
up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol=" ~`!@#$%^&*()-_+=}{[]|;:<>,./?"
nr="0123456789"
prd=input("Password: ")
change=0
if (len(prd)<8)or(len(prd)>20):
       if len(prd)<8:
              change=8-len(prd)
       else:
              change=len(prd)-20
else:
       
       characters=0
       for i in prd:
              for j in low:
                     if i==j:
                            characters+=1
       if characters==0:
              change+=1
       
       characters=0
       for i in prd:
              for j in up:
                     if i==j:
                            characters+=1
       if characters==0:
              change+=1
       
       characters=0
       for i in prd:
              for j in nr:
                     if i==j:
                            characters+=1
       if characters==0:
              change+=1
       
       characters=0
       for i in prd:
              for j in symbol:
                     if i==j:
                            characters+=1
       if characters==0:
              change+=1
       
       for i in range(len(prd)-2):
              if prd[i]==prd[i+1]==prd[i+2]:
                     change+=1
if change==0:
       print("Very good!")
else:
       print(change)