import random
from display import Display


class CarPark:

    def __init__(self, name, location, max_bays, displays=None):
        self.available_bays = max_bays
        self.name = name
        self.location = location
        self.max_bays = max_bays
        self.occupied_bays = 0
        self.cars_in_car_park = []
        self.temperature = self.update_temperature()
        if displays is None:
            self.displays = []


    def update_available_bays(self):
        self.available_bays = self.max_bays - self.occupied_bays

    def update_temperature(self):
        """Updates the temperature"""
        return random.randint(28, 34)

    def publish_car_park_status(self):
        for display in self.displays:
            display.display_board(f"<PARKING INFO>", self.temperature, self.available_bays)


    def add_car(self, car):
        if self.available_bays > 0:
            self.cars_in_car_park.append(car)
            self.occupied_bays += 1
            self.update_available_bays()
            self.publish_car_park_status()
        else:
            print("Car park FULL!")

    def remove_car(self, car):
        assert self.occupied_bays > 0
        self.occupied_bays -= 1
        self.cars_in_car_park.remove(car)
        self.update_available_bays()
        self.publish_car_park_status()

    def register_display(self, display):
        self.displays.append(display)

