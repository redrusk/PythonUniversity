X = int(input("Введите минимальную сумму инвестиций X: "))
A = int(input("Введите сумму у Майкла A: "))
B = int(input("Введите сумму у Ивана B: "))

if A >= X and B >= X:
    result = 2
elif A >= X:
    result = "Mike"
elif B >= X:
    result = "Ivan"
elif A + B >= X:
    result = 1
else:
    result = 0

print(result)
