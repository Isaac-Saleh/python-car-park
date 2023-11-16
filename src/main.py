

# Set up:
# Carpark
# Display
# EntrySensor
# ExitSensor


# Car Enters -
    # Sensor detects

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