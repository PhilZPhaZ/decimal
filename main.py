class Number:
    def __init__(self, value):
        self._value = str(value)
        self._number_of_decimal = self._value[::-1].find('.')
        self._number_list = [self._value.split('.')[0], self._value.split('.')[1]]
    
    def __str__(self):
        return self._value
    
    def __add__(self, other):
        return self.value + other.value

        
n1 = Number(0.1)
n2 = Number(0.2)

print(n2)