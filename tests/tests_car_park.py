import unittest
from _datetime import datetime
from car_park import CarPark
from display import Display
from sensor import Sensor, ExitSensor, EntrySensor


class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Bay-kers Delight", "Moondalup", 5)
        self.display = Display(self.car_park)
        self.entry_sensor = EntrySensor(self.car_park)
        self.exit_sensor = ExitSensor(self.car_park)

    def test_car_park_is_instantiated(self):
        self.assertIsInstance(self.car_park, CarPark)

    def test_display_is_instantiated(self):
        self.assertIsInstance(self.display, Display)

    def test_sensor_is_instantiated(self):
        car_park = self.car_park
        self.assertIsInstance(EntrySensor(car_park), Sensor)
        self.assertIsInstance(ExitSensor(car_park), Sensor)

    def test_add_car_adds_car_to_car_park(self):
        car_park = self.car_park
        car = "fke-123"
        self.assertEqual(car_park.available_bays, 5)
        car_park.add_car(car)
        self.assertEqual(car_park.available_bays, 4)

    def test_remove_car_removes_car_from_car_park(self):
        car_park = self.car_park
        car = "FKE-123"
        self.assertEqual(car_park.available_bays, 5)
        car_park.add_car(car)
        self.assertEqual(car_park.available_bays, 4)
        car_park.remove_car(car)
        self.assertEqual(car_park.available_bays, 5)

    def test_display_board_displays_info(self):
        message = "Display board Displaying"
        temp = 33
        bays = 5
        result = self.display.display_board(message, temp, bays)
        expected_result = f"Display board Displaying\nCurrent Time:{datetime.now().strftime('%H:%M:%S')}\nTemperature: {33}\nAvailable Bays: {5}"
        self.assertEqual(result, expected_result)

    def test_display_board_updates_with_entered_car(self):
        car_park = self.car_park
        message = "Display board Displaying"
        temp = 33
        car = "FKE-123"
        car_park.add_car(car)
        result = self.display.display_board(message, temp, self.car_park.available_bays)
        expected_result = f"Display board Displaying\nCurrent Time:{datetime.now().strftime('%H:%M:%S')}\nTemperature: {33}\nAvailable Bays: {4}"

        self.assertEqual(result, expected_result)

    def test_display_board_updates_with_exited_car(self):
        car_park = self.car_park
        car_park.occupied_bays = 1
        message = "Display board Displaying"
        temp = 33
        car_park.cars_in_car_park = ["FKE-123"]
        car = "FKE-123"
        car_park.remove_car(car)
        result = self.display.display_board(message, temp, self.car_park.available_bays)
        expected_result = f"Display board Displaying\nCurrent Time:{datetime.now().strftime('%H:%M:%S')}\nTemperature: {33}\nAvailable Bays: {5}"

        self.assertEqual(result, expected_result)

    def test_entry_sensor_detects_entry(self):
        car_park = self.car_park
        entry_sensor = self.entry_sensor
        entry_sensor.detect()

        self.assertEqual(car_park.available_bays, 4)
        self.assertEqual(len(car_park.cars_in_car_park), 1)

    def test_exit_sensor_detects_exit(self):
        car_park = self.car_park
        car_park.cars_in_car_park = ["FKE-123"]
        car_park.occupied_bays = 1
        exit_sensor = self.exit_sensor
        exit_sensor.detect()

        self.assertEqual(car_park.available_bays, 5)
        self.assertEqual(len(car_park.cars_in_car_park), 0)

