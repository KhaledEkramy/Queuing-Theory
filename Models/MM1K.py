import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import SystemInputs
class MM1K:
    '''
    Methods:
        average_customers = L
        average_customers_queue = Lq
        average_wait = W
        average_wait_queue = Wq
        lambda_dash = lambda * (1 - p_k)
    
    Attributes:
        _sys_inputs (SystemInputs): The system inputs for the queueing model.
        _sys_capacity (int): The system's capacity.
        _row (float): The traffic intensity (arrival_rate / service_rate).
        _p_k (float): The probability of all servers being occupied.
        _lambda_dash (float): The adjusted arrival rate after considering server occupation.
    '''
    def __init__(self, sys_inputs: SystemInputs):
        self._sys_inputs = sys_inputs
        self._sys_capacity = self._sys_inputs.sys_capacity  
        self._row = self._sys_inputs.arrival_rate / self._sys_inputs.service_rate  
        
        # Calculate p_k 
        if self._row == 1:
            self._p_k = 1 / (self._sys_capacity + 1)
        else:
            numerator = (1 - self._row) * (self._row ** self._sys_capacity)
            denominator = 1 - (self._row ** (self._sys_capacity + 1))
            self._p_k = numerator / denominator
        
        # Calculate lambda_dash (adjusted arrival rate)
        self._lambda_dash = self._sys_inputs.arrival_rate * (1 - self._p_k)
            
    @property
    def sys_inputs(self):
        return self._sys_inputs
    
    
    def average_customers(self):
        K = self._sys_capacity
        
        if self._row == 1:
            return K / 2
        else:
            numerator = self._row * (1 - (K + 1) * (self._row ** K) + K * (self._row ** (K + 1)))
            denominator = (1 - self._row) * (1 - (self._row ** (K + 1)))
        
        return numerator / denominator
    
    def average_wait(self):
        return self.average_customers() / self._lambda_dash
    
    def average_customers_queue(self):
        return self.average_customers() - (self._row * (1 - self._p_k))
    
    def average_wait_queue(self):
        return self.average_customers_queue() / self._lambda_dash
    