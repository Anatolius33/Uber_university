def generate_password(n):
    password_parts = []

    # Собираем пары чисел
    for i in range(1, n):  # Первое число от 1 до n-1
        for j in range(i + 1, n + 1):  # Второе число от (i+1) до n
            if i + j <= n:
                password_parts.append(str(i + j))

    # Формируем пароль
    password = ''.join(password_parts)
    return password

# Генерация паролей для чисел от 3 до 20
passwords = {}
for i in range(3, 21):
    passwords[i] = generate_password(i)

# Вывод результатов
for key, value in passwords.items():
    print(f"{key} - {value}")
