import math

def sum(x):
    total = 0
    for i in x:
        total = total + i
    return total

def avg(x):
    return sum(x)/len(x)
    
def minn(x): 
    return min(x)

x = [10, 5, 6, 8, 12, 16, 21]

print(sum(x), avg(x), minn(x))



