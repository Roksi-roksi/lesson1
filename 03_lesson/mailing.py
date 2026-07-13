from address import Address


class Mailing:

    def __init__(self, cost, track):
        self.to_address = None
        self.from_address = None
        self.cost = cost
        self.track = track

    def add_address(self, address_1, address_2):
        self.to_address = address_1
        self.from_address = address_2


    def get_address_to(self):
        return self.to_address

    def get_address_from(self):
        return self.from_address