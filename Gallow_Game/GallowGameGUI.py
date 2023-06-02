import tkinter as tk
from files.modules.mGallowGame import Game, Gallow, Player
class InputTerminal(tk.Frame):
    def __init__(self, master,game,stateGallow: tk.Frame):
        super().__init__(master, background= "cornsilk3",width = 350, height = 400, relief="groove",borderwidth=5)
        self.game = game
        self.stateGallow = stateGallow
        self.pack_propagate(0)
        self.create_widgets()
    def create_widgets(self):
        self.letinput = tk.Entry(self, width= 45,highlightthickness= 12)
        self.letinput.pack(ipady= 5, pady= 15)
        self.letinput.focus()
        self.bttnlet = tk.Button(self, text = "Check letter", font=("Arial",13), width= 15, command= self.checkletter)
        self.bttnlet.pack()
        self.lblLetCheck: tk.Label = tk.Label(self, text= "Something text",background = "cornsilk3" ,foreground= "red", font=("Arial",13))
        self.lblLetCheck.pack(pady = 15)
    def checkletter(self):
        letter = self.letinput.get().upper()
        if letter != "":
            IsInWord = self.game.processLetter(letter)[0]
            if IsInWord:
                self.lblLetCheck.config(text= "Well done! This letter is in the word!", foreground = "green")
            else:
                self.lblLetCheck.config(text = "Unfortunately, this letter is not in the word", foreground = "red")
            self.stateGallow.GUIgame.config(text = self.game.__str__())
        self.letinput.delete(0,tk.END)
class GuiGallow(tk.Frame):
    def __init__(self, master, game):
        super().__init__(master, background= "thistle", width= 350, height = 400)
        self.game = game
        self.grid_propagate(0)
        self.create_widgets()
    def create_widgets(self):
        self.GUIgame: tk.Label = tk.Label(self, text = self.game.__str__()
                                                    , justify = tk.LEFT,foreground= "black"
                                                    , font= ("Arial",18), background = "thistle")
        self.GUIgame.grid()
        pass
class GamePlay(tk.Frame):
    def __init__(self, master, game):
        super().__init__(master)
        self.grid()
        self.guiGallow = GuiGallow(master, game)
        self.guiGallow.grid(row =0, column=0)
        self.inputTerminal = InputTerminal(master,game, self.guiGallow)
        self.inputTerminal.grid(row = 0, column= 1, sticky = tk.N+tk.S+tk.W+tk.E)
        pass
def main_gameGUI():
    window = tk.Tk()
    window.title("GALLOW GAME")
    window.geometry("700x400")
    window.resizable(0,0)
    game = Game(Gallow(),Player())
    game.create_HidWord("Посудомойчная машина".upper())
    gameplay = GamePlay(window,game)
    tk.mainloop()
if __name__ == "__main__":
    main_gameGUI()
