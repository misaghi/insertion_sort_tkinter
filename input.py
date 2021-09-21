import tkinter as tk
import tkinter.ttk as ttk

class Input(ttk.Frame):

    def __init__(self, master=None, **kw):
        super().__init__(master=master, **kw)

        self.image = tk.PhotoImage(file='assets/pictures/warning.png')

        self.menu = tk.Menu(self, tearoff=False)
        self.menu.add_command(label='Copy', command=self.copy)
        self.menu.add_command(label='Cut', command=self.cut)
        self.menu.add_command(label='Paste', command=self.paste)
        self.menu.add_command(label='Delete', command=self.delete)

        ttk.Label(
            self, text='Please use menu bar to access instructions.\nRead instructions first.', foreground='red',
            image=self.image, compound=tk.LEFT
        ).pack(anchor=tk.W, pady=20)
        ttk.Label(
            self, text='Please enter numbers:'
        ).pack(anchor=tk.W, padx=20, pady=(0, 5))

        self.text_area = tk.Text(self, background='white', height=5, width=46)
        self.text_area.bind('<Button-3>', self.post_menu)
        self.text_area.bind('<Button-1>', self.hide_menu)

        self.text_area.pack(pady=(0, 20))

    def get_numbers(self) -> str:
        return self.text_area.get(1.0, tk.END)

    def post_menu(self, event):
        '''Creates a menu with mouse right click button.
        '''
        self.menu = tk.Menu(self, tearoff=False)
        self.menu.add_command(label='Copy', command=self.copy)
        self.menu.add_command(label='Cut', command=self.cut)
        self.menu.add_command(label='Paste', command=self.paste)
        self.menu.add_command(label='Delete', command=self.delete)
        self.menu.post(event.x_root, event.y_root)

    def hide_menu(self, event):
        '''Destroys the right clicked generated menu.
        '''
        self.menu.destroy()
    
    def copy(self):
        select_range = self.text_area.tag_ranges(tk.SEL)
        if select_range:
            self.clipboard_clear()
            self.clipboard_append(self.text_area.get(*select_range))

    def delete(self):
        select_range = self.text_area.tag_ranges(tk.SEL)
        if select_range:
            self.text_area.delete(*select_range)
    
    def cut(self):
        self.copy()
        self.delete()

    def paste(self):
        try:
            self.text_area.insert(tk.INSERT, self.clipboard_get())
        except tk.TclError:
            pass

if __name__ == '__main__':
    root = tk.Tk()
    i = Input(root)
    i.pack()
    root.mainloop()