from tkinter import *

class Calculatortk():
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x430")
        self.root.resizable(False, False)
        
        self.screen = self.display_screen()
        self.buttons = self.buttons_on_display()
        self.input = ''  
        
    def display_screen(self):
        """displays the screen of the calculator. This is where the user sees the input and output.

        Returns:
            The display screen of the calculator.
        """
        screen = Entry(self.root, font=("Courier New", 24), width=18, borderwidth=0.5, justify=RIGHT, state='normal')
        screen.grid(row=0, column=0, columnspan=4, padx=1, pady=1)
        return screen
        
    def buttons_on_display(self):
        """
        displays the buttons on the calculator. The buttons are arranged in a 4x4 grid.
        
        Returns:
            The buttons on the calculator.
        """
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
        """
        This method is called when a button is clicked. It updates the input on the screen.
        
        returns:
            None
        """
        if text == 'C':
            self.screen.config(state=NORMAL)
            self.screen.delete(0, END)
            self.input = ''  
        
        elif text == '=':
            self.screen.config(state=NORMAL)
            self.screen.delete(0, END)
            result = self.evaluate(self.input)
            self.input = ''  
            self.screen.insert(END, result)
        
        else:
            self.screen.config(state=NORMAL)
            self.screen.insert(END, text)
            self.input += text  

            
    def slicing(self, string):
        """
        Slices the string into numbers and operators.

        Args:
            string (string): input string

        Returns:
            numbers (list): numbers in the form of list
            operators (list): operators in the form of list
        """
        
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
    
    def operate(self, number, operator):
        """
        This method performs the operations on the numbers.

        Args:
            number (list): list of numbers to be operated. the list is generated by the slicing method.
            operator (list): list of operators to be operated. the list is generated by the slicing method.

        Returns:
            number[0]: the result of the operation. In the form of a float.
        """
        
        i = 0
        
        while i < len(operator):
            if operator[i] == '/':
                if number[i+1] == 0:
                    return "Error:0 Division"
                result = number[i] / number[i+1]
                number[i:i+2] = [result]
                operator.pop(i)
            elif operator[i] == '*':
                result = number[i] * number[i+1]
                number[i:i+2] = [result]
                operator.pop(i)
            else:
                i += 1
        
        i = 0
        
        while i < len(operator):
            if operator[i] == '+':
                result = number[i] + number[i+1]
                number[i:i+2] = [result]
                operator.pop(i) 
            elif operator[i] == '-':
                result = number[i] - number[i+1]
                number[i:i+2] = [result]
                operator.pop(i)
        
        return number[0]
    
    def evaluate(self, expression):
        """
        Evaluates the expression.

        Args:
            expression (string): takes the expression as input. after slicing the expression, it is passed to the operate method.

        Returns:
            result (floaf): returns the result of the expression.
        """
        numbers, operators = self.slicing(expression)
        result = self.operate(numbers, operators)
        return result
    
root = Tk()
app = Calculatortk(root)
root.mainloop()