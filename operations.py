class Operations():
    def __init__(self, value):
        self._value = value
    
    def __add__(self, other):
        return self._value + other._value  
    
    def __sub__(self, other):
        return self._value - other._value
    
    def __mul__(self, other):
        return self._value * other._value
    
    def __truediv__(self, other):
        return self._value / other._value
    
    def __floordiv__(self, other):
        return self._value // other._value
    
    def __mod__(self, other):
        return self._value % other._value
    
    def __pow__(self, other):
        return self._value ** other._value
    
    