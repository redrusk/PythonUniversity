number = int(input("Введите целое число: "))
is_even = number % 2 == 0

if number == 0:
    print("нулевое число")
elif number > 0 and is_even:
    print("положительное четное число")
elif number < 0 and is_even:
    print("отрицательное четное число")
else:
    print("число не является четным")
