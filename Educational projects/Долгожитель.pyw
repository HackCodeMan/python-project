from tkinter import *
class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        # Создание метки
        self.inst_lbl = Label(self, text = "Чтобы узнать секрет долголетия, введите пароль")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = N)
        self.pasword_lbl = Label(self, text="Пароль:")
        self.pasword_lbl.grid(row=1, column=0, sticky=W)
        # row - строка, column - столбец, columnspan - сколько столбцов занимает объект
        # sticky - Выравнивание: N - вверх,S - вниз, E - вправо, W - влево
        #Создание Поля для ввода
        self.wr_field = Entry(self)
        self.wr_field.grid(row = 1, column = 1, sticky = W)
        # создание кнопки
        self.bttn_submit = Button(self, text= "Узнать секрет")
        self.bttn_submit["command"] = self.reveal
        self.bttn_submit.grid(row = 2, column = 0, sticky = W)
        # Создание текста
        self.secret_txt = Text(self, width= 35, height= 5, wrap = WORD)
        #width - Ширина, height - высота, wrap - Механизм переноса текста:
        #WORD - по слову, CHAR - по символьно, NONE - не переносит
        self.secret_txt.grid(row=3,column=0,columnspan=2,sticky= W)
    def reveal(self):
        contents = self.wr_field.get()
        if contents == "GUI":
            text = "Доживи до 99, а потом живи очень аккуратно"
        else:
            text = "Неверный пароль"
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, text)
        pass
def main():
    """Main program"""
    root = Tk()
    root.title("Долгожитель")
    app = Application(root)
    mainloop()


main()
