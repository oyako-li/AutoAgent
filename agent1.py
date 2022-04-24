import tkinter as tk
import tkhtmlview as tv
from logger import logger
from activator6 import activator
from tkinter import messagebox
import time

class Agent(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('AutoAgent')
        self.geometry('300x300')
        self.start_button = tk.Button(text="録動", command=self.logging)
        self.start_button.place(x=50, y=50)
        self.actions = []

    def logging(self):
        self.iconify()
        filename = time.strftime("%a,%d,%b,%Y,%H,%M,%S", time.gmtime())
        logger(filename)
        print(f"{filename} is stopped")
        self.deiconify()
        self.wm_state('zoom')
        self.actions.append(filename)
        self.action_button = tk.Button(text="起動", command=self.actting)
        self.action_button.place(x=100, y=50)

    def actting(self):
        self.iconify()
        for action in self.actions:
            activator(action)
            print(f"{action} is complete.")
        
        self.deiconify()
        

    class Actions:
        def __init__(self, _filename):
            self.sub = tk.Toplevel()
            self.sub.title(_filename)
            self.sub.geometry("300x100")
            self.action_button = tk.Button(self.sub, text="activate", command=self.callback)
            self.action_button.place(x=100, y=50)
            

        def callback(self):
            self.sub.iconify()
            filename = self.sub.title()
            print(filename)
            activator(filename)
            print(f"{filename} is complete.")
            self.sub.deiconify()
            self.sub.attributes("-topmost", True)


if __name__ == '__main__':
    autoagent = Agent()
    autoagent.mainloop()