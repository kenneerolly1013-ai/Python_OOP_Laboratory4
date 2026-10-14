
class Vehicle:
    brand = "Toyota"
    speed = 100

    def start(self):
        print("Vehicle is starting.")


class Car(Vehicle):
    def start(self):
        print("Car engine is starting.")


vehicle = Vehicle()
car = Car()

vehicle.start()
car.start()
