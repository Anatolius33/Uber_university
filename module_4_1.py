# module_4_1.py

from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Тестирование функций
results = [
    fake_divide(69, 3),  # Ожидается 23.0
    fake_divide(3, 0),    # Ожидается 'Ошибка'
    true_divide(49, 7),   # Ожидается 7.0
    true_divide(15, 0)    # Ожидается inf
]

# Вывод результатов через цикл for
for result in results:
    print(result)
