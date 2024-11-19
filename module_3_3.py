# module_3_3.py

def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Создание списка с тремя элементами разных типов
values_list = [3.14, "Hello", False]  # float, string, boolean

# Создание словаря с тремя ключами и значениями разных типов
values_dict = {
    "a": 42,            # integer
    "b": "World",      # string
    "c": None          # NoneType
}

# Передаем values_list и values_dict в функцию print_params
print_params(*values_list)  # Распаковка списка
print_params(**values_dict)  # Распаковка словаря
