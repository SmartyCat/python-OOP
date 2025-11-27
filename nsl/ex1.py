"""С помощью наследования и приведенной ниже схемы постройте
иерархию пустых классов, описывающих транспортные средства:"""


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class WaterVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):
    pass


class Car(LandVehicle):
    pass


class Motorcycle(LandVehicle):
    pass


class Popeller(AirVehicle):
    pass


class Jet(AirVehicle):
    pass
