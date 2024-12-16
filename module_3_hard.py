def calculate_structure_sum(data):
    total = 0

    for item in data:
        if isinstance(item, int):  # Если элемент - целое число
            total += item
        elif isinstance(item, list):  # Если элемент - список
            total += calculate_structure_sum(item)  # Рекурсивный вызов
        elif isinstance(item, dict):  # Если элемент - словарь
            # Сначала обрабатываем ключи
            total += calculate_structure_sum(list(item.keys()))  # Рекурсивный вызов для ключей
            # Затем обрабатываем значения
            total += calculate_structure_sum(list(item.values()))  # Рекурсивный вызов для значений
        elif isinstance(item, tuple):  # Если элемент - кортеж
            total += calculate_structure_sum(item)  # Рекурсивный вызов
        elif isinstance(item, str):  # Если элемент - строка
            total += len(item)  # Добавляем длину строки

    return total


# Данные
data_structure = [
    [1, 2, 3],  # 1 + 2 + 3 = 6
    {'a': 4, 'b': 5},  # 4 + 5 + len('a') + len('b') = 4 + 5 + 1 + 1 = 11
    (6, {'cube': 7, 'drum': 8}),  # 6 + 7 + 8 + len('cube') + len('drum') = 6 + 7 + 8 + 5 + 4 = 30
    "Hello",  # len('Hello') = 5
    (2, 'Urban', ('Urban2', 35))  # 2 + len('Urban') + len('Urban2') + 35 = 2 + 6 + 8 + 35 = 51
]

# Вычисление суммы
result = calculate_structure_sum(data_structure)
print(result)  # Теперь это даст 99.
