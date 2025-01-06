from tkinter import *
from operations import Operations

class Calculatortk():
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        self.screen = self.display_screen()
        self.buttons = self.buttons_on_display()
        
    
    def display_screen(self):
        screen = Entry(self.root, font=("Courier New", 24), width=14, borderwidth=0.5, justify=CENTER)
        screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        return screen
        
    def buttons_on_display(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        
        for (text, row, col) in buttons:
            button = Button(self.root, text=text, padx=30, pady=16, font=("Courier", 16), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=1, pady=4)
    
    def on_button_click(self, text):
        if text == 'C':
            self.screen.config(state=NORMAL)
            self.screen.delete(0, END)
            self.screen.config(state='readonly')
        elif text == '=':
            pass
        else:
            self.screen.config(state=NORMAL)
            self.screen.insert(END, text)
            self.screen.config(state='readonly')
    
root = Tk()
app = Calculatortk(root)
root.mainloop()