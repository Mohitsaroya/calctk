from tkinter import *
from operations import Operations

class Calculatortk():
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.buttons_on_display()
        
    def buttons_on_display(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),]
        
        for (text, row, col) in buttons:
            button = Button(self.root, text=text, padx=30, pady=16, font=("Arial", 16), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
    
    def on_button_click(self, text):
        print(f"Button {text} clicked")
    
            
root = Tk()

app = Calculatortk(root)

root.mainloop()