import random
import time
from datetime import datetime
from sensor import EntrySensor, ExitSensor
from display import Display
from car_park import CarPark

car_park = CarPark("Santa Monica Bays", "California", 66)
car_park.register_display(Display(car_park))
entry_sensor = EntrySensor(car_park)
exit_sensor = ExitSensor(car_park)
TIME_OPEN_FOR = 60  # The length of time (s) you wish to run the program for
FILE_PATH = "car_park_log.txt"

car_park.clear_log(FILE_PATH)
user_input = input("Hit Enter to open the Santa Monica Bays for business...\n")
if len(user_input) < 1:
    open_time = time.time()
    print("\nCAR PARK NOW OPEN!!\n")

    while True:
        sensor_choice = random.choice([0, 1])
        time_between_cars = random.randint(3, 5)

        if car_park.available_bays == car_park.max_bays:
            entry_sensor.detect()
        elif car_park.occupied_bays == car_park.max_bays:
            exit_sensor.detect()
        else:
            if sensor_choice == 0:
                entry_sensor.detect()
            else:
                exit_sensor.detect()

        elapsed_time = time.time() - open_time
        if elapsed_time >= TIME_OPEN_FOR:
            break

        time.sleep(time_between_cars)
print("Santa Monica Bays is Closing Soon. Entry Prohibited... Please exit in a timely manner\n")
while car_park.available_bays != car_park.max_bays:
    exit_sensor.detect()
    time.sleep(1)

print("CAR PARK NOW CLOSED!! \nThank you for choosing Santa Monica Bays!\n")
car_park.publish_car_park_status()

print(f"Today's Logs: {datetime.now().strftime('%Y-%m-%d')}")
car_park.print_car_park_log('car_park_log.txt')
