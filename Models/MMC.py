import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import math
import SystemInputs

class MMC:
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
        self._C = self._sys_inputs._num_of_servers
        self._row = self._r / self._C
        self._p0 = self.calculate_p0()
        self._Lq = self.average_customers_queue()
        
        
    @property
    def sys_inputs(self):
        return self._sys_inputs
        
    def calculate_p0(self):
        final_output = None
        if self._row < 1:
            summation = 0.0
            for n in range(self._C):
                summation += ((self._r ** n) / math.factorial(n))
            final_output = summation + ((self._C * (self._r ** self._C)) / (math.factorial(self._C) * (self._C - self._r)))
        else:
            summation = 0.0
            for n in range(self._C):
                summation += ((1/math.factorial(n)) * (self._r ** n))
            final_output = summation + ((1/math.factorial(self._C)) * (self._r ** self._C) * ((self._C * self._sys_inputs.service_rate) / ((self._C * self._sys_inputs.service_rate) - self._sys_inputs.arrival_rate)))
        
        return final_output ** -1
    
    
    def average_customers_queue(self):
        numerator = (self._r ** (self._C+1)) / self._C
        denumerator = (math.factorial(self._C))*((1 - self._row) ** 2)
        
        return (numerator * self._p0) / denumerator
    
    def average_wait_queue(self):
        return self._Lq / self._sys_inputs.arrival_rate
    
    def average_customers(self):
        return self._Lq + self._r
    
    def average_wait(self):
        return (self._Lq / self._sys_inputs.arrival_rate) + (1 / self._sys_inputs.service_rate) 
    


# Testing
def test():
    sys_in = SystemInputs.SystemInputs(6, 3, 3, float('inf'))
    mmc = MMC(sys_in)
    print('L = ' , mmc.average_customers())
    print('Lq = ' , mmc.average_customers_queue())
    print('W = ' , mmc.average_wait())
    print('Wq = ' , mmc.average_wait_queue())