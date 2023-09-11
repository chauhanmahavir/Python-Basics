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
        file1.add_command(label='New Files')
        file1.add_command(label='Open Files')
        file1.add_command(label='Save')
        file1.add_command(label='Save as')
        file1.add_command(label='Print')
        file1.add_command(label='Close')
        file1.add_command(label='Exit',command=self.client_exit)        
        menu1.add_cascade(label='File',menu=file1)

        edit1=Menu(menu1)
        edit1.add_command(label='Undo')
        edit1.add_command(label='Redo')
        edit1.add_command(label='Cut')
        edit1.add_command(label='Copy')
        edit1.add_command(label='Paste')
        edit1.add_command(label='Select All')
        edit1.add_command(label='Find')
        edit1.add_command(label='Replace')
        menu1.add_cascade(label='Edit',menu=edit1)

        format1=Menu(menu1)
        format1.add_command(label='Font Size')
        menu1.add_cascade(label='Format',menu=format1)

        run1=Menu(menu1)
        run1.add_command(label='Python Shell')
        run1.add_command(label='Check Module')
        run1.add_command(label='Run Module')
        menu1.add_cascade(label='Run',menu=run1)

        option1=Menu(menu1)
        option1.add_command(label='Configure IDEL')
        option1.add_command(label='Code Context')
        menu1.add_cascade(label='Option',menu=option1)

        help1=Menu(menu1)
        help1.add_command(label='About IDEL')
        help1.add_command(label='IDEL Help')
        help1.add_command(label='Python Docs')
        help1.add_command(label='Turtle Demo')
        menu1.add_cascade(label='Help',menu=help1)
        


    def client_exit(self):
        exit()

   
    

root = Tk()
root.geometry("400x300")

app=Window(root)

root.mainloop()
