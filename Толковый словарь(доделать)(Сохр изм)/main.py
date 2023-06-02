DICT_ERRORS = {"IOError":"Генерируется, если невозможно выполнить операцию ввода/вывода",
               "IndexError":"Генерируется, если в последовательности не найден элементы с данным индексом",
               "KeyError":"Если в словаре не найден указанный ключ",
               "NameError":"Если не найдено имя переменной или функции",
               "SyntaxError": "Если в коде обнаружена синтаксическая ошибка",
               "TypeError":"Если стандартная операция применяема к объекту неподходящего типа",
               "ValueError":"Если операция или функция принимает аргумент с неподходящем значением",
               "ZeroDivisionError":"Если есть деление на ноль"}
print("Это программа работает с терминами исключений в PYTHON!!")
choice = None
while choice != "0":
    print("""Выберите, что хотите сделать:
        0 - Выйти
        1 - Найти значение исключения
        2 - Показать список существующих в базе исключений
        3 - Добавить в список новое исключеие
        4 - Удалить исключение""")
    choice = input("Ваш ответ: ")
    if choice == "0":
        print("Удачи:)))")
        break
    elif choice == "1":
        print("Сейчас вы найдете значение нужного вам исключения")
        users_error = input("Введите имя вашего исключения: ").lower()
        finded = False
        for key in DICT_ERRORS:
            if key.lower() == users_error.lower():
                     print(DICT_ERRORS[key])
                     finded = True
        if not finded:
            print("Такой ошибки нет в базе данных этой программы:(")
            for i in DICT_ERRORS.keys():
                print(i)
    elif choice == "2":
        for key in DICT_ERRORS:
            print(key,"-",DICT_ERRORS[key])
    elif choice == "3":
        termin = input("Сейчас вы добавляете новое исключение.\nВведите имя исключения: ")
        if termin not in DICT_ERRORS:
            value = input("Впишите, что означает это исключение: ")
            DICT_ERRORS[termin] = value
            print ("В списке исключений появилось исключение '",termin,"'с его значением.\
Значение: ",value, sep = '')
    elif choice == "4":
        termin = input("Сейчас в удалите исключение.\nВведите имя исключения: ")
        if termin in DICT_ERRORS:
            print("Вы точно хотите удалить исключение", termin,'? Напишите "да" или "нет".', end = '')
            confidence = None
            while confidence != "да" and confidence != "нет":
                confidence = input().lower()
                if confidence == "да":
                    del DICT_ERRORS[termin]
                    print('Исключение"',termin,'"Удалено успешно!!',sep = '')
                elif  confidence == "нет":
                    continue
                else:
                    print('Нет такой команды "',confidence,'". Есть только "да" и "нет".\nПопробуйте ещё раз:)', sep = '')
    else:
        print("Я не понял, чего вы хотите. Введите доступную в списке команду.")



