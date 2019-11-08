def smallest(a,b,c):
   if a<b and a<c:
       return a
   elif c<b and c<a:
       return c
   else:
       return b

print(smallest(4,5,6))

#next one#

def smaller(a,b):
    if a>b:
        return b
    else:
        return a

print(smaller(4,5))
