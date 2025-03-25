class Car:
    def __init__(self, make, model, speed_mph, seats):
        self.make = make
        self.model = model
        self.speed_mph = speed_mph
        self.seats = seats
    
    def calculate_distance(self, time_hrs):
        return time_hrs * self.speed_mph
    
    @property
    def passengers(self):
        return self._passengers

    @passengers.setter
    def passengers(self, p):
        self._passengers = p
    
        
class Coupe(Car):
    def __init__(self, make, model, speed_mph, is_street_legal):
        super().__init__(make, model, speed_mph, 2)
        self.is_street_legal = is_street_legal


c = Coupe("BMW", "525i", 130, True)
c.passengers = 3
print(c.passengers)