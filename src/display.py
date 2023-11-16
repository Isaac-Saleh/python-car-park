from car_park import CarPark


class Display:
    def __init__(self, car_park):
        self.car_park = car_park
        self.temperature = car_park.CarPark.update_temperature
        self.available_bays = car_park.CarPark.available_bays
        self.show_full = False
        self.banner = None

    def display_board(self, message):
        print(f"Temperature: {self.temperature}\n"
              f"Available Bays: {self.available_bays}")