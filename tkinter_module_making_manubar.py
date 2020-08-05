from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master=master

        self.init_window()

    def init_window(self):
        self.master.title("First GUI")
        self.pack(fill=BOTH, expand=1)
        
        menu1 = Menu(self.master)
        self.master.config(menu=menu1)
        file1=Menu(menu1)
        file1.add_command(label='New',command=self.client_new)
        file1.add_command(label='Exit',command=self.client_exit)        
        menu1.add_cascade(label='File',menu=file1)

    def client_exit(self):
        exit()

    def client_new(self):
        print('hello')
    

root = Tk()
root.geometry("400x300")

app=Window(root)

root.mainloop()
