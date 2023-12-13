
class vehicle():
    def __init__(self,make,model,type):
        self.make=make
        self.__model=model
        self.__type=type
    
   

class car(vehicle):
    def __init__(self,make,model,type,distance):
        super().__init__(make,model,type)
        self.distance=distance
    def getValue(self):
        return "move"

class boat(vehicle):
    def __init__(self,make,model,type,distance):
        super().__init__(make,model,type)
        self.distace=distance
    def getValue(self):
        return "float"

class plane(vehicle):
    def __init__(self,make,model,type,distance):
        super().__init__(make,model,type)
        self.distace=distance
    def getValue(self):
        return "fly"

tesla=car('tesla',2019,'electric','100KM')
row=boat('marcedez',2011,'petrol','50KM')
flight=plane('kingfisher',2033,'airfuel','100KM')
print(tesla.__dict__)
a=[tesla,row,flight]
for i in a:
    print(i.getValue())