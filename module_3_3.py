def print_params(*args):
    for item in args:
        print(item, end=' ')
    print()  # Переход на новую строку после вывода

# Исходный код
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
