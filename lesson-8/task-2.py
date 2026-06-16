def reverse_shift(arr):
    return [arr[-1]] + arr[:-1]


n = int(input("Введите число N: "))
str_seq = input().split()
num_seq = list(map(int, str_seq))

for num in reverse_shift(num_seq):
    print(num, end=" ")
