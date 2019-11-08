def isArmstrong(n):
    if n == (n//1000)**4 + ((n%1000)//100)**4 + ((n%100)//10)**4 + (n%10)**4:
        return n
    
for i in range(1000,10000):
    if isArmstrong(i) == i:
        print(i)
    

