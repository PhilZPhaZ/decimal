class Number:
    def __init__(self, value):
        self._value = str(float(value))
        self._number_of_decimal = self._value[::-1].find('.')
        self._number_list = [int(self._value.split('.')[0]), int(self._value.split('.')[1])]
    
    def __str__(self):
        return self._value
    
    # ---------- Addition ----------
    def __add__(self, other):
        # Create 0 
        self._max_decimal = self._get_max_decimal(other)
        self._add_zero(other)
        
        # Add the numbers
        self._number = self._number_list[0] + other._number_list[0]
        self._decimal = self._number_list[1] + other._number_list[1]
        
        if len(str(self._decimal)) > self._max_decimal:
            self._decimal = str(self._decimal)[1:]
            self._number += 1
            
        return f'{self._number}.{self._decimal}'
    
    # ---------- Subtraction ----------
    def __sub__(self, other):
        pass
            
    
    # ---------- Other Methods ----------
    def _get_max_decimal(self, other):
        return self._number_of_decimal if self._number_of_decimal > other._number_of_decimal else other._number_of_decimal

    def _add_zero(self, other):
        if self._number_list[1] != 0:
            while len(str(self._number_list[1])) != self._max_decimal:
                self._number_list[1] = int(f'{str(self._number_list[1])}0')
        elif other._number_list[1] != 0:
            while len(str(other._number_list[1])) != self._max_decimal:
                other._number_list[1] = int(f'{str(other._number_list[1])}0')
            

n1 = Number(2.7)
n2 = Number(10)

print(n1 - n2)