n = int(input("Введите число N: "))
numbers = [int(input()) for _ in range(n)]
reversed_numbers = numbers[::-1]

for num in reversed_numbers:
    print(num, end=" ")
