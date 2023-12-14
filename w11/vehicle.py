
class Vehicle:
    def __init__(self) -> None:
        print("A vehicle initilized")
    def go(self, distance):
        print("We travel {} kms!".format(distance))
    
class Plane(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        print("A Plane is initilized")
    def sound(self):
        print("Fiyuuu")
    
class Ship(Vehicle):
    def __init__(self) -> None:
        super().__init__() 
        # parent yerine super kullanıyor, parent initini çağırı
        print("A Ship is initilized")
    def sound(self):
        print("Woot Woot")

class Car(Vehicle):
    def __init__(self) -> None:
        super().__init__()
        print("A Car is initilized")
    def sound(self):
        print("Wroom Wroom")
    def go(self, distance): # Vehicle daki go yu override ettik
        print("I would like to walk {} miles and I would walk {} more".format(distance, distance))
        