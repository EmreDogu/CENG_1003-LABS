import math
def calculateArea(r):
    area = math.pi*r**2
    return area
r = float(input("Enter the radius:"))
calculateArea(r)
print(calculateArea(r))
