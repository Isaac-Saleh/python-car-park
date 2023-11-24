import car_park
import time


class Display:
    def __init__(self, car_park):
        self.car_park = car_park
        self.temperature = car_park.temperature
        self.available_bays = car_park.available_bays
        #self.show_full = False
        # self.banner = None

    def display_board(self, message, temp, bays):
        display_message = f"{message}\nCurrent Time:{car_park.datetime.now().strftime('%H:%M:%S')}\nTemperature: {temp}\nAvailable Bays: {bays}"
        print(display_message)
        return display_message


