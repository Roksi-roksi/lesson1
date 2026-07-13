from email.headerregistry import Address


class Mailing:
    to_adress: Address
    from_address: Address
    cost: int
    track: str

    def __init__(self, to_adress, from_address, cost, track):
        self.to_adress = to_adress
        self.from_address = from_address
        self.cost = cost
        self.track = track
