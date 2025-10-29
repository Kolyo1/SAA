# 1

def Binary(a):
    if a < 2:
        return str(a)
    else:
        return Binary(a // 2) + str(a % 2)
    
print(Binary(10))  # Output: 1010

# 2

def Power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / Power(x, -n)
    else :
        return x * Power(x, n - 1)
    
print(Power(2, 3))  # Output: 8


# 3

def Sum(arr):
    if not arr:
        return 0
    else:
        return arr[0] + Sum(arr[1:])
    
print(Sum([1, 2, 3, 4, 5]))  # Output: 15


# 4

def Contains(b, c):
    if b == 0:
        return False
    elif b %10 == c:
        return True
    else:
        return Contains(b // 10, c)
    

print(Contains(12345, 3))  # Output: True
print(Contains(12345, 6))  # Output: False