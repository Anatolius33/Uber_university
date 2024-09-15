# 1. Инициализация списков
primes = []  # Список для простых чисел
not_primes = []  # Список для не простых (составных) чисел

# 2. Проверка чисел от 2 до 15
for num in range(2, 16):
    is_prime = True  # Переменная-флаг, предполагаем, что число простое
    
    # 3. Проверка на простоту
    for divisor in range(2, num):  # Проверяем делители от 2 до num-1
        if num % divisor == 0:  # Если num делится на divisor
            is_prime = False  # Устанавливаем флаг в False
            break  # Прерываем цикл, так как мы нашли делитель
    
    # 4. Заполнение списков
    if is_prime:
        primes.append(num)  # Добавляем в список простых чисел
    else:
        not_primes.append(num)  # Добавляем в список составных чисел

# 5. Вывод результатов
print("Primes:", primes)
print("Not Primes:", not_primes)
