arr = [9,5,3,2,4,10,7,6,1,8, -6, -3, -7, -10, -4, -1, -5, -2, -9, -8]
neg =[]
pos = []
for num in arr:
    if num < 0:
        neg.append(num)
    else:
        pos.append(num)

print("Negative numbers:", sorted(neg, reverse=True))
print("Positive numbers:", sorted(pos))

#------------------------------------------------------------

arr2 = [12, 15, 7, 9, 20, 33, 25, 18, 30, 22]
sorted_arr2 = sorted(arr2, reverse=True)
k = 3
top = sorted_arr2[:k]

if not top:
    print(0)
else:
    g = reduce(math.gcd, (abs(x) for x in top))
    print(g)

#------------------------------------------------------------

import math
from functools import reduce
mm = [8, 2, 10, 4, 12 , 6]
print(reduce(math.gcd, (abs(x) for x in mm)))

#------------------------------------------------------------

def is_fib(a):
    if len(a) < 3:
        return True
    for i in range(2, len(a)):
        if a[i] != a[i - 1] + a[i - 2]:
            return False
    return True

print(is_fib([0, 1, 1, 2, 3, 5, 8, 13]))
print(is_fib([2, 3, 5, 8, 13, 21]))
print(is_fib([1, 2, 4, 6, 10]))

#------------------------------------------------------------