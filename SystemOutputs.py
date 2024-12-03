from SystemInputs import SystemInputs
from Models.MM1 import MM1
from Models.MM1K import MM1K
from Models.MMC import MMC
from Models.MMCK import MMCK

def play(arrival_rate: float, service_rate: float, num_of_servers: int, sys_capacity: str) -> tuple:
    
    if sys_capacity == 'inf':
        sys_capacity = float('inf')
    else:
        sys_capacity = int(sys_capacity)
    
    # May raise Error of type ValueError if the user entered any invalid input    
    inputs = SystemInputs(arrival_rate, service_rate, num_of_servers, sys_capacity)
    
    # Determine which model to use based on the number of servers and the system capacity
    if num_of_servers == 1:
        if sys_capacity == float('inf'):
            model = MM1(inputs)
        else:
            model = MM1K(inputs)
    else:
        if sys_capacity == float('inf'):
            model = MMC(inputs)
        else:
            model = MMCK(inputs)
    
    # Model parameters        
    L = model.average_customers()
    Lq = model.average_customers_queue()
    W = model.average_wait()
    Wq = model.average_wait_queue()
    
    # Return the results of the model as a list of the form [L, Lq, W, Wq]
    return (str(type(model)).split('.')[1], [L, Lq, W, Wq] )