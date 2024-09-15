   # 1. Ввод чисел
   first = int(input("Введите первое число: "))  # Запрашиваем первое число
   second = int(input("Введите второе число: "))  # Запрашиваем второе число
   third = int(input("Введите третье число: "))  # Запрашиваем третье число

   # 2. Проверка условий
   if first == second == third:  # Все числа равны
       print(3)
   elif first == second or first == third or second == third:  # Хотя бы два числа равны
       print(2)
   else:  # Все числа разные
       print(0)
   
