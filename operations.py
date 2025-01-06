from comparable import Comparable

class Operations(Comparable): 
    def __init__(self, value):
        self.value = value 
    
    def __add__(self, other):
        return Operations(self.value + other.value)  
    
    def __sub__(self, other):
        return Operations(self.value - other.value)
    
    def __mul__(self, other):
        return Operations(self.value * other.value)
    
    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Cannot divide by zero")
        return Operations(self.value / other.value)
    
    def __floordiv__(self, other):
        return Operations(self.value // other.value)
    
    def __mod__(self, other):
        return Operations(self.value % other.value)
    
    def __pow__(self, other):
        return Operations(self.value ** other.value)
