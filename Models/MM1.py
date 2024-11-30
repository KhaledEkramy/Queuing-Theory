import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import SystemInputs
class MM1:
    '''
    Methods:
        average_customers = L
        average_customers_queue = Lq
        average_wait = W
        average_wait_queue = Wq
        
    constructor:
        sys_inputs (SystemInputs): The system inputs for the queueing model.
    '''
    def __init__(self, sys_inputs: SystemInputs):
        self._sys_inputs = sys_inputs
        
    @property
    def sys_inputs(self):
        return self._sys_inputs
    
    def average_customers(self):
        return (self._sys_inputs.arrival_rate / (self._sys_inputs.service_rate - self._sys_inputs.arrival_rate) )
    
    def average_customers_queue(self):
        return (self._sys_inputs.arrival_rate / self._sys_inputs.service_rate) * self.average_customers()
    
    def average_wait(self):
        return self.average_customers() / self._sys_inputs.arrival_rate
    
    def average_wait_queue(self):
        return self.average_customers_queue() / self._sys_inputs.arrival_rate
