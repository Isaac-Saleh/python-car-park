from sensor import EntrySensor, ExitSensor
from display import Display
from car_park import CarPark

car_park = CarPark("Santa Monica Bays", "California", 66)
car_park.register_display(Display(car_park))
entry_sensor = EntrySensor(car_park)
exit_sensor = ExitSensor(car_park)

# user_input = input("Hit space bar to open the Santi Monica Bays for business")
#
# while user_input:
#     entry_sensor.detect()


entry_sensor.detect()
entry_sensor.detect()
entry_sensor.detect()
exit_sensor.detect()



        # Random Plate is generated
        # Append plate to carpark list
        # Update available bays
        # Update Displays - includes print statuses
    # Print ( Detection occured: Plate "ABC-123" entered)


# Car Exits -
    # Sensor detects
        # Random plate chosen from carpark list
        # Assign plate to variable 'exiting_car'
        # Delete from carpark list
        # Update available bays
        #update Displays - includes prints dispaly statuses
    # Print (Detection occured: Plate "exiting_car" exited)


# Put the above code in a while loop that runs with the Enter Button and chooses to:
    # if available bays < max bays or available bays - max bays
        #randomly choose enter or exit function

    # else
        # choose enter function


# if available bay = 0  (exit function only has to run)
# else if availble bay = max bay  (entry function only has to run)
#     else function can be randomised.