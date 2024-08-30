from abc import ABC, abstractmethod
from Product import Car, Manual
class Builder(ABC):
    @abstractmethod
    def reset(self):
        raise NotImplementedError()

    @abstractmethod
    def setSeats(self):
        raise NotImplementedError()
    @abstractmethod
    def setEngine(self):
        raise NotImplementedError()
    @abstractmethod
    def setTripComputer(self):
        raise NotImplementedError()
    @abstractmethod
    def setGPS(self):
        raise NotImplementedError()

class CarBuilder(Builder):
    def __init__(self):
        self.reset()
    def reset(self):
        self.car = Car()
    def setSeats(self, number):
        self.car.seats = number
    def setEngine(self, engine):
        self.car.engine = engine
    def setTripComputer(self, presence):
        self.car.trip_computer = presence
    def setGPS(self,gps):
        self.car.gps = gps
    def get_product(self):
        return self.car

class CarManualBuilder(Builder):
    def __init__(self):
        self.reset()
    def reset(self):
        self.manual = Manual()
    def set_seats(self, number):
        self.manual.seats = number
    def set_engine(self, engine):
        self.manual.engine = engine
    def set_trip_computer(self, presence):
        self.manual.trip_computer = presence
    def set_gps(self, presence):
        self.manual.gps = presence
    def get_product(self):
        product = self.manual
        self.reset()
        return product