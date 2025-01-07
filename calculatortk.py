from tkinter import *

class Calculatortk():
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x430")
        self.root.resizable(False, False)
        
        self.screen = self.display_screen()
        self.buttons = self.buttons_on_display()
        
    def display_screen(self):
        screen = Entry(self.root, font=("Courier New", 24), width=18, borderwidth=0.5, justify=RIGHT, state='normal')
        screen.grid(row=0, column=0, columnspan=4, padx=1, pady=1)
        return screen
        
    def buttons_on_display(self):
        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        
        for (text, row, col) in buttons:
            button = Button(self.root, text=text, padx=12, pady=14, font=("Courier", 16), width=4, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=1, pady=4)
    
    
    def on_button_click(self, text):
        
        input = ''
        
        if text == 'C':
            self.screen.config(state=NORMAL)
            self.screen.delete(0, END)
        
        if text in ['+', '-', '*', '/']:
            self.screen.config(state=NORMAL)
            self.operate(text)
            input += text
        elif text == '=':
            self.evaluate(input)
        else:
            self.screen.config(state=NORMAL)
            self.screen.insert(END, text)
            input += text
            
    def slicing(self, string):
        
        numbers = []
        operators = []
        temp = ''
        
        for i in string:
            if i.isdigit() or i == '.':
                temp += i
            else:
                if temp:
                    numbers.append(float(temp))
                    temp = ''
                operators.append(i)
        if temp:
            numbers.append(float(temp))
        
        return numbers, operators
                    
            
    
    def evaluate(self, expression):
        numbers, operators = self.slicing(expression)
        return self.operate(numbers, operators)
    
    def operate(self, number, operator):
        
        i = 0
        while i < len(operator):
            if operator[i] == '+':
                pass
            
            if operator == '-':
                pass
        
        i = 0
        while i < len(operator):
            if operator == '*':
                pass
            
            if operator == '/':
                pass
    
root = Tk()
app = Calculatortk(root)
root.mainloop()