from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def getValue(self):
        return 1
class car(vehicle):
    def __init__(self):
        super().__init__()
    # def getValue(self):
    #     return 1
bar = car()
print(bar.getValue())