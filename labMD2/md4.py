string=input("Input the string: ");string2=string[::-1]
if string==string[::-1]:
       print(string)
else:
       a=1
       while a<=len(string):
              result=string2[0:a]+string
              a+=1
              if result==result[::-1]:
                     break
       print(result)