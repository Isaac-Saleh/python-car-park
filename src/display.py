


class Display:
    def __init__(self, car_park):
        self.car_park = car_park
        self.temperature = car_park.temperature
        self.available_bays = car_park.available_bays
        self.show_full = False
        self.banner = None

    def display_board(self, message, temp, bays):
        print(message)
        print(f"Temperature: {temp}\n"
              f"Available Bays: {bays}")
