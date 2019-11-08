import random

y = random.randrange(1,100)
flag = False

for i in range(10):
  if not flag: 
    x = int(input("Please enter a number:"))
    if x<y:
      print("Try bigger.")
    elif x>y:
      print("Try lesser.")
    else:
      flag = True

if flag:
  print("You won")
else:
  print("You lost and number was", y)






