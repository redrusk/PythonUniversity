numbers1 = set(map(int, input("Введите список чисел №1: ").split()))
numbers2 = set(map(int, input("Введите список чисел №2: ").split()))
print(len(numbers1 & numbers2))