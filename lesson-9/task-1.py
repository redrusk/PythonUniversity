n = int(input("Введите число N: "))
numbers = list(map(int, input().split()))[:n]
distinct_count = len(set(numbers))
print(distinct_count)