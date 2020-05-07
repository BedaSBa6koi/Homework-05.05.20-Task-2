class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70
    
    def drive(self, km):
        self.km = km
        if (self.fuel - km/10) >= 0:
            self.__add_distance(km)
            self.__subtract_fuel(km)
            print("lets drive")
        else:
            print("Need more fuel")

    def __add_distance(self, km):
        self.odometer += self.km

    def __subtract_fuel(self, km):
        self.fuel -= km/10

car1 = Car("Honda", "Fit", "2020") 
print(car1.make, car1.model, car1.year) 
car1.drive(100)     
print(car1.odometer)
print(car1.fuel)
car1.drive(100)
print(car1.odometer)
print(car1.fuel)
car1.drive(1000)
print(car1.odometer)
print(car1.fuel)