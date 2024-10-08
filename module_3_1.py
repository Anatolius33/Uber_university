# module_3_1.py
# Глобальная переменная для подсчета вызовов
calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()  # Подсчет вызовов
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()  # Подсчет вызовов
    string = string.lower()  # Приводим строку к нижнему регистру
    return any(string in item.lower() for item in list_to_search)


# Примеры вызовов функций
print(string_info('Capybara'))  # Вызов 1
print(string_info('Armageddon'))  # Вызов 2
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Вызов 3
print(is_contains('cycle', ['recycling', 'cyclic']))  # Вызов 4

# Вывод значения переменной calls
print(calls)  # Общее количество вызовов
