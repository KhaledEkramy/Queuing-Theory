import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import math
import SystemInputs

class MMC:
    '''
    '''
    
    def __init__(self, sys_inputs: SystemInputs):
        self._sys_inputs = sys_inputs
        self._sys_capacity = self._sys_inputs.sys_capacity
        self._row = self._sys_inputs.arrival_rate / self._sys_inputs.service_rate
        
    