import math
def calculateRadius(x1, y1, x2, y2):
    a = ((x2-x1)**2 + (y2-y1)**2)**1/2
    return a
x1 = float(input("Enter x1:"))
x2 = float(input("Enter x2:"))
y1 = float(input("Enter y1:"))
y2 = float(input("Enter y2:"))
r = calculateRadius(x1, y1, x2, y2)

def calculateArea(r):
    area = math.pi*r**2
    return area
calculateArea(r)
print(calculateArea(r))

