# module_average_grade.py

# Данные на входе
grades = [
    [5, 3, 3, 5, 4],  # Оценки для "Aaron"
    [2, 2, 2, 3],     # Оценки для "Bilbo"
    [4, 5, 5, 2],     # Оценки для "Johnny"
    [4, 4, 3],        # Оценки для "Khendrik"
    [5, 5, 5, 4, 5]   # Оценки для "Steve"
]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # Имена учеников

# Функция для создания словаря с именами и средними баллами
def compute_average_grades(grades, students):
    average_grades = {}  # Создаем пустой словарь для хранения средних баллов
    
    # Преобразуем множество в упорядоченный список
    students_list = sorted(students)  # Сортируем в алфавитном порядке
    
    for i in range(len(grades)):
        student_name = students_list[i]  # Имя студента по индексу
        average_grade = sum(grades[i]) / len(grades[i])  # Вычисляем средний балл
        average_grades[student_name] = average_grade  # Сохраняем в словаре

    return average_grades

# Основная функция программы
def main():
    # Получаем словарь средних баллов
    average_grades = compute_average_grades(grades, students)
    
    # Выводим результаты на экран
    print(average_grades)

# Запуск основной функции
if __name__ == "__main__":
    main()
