"""
    Автор модуля: Антон Покровский Группа 51
    Программа: Шифровальщик цезаря
"""
class Cryptographer(object): # Объявление класса шифровальщик
    """Наш шифровальщик"""
    ALPHABETS = {"rus": "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
            ,"en" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ"} #Атрибут класса с дефолтными Алфавитами
    def __init__(self, alphabets: dict = ALPHABETS) -> None: # Создание Метода-конструктора
        """ В методе конструкторе содержится блок кода,
            который запускается тогда, когда мы инициализируем(создаём) объект класса"""
        if type(alphabets) == dict:
            self.ALPHABETS: dict = alphabets # Создание атрибута ALPHABETS для объекта класса
        else: raise TypeError(f"у вас аргумент типа {type(alphabets)}, а должен быть dict,\n\
        где ключ - название алфавита (тип str), а значение - Алфавит в верхнем регистре (типа str)")
    def encryption(self,string, mode="Шифровка") -> str: # Создание Метода Шифровки 
        """Возвращает зашифрованный или расшифрованный string
        mode - это решим. У него может быть значение 'Расшифровка' или 'Шифровка'.
        Если в mode ничего не вписать, то по дефолту будет 'Шифрровка'"""
        cryptString = "" # создание переменной для записи в нее шифрованных букв
        for letter in string: # Итерация. Проходим временной переменной letter по итерируемому объекту string(аргумент функции).(Перебираем буквы в строке)
            letAlphabet = self.__findAlphabet(letter) # Находим в каком алфавите находится эта буква.
            # Используется приватный метод объекта этого класса. Он объявляетсья на 52 строке
            if letAlphabet is None: # Если буквы нет не в одном алфавите
                cryptString += letter # Она просто прибавляется без шифрования
            else: # А если буква всё же есть
                indexLet = self.ALPHABETS[letAlphabet].index(letter.upper()) #Находим индекс этой буквы в алфавите
                if mode == "Шифровка": # Если мы шифруем сообщение
                    encryptLet = self.__crypting_letter(indexLet, self.ALPHABETS[letAlphabet]) 
                    # Вызываем приватный метод шифрования и передаем в аргументы букву. Записываем результат в переменную encryptLet. 
                    # Объявление приватной функции в 57 строке
                elif mode == "Расшифровка": # А если мы расшифровываем сообщение
                    encryptLet = self.__decripting_letter(indexLet, self.ALPHABETS[letAlphabet])
                    # Вызываем приватный метод расшифровкии передаем в аргументы букву. Записываем результат в переменную encryptLet. 
                    # Объявление приватной функции в 74 строке
                else: # А если пользователь ввел иное значение
                    raise ValueError("Не подходит значение вписанного вами аргумента") # Компьютер его не понимает и выкидывает исключение(ошибку)
                if letter.islower(): # Мы из алфавита брали большие буквы, а если она была маленькой
                    encryptLet = encryptLet.lower() # Переводим в нижний регистр
                cryptString += encryptLet # Добавляем обработанную букву в cryptString (Зашифрованное слово)
        return cryptString # После Обработки строки возвращаем обработанную строку
    def __findAlphabet(self,letter) -> str: # Объявление приватного метода
        """Определяет алфавит буквы. В аргументах буква, которую надо обработать"""
        letAlphabet = None # Алфавит буквы не определен
        for alphabet in self.ALPHABETS.items(): # Проходимся по каждому алфавиту из словаря
            if letter.upper() not in alphabet[1]: # Если буква в верхнем регистре нет в значении алфавите
                continue # Пропускаем
            else: # Если есть 
                letAlphabet = alphabet[0] # Записываем в переменную letAlphabet название алфавита(ключ)
        return letAlphabet # Возвращаем название алфавита
    @staticmethod # Декоратор статического метода. Означает, что следощий метод будет статическим(для его вызова не требуется инициализация(Создание) объекта)
    def __crypting_letter(indexletter, alphabet) -> str: #Объявление статического приватного метода 
        """Шифровка буквы. В аргументы индекс буквы и алфавит буквы"""
        encrypted_letter = None #  Зашифрованная буква на выходе не определена
        try: # Попытаться сделать этот блок кода
            encrypted_letter = alphabet[indexletter + 3] # Зашифрованна буква - буква на 3 позиции дальше чем исходная
        except IndexError: # Если вылезет ошибка свзанная с индексами, перехватить её и сделать вот этот блок кода
            # Для создания корректного алгоритма замены букв я приведу аналогию с целочисленными переполнениями в ячейках памяти(ЭТО НЕ ОДНО И ТОЖЕ)
            # Простой пример переполнения в C++ для понимания: Допустим у нас есть тип переменной где может быть целочисленное значение в диапазоне от 0 до 3
            # Если мы выйдем за пределы этого диапазона счетчик начнется с начала. То есть 2 * 2 = 0 ,тк 2*2 = 4, а 4 нет в диапазоне значит счетчик обнуляется(переходит в начало)
            # А например 2*3 будет равное не 6 , а 2 тк произошло переполнение. Этого следует избегать и следить за этим в языках C и C++.
            # Если интересно узнать больше про переполнения, кодировки и 0 и 1 в двоичной системе , операции над ними, советую посмотреть Тимофея Хирьянова, его 2 лекцию по алгоритмам  и структурам данных(C++)
            # Она есть в свободном доступе на просторах интернета . (https://www.youtube.com/watch?v=nkuNsxLcN0g&t=3625s)
            # А теперь возвращаемся к алгоритму: если мы при перемещении на 3 позиции дальше, выходим за пределы диапазона возможных индексов
            # то счетчик индексов переходит в начало и продолжает счет.  Похоже на переполнение? Думаю да
            # Поэтому следующими 3 строчками Я придумал небольшой алгоритм для замены буквы на основе имитации переполнения(НО ЭТО НЕ ПЕРЕПОЛНЕНИЕ),
            # Чтобы при выходе за пределы не вылезала ошибка IndexError, а продолжал счет с начала алфавита
            difference = len(alphabet) - len(alphabet[:indexletter]) # из всей длины алффавита вычетаем Длину от начала до нашей буквы
            # Чтобы узнать сколько букв осталось до конца алфавита
            new_index = 3 - difference # Индекс буквы равен разнице между 3 и difference. 
            encrypted_letter = alphabet[new_index] # Записываем зашифрованную букву 
        return encrypted_letter # Возвращаем зашифрованную букву 
    @staticmethod
    def __decripting_letter(indexletter, alphabet): # Эта приватная статическая функция работает также как и функция выше, но с некоторыми изменениями
        """Расшифровывает букву. В аргументы индекс буквы и алфавит буквы"""
        decrypted_letter = None
        try:
            decrypted_letter = alphabet[indexletter - 3] # Мы меняем нашу букву на букву стоящую на 3 позиции раннее,в отличии от шифровки
        except IndexError:
            # Точно такой же алгоритм замены ,с одним но
            difference = len(alphabet) - len(alphabet[:indexletter])
            new_index = -abs(3 - difference) # Мы делаем индекс с отрицательным знаком, чтобы буквы в Алфавите брались с конца
            decrypted_letter = alphabet[new_index]
        return decrypted_letter
# И наконец главная часть программы
if __name__ == "__main__": # Если она запускаеться на прямую, а не импортируется как модуль то
    # Благодоря этому условию вы можете использовать мой модуль в своих программах, 
    # пропуская мою готовую программу которая срабатывает при запуске модуля напрямую
    cryptographer1 = Cryptographer() # Инициализация объекта созданного нами класса 
    # Если поместить в скобки словарь с другими алфавитами , то наш объект будет работать с вашими указанными алфавитами. 
    # Если нет по дефолту алфавит русского и английского языка
    string = input("Введите строку: ")
    cryptstr = cryptographer1.encryption(string) # Шифруем строку
    decryptstr = cryptographer1.encryption(cryptstr, mode = "Расшифровка") # Расшифруем строку
    print(f"Ваша строка: {string}\nЗашифрованная строка: {cryptstr}\nРасшифрованная строка: {decryptstr}") # Вывод результата
    input("Нажмите 'Enter' чтобы выйти")