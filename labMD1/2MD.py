'''
XNOR
Input example: 0 / 1 / true / false
'''

a=input("First  value: "); b=input("Second value: ")
if a=="true" or a=='1':
    x=True
else:
    x=False
if b=="true" or b=='1':
    y=True
else:
    y=False
result=(x and y) or (not x and not y)
print("XNOR: "+str(result))