import tkinter as tk
import tkinter.ttk as ttk

from input import Input
from output import Output
from insertion_sort import insertionSort
from pop_up import popUp

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.geometry('500x400')

        self.inp = Input(self)  
        self.sort_btn = ttk.Button(self, text='Sort', command=self.sort)
        self.return_btn = ttk.Button(self, text='Return', command=self.new_input)

        self.menu = tk.Menu(self)
        self.menu.add('command', label='Instructions', command=self.instructions)
        self.menu.add('command', label='About', command=self.about)

        self.config(menu=self.menu)

        self.inp.pack(pady=(75, 0))
        self.sort_btn.pack()

    def sort(self):
        try:
            unsorted_list = list(map(float, self.inp.get_numbers().split(',')))
            sorted_list = insertionSort.insertion_sort(unsorted_list)
            self.out = Output(self, sorted_list)
            self.inp.pack_forget()
            self.sort_btn.pack_forget()
            self.out.pack(pady=(75, 0))
            self.return_btn.pack(pady=(20, 0))
        except ValueError as e:
            p = popUp(
                self, mode='error', title='Error', message='An error has been occurred:\n{}'.format(e)
            )

    def new_input(self):
        self.out.pack_forget()
        self.return_btn.pack_forget()
        self.inp = Input(self)
        self.inp.pack(pady=(75, 0))
        self.sort_btn.pack()

    def instructions(self):
        p = popUp(
            self, mode='instruction', title='Instrucions', message='''  1. Use numbers not letters.
  2. Seperate each number using a ","(comma).'''
        )

    def about(self):
        p = popUp(
            self, mode='info', title='About', message='''
  An experimental small project created by
  Seyed Amirhossein Misaghi
  CE student University of Guilan
  Summer 1400'''
        )
        
if __name__ == '__main__':
    app = App()
    app.mainloop()