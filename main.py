# main.py

# Задача 1 (просто) "Арифметика"
# 1st program
result1 = (9 ** 0.5) * 5
print(result1)  # Ожидаемый результат: 15.0

# Задача 2 (просто) "Логика"
# 2nd program
result2 = (9.99 > 9.98) and (1000 != 1000.1)
print(result2)  # Ожидаемый результат: True

# Задача 3 (средне) "Школьная загадка"
# 3rd program
result3_1 = 2 * 2 + 2  # без приоритета
result3_2 = 2 * (2 + 2)  # с приоритетом
print(result3_1)  # Ожидаемый результат: 6
print(result3_2)  # Ожидаемый результат: 8
print(result3_1 == result3_2)  # Ожидаемый результат: False

# Задача 4 (сложно) "Первый после точки"
# 4th program
string_number = '123.456'
number = float(string_number)  # Преобразование строки в дробное число
shifted_number = number * 10  # Умножаем на 10
first_digit_after_point = int(shifted_number) % 10  # Оставшееся деление на 10
print(first_digit_after_point)  # Ожидаемый результат: 4
