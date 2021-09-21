import tkinter as tk
import tkinter.ttk as ttk

class popUp(tk.Toplevel):
    '''A custom pop window class. Use 'mode' arg to specify the use.
    mode='info'|'instruction'|'error'
    '''

    def __init__(self, master, mode, title, message):
        super().__init__(master=master)

        self.title(title)
        self.img = tk.PhotoImage()
        
        self.choose_picture(mode)

        ttk.Label(self, image=self.img, text=message, compound=tk.LEFT).pack(padx=20, pady=20)
        ttk.Button(self, text='OK', command=self.close).pack(anchor=tk.E, padx=20, pady=20)
    
    def choose_picture(self, mode):
        if mode == 'info':
            self.img.config(file='assets/pictures/info.png')
        elif mode == 'instruction':
            self.img.config(file='assets/pictures/instruction.png')
        elif mode == 'error':
            self.img.config(file='assets/pictures/no_entry.png')

    def close(self):
        self.destroy()