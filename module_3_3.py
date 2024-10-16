def print_params(txt, *args, **kwargs):
    # Выводим текстовый параметр
    print(txt)
    
    # Выводим аргументы из списка
    for item in args:
        print(item, end=' ')
    
    # Выводим аргументы из словаря
    for key, value in kwargs.items():
        print(f"{key}: {value}", end=' ')
    
    print()  # Переход на новую строку после вывода

# Создаём список с тремя элементами разных типов
values_list = [54.32, 'Строка', True]

# Создаём словарь с тремя ключами и значениями разных типов
values_dict = {
    'число': 100,
    'фраза': 'Пример',
    'логическое': False
}

# Передаём значения в функцию print_params
print_params('Список параметров:', *values_list, **values_dict)
