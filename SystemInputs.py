class SystemInputs:
    """
    SystemInputs Class

    Represents the key parameters of a queueing system.

    Attributes:
        arrival_rate (float): The arrival rate of the system (λ), must be > 0.
        service_rate (float): The service rate of the system (μ), must be > 0.
        num_of_servers (int): The number of servers in the system, must be > 0.
        sys_capacity (int): The maximum capacity of the system, must be > 0.
    """

    def __init__(self, arrival_rate: float, service_rate: float, num_of_servers: int, sys_capacity: int):
        if arrival_rate <= 0:
            raise ValueError(f"Arrival Rate must be greater than zero. Received: {arrival_rate}")
        if service_rate <= 0:
            raise ValueError(f"Service Rate must be greater than zero. Received: {service_rate}")
        if num_of_servers <= 0:
            raise ValueError(f"Number of servers must be greater than zero. Received: {num_of_servers}")
        if sys_capacity <= 0:
            raise ValueError(f"System Capacity must be greater than zero. Received: {sys_capacity}")
        
        self._arrival_rate = arrival_rate
        self._service_rate = service_rate
        self._num_of_servers = num_of_servers
        self._sys_capacity = sys_capacity

    @property
    def arrival_rate(self):
        return self._arrival_rate

    @arrival_rate.setter
    def arrival_rate(self, value: float):
        if value <= 0:
            raise ValueError("Arrival Rate must be greater than zero")
        self._arrival_rate = value

    @property
    def service_rate(self):
        return self._service_rate

    @service_rate.setter
    def service_rate(self, value: float):
        if value <= 0:
            raise ValueError("Service Rate must be greater than zero")
        self._service_rate = value

    @property
    def num_of_servers(self):
        return self._num_of_servers

    @num_of_servers.setter
    def num_of_servers(self, value: int):
        if value <= 0:
            raise ValueError("Number of servers must be greater than zero")
        self._num_of_servers = value

    @property
    def sys_capacity(self):
        return self._sys_capacity

    @sys_capacity.setter
    def sys_capacity(self, value: int):
        if value <= 0:
            raise ValueError("System Capacity must be greater than zero")
        self._sys_capacity = value
