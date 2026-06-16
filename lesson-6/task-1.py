N = int(input("Введите число N: "))

count_zeros = 0

for _ in range(N):
    num = int(input("Введите целое число: "))
    if num == 0:
        count_zeros += 1

print(f"Количество нулей: {count_zeros}")
