class Number:
    def __init__(self, value):
        self._value = str(float(value))
        self._number_of_decimal = self._value[::-1].find('.')
        self._number_list = [int(self._value.split('.')[0]) if int(self._value.split('.')[0]) <= 0 else int(self._value.split('.')[0]), int(self._value.split('.')[1])]
        self._decimal_signe = self._number_list[1] if self._number_list[0] > 0 else -self._number_list[1]
        self._number_final = []
        
    def __str__(self):
        return self._value
    
    # ---------- Addition ----------
    def __add__(self, other):  # sourcery skip: low-code-quality
        self._get_max_decimal(other)
        self._add_zeros(other)
        
        # positif - positif
        if self._number_list[0] >= 0 and other._number_list[0] >= 0:
            self._number = self._number_list[0] + other._number_list[0]
            self._decimal = self._number_list[1] + other._number_list[1]

            if self._decimal >= 10**self._max_decimal_n:
                self._decimal = int(str(self._decimal)[1:])
                self._number += 1
        # negatif - negatif
        elif self._number_list[0] < 0 and other._number_list[0] < 0:
            self._number = abs(self._number_list[0]) + abs(other._number_list[0])
            self._decimal = self._number_list[1] + other._number_list[1]
            
            if self._decimal >= 10**self._max_decimal_n:
                self._decimal = int(str(self._decimal)[1:])
                self._number += 1
            self._number = -self._number
        # positif - negatif | negatif - positif
        else:
            self._find_signe(other)
            self._number = abs(self._number_list[0]) - abs(other._number_list[0])
            self._decimal = abs(self._decimal_signe) - abs(other._decimal_signe)
            
        
        return self._number, self._decimal

    # ---------- Subtraction ----------
    def __sub__(self, other):
        pass
            
    
    # ---------- Other Methods ----------
    def _find_signe(self, other):
        self._number1 = float(f'{self._number_list[0]}.{self._number_list[1]}')
        self._number2 = float(f'{other._number_list[0]}.{other._number_list[1]}')
        if abs(self._number1) > abs(self._number2):
            if self._number1 < 0:
                self._signe = '-'
        elif self._number2 < 0:
            self._signe = '-'
    
    def _get_max_decimal(self, other):
        self._max_decimal_n = self._number_of_decimal if self._number_of_decimal > other._number_of_decimal else other._number_of_decimal

    def _add_zeros(self, other):
        if self._number_list[1] != 0:
            while len(str(self._number_list[1])) != self._max_decimal_n:
                self._number_list[1] = int(f'{str(self._number_list[1])}0')
        if other._number_list[1] != 0:
            while len(str(other._number_list[1])) != self._max_decimal_n:
                other._number_list[1] = int(f'{str(other._number_list[1])}0')
    

n1 = Number(10)
n2 = Number(-18.3)
print(n1 + n2)