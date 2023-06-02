word = 'Пельмени'
print(word.upper())#Верхний регистр
word = word.lower()#Нижний регистр
print(word.isupper())#Проверка , стоит ли слово польностью в верхнем регистре
print(word.islower())#Проверка , стоит ли слово польностью в нижнем регистре
print(word[3])#Вывод симбвола
print('Это слово состоит из', len(word),' буквы')
print('Сумма букв "а" =',word.count('а'))
print(word.find('к')) # Находит первый симбвол
print(word.capitalize())# Первая буква в верхний регистр а остальные в нижнии
print(list(word))
a= 'pelmeni, vareniki, hinkali'
array = a.split(', ')#Разделяет строку на симбволы
print(array)
array_str = ", ".join(array)
print(array_str)
#Срез. Несколько объектов на вывод
word = 'football'
print(word[0:4])#foot
print(word[4:8])#ball
print(word[0:8:2])#fobl Через раз
a = [14,14,25,3,637,'agf']
print(a[2:]) # от 2 до конца
print(a[2::2])# от 2 до конца через  раз
