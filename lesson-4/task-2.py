def calculate_from_number(number):
    tens_of_thousands = number // 10000
    thousands = (number // 1000) % 10
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    units = number % 10

    power_result = tens**units
    multiplied_result = power_result * hundreds
    difference = tens_of_thousands - thousands

    if difference == 0:
        raise ZeroDivisionError(
            "Разность десятков тысяч и тысяч равна нулю, деление невозможно"
        )

    final_result = multiplied_result / difference

    return final_result


number = 46275
result = calculate_from_number(number)
print(f"Результат для числа {number}: {result}")
