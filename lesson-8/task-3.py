def min_boats(max_weight, num_fishers, weights):
    weights.sort()
    
    i = 0
    j = num_fishers - 1
    boats = 0
    
    while i <= j:
        if weights[i] + weights[j] <= max_weight:
            i += 1
        
        j -= 1
        boats += 1
    
    return boats


m = int(input())
n = int(input())
weights = [int(input()) for _ in range(n)]

result = min_boats(m, n, weights)
print(result)
