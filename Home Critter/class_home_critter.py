import random
import sys
from Guess_the_number_for_critters import quess_the_number


class Critters:
    """Virtual Critter"""
    def __init__(self,name):
        self.__name = name
        self.__energy = 0
        self.__coin = 100
        print("Создана новая зверюшка")
        print("Её имя", self.__name)

    def __str__(self):
        rep = "\nЗверюшка " + self.__name + ":"
        rep += "\n\t-Энергия: " + str(self.__energy)
        rep += "\n\t-Монеток: " + str(self.__coin)
        rep += "\n\t-Его самочувствие: " + self.mood_for_display("setval") + "\n"
        return  rep

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Нельзя оставить поле пустым!!")
            return
        else:
            print("Хорошо", self.__name, "теперь", end= "")
            self.__name = new_name
            print(self.__name)

    @property
    def __mood(self):
        budget_size = None
        if 0 <= self.__coin <= 100:
            budget_size = 0
        elif 100 < self.__coin <= 200:
            budget_size = 1
        elif 200 < self.__coin <= 300:
            budget_size = 2
        elif 300 < self.__coin <= 400:
            budget_size = 3
        elif self.__coin > 400:
            budget_size = 4
        return self.__energy + budget_size

    def mood_for_display(self, mode = "disp"):
        """display mood 'disp' or 'setval'"""
        if mode == "disp":
            if self.__mood <= 3:
                print("Мне очень плохо, хозяин")
            elif 3 < self.__mood <= 5:
                print("Я в норме, хозяин")
            elif 5 < self.__mood <= 8:
                print("Мне хорошо, хозяин")
        elif mode == "setval":
            mood = None
            if self.__mood <= 3:
                mood = "Ему очень плохо"
            elif 3 < self.__mood <= 5:
                mood = "Он в норме"
            elif 5 < self.__mood <= 8:
                mood = "Ему хорошо"
            return mood

    def __coin_change(self, mode):
        """Change coins mode 'u' or 'l'"""
        if mode == "u":
            self.__coin += 120
        if mode == "l":
            if self.__coin >= 100:
                self.__coin -= 100
            else:
                print("У МЕНЯЯ НЕТТТ ДЕНЯЯЯК")



    def __energy_change(self, mode):
        """low or up the played enough"""
        if mode == "l":
            if self.__energy > 0:
                self.__energy -= 1
            else:
                print("Я не могу потратить энергию")
                return
        elif mode == "u":
            if 0 <= self.__energy:
                self.__energy += 1
            else:
                print("Я не могу добавить энергию")

    def eating(self):
        """Critter eating and add energy"""
        if self.__coin >= 100:
            self.__coin_change("l")
            self.__energy_change("u")
        else:
            print("Не могу поесть, хозяин")
            return

    __GAMES_NUMBER = (1,)
    def play(self):
        """Users play games with Critter"""
        if  0 < self.__energy <= 4:
            self.__energy_change("l")
        else:
            print("Я не могу поиграть")
            return

        game_number = random.choice(Critters.__GAMES_NUMBER)
        if game_number == 1:
            quess_the_number()
            print("ООО ты поиграл со мной. Я рада!")
        self.__coin_change("u")