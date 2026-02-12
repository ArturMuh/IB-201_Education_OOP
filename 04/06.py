class Transport:
    pass

class WaterTransport(Transport):
    pass

class Ship(WaterTransport):
    pass

class Boat(WaterTransport):
    pass

class AirTransport(Transport):
    pass

class Aviation(AirTransport):
    pass

class Plan(Aviation):
    pass

class Helicopter(Aviation):
    pass

class Aerostat(AirTransport):
    pass

class AirShip(Aerostat):
    pass

class Balloon(Aerostat):
    pass

class GroundTransport:
    pass

class RailwayTransport(GroundTransport):
    pass # Железнодорожный транспорт

class Train(RailwayTransport):
    pass

class Tram(RailwayTransport):
    pass

class AutomotiveTransport(GroundTransport):
    pass

class Car(AutomotiveTransport):
    pass

class Bus(AutomotiveTransport):
    pass

class Truck(AutomotiveTransport):
    pass

class BicycleTransport(GroundTransport):
    pass # Велосипедный транспорт

class Bicycle(BicycleTransport):
    pass

class AnimalPoweredTransport(GroundTransport):
    pass

class HorseCart(AnimalPoweredTransport):
    pass

class SpaceTransport(Transport):
    pass

class Satellite(SpaceTransport):
    pass # спутник

class Spececraft(SpaceTransport):
    pass

class Rocket(SpaceTransport):
    pass








