class Comparable():
    def __init__(self, value):
        self._value = value
    
    def __eq__(self, other):    
        return self._value == other._value
    
    def __lt__(self, other):
        return self._value < other._value
    
    def __gt__(self, other):
        return self._value > other._value
    
    def __le__(self, other):
        return self._value <= other._value
    
    def __ge__(self, other):
        return self._value >= other._value
    
    def __ne__(self, other):
        return self._value != other._value
    
    def __str__(self):
        return str(self._value)
    
    def __repr__(self):
        return str(self._value)
    
    def __hash__(self):
        return hash(self._value)
    
