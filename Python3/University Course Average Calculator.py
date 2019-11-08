a = float(input("Enter your midterm score:"))
b = float(input("Enter your final score:"))
c = float(input("Enter your first quiz score:"))
d = float(input("Enter your second quiz score:"))
e = float(input("Enter your third quiz score:"))

print("Your grade is:", ((a*0.2)+(b*0.5)+(((c+d+e)/3)*0.3)))
