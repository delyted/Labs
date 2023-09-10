alf=" abcdefghijklmnopqrstuvwxyz"
p=47;q=59;k=0;n=p*q;fi=(p-1)*(q-1);e=17;d=pow(e,n-2,fi)
message=input("Insert the message: ").lower()
mes="";enc="";denc="";mes2=""
for i in message:
       for j in range(0,len(alf)):
              if i==alf[j]:
                     k+=1
                     if j<10:
                            mes=mes+"0"+str(j)
                     else:
                            mes=mes+str(j)
                     if k%2==0:
                            mes=mes+" "
if k%2==1:
       mes=mes+"00"
a=0
while a<len(mes):
       if len(str(pow(int(mes[a:a+4]),e,n)))<4:
              for i in range(0,4-len(str(pow(int(mes[a:a+4]),e,n)))):
                     enc=enc+"0"
       enc=enc+str(pow(int(mes[a:a+4]),e,n))+" "
       a=a+5
a=0
while a<len(enc):
       if len(str(pow(int(enc[a:a+4]),d,n)))<4:
              for i in range(0,4-len(str(pow(int(enc[a:a+4]),d,n)))):
                     denc=denc+"0"
       denc=denc+str(pow(int(enc[a:a+4]),d,n))+" "
       a=a+5
k=0;a=0
while a<len(denc):
       k+=1;mes2=mes2+alf[int(denc[a:a+2])];a+=2
       if k%2==0:
              a+=1
print("Encrypted message:",enc)
print("Decrypted message:",denc)
print("Message:",mes2)