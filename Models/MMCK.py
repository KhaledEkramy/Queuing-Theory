import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import math
import SystemInputs

class MMCK:
    '''
    Methods:
        average_customers = L
        average_customers_queue = Lq
        average_wait = W
        average_wait_queue = Wq
        
    Constructor:
        sys_inputs (SystemInputs): The system inputs for the queueing model.
    '''
    def __init__(self, sys_inputs: SystemInputs):
        self._sys_inputs = sys_inputs
        self._r = self._sys_inputs.arrival_rate / self._sys_inputs.service_rate
        self._C = self._sys_inputs.num_of_servers
        self._K = self._sys_inputs.sys_capacity
        self._row = self._r / self._C
        self._p0 = self.calculate_p0()
        self._Lq = self.average_customers_queue()
        self._pk = self.calculate_pk()
        self._rho_dash = self._sys_inputs.arrival_rate * (1 - self._pk)
    @property
    def sys_inputs(self):
        return self._sys_inputs
        
    def calculate_p0(self):
        final_output = None
        summation = 0.0
        for n in range(self._C):
            summation += ((self._r ** n) / math.factorial(n))
        
        # r^c / c!
        left = (self._r ** self._C) / math.factorial(self._C)
        right = None    
        
        if self._row == 1:
            # (k - c + 1)
            right = self._K - self._C + 1
        else:
            # (1 - row^(k - c + 1)) / (1 - row)
            numerator = 1 - (self._row ** (self._K - self._C + 1))
            denumerator = 1 - self._row
            right = numerator / denumerator
        
        final_output = summation + left * right
        
        return final_output ** -1
    
    
    def calculate_pk(self):
        if self._row == 1:
            return 1/(self._K + 1)
        else:
            numerator = (1 - self._row) * (self._row ** self._K)
            denominator = 1 - (self._row ** (self._K + 1))
            return numerator / denominator
        
        
    def average_customers_queue(self):
        left_numerator = (self._r ** self._C) * self._p0  * self._row
        left_denumerator = math.factorial(self._C) * ((1 - self._row) ** 2)
        left = left_numerator / left_denumerator
        
        term1 = (self._row ** (self._K - self._C + 1))
        term2 = (1 - self._row) * (self._K - self._C + 1) * (self._row ** (self._K - self._C))
        right = (1 - term1 - term2)
        
        return left * right
    
    def average_customers(self):
        summation = 0.0
        for n in range(self._C):
            summation += ( (self._C - n) * ((self._r ** n) / math.factorial(n)) )
        return self._Lq + self._C - (self._p0 * summation)
    
    def average_wait_queue(self):
        return self._Lq / self._rho_dash
    
    def average_wait(self):
        return self.average_customers() / self._rho_dash
    
    
# Testing
def test():
    sys_in = SystemInputs.SystemInputs(1, 1/6, 3, 7)
    mmck = MMCK(sys_in)
    print('L = ' , mmck.average_customers())
    print('Lq = ' , mmck.average_customers_queue())
    print('W = ' , mmck.average_wait())
    print('Wq = ' , mmck.average_wait_queue())