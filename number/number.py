class Number:
    def __init__(self, value):
        self._value = str(float(value))
        self._number_of_decimal = self._value[::-1].find('.')
        self._number_list = [int(self._value.split('.')[0]) if int(self._value.split('.')[0]) <= 0 else int(self._value.split('.')[0]), int(self._value.split('.')[1])]
        self._decimal_signe = None
        self._signe = '-' if value < 0 else None
        self._number_final = []
        
    def __str__(self):
        return self._value
    
    # ---------- Addition ----------
    def __add__(self, other):  # sourcery skip: low-code-quality
        self._get_max_decimal(other)
        self._add_zeros(other)

        self._decimal_signe = self._number_list[1] if float(self._value) > 0 else -self._number_list[1]
        other._decimal_signe = other._number_list[1] if float(other._value) > 0 else -other._number_list[1]

        # positif - positif
        if self._number_list[0] > 0 and other._number_list[0] > 0:
            self._number = self._number_list[0] + other._number_list[0]
            self._decimal = self._number_list[1] + other._number_list[1]

            if self._decimal >= 10**self._max_decimal_n:
                self._decimal = int(str(self._decimal)[1:])
                self._number += 1
        elif self._number_list[0] < 0 and other._number_list[0] < 0:
            self._number = abs(self._number_list[0]) + abs(other._number_list[0])
            self._decimal = self._number_list[1] + other._number_list[1]

            if self._decimal >= 10**self._max_decimal_n:
                self._decimal = int(str(self._decimal)[1:])
                self._number += 1
            self._number = -self._number
        elif self._number_list[0] == 0 or other._number_list[0] == 0:
            self._find_signe(other)
            self._number = self._number_list[0] + other._number_list[0]
            self._decimal = self._decimal_signe + other._decimal_signe

            print(self._number, self._decimal)
            
            if self._decimal < 0:
                if self._number < 0:
                    self._number = self._number
                    self._decimal = self._decimal
                elif self._number > 0:
                    self._number -= 1
                    self._decimal = 10**self._max_decimal_n - abs(self._decimal)
            elif self._decimal > 0:
                self._number += 1
                self._decimal = int(str(self._decimal)[1:])
        else:
            self._find_signe(other)
            self._number = abs(self._number_list[0]) - abs(other._number_list[0])
            self._decimal = abs(self._decimal_signe) - abs(other._decimal_signe)

            if self._decimal < 0:
                if self._number < 0:
                    self._number = self._number
                    self._decimal = self._decimal
                elif self._number > 0:
                    self._number -= 1
                    self._decimal = 10**self._max_decimal_n - abs(self._decimal)
        self._number_final = [str(self._number), self._complete_zeros(self._decimal)]
        return self._number_final

    # ---------- Subtraction ----------
    def __sub__(self, other):
        pass
            
    
    # ---------- Other Methods ----------
    def _complete_zeros(self, decimal):
        self._decimal_zeros = abs(self._decimal)
        while len(str(self._decimal_zeros)) != self._max_decimal_n:
            self._decimal_zeros = f'0{self._decimal_zeros}'
        return str(self._decimal_zeros)
    
    def _find_signe(self, other):
        self._number1 = float(self._value)
        self._number2 = float(other._value)
        if abs(self._number1) > abs(self._number2):
            self._signe = self._signe
        elif abs(self._number2) > abs(self._number1):
            self._signe = other._signe
    
    def _get_max_decimal(self, other):
        self._max_decimal_n = max(self._number_of_decimal, other._number_of_decimal)

    def _add_zeros(self, other):
        if self._number_list[1] != 0:
            while len(str(self._number_list[1])) != self._max_decimal_n:
                self._number_list[1] = int(f'{str(self._number_list[1])}0')
        if other._number_list[1] != 0:
            while len(str(other._number_list[1])) != self._max_decimal_n:
                other._number_list[1] = int(f'{str(other._number_list[1])}0')
    

n1 = Number(-0.2)
n2 = Number(-1.91)
print(n1 + n2)