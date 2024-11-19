# module_3_4.py

def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой список для подходящих слов
    
    # Приводим корневое слово к нижнему регистру для сравнения
    root_word_lower = root_word.lower()
    
    # Проходим по каждому слову в предполагаемых подходящих словах
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()
        
        # Проверяем, содержится ли корневое слово в текущем слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)  # Добавляем слово в список
    
    return same_words  # Возвращаем список подходящих слов

# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результатов на экран
print(result1)
print(result2)
