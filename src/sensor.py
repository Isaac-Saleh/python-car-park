
import random
from abc import ABC, abstractmethod

import car_park


class Sensor(ABC):
    """Defines a Sensor for the CarPark"""

    def __init__(self, car_park):
        self.car_park = car_park

    def _read_plate(self):
        return f"FKE-{random.randint(100, 1000)}"

    def detect(self):
        """Triggers when car moves past Sensor"""
        print("DETECTION OCCURRED:")
        plate = self._read_plate()
        self.update_car_park(plate)



    @abstractmethod
    def update_car_park(self):
        ...


class EntrySensor(Sensor):
    """Triggered on entry"""
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"PLATE #: {plate}")


class ExitSensor(Sensor):
    """Triggered on exit"""

    def detect(self):
        plate = random.choice(self.car_park.cars_in_car_park)
        self.update_car_park(plate)

    def update_car_park(self, car):
        self.car_park.remove_car(car)
        print(f"EXITED PLATE #: {car}")

