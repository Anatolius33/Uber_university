# module_3_5.py

def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку
    if len(str_number) > 1:
        first = int(str_number[0])  # Извлекаем первую цифру
        return first * get_multiplied_digits(int(str_number[1:]))  # Рекурсивный вызов
    elif len(str_number) == 1:
        return int(str_number)  # Базовый случай: одна цифра
    else:
        return 1 #базовый случай: пустая строка


# Пример вызова функции:
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24
