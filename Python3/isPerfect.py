def isPerfect(a):
    total = 0
    for i in range(1,a):
        if a%i == 0:
            total = total + i
    if total == a:
        return True
    return False

print(isPerfect(6))

