#inheritance
# Vehicle
# -> Car
# -> Ship
# -> Plane

from vehicle import Vehicle, Car, Ship, Plane


veni = Vehicle()
veni.go(100)

vici = Ship()
vici.sound()
vici.go(200)

vidi = Plane()
vidi.sound()
vidi.go(1000)

vindi = Car()
vindi.sound()
vindi.go(50)