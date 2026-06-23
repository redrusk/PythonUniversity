def factorial(n):
    """Вычисляет факториал числа n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def get_factorial_sequence(num):
    """
    Принимает натуральное число, вычисляет его факториал,
    затем создаёт список факториалов от этого значения до 1 в убывающем порядке.
    """
    initial_factorial = factorial(num)
    print(f"Факториал числа {num} равен {initial_factorial}")

    factorial_list = []
    for i in range(initial_factorial, 0, -1):
        factorial_value = factorial(i)
        factorial_list.append(factorial_value)

    return factorial_list


input_number = int(input("Введите число: "))
result = get_factorial_sequence(input_number)
print(f"Результирующий список: {result}")
