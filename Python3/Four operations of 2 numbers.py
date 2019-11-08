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

print(add(x1, x2))
print(sub(x1, x2)) 
print(mul(x1, x2)) 
print(div(x1, x2))
