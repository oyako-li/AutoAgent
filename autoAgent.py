import tkinter as tk
import tkhtmlview
import logger
import activator

class AutoAgent:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('AutoAgent')
        self.root.geometry('100x100')

        self.start_button = tk.Button(text="Start", command=self.logging)
        self.start_button.place(x=50, y=50)



    def logging(self):
        self.root.iconify()
        self.logname = logger.logger()
        print("logger is stopped")
        self.sub_win = self.sub_window()

    def activating(self):
        self.root.iconify()
        activator.activator(self.logname)
        print("logger is stopped")
        self.root.deiconify()
        self.root.wm_state('normal')
        
    def start(self):
        self.root.mainloop()

    def sub_window(self):
        sub_win = tk.Toplevel()
        sub_win.geometry("300x100")
        label_sub = tk.Label(sub_win, text="sub")
        activate_button = tk.Button(sub_win, text="activate", command=self.activating)
        activate_button.place(x=100, y=50)
        
        label_sub.pack()
        return sub_win

if __name__ == '__main__':
    autoagent = AutoAgent()
    autoagent.start()