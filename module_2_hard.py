def generate_password(n):
    parts = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if i + j == n:
                parts.append(str(i))
                parts.append(str(j))
    return ''.join(parts)

# Генерация паролей для чисел от 3 до 20
for i in range(3, 21):
    generated_password = generate_password(i)
    print(f"{i} - {generated_password}")
