a = int(input("Enter number:"))
b = int(input("Enter number:"))

if a>b:
    greater = a
elif a<b:  
    greater = b
else:
    greater = a

def lcm(a,b):
    if greater%b==0 and greater%a==0:
        return greater
    for i in range(greater,a*b+1):
        if i%b==0 and i%a==0:
            return i
   
print(lcm(a,b))        

