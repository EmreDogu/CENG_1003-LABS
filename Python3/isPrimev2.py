def isPrime(a):
    if a==1:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True

for a in range(1,100):
    if isPrime(a):
        print(a)
