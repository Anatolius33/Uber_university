def get_matrix(n, m, value):
    # Проверяем значения n и m, если они меньше или равны 0, возвращаем пустой список
    if n <= 0 or m <= 0:
        return []

    # Создаем пустой список для матрицы
    matrix = []
    
    # Внешний цикл для количества строк
    for _ in range(n):
        row = []  # Создаем пустую строку
        # Внутренний цикл для количества столбцов
        for _ in range(m):
            row.append(value)  # Заполняем строку значением
        matrix.append(row)  # Добавляем строку в матрицу
    
    return matrix  # Возвращаем матрицу

# Примеры использования функции
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результата на экран
print(result1)
print(result2)
print(result3)
