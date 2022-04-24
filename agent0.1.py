from distutils.log import Log
import tkinter as tk
from tkinter import messagebox
import tkhtmlview as tv
from logger import logger
from activator import activator
import time
import os

class Agent(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Agent')
        self.geometry('300x100')
        self.start_button = tk.Button(text="Start", command=self.logging)
        self.start_button.place(x=50, y=50)
        self.load_button = tk.Button(text="load", command=self.load)
        self.load_button.place(x=100, y=50)

    def logging(self):
        self.iconify()
        filename = time.strftime("%a,%d,%b,%Y,%H,%M,%S", time.gmtime())
        logger(filename)
        self.Actions(filename)

    def load(self):
        self.loader = tk.Toplevel()
        self.loader.title("loading")
        self.loader.geometry("300x100")
        self.load_entry = tk.Entry(self.loader)
        self.load_entry.bind('<Return>', self.pre_reload)
        self.load_entry.place(x=10, y=25)
        self.load_entry.focus()
        self.ok_button = tk.Button(self.loader, text="ok", command=self.reload)
        self.ok_button.place(x=100, y=50)

    def pre_reload(self, event):
        self.reload()

    def reload(self):
        try:
            filename = self.load_entry.get()
            open(f'./log/{filename}.log')
            self.iconify()
            self.Actions(filename)
            self.loader.destroy()


        except FileExistsError as err:
            tk.messagebox.showerror(title='Exeption', message=f'FileExistsError: {err}')
        except FileNotFoundError as err:
            tk.messagebox.showerror(title='Exeption', message=f'FileNotFoundError: {err}')

    def popup(self):
        self.deiconify()
        self.grab_set()
        

    class Actions:
        def __init__(self, _filename):
            self.sub = tk.Toplevel()
            self.sub.title(_filename)
            self.sub.geometry("300x100")
            self.action_button = tk.Button(self.sub, text="activate", command=self.action)
            self.action_button.place(x=100, y=50)
            self.rename_button = tk.Button(self.sub, text="rename", command=self.rename)
            self.rename_button.place(x=200, y=50)
            

        def action(self):
            self.sub.iconify()
            filename = self.sub.title()
            activator(filename)
            tk.messagebox.showinfo(title="Complete", message=f"{filename} was completed.")
            self.sub.deiconify()
            # self.sub.grab_set()
            
            
        def rename(self):
            self.re_name = tk.Toplevel()
            self.re_name.title("名前変更")
            self.re_name.geometry("300x100")
            self.name_entry = tk.Entry(self.re_name)
            self.name_entry.insert(0, self.sub.title())
            self.name_entry.bind('<Return>', self.pre_name)
            # self.name_entry.bind('<Button-1>', self.click_name)
            self.name_entry.place(x=10, y=25)
            self.name_entry.select_range(0, tk.END)
            self.name_entry.focus()
            self.ok_button = tk.Button(self.re_name, text="ok", command=self.name)
            self.ok_button.place(x=100, y=50)
            self.re_name.grab_set()

        def pre_name(self, event):
            self.name()

        # def click_name(self, event):


        def name(self):
            try:
                os.rename(f'./log/{self.sub.title()}.log', f'./log/{self.name_entry.get()}.log')
                self.sub.destroy()
                self.__init__(self.name_entry.get())
                self.re_name.destroy()

            except FileExistsError as err:
                tk.messagebox.showerror(title='Exeption', message=f'FileExistsError: {err}')
            



if __name__ == '__main__':
    agent = Agent()
    agent.mainloop()