class CarPark:

    def __int__(self,
                name,
                location,
                max_bays,
                occupied_bays=0,
                display=None,
                ):
        self.available_bays = max_bays - occupied_bays
        self.cars_in_car_park = []
        self.max_bays = max_bays
        if display is None:
            self.displays = []