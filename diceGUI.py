import dice as die
import tkinter


class DiceGUI(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.winfo_toplevel().title("Dice Roller")
        self.num_dice = tkinter.Entry(master)
        self.roll_dice = tkinter.Button(master, text="Roll Dice", command=self.throw_dice)
        self.num_label = tkinter.Label(master, text="Number of Dice")
        self.num_label.pack()
        self.num_dice.pack()
        self.sides_label = tkinter.Label(master, text="Number of Sides on Dice")
        self.sides_label.pack()
        self.dice_sides = tkinter.Entry(master)
        self.dice_sides.pack()
        self.quit = tkinter.Button(master, text="QUIT", fg="red", command=root.destroy)
        self.roll_dice.pack()
        self.result_string = ""
        self.results = tkinter.Label(master, text=self.result_string)
        self.results.pack()
        self.quit.pack(side="bottom")
        self.pack()

    def throw_dice(self):
        dice = []
        self.result_string = ''
        for each in range(int(self.num_dice.get())):
            dice.append(die.Dice(int(self.dice_sides.get())))
        for d in dice:
            self.result_string += str(d.roll())
        self.results["text"] = self.result_string


if __name__ == '__main__':
    root = tkinter.Tk()
    window = DiceGUI(master=root)
    window.mainloop()
