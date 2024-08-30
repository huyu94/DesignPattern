class Manual:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = None
        self.gps = None

    def __str__(self):
        return (f"Manual with {self.seats} seats, {self.engine} engine description, "
                f"Trip Computer: {'described' if self.trip_computer else 'not described'}, "
                f"GPS: {'described' if self.gps else 'not described'}")

class Car:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = None
        self.gps = None
    def __str__(self):
        return (f"Car with {self.seats} seats, {self.engine} engine, "
                f"Trip Computer: {'present' if self.trip_computer else 'absent'}, "
                f"GPS: {'present' if self.gps else 'absent'}")