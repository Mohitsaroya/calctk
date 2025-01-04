from tkinter import *

root = Tk()

root.title("Calculator")
root.geometry("300x500")
root.resizable(False, False)



one = Button(root, text="1", padx= 30, pady=16)
one.grid(row=2, column=0)
two = Button(root, text="2", padx= 30, pady=16)
two.grid(row=2, column=1)
three = Button(root, text="3", padx= 30, pady=16)
three.grid(row=2, column=2)

root.mainloop()