import math

def count_divisors(x):
    count = 0
    sqrt_x = int(math.isqrt(x))
    
    for i in range(1, sqrt_x + 1):
        if x % i == 0:
            if i * i == x:
                count += 1
            else:
                count += 2
    
    return count

x = int(input())
print(count_divisors(x))
