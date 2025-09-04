class ChargingStation:
    def __init__(self, name):
        self.name = name
        self.slots = ["Available"] * 3
