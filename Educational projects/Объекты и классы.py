class instruments_for_art: #Создание класса instruments_for_art. Если проще, есть инструменты для рисования
    pass # Pass мы пишем, пока никаких функций туда не записываем. Если проще, просто класс, который ничего не выполняет или конец функций, которые он выполняет
class pens(instruments_for_art): #Создание подкласса pens суперкласса instruments_for_art . Если проще, Ручка - это инструмент для рисования
    pass
# Ручки у нас бывают разных цветов, допустим красная и синяя. И красная и синяя ручка - это ручки, тоесть относятся к классу ручки.
class red_pens(pens):#Создание подкласса red_pens суперкласса pens . Если проще, Красная Ручка - это естественно ручка, тоесть относятся к классу ручки.
    pass
class blue_pens(pens):#Создание подкласса blue_pens суперкласса pens . Если проще, Cиняя Ручка - это естественно ручка, тоесть относятся к классу ручки.
    pass
class pensils(instruments_for_art):#Создание подкласса pensils. Если проще, Карандаш - это тоже инструмент для рисования
    #Допустим, карандаши бывают разные по степени наточенности, поэтому мы своиство острота сейчас добавим
    def __init__(self,ostrota): #это Херня ваще не разбирайса просто мы к карандашу добавили своиство острота
        self.ostriy = 0
        self.ostriy = ostrota
    
    pass



#После написанного выше, можно теперь заниматься творчеством
#Теперь мы можем с нуля создать какой то объект
object0 = blue_pens()# Мы создали переаменную object0 и определили ее в подкласс blue_pens.Проще говоря , Этот объект теперь синяя ручка.
# И прикол в том, что синяя ручка относится к 3 классам:синяя ручка, ручка и инструменты для рисования
#Создадим карандашик и пусть по степени наточенности он будет 5 из 10
object1 = pensils(5)
# и это карандаш со степению наточенности 5
