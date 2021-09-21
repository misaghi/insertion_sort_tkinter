import tkinter as tk
import tkinter.ttk as ttk

class Output(ttk.Frame):

    def __init__(self, master, steps):
        super().__init__(master=master)

        self.steps = steps
        self.current_step = 0
        self.text_area = tk.Text(self, background='white', width=55, height=5)
        self.left_btn = ttk.Button(self, text='<', command=self.previous_step)
        self.right_btn = ttk.Button(self, text='>', command=self.next_step)

        self.show_step_0()
        self.text_area.tag_config('moved', foreground='red')

        self.text_area.grid(row=0, column=0, padx=20, pady=20, columnspan=2)
        self.left_btn.grid(padx=20, row=1, column=0, sticky=tk.W)
        self.right_btn.grid(padx=20, row=1, column=1, sticky=tk.E)

    def next_step(self):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.insert_step()

    def previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            if self.current_step == 0:
                self.show_step_0()
            else:
                self.insert_step()
    
    def insert_step(self):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        step, tag_point_1, tag_point_2 = self.get_points(self.steps[self.current_step])
        self.text_area.insert(1.0, step)
        tag_point_1 = '1.' + str(tag_point_1)
        tag_point_2 = '1.' + str(tag_point_2)
        self.text_area.tag_add('moved', tag_point_1, tag_point_2)
        self.text_area.config(state=tk.DISABLED)

    def get_points(self, step:str):
        '''Returns the points which tags must be entered. Also it will prepare our step
        for insertion.
        '''
        start_point_1 = step.find("'*', ", 0)
        end_point = start_point_1 + 5
        step = step[:start_point_1] + step[end_point:]
        start_point_2 = step.find("'*', ", end_point)
        if start_point_2 < 0:
            start_point_2 = len(step) - 6
        else:
            start_point_2 -= 2 # This minus 2 is needed for correct coloring.
        end_point = start_point_2 + 5
        step = step[:start_point_2] + step[end_point:]

        return step, start_point_1, start_point_2

    def show_step_0(self):
        '''Insert the unsorted list into the Text widget.
        '''
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(1.0, self.steps[0])
        self.text_area.config(state=tk.DISABLED)