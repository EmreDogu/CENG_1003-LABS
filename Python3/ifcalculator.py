e = int(input("for addition press 1, for substruction press 2, for multiplication press 3, for division press 4"))
def add(x1, x2):
    a = x1+x2
    return a

def sub(x1, x2):
    b = x1-x2
    return b

def mul(x1, x2):
    c = x1*x2
    return c 

def div(x1, x2):
    d = x1/x2
    return d 

x1 = float(input("Enter first number:"))
x2 = float(input("Enter second number:"))

add(x1, x2)
sub(x1, x2)
mul(x1, x2)
div(x1, x2)

if e==1:
    print("Result of addition is:", add(x1, x2))
elif e==2:
    print("Result of substruction is:", sub(x1, x2))
elif e==3:
    print("Result of multiplication is:", mul(x1, x2))
elif e==4:
    print("Result of dvision is:", div(x1, x2))


