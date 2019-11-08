#tip is %20 and tax is %8#

def cost(x, y, z):
    tip = x * y / 100
    tax = x * z / 100
    a = tip + tax + x
    return a

b = int(input("Please enter the cost of food:"))
c = int(input("Please enter the tip percantage:"))
d = int(input("Please enter the tax percantage:"))
cost(b, c, d)
print(cost(b, c, d))


    

