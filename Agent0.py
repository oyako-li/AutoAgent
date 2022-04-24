from distutils.log import Log
import tkinter as tk
import tkhtmlview as tv
from logger import logger
from activator6 import activator
import time

class Agent(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('AutoAgent')
        self.geometry('100x100')
        self.start_button = tk.Button(text="Start", command=self.logging)
        self.start_button.place(x=50, y=50)

    def logging(self):
        self.iconify()
        filename = time.strftime("%a,%d,%b,%Y,%H,%M,%S", time.gmtime())
        logger(filename)
        self.deiconify()
        self.Actions(filename)
        print(f"{filename} is stopped")

    class Actions:
        def __init__(self, _filename):
            self.sub = tk.Toplevel()
            self.sub.title(_filename)
            self.sub.geometry("300x100")
            self.action_button = tk.Button(self.sub, text="activate", command=self.action)
            self.action_button.place(x=100, y=50)
            

        def action(self):
            self.sub.iconify()
            filename = self.sub.title()
            print(filename)
            activator(filename)
            print(f"{filename} is complete.")
            self.sub.deiconify()
            self.sub.wm_state('normal')
            self.sub.attributes("-topmost", True)


if __name__ == '__main__':
    autoagent = Agent()
    autoagent.mainloop()