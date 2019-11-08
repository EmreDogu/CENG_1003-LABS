def is_armstrong(number):
  num_str = str(number)
  num_len = len(num_str)
  sum_of_digits = 0
  for d in num_str:
    sum_of_digits = sum_of_digits + int(d) ** num_len 
  if number == sum_of_digits:
      return True
  else:
      return False

a = int(input("Please enter the digits for Armstrong number check:"))

for n in range(1,10**a+1): 
    if is_armstrong(n):
        print(n, "is an Armstrong number.")
