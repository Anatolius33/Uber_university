# fake_math.py

def divide(first, second):
    """Деление с обработкой деления на 0."""
    if second == 0:
        return 'Ошибка'
    return first / second
