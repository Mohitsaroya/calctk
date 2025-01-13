from tkinter import *

class Calculatortk():
    """
    This class creates a calculator using Tkinter. The calculator has a screen and buttons.
    The user can input numbers and operators using the buttons.
    The calculator can perform basic arithmetic operations such as addition, subtraction, multiplication, and division.
    The calculator also has a history feature that displays the history of the calculations. The history is saved in a stack data structure.
    The calculator has a toolbar that allows the user to view the history and exit the application.
    """
    def __init__(self, root):
        """
        This is the constructor of the class. It initializes the root window and the screen of the calculator

        Args:
            root (Tk): The root window of the Tkinter application.
        """
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x430")
        self.root.resizable(False, False)
        
        self.screen = self.display_screen()
        self.buttons = self.buttons_on_display()
        self.input = ''  
        self.stack = Stack()
        self.toolbar = Toolbar(self)
        
    def display_screen(self):
        """
        Displays the screen of the calculator. This is where the user sees the input and output.

        Returns:
            The display screen of the calculator.
        """
        screen = Entry(self.root, font=("Courier New", 24), width=18, borderwidth=0.5, justify=RIGHT)
        screen.grid(row=0, column=0, columnspan=4, padx=1, pady=1)
        return screen
        
    def buttons_on_display(self):
        """
        Displays the buttons on the calculator. The buttons are arranged in a 4x4 grid.
        
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
            button = Button(self.root, text=text, padx=12, pady=14, font=("Courier", 16),
                            width=4, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=1, pady=4)
    
    def on_button_click(self, text):
        """
        This method is called when a button is clicked. It updates the input on the screen.

        Args:
            text (str): The button text.

        Returns:
            None
        """
        if text == 'C':
            self.screen.config(state=NORMAL)
            self.screen.delete(0, END)
            self.input = []

        elif text == '=':
            self.screen.config(state=NORMAL)
            self.screen.delete(0, END)
            result = self.evaluate(self.input)
            
            if result.is_integer():
                result = int(result)
                self.stack.push(f'{self.input} = {result}')
            else:
                self.stack.push(f'{self.input} = {result}')
            self.screen.insert(END, result)
            self.input = str(result)  

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
        for index, char in enumerate(string):
            if char.isdigit() or char == '.':
                temp += char
            elif char == '-' and (index == 0 or string[index - 1] in "+-*/("):  
                temp += char
            else:
                if temp:
                    numbers.append(float(temp))
                    temp = ''
                operators.append(char)
        if temp:
            numbers.append(float(temp))

        return numbers, operators
    
    def operation(self, number1, number2, operator):
        """
        Perform a single arithmetic operation.

        Args:
            number1 (float): The first number.
            number2 (float): The second number.
            operator (str): The operator ('+', '-', '*', '/').

        Returns:
            float: The result of the operation.
            str: Error message if division by zero occurs.
        """
        if operator == '/':
            if number2 == 0:
                return "Error: Division by 0"
            return number1 / number2
        elif operator == '*':
            return number1 * number2
        elif operator == '+':
            return number1 + number2
        elif operator == '-':
            return number1 - number2
        else:
            return "Error: Invalid operator"

    def operate(self, numbers, operators):
        """
        Perform a series of operations on numbers based on the operators.

        Args:
            numbers (list): List of numbers to be operated on.
            operators (list): List of operators to be used.

        Returns:
            numbers[0]: The result of the operations.
        """
        i = 0
        while i < len(operators):
            result = self.operation(numbers[i], numbers[i + 1], operators[i])
            numbers[i:i + 2] = [result]  
            operators.pop(i) 
        return numbers[0]


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
    
    def display_history(self):
        """
        Displays the history of the calculations onto a new window.
        
        Returns: None
        """
        history = self.stack.items()
        history_window = Toplevel(self.root)
        history_window.title("History")
        history_window.geometry("300x400")
        
        history_text = Text(history_window, wrap=WORD)
        history_text.pack(expand=True, fill=BOTH)
        
        for item in history:
            history_text.insert(END, item + '\n')
        
        history_text.config(state=DISABLED)
    
    def clear_history(self):
        if self.stack.is_empty():
            return
        self.stack = Stack()
        
class Toolbar(Frame):
    def __init__(self, parent):
        """
        This is the constructor of the class. It initializes the toolbar of the calculator.
        
        Args:
            parent (Calculatortk): The parent class of the toolbar.
        """
        super().__init__(parent.root)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        """
        Initializes the toolbar of the calculator.
        """
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        Option = Menu(menubar)
        menubar.add_cascade(label="Options", menu=Option)
        submenu = Menu(Option)

        Option.add_cascade(label="History", menu=submenu, underline=0)
        submenu.add_command(label="Display History", underline=0, command=self.parent.display_history)
        submenu.add_command(label="Clear History", underline=0, command=self.parent.clear_history)
        
        Option.add_command(label="Exit", underline=0, command=self.onExit)
    
    def onExit(self):
        """
        Exits the application.
        """
        self.parent.root.quit()


class Stack():
    """
    This class creates a stack data structure. The stack is used to store the history of the calculations.
    """
    def __init__(self):
        """
        This is the constructor of the class. It initializes the stack.
        """
        self.stack = []
    
    def push(self, item):
        """
        Pushes an item onto the stack.

        Args:
            item (string): The item to be pushed onto the stack.
        """
        self.stack.append(item)
    
    def pop(self):
        """
        Pops an item from the stack.

        Returns:
            string : The item popped from the stack.
        """
        if not self.is_empty():
            return self.stack.pop()
    
    def is_empty(self):
        """
        Checks if the stack is empty.
        
        Returns:
            Bool : True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0
    
    def items(self):
        """
        Returns the items in the stack.

        Returns:
            list : The items in the stack.
        """
        return self.stack


if __name__ == '__main__':
    root = Tk()
    app = Calculatortk(root)
    root.mainloop()