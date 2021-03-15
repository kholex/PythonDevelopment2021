import random as rnd
from tkinter import *
import tkinter.messagebox as msg

class App(Frame):
    def __init__(self):
        super().__init__(Tk())
        self.pack(expand=True, fill='both')

        for i in range(5):
            self.grid_rowconfigure(i, weight=1, uniform='row')
            if i < 4:
                self.grid_columnconfigure(i, weight=1, uniform='col')

        self.puzzles = []
        for i in range(1, 16):
            button = Button(self, text=str(i))
            button['command'] = lambda button=button, index=i-1: self.step(button, index)
            self.puzzles.append(button)

        Button(self,command=exit, text='Exit').grid(row=0, column=1, sticky=N+S+W+E)
        Button(self, command=self.new_game, text='New').grid(row=0, column=0, sticky=N+S+W+E)
        self.new_game()

    def new_game(self):
        self.pos = rnd.sample(list(range(16)), 16)
        for pos, button in zip(self.pos, self.puzzles):
            button.grid(row=pos // 4+1, column=pos % 4, sticky=N+S+W+E)

    def step(self, button, index):
        x_e, y_e = divmod(self.pos[-1], 4)
        x, y = divmod(self.pos[index], 4)
        if abs(x - x_e) + abs(y - y_e) > 1:
            return
        self.pos[index], self.pos[-1] = self.pos[-1], self.pos[index]
        button.grid(row=x_e+1, column=y_e, sticky=N+S+W+E)
        if self.pos == list(range(16)):
            msg.showinfo(message='You are winner!')

App().mainloop()
