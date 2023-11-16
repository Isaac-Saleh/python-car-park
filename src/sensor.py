from abc import ABC, abstractmethod


class Sensor(ABC):
    """Defines a Sensor for the CarPark"""

    def __int__(self, car_park):
        self.car_park = car_park
