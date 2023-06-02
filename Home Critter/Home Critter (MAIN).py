#import modules
from  class_home_critter import Critters
#Description functions
def choice_main_menu():
    user_chose = False
    user_choice_main = None
    while not user_chose:
        user_choice_main = input("Ваш выбор: ")
        if user_choice_main in ("0", "1", "2", "3","4"):
            user_chose = True
        else:
            continue
    return user_choice_main

def main():
    name_critter = ""
    while name_critter == "":
        name_critter = input("Введите имя зверюшки: ")
        if name_critter == "":
            print("Имя зверюшки не может быть пустым.\nПопробуйте ещё раз")

    obj = Critters(name_critter)
    print("Моя зверюшка ", obj.name, ":", sep="")
    user_choice = None
    while user_choice != "0":
        print(obj)
        print("Главное меню зверюшки:")
        print(
        """ \t\t\t0 - Выйти
            1 - Узнать о самочувствии зверька
            2 - Покормить зверюшку
            3 - Поиграть со Зверюшкой
            4 - Изменить имя зверюшки""")
        user_choice = choice_main_menu()
        if user_choice == "0":
            pass
        elif user_choice == "1":
            obj.mood_for_display()
        elif user_choice == "2":
            obj.eating()
        elif user_choice == "3":
            obj.play()
        elif user_choice == "4":
            new_name = input("Введите новое имя зверюшки: ")
            obj.name = new_name
#MAIN
main()

